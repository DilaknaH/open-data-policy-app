import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pdfplumber
import re
import random
from transformers import pipeline

app = Flask(__name__, static_folder="../frontend/build", static_url_path="")
CORS(app)

# -------------------------
# FAST SUMMARIZER (CPU) - OPTIMIZED
# -------------------------
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",  # distilled, much faster
    device=-1  # CPU
)

# -------------------------
# CLEAN FUNCTION
# -------------------------
def clean_text(text: str) -> str:
    text = re.sub(r"\.{3,}", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# -------------------------
# SUMMARIZE FUNCTION (FAST)
# -------------------------
def summarize_text(text, chunk_size=1500):
    """
    Summarizes text in chunks to reduce time and handle large PDFs.
    Optimized for CPU speed.
    """
    text = clean_text(text)
    text = text[:15000]  # trim very long documents

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = []

    for chunk in chunks:
        if len(chunk) < 200:
            continue
        try:
            result = summarizer(
                chunk,
                max_length=120,
                min_length=40,
                do_sample=False
            )
            summaries.append(result[0]["summary_text"])
        except:
            continue

    return " ".join(summaries)

# -------------------------
# SUMMARIZE ROUTE
# -------------------------
@app.route("/summarize", methods=["POST"])
def summarize_policy():
    try:
        text = ""

        if "file" in request.files:
            file = request.files["file"]

            if not file.filename.lower().endswith(".pdf"):
                return jsonify({"summary": "Invalid PDF"}), 400

            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + " "

        elif request.is_json:
            text = request.json.get("policy_text", "")

        if not text.strip():
            return jsonify({"summary": "No text provided"}), 400

        summary = summarize_text(text)
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"summary": f"Error: {str(e)}"}), 500

# -------------------------
# DYNAMIC RULE-BASED SCENARIO BUILDER
# -------------------------
def build_rule_based_scenario(summary, scenario_type):
    """
    Creates scenario drafts based on rules + summarized policy.
    Adds slight variation per PDF and includes a short interpretation.
    """
    base_intro = f"This scenario draft is adapted from the uploaded policy summary for: {scenario_type}.\n\n"

    context_sentences = ". ".join(summary.split(".")[:3]).strip()
    context_text = f"Policy Context:\n{context_sentences}\n\n"

    if scenario_type == "Research Universities":
        bullets = [
            random.choice([
                "Integrate the policy within academic governance frameworks.",
                "Embed policy objectives into university administrative and academic systems.",
                "Align institutional mandates with the policy guidance."
            ]),
            random.choice([
                "Ensure research ethics and compliance with regulatory standards.",
                "Strengthen ethical review mechanisms and research oversight.",
                "Maintain high standards of academic integrity and compliance."
            ]),
            random.choice([
                "Protect student, faculty, and research data.",
                "Implement robust data protection protocols for academic data.",
                "Safeguard sensitive information while maintaining transparency."
            ]),
            random.choice([
                "Develop cross-faculty coordination and continuous evaluation strategies.",
                "Promote inter-departmental collaboration and iterative policy adoption.",
                "Implement ongoing monitoring and assessment for sustainable adoption."
            ])
        ]

    elif scenario_type == "Startups & Tech Companies":
        bullets = [
            random.choice([
                "Align policy objectives with innovation and business strategy.",
                "Integrate policy into product development and innovation roadmaps.",
                "Ensure strategic alignment with company growth and digital transformation."
            ]),
            random.choice([
                "Implement strong data governance and cybersecurity practices.",
                "Ensure secure handling of company data assets.",
                "Maintain rigorous data protection and risk management protocols."
            ]),
            random.choice([
                "Ensure compliance with legal obligations and operational risk mitigation.",
                "Embed regulatory and risk management processes across operations.",
                "Mitigate operational risks through adherence to data and legal standards."
            ]),
            random.choice([
                "Adopt agile and measurable implementation strategies.",
                "Apply iterative and performance-driven operational plans.",
                "Monitor and evaluate implementation for continual improvement."
            ])
        ]

    elif scenario_type == "NGOs & Social Impact Groups":
        bullets = [
            random.choice([
                "Ensure transparent reporting and governance structures.",
                "Implement mechanisms for accountability and donor confidence.",
                "Maintain clarity in organizational operations and oversight."
            ]),
            random.choice([
                "Protect sensitive beneficiary data with ethical handling frameworks.",
                "Safeguard personal information using strict privacy protocols.",
                "Ensure responsible data collection and management practices."
            ]),
            random.choice([
                "Focus on fairness, inclusivity, and responsible resource allocation.",
                "Promote equitable practices and ethical governance.",
                "Ensure resources are allocated responsibly and inclusively."
            ]),
            random.choice([
                "Prioritize long-term social impact and measurable community outcomes.",
                "Engage stakeholders and measure impact effectively.",
                "Focus on sustainable programs with measurable benefits."
            ])
        ]

    else:
        bullets = [
            "Adapt policy to the operational environment of the organization.",
            "Follow governance best practices and ethical standards.",
            "Consider practical implementation strategies for the context.",
            "Ensure sustainable and effective policy adoption."
        ]

    bullet_text = "Recommendations:\n" + "\n".join(f"- {b}" for b in bullets) + "\n"

    interpretation = f"\nInterpretation:\nThis scenario draft interprets the policy summary in the context of {scenario_type}. The recommendations provide practical guidance tailored to the organization's role and responsibilities, ensuring alignment with the core policy objectives.\n"

    conclusion = "\nConclusion:\nImplementing these recommendations ensures that organizations align their operations with the core objectives of the policy while achieving effective and sustainable outcomes.\n"

    return base_intro + context_text + bullet_text + interpretation + conclusion

# -------------------------
# SCENARIO ROUTE
# -------------------------
@app.route("/generate", methods=["POST"])
def generate_scenario():
    try:
        data = request.json
        summary = data.get("summary", "")
        scenario = data.get("scenario", "")

        if not summary.strip():
            return jsonify({"draft": "Missing summary"}), 400
        if not scenario.strip():
            return jsonify({"draft": "Missing scenario type"}), 400

        draft = build_rule_based_scenario(summary, scenario)
        return jsonify({"draft": draft})

    except Exception as e:
        return jsonify({"draft": f"Error: {str(e)}"}), 500

# -------------------------
# SERVE FRONTEND
# -------------------------
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    