import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import pipeline
import pdfplumber
import re

app = Flask(__name__, static_folder="../frontend/build", static_url_path="")
CORS(app)

# --- Load NLP Models ---
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

# --- Helper Functions ---
def clean_text(text: str) -> str:
    text = re.sub(r"\.{5,}", " ", text)
    text = re.sub(r"\s*\d+\s*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"[^\x20-\x7E]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def summarize_chunk(chunk: str) -> str:
    chunk = chunk.strip()
    if len(chunk) < 50:
        return ""
    try:
        res = summarizer(chunk, max_length=150, min_length=60, do_sample=False)
        if res and isinstance(res, list) and "summary_text" in res[0]:
            return res[0]["summary_text"]
    except Exception as e:
        print(f"Summarizer failed on chunk: {e}")
    return ""

def summarize_text(text, chunk_size=4000, max_summary_words=1000):
    text = clean_text(text)
    if not text:
        return "No content to summarize."

    MAX_INPUT_LENGTH = 20000
    text = text[:MAX_INPUT_LENGTH]

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = []

    for chunk in chunks:
        summary = summarize_chunk(chunk)
        if summary:
            summaries.append(summary)

    full_summary = " ".join(summaries)
    words = full_summary.split()
    if len(words) > max_summary_words:
        full_summary = " ".join(words[:max_summary_words]) + "..."
    return full_summary

# --- Routes ---
@app.route("/summarize", methods=["POST"])
def summarize_policy():
    try:
        text = ""

        if "file" in request.files:
            file = request.files["file"]
            if file.filename == "" or not file.filename.lower().endswith(".pdf"):
                return jsonify({"summary": "Error: Invalid PDF file"}), 400
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += clean_text(page_text) + " "

        elif request.is_json:
            text = request.json.get("policy_text", "")

        if not text.strip():
            return jsonify({"summary": "Error: No text provided"}), 400

        summary = summarize_text(text)

        return jsonify({"summary": summary})

    except Exception as e:
        print(f"Error in /summarize: {e}")
        return jsonify({"summary": f"Error during summarization: {str(e)}"}), 500


@app.route("/generate", methods=["POST"])
def generate_scenario():
    try:
        data = request.json
        summary = data.get("summary", "")
        scenario = data.get("scenario", "")

        if not summary.strip():
            return jsonify({"draft": "Error: Missing summary"}), 400

        MAX_SUMMARY_LENGTH = 2000
        summary = summary[:MAX_SUMMARY_LENGTH]

        scenario_prompts = {
            "Research Universities": (
                "Adapt this Data Governance Framework summary for a Research University context. "
                "Focus on academic research ethics, student data protection, open data policies, "
                "and compliance requirements."
            ),
            "Startups & Tech Companies": (
                "Adapt this Data Governance Framework summary for Startups & Tech Companies. "
                "Focus on scalability, regulatory compliance, innovation, cloud security, and data monetization risks."
            ),
            "NGOs & Social Impact Groups": (
                "Adapt this Data Governance Framework summary for NGOs & Social Impact Organizations. "
                "Focus on donor transparency, beneficiary data protection, ethical data usage, and community accountability."
            ),
        }

        prompt_intro = scenario_prompts.get(
            scenario, "Adapt this Data Governance Framework summary into a concise narrative:"
        )

        prompt = f"{prompt_intro}\n\n{summary}\n\nAdapted Version:\n"

        output = generator(
            prompt,
            max_new_tokens=400,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            no_repeat_ngram_size=3,
            pad_token_id=50256
        )

        generated_text = output[0]["generated_text"]
        draft = generated_text[len(prompt):].strip()

        if not draft:
            draft = generated_text.strip()

        # --- Post-filter repetitive phrases ---
        draft = re.sub(r"\b(\w+)( \1){2,}\b", r"\1", draft)

        return jsonify({"draft": draft})

    except Exception as e:
        print(f"Error in /generate: {e}")
        return jsonify({"draft": f"Error during generation: {str(e)}"}), 500


# --- Serve React Frontend ---
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
