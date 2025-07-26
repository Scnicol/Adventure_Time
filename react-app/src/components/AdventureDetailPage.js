import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function AdventureDetailPage() {
  const { adventureId } = useParams();
  const [adventure, setAdventure] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAdventure = async () => {
      setLoading(true);
      try {
        const res = await fetch(`/api/adventures/${adventureId}`);
        if (!res.ok) throw new Error('Failed to fetch adventure');
        const data = await res.json();
        setAdventure(data);
      } catch (err) {
        setError('Adventure not found.');
      } finally {
        setLoading(false);
      }
    };
    fetchAdventure();
  }, [adventureId]);

  if (loading) return <div style={{ padding: '2rem' }}>Loading adventure details...</div>;
  if (error) return <div style={{ padding: '2rem', color: 'red' }}>{error}</div>;
  if (!adventure) return null;

  let localDate = 'N/A';
  if (adventure && adventure.adventureDate) {
    const dateObj = new Date(adventure.adventureDate);
    localDate = dateObj.toLocaleString(undefined, {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      timeZoneName: 'short',
    });
  }

  return (
    <div style={{ padding: '2rem', maxWidth: 700, margin: '2rem auto', background: '#fff', borderRadius: 14, boxShadow: '0 2px 12px 0 rgba(60,60,120,0.06)' }}>
      <h1 style={{ color: '#3a3a7c', fontSize: '2.2rem', marginBottom: '1.2rem', textAlign: 'center' }}>{adventure.name}</h1>
      <p><strong>Description:</strong> {adventure.description || 'No description provided.'}</p>
      <p><strong>Date:</strong> {localDate}</p>
      <p><strong>Created by:</strong> {adventure.creatorUsername ? adventure.creatorUsername : 'Unknown'}</p>
      {/* Add more fields as needed */}
    </div>
  );
}

export default AdventureDetailPage;
