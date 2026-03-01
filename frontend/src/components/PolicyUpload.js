import React, { useState, useEffect, useRef } from "react";

function PolicyUpload({ setSummary, setLoading, resetSignal, addToHistory }) {
  const [text, setText] = useState("");
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState("");
  const [pdfWordCount, setPdfWordCount] = useState(0); // ✅ NEW
  const fileInputRef = useRef(null);

  useEffect(() => {
    if (resetSignal) {
      setText("");
      setFile(null);
      setFileName("");
      setPdfWordCount(0); // ✅ reset pdf word count

      if (fileInputRef.current) {
        fileInputRef.current.value = "";
      }
    }
  }, [resetSignal]);

  const handleSummarize = async () => {
    if (!text.trim() && !file) {
      setSummary("Please upload a PDF or paste policy text.");
      return;
    }

    setLoading(true);

    try {
      let response;

      if (file) {
        const formData = new FormData();
        formData.append("file", file);

        response = await fetch("http://127.0.0.1:5000/summarize", {
          method: "POST",
          body: formData,
        });
      } else {
        response = await fetch("http://127.0.0.1:5000/summarize", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ policy_text: text }),
        });
      }

      const data = await response.json();

      if (data.summary) {
        setSummary(data.summary);
        addToHistory("Summary", data.summary);
      } else {
        setSummary("Backend returned an empty summary.");
      }
    } catch (error) {
      console.error(error);
      setSummary("Error: Could not connect to backend.");
    } finally {
      setLoading(false);
    }
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    if (selectedFile.type !== "application/pdf") {
      setSummary("Only PDF files are allowed.");
      return;
    }

    setFile(selectedFile);
    setFileName(selectedFile.name);
    setText("");

    // ✅ Estimate word count from PDF file (basic text extraction)
    const reader = new FileReader();
    reader.onload = function () {
      const rawText = reader.result;
      const words = rawText
        .replace(/[^a-zA-Z\s]/g, " ")
        .split(/\s+/)
        .filter(Boolean);
      setPdfWordCount(words.length);
    };
    reader.readAsText(selectedFile);
  };

  const handleRemoveFile = () => {
    setFile(null);
    setFileName("");
    setPdfWordCount(0);

    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const textWordCount = text.trim().split(/\s+/).filter(Boolean).length;

  // ✅ Show correct word count
  const wordCount = file ? pdfWordCount : textWordCount;

  return (
    <div>
      <h2>Upload PDF OR Paste Policy Text</h2>

      <input
        type="file"
        accept="application/pdf"
        className="file-input"
        onChange={handleFileChange}
        ref={fileInputRef}
      />

      {fileName && (
        <p className="selected-file">
          Selected File: {fileName}
          <span
            onClick={handleRemoveFile}
            style={{
              marginLeft: "8px",
              cursor: "pointer",
              fontWeight: "bold",
            }}
          >
            ✖
          </span>
        </p>
      )}

      <textarea
        rows="12"
        placeholder="OR paste policy text here..."
        value={text}
        onChange={(e) => {
          setText(e.target.value);
          setFile(null);
          setFileName("");
          setPdfWordCount(0);
          if (fileInputRef.current) {
            fileInputRef.current.value = "";
          }
        }}
      />

      <p className="word-count">Word count: {wordCount}</p>

      <button onClick={handleSummarize} className="primary-btn">
        Summarize
      </button>
    </div>
  );
}

export default PolicyUpload;
