import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import pipeline

# Point Flask to the React build folder
app = Flask(__name__, static_folder="build", static_url_path="")
CORS(app)   # Allow requests if needed (though not strictly necessary now)

# Load models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
generator = pipeline("text-generation", model="gpt2")

# --- API Routes ---
@app.route("/summarize", methods=["POST"])
def summarize_policy():
    try:
        text = request.json.get("policy_text")
        if not text or text.strip() == "":
            return jsonify({"summary": "Error: No text provided"}), 400

        summary = summarizer(text, max_length=200, min_length=80, do_sample=False)
        return jsonify({"summary": summary[0]['summary_text']})
    except Exception as e:
        return jsonify({"summary": f"Error during summarization: {str(e)}"}), 500

@app.route("/generate", methods=["POST"])
def generate_scenario():
    try:
        summary = request.json.get("summary")
        scenario = request.json.get("scenario")
        if not summary or not scenario:
            return jsonify({"draft": "Error: Missing summary or scenario"}), 400

        prompt = f"Adapt this Data Governance Framework summary for {scenario}: {summary}"
        output = generator(prompt, max_length=300, num_return_sequences=1)
        return jsonify({"draft": output[0]['generated_text']})
    except Exception as e:
        return jsonify({"draft": f"Error during generation: {str(e)}"}), 500

# --- Frontend Route ---
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    """
    Serve React frontend from build folder.
    If the requested file exists, return it.
    Otherwise, return index.html (React handles routing).
    """
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
