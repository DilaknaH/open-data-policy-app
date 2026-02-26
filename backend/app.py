from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)   # Allow requests from React frontend

# Load models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
generator = pipeline("text-generation", model="gpt2")

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

if __name__ == "__main__":
    app.run(debug=True)
