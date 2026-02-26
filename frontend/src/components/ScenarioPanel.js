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

  useEffect(() => {
    if (resetSignal) {
      setScenario("");
      setDraft("");
    }
  }, [resetSignal]);

  const handleGenerate = async () => {
    setLoading(true); // only affects scenario loading
    try {
      const response = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ summary, scenario }),
      });
      const data = await response.json();
      setDraft(data.draft);
      addToHistory("Scenario Draft", data.draft);
    } catch (error) {
      setDraft("Error: Could not connect to backend or generation failed.");
      console.error("Error generating scenario:", error);
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
      <button onClick={handleGenerate} className="primary-btn">
        Generate Draft
      </button>
      <div>
        <h3>Scenario Draft</h3>
        {loading ? <div className="spinner"></div> : <p>{draft}</p>}
        {draft && !draft.startsWith("Error") && (
          <>
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
          </>
        )}
      </div>
    </div>
  );
}

export default ScenarioPanel;
