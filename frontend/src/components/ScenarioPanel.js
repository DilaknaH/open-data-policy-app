import React, { useState, useEffect } from "react";

function ScenarioPanel({
  summary,
  setLoading,
  resetSignal,
  addToHistory,
  loading,
}) {
  const [scenario, setScenario] = useState("");
  const [draft, setDraft] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    if (resetSignal) {
      setScenario("");
      setDraft("");
      setError("");
    }
  }, [resetSignal]);

  const handleGenerate = async () => {
    if (!scenario) {
      setError("Please select a scenario.");
      return;
    }

    if (!summary || summary.trim().length === 0) {
      setError("Summary is missing.");
      return;
    }

    setError("");
    setLoading(true);

    try {
      const MAX_SUMMARY_LENGTH = 2000;
      const trimmedSummary =
        summary.length > MAX_SUMMARY_LENGTH
          ? summary.substring(0, MAX_SUMMARY_LENGTH)
          : summary;

      const response = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          summary: trimmedSummary,
          scenario: scenario,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.draft || "Generation failed");
      }

      const cleanDraft = data.draft?.trim() || "";

      setDraft(cleanDraft);
      addToHistory("Scenario Draft", cleanDraft);
    } catch (err) {
      console.error("Error generating scenario:", err);
      setError("Error: Could not connect to backend or generation failed.");
      setDraft("");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Scenario Adaptation</h2>

      <select value={scenario} onChange={(e) => setScenario(e.target.value)}>
        <option value="">Select scenario</option>
        <option value="Research Universities">Research Universities</option>
        <option value="Startups & Tech Companies">
          Startups & Tech Companies
        </option>
        <option value="NGOs & Social Impact Groups">
          NGOs & Social Impact Groups
        </option>
      </select>

      <button
        onClick={handleGenerate}
        className="primary-btn"
        disabled={loading}
      >
        {loading ? "Generating..." : "Generate Draft"}
      </button>

      {error && <p style={{ color: "#e64a19", marginTop: "10px" }}>{error}</p>}

      <div style={{ marginTop: "20px" }}>
        <h3>Scenario Draft</h3>

        {loading ? (
          <div className="spinner"></div>
        ) : (
          <div className="draft-box">
            {draft || "Generated draft will appear here..."}
          </div>
        )}

        {draft && !loading && !draft.startsWith("Error") && (
          <div style={{ marginTop: "10px" }}>
            <button
              onClick={() => navigator.clipboard.writeText(draft)}
              className="copy-btn"
            >
              Copy
            </button>

            <button
              className="download-btn"
              onClick={() => {
                const blob = new Blob([draft], { type: "text/plain" });
                const link = document.createElement("a");
                link.href = URL.createObjectURL(blob);
                link.download = "scenario_draft.txt";
                link.click();
              }}
            >
              Download
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default ScenarioPanel;
