// WelcomeScreen.js
import React from "react";

export default function WelcomeScreen({ onStart }) {
  return (
    <div className="welcome-container">
      <div className="welcome-box">
        <h1 className="app-title">Open Data Policy Summarizer</h1>
        <p className="welcome-tagline">
          Turning complex policies into clear insights.
        </p>
        <ul className="welcome-features">
          <li>Upload policy documents easily</li>
          <li>Get instant summaries</li>
          <li>Explore scenarios and history</li>
        </ul>
        <button className="get-started-btn" onClick={onStart}>
          Get Started
        </button>
      </div>
    </div>
  );
}
