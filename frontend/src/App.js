import React, { useState } from "react";
import PolicyUpload from "./components/PolicyUpload";
import SummaryPanel from "./components/SummaryPanel";
import ScenarioPanel from "./components/ScenarioPanel";
import HistoryPanel from "./components/HistoryPanel";
import "./App.css";

function App() {
  const [summary, setSummary] = useState("");
  const [loadingSummary, setLoadingSummary] = useState(false);
  const [loadingScenario, setLoadingScenario] = useState(false);
  const [resetSignal, setResetSignal] = useState(false);
  const [history, setHistory] = useState([]);

  const handleReset = () => {
    setSummary("");
    setResetSignal(true);
    setHistory([]);
    setTimeout(() => setResetSignal(false), 100);
  };

  const addToHistory = (type, content) => {
    setHistory((prev) => [
      ...prev,
      { type, content, timestamp: new Date().toLocaleTimeString() },
    ]);
  };

  const clearHistory = () => {
    setHistory([]);
  };

  return (
    <div className="container">
      <div className="panel card">
        <h1 className="app-title">Open Data Policy Summarizer</h1>
        <PolicyUpload
          setSummary={setSummary}
          setLoading={setLoadingSummary}
          resetSignal={resetSignal}
          addToHistory={addToHistory}
        />
        <button className="reset-btn" onClick={handleReset}>
          Reset All
        </button>
      </div>

      <div className="panel card">
        <SummaryPanel summary={summary} loading={loadingSummary} />
        <ScenarioPanel
          summary={summary}
          setLoading={setLoadingScenario}
          resetSignal={resetSignal}
          addToHistory={addToHistory}
          loading={loadingScenario}
        />
        <HistoryPanel history={history} clearHistory={clearHistory} />
      </div>
    </div>
  );
}

export default App;
