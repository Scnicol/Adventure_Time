import React from "react";
import "./HomePage.css";
import AdventureTimeLogo from "./Adventure-Time.svg";
import SpinningWheel from "./SpinningWheel";

function HomePage() {
  return (
    <div className="homepage-container">
      <img src={AdventureTimeLogo} alt="Adventure Time Logo" className="homepage-logo" />
      <h1 className="homepage-title">Welcome to Adventure Time!</h1>
      <p className="homepage-subtitle">Your adventure is a wheel spin away!</p>
      <SpinningWheel />
    </div>
  );
}

export default HomePage;
