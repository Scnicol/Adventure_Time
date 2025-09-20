import React, { useEffect, useState } from 'react';

function FoodPage() {
  const [food, setFood] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchFood = async () => {
      setLoading(true);
      try {
        const res = await fetch('/api/food/user/current');
        const data = await res.json();
        setFood(data.food || []);
      } catch (err) {
        setFood([]);
      } finally {
        setLoading(false);
      }
    };
    fetchFood();
  }, []);

  if (loading) return <div style={{ padding: '2rem' }}>Loading food...</div>;

  return (
    <div className="my-adventures-container">
      <h1 className="my-adventures-title">My Food</h1>
      <div className="adventures-section">
        <h2 className="adventures-section-title">Food I've Created</h2>
        <ul className="adventures-list">
          {food.length === 0 && <li className="adventures-empty">You have not created any food yet.</li>}
          {food.map(item => (
            <li key={item.id}>
              <button className="adventure-btn">{item.food}</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default FoodPage;
