import React, { useEffect, useState } from 'react';

function ActivitiesPage() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchActivities = async () => {
      setLoading(true);
      try {
        const res = await fetch('/api/activities/user/current');
        console.log('Fetch status:', res.status);
        const data = await res.json();
        console.log('Fetch data:', data);
        setActivities(data.activities || []);
      } catch (err) {
        console.error('Fetch error:', err);
        setActivities([]);
      } finally {
        setLoading(false);
      }
    };
    fetchActivities();
  }, []);

  if (loading) return <div style={{ padding: '2rem' }}>Loading activities...</div>;

  return (
    <div className="my-adventures-container">
      <h1 className="my-adventures-title">My Activities</h1>
      <div className="adventures-section">
        <h2 className="adventures-section-title">Activities I've Created</h2>
        <ul className="adventures-list">
          {activities.length === 0 && <li className="adventures-empty">You have not created any activities yet.</li>}
          {activities.map(activity => (
            <li key={activity.id}>
              <button className="adventure-btn">{activity.name || activity.activity}</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default ActivitiesPage;
