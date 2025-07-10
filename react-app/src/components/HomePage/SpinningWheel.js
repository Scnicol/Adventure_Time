import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getDirections } from "../../store/directions";
import "./SpinningWheel.css";

const COLORS = [
  "#f9d423", "#ff4e50", "#f67280", "#355c7d", "#6c5b7b", "#c06c84", "#11998e", "#38ef7d", "#fc5c7d", "#6a82fb", "#fc466b", "#3f5efb"
];

function getCoordinatesForAngle(angle, radius, cx, cy) {
  const rad = (angle - 90) * (Math.PI / 180);
  return {
    x: cx + radius * Math.cos(rad),
    y: cy + radius * Math.sin(rad)
  };
}

function SpinningWheel() {
  const dispatch = useDispatch();
  const directionsObj = useSelector((state) => state.directions);
  const directions = Object.values(directionsObj);
  const [spinning, setSpinning] = useState(false);
  const [selected, setSelected] = useState(null);
  const [rotation, setRotation] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [containerSize] = useState(650); // keep container square and fixed
  const animationRef = useRef();
  const startRotationRef = useRef(0);
  const targetRotationRef = useRef(0);
  const startTimeRef = useRef(0);
  const duration = 8000; // ms
  // SVG wheel parameters
  const size = 650;
  const radius = size / 2 - 16;
  const cx = size / 2;
  const cy = size / 2;

  useEffect(() => {
    dispatch(getDirections());
  }, [dispatch]);

  // Animate rotation with ease-out
  const animateSpin = (timestamp) => {
    if (!startTimeRef.current) startTimeRef.current = timestamp;
    const elapsed = timestamp - startTimeRef.current;
    const t = Math.min(elapsed / duration, 1);
    // Ease-out cubic
    const ease = 1 - Math.pow(1 - t, 3);
    const newRot = startRotationRef.current + (targetRotationRef.current - startRotationRef.current) * ease;
    setRotation(newRot);
    if (t < 1) {
      animationRef.current = requestAnimationFrame(animateSpin);
    } else {
      setSpinning(false);
      startTimeRef.current = 0;
      setRotation(targetRotationRef.current);
      setTimeout(() => {
        setSelected(spinWheel.pendingIndex);
        setShowResult(true);
      }, 4000);
    }
  };

  // Generate SVG paths for each slice
  const slices = directions.map((dir, i) => {
    const sliceAngle = 360 / directions.length;
    const startAngle = i * sliceAngle;
    const endAngle = startAngle + sliceAngle;
    const largeArc = sliceAngle > 180 ? 1 : 0;
    const start = getCoordinatesForAngle(startAngle, radius, cx, cy);
    const end = getCoordinatesForAngle(endAngle, radius, cx, cy);
    const pathData = [
      `M ${cx} ${cy}`,
      `L ${start.x} ${start.y}`,
      `A ${radius} ${radius} 0 ${largeArc} 1 ${end.x} ${end.y}`,
      "Z"
    ].join(" ");
    const color = COLORS[i % COLORS.length];
    // Text position: middle of the arc
    const textAngle = startAngle + sliceAngle / 2;
    const textRadius = radius * 0.65;
    const textPos = getCoordinatesForAngle(textAngle, textRadius, cx, cy);
    return (
      <g key={dir.id}>
        <path d={pathData} fill={color} />
        <text
          x={textPos.x}
          y={textPos.y}
          textAnchor="middle"
          alignmentBaseline="middle"
          fill="#fff"
          fontSize="11"
          fontFamily="'Comic Sans MS', 'Comic Sans', cursive, sans-serif"
          transform={`rotate(${textAngle + 90}, ${textPos.x}, ${textPos.y})`}
          style={{ pointerEvents: "none", userSelect: "none", filter: "drop-shadow(0 1px 2px #0008)" }}
        >
          {dir.direction.length > 18 ? dir.direction.slice(0, 15) + "..." : dir.direction}
        </text>
      </g>
    );
  });

  // --- FIX ROTATION: selected slice always at top (arrow) ---
  const spinWheel = () => {
    if (spinning || directions.length === 0) return;
    setShowResult(false);
    // Pick the random index but don't set it until after spin
    const randomIndex = Math.floor(Math.random() * directions.length);
    spinWheel.pendingIndex = randomIndex;
    const slice = 360 / directions.length;
    const minSpins = 5;
    const baseTarget = 360 - (randomIndex * slice + slice / 2);
    // Always spin at least minSpins times from current rotation
    const newRotation = rotation + minSpins * 360 + ((baseTarget - (rotation % 360) + 360) % 360);
    startRotationRef.current = rotation;
    targetRotationRef.current = newRotation;
    setSpinning(true);
    cancelAnimationFrame(animationRef.current);
    animationRef.current = requestAnimationFrame(animateSpin);
  };

  useEffect(() => {
    return () => cancelAnimationFrame(animationRef.current);
  }, []);

  return (
    <div className="wheel-section" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <div style={{ position: 'relative', width: size, height: size, margin: '0 auto', padding: 0, boxSizing: 'content-box' }}>
        <svg
          className={`spinning-wheel${spinning ? " spinning" : ""}`}
          width={size}
          height={size}
          viewBox={`0 0 ${size} ${size}`}
          style={{ display: 'block', position: 'absolute', left: 0, top: 0,  '--rotation': `${rotation}deg` }}
          onClick={spinWheel}
        >
          <defs>
            <filter id="svg-blur" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="12" />
            </filter>
          </defs>
          {/* Stationary shadow circle behind the wheel */}
          <circle
            cx={cx}
            cy={cy}
            r={radius}
            fill="rgba(31,38,135,0.18)"
            filter="url(#svg-blur)"
          />
          <g>
            {directions.length > 0 ? (
              slices
            ) : (
              <></>
            )}
            {/* Add a single outline circle */}
            <circle
              cx={cx}
              cy={cy}
              r={radius}
              fill="none"
              stroke="#fffbe7"
              strokeWidth="6"
            />
          </g>
        </svg>
        {/* Arrow overlay at the top center, outside SVG */}
        <svg width="48" height="48" style={{ position: 'absolute', left: '50%', top: '-24px', transform: 'translateX(-50%) rotate(180deg)', zIndex: 3, pointerEvents: 'none' }}>
          <polygon points="24,0 44,44 24,34 4,44" fill="#fffbe7" stroke="#ff4e50" strokeWidth="3" />
        </svg>
      </div>
      <button className="spin-btn" onClick={spinWheel} disabled={spinning}>
        {spinning ? "Spinning..." : "Spin the Wheel!"}
      </button>
      {selected !== null && showResult && directions[selected] && (
        <div className="wheel-result">Direction: <b>{directions[selected].direction}</b></div>
      )}
    </div>
  );
}

export default SpinningWheel;
