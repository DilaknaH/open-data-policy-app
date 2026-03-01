import React, { useState } from "react";

function SummaryPanel({ summary, loading }) {
  const [expanded, setExpanded] = useState(false);

  // Max length for preview before "Read More"
  const MAX_LENGTH = 800;

  const isLong = summary && summary.length > MAX_LENGTH;

  const displayedSummary =
    isLong && !expanded ? summary.substring(0, MAX_LENGTH) + "..." : summary;

  // Format summary for readable paragraphs
  const formatSummary = (text) => {
    if (!text) return null;
    return text
      .replace(/\. /g, ".\n\n") // insert line break after sentences
      .split("\n")
      .map((para, index) => <p key={index}>{para.trim()}</p>);
  };

  return (
    <div>
      <h2>Policy Summary</h2>

      {loading ? (
        <div className="spinner"></div>
      ) : summary ? (
        <div>
          <div className="summary-box">{formatSummary(displayedSummary)}</div>

          {isLong && (
            <button
              onClick={() => setExpanded(!expanded)}
              className="expand-btn"
            >
              {expanded ? "Show Less" : "Read More"}
            </button>
          )}

          <button
            onClick={() => navigator.clipboard.writeText(summary)}
            className="copy-btn"
          >
            Copy Full Summary
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
            Download Full Summary
          </button>
        </div>
      ) : (
        <p>No summary yet. Upload a PDF or paste text and click Summarize.</p>
      )}
    </div>
  );
}

export default SummaryPanel;
