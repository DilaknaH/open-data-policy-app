import React, { useState } from "react";

function HistoryPanel({ history, clearHistory }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="history-panel">
      <div className="history-header" onClick={() => setOpen(!open)}>
        {open ? "▼ Session History" : "▶ Session History"}
      </div>
      {open && (
        <>
          <ul className="history-list">
            {history.length === 0 ? (
              <li>No history yet.</li>
            ) : (
              history.map((item, index) => (
                <li key={index}>
                  <strong>{item.type}</strong> ({item.timestamp}):{" "}
                  {item.content}
                </li>
              ))
            )}
          </ul>
          {history.length > 0 && (
            <button onClick={clearHistory} className="reset-btn">
              Clear History
            </button>
          )}
        </>
      )}
    </div>
  );
}

export default HistoryPanel;
