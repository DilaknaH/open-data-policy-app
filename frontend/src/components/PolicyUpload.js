import React, { useState, useEffect } from "react";

function PolicyUpload({ setSummary, setLoading, resetSignal, addToHistory }) {
  const [text, setText] = useState("");

  useEffect(() => {
    if (resetSignal) {
      setText("");
    }
  }, [resetSignal]);

  const handleSummarize = async () => {
    setLoading(true); // only affects summary loading
    try {
      const response = await fetch("http://127.0.0.1:5000/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ policy_text: text }),
      });
      const data = await response.json();
      setSummary(data.summary);
      addToHistory("Summary", data.summary);
    } catch (error) {
      setSummary(
        "Error: Could not connect to backend or summarization failed.",
      );
      console.error("Error summarizing:", error);
    } finally {
      setLoading(false);
    }
  };

  const wordCount = text.trim().split(/\s+/).filter(Boolean).length;

  return (
    <div>
      <h2>Upload Policy</h2>
      <textarea
        rows="12"
        placeholder="Paste Data Governance Framework text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <p className="word-count">Word count: {wordCount}</p>
      <button onClick={handleSummarize} className="primary-btn">
        Summarize
      </button>
    </div>
  );
}

export default PolicyUpload;
