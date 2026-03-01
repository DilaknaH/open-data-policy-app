import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import pipeline
import pdfplumber
import re

app = Flask(__name__, static_folder="../frontend/build", static_url_path="")
CORS(app)

# -------------------------
# FAST SUMMARIZER
# -------------------------

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

# -------------------------
# CLEAN FUNCTION
# -------------------------

def clean_text(text: str) -> str:
    text = re.sub(r"\.{3,}", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# -------------------------
# SUMMARIZE FUNCTION
# -------------------------

def summarize_text(text, chunk_size=1200):
    text = clean_text(text)
    text = text[:12000]

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = []

    for chunk in chunks:
        if len(chunk) < 200:
            continue
        try:
            result = summarizer(
                chunk,
                max_length=130,
                min_length=60,
                do_sample=False
            )
            summaries.append(result[0]["summary_text"])
        except:
            continue

    return " ".join(summaries)

# -------------------------
# ROUTES
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
# DETERMINISTIC SCENARIO BUILDER
# -------------------------

def build_scenario(summary, scenario):

    base_intro = f"""
This adapted policy interpretation is tailored specifically for the {scenario} context. 
It builds upon the core objectives and strategic priorities outlined in the original policy document.
"""

    if scenario == "Research Universities":

        body = f"""
Institutional Governance Implications:
Research universities must integrate the policy within existing academic governance frameworks, 
ensuring alignment with institutional mandates, research oversight bodies, and strategic development plans.

Research Ethics and Compliance:
Strong emphasis should be placed on ethical review mechanisms, responsible innovation, 
and regulatory compliance aligned with academic standards and international best practices.

Data Protection and Academic Integrity:
Universities must safeguard student, faculty, and research data while maintaining transparency, 
academic freedom, and responsible data-sharing practices.

Implementation Strategy:
Implementation should involve cross-faculty coordination, capacity building, 
and continuous evaluation to ensure sustainable institutional adoption.
"""

    elif scenario == "Startups & Tech Companies":

        body = f"""
Business and Innovation Strategy:
Technology firms should align the policy objectives with innovation roadmaps, 
ensuring scalability and competitive advantage within evolving digital markets.

Regulatory and Risk Management:
Clear compliance mechanisms must be embedded to address legal obligations, 
data governance standards, and operational risk mitigation.

Data Security and Monetization:
Companies must ensure strong cybersecurity practices while responsibly leveraging 
data assets for value creation and sustainable revenue growth.

Operational Implementation:
Adoption should be agile, iterative, and integrated into product development cycles 
with measurable performance indicators.
"""

    elif scenario == "NGOs & Social Impact Groups":

        body = f"""
Transparency and Accountability:
Non-profit organizations must ensure transparent reporting mechanisms 
and clear governance structures that reinforce public trust and donor confidence.

Beneficiary Data Protection:
Sensitive beneficiary information must be protected through strict data privacy 
controls and ethical data handling frameworks.

Ethical Governance:
The policy should reinforce fairness, inclusivity, and responsible resource allocation 
while maintaining compliance with relevant legal standards.

Sustainable Community Impact:
Implementation should prioritize long-term social value, stakeholder engagement, 
and measurable community outcomes.
"""

    else:
        body = "This policy should be adapted to align with the operational environment and governance structure of the target organization."

    conclusion = f"""
In conclusion, effective adaptation of this policy within the {scenario} setting requires 
structured governance, responsible oversight, and a commitment to continuous improvement. 
By aligning institutional priorities with the core objectives of the original policy, 
organizations can ensure meaningful and sustainable implementation.
"""

    return base_intro + "\n" + body + "\n" + conclusion


@app.route("/generate", methods=["POST"])
def generate_scenario():
    try:
        data = request.json
        summary = data.get("summary", "")
        scenario = data.get("scenario", "")

        if not summary.strip():
            return jsonify({"draft": "Missing summary"}), 400

        draft = build_scenario(summary, scenario)

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

    