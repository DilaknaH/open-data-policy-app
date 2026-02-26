import React from "react";

function SummaryPanel({ summary, loading }) {
  return (
    <div>
      <h2>Policy Summary</h2>
      {loading ? (
        <div className="spinner"></div>
      ) : summary ? (
        <div>
          <p>{summary}</p>
          <button
            onClick={() => navigator.clipboard.writeText(summary)}
            className="copy-btn"
          >
            Copy
          </button>
          <button
            className="download-btn"
            onClick={() => {
              const blob = new Blob([summary], { type: "text/plain" });
              const link = document.createElement("a");
              link.href = URL.createObjectURL(blob);
              link.download = "policy_summary.txt";
              link.click();
            }}
          >
            Download
          </button>
        </div>
      ) : (
        <p>No summary yet. Paste policy text and click Summarize.</p>
      )}
    </div>
  );
}

export default SummaryPanel;
