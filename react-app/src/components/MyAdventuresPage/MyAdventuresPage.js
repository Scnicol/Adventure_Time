import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';
import './MyAdventuresPage.css';

function MyAdventuresPage() {
  const [createdAdventures, setCreatedAdventures] = useState([]);
  const [joinedAdventures, setJoinedAdventures] = useState([]);
  const [loading, setLoading] = useState(true);
  const history = useHistory();

  useEffect(() => {
    const fetchAdventures = async () => {
      setLoading(true);
      try {
        const [createdRes, joinedRes] = await Promise.all([
          fetch('/api/adventures/user/current'),
          fetch('/api/adventures/user/current/joined'),
        ]);
        const createdData = await createdRes.json();
        const joinedData = await joinedRes.json();
        setCreatedAdventures(createdData.adventures || []);
        setJoinedAdventures(joinedData.adventures || []);
      } catch (err) {
        // handle error
        setCreatedAdventures([]);
        setJoinedAdventures([]);
      } finally {
        setLoading(false);
      }
    };
    fetchAdventures();
  }, []);

  if (loading) return <div style={{ padding: '2rem' }}>Loading adventures...</div>;

  return (
    <div className="my-adventures-container">
      <h1 className="my-adventures-title">My Adventures</h1>
      <div className="adventures-section">
        <h2 className="adventures-section-title">Adventures I've Created</h2>
        <ul className="adventures-list">
          {createdAdventures.length === 0 && <li className="adventures-empty">You have not created any adventures yet.</li>}
          {createdAdventures.map(adventure => (
            <li key={adventure.id}>
              <button className="adventure-btn" onClick={() => history.push(`/adventures/${adventure.id}`)}>{adventure.name}</button>
            </li>
          ))}
        </ul>
      </div>
      <div className="adventures-section" style={{ marginTop: '2rem' }}>
        <h2 className="adventures-section-title">Adventures I've Joined</h2>
        <ul className="adventures-list">
          {joinedAdventures.length === 0 && <li className="adventures-empty">You have not joined any adventures yet.</li>}
          {joinedAdventures.map(adventure => (
            <li key={adventure.id}>
              <button className="adventure-btn" onClick={() => history.push(`/adventures/${adventure.id}`)}>{adventure.name}</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default MyAdventuresPage;
