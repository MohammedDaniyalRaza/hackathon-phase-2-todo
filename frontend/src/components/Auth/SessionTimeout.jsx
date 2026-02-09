import { useEffect, useState } from 'react';
import { useAuth } from '../context/AuthContext';

const SessionTimeoutWarning = () => {
  const { user, logout } = useAuth();
  const [showWarning, setShowWarning] = useState(false);
  const [timeLeft, setTimeLeft] = useState(0);

  // In a real implementation, you would calculate the actual time left
  // based on the JWT expiration time
  useEffect(() => {
    if (!user) return;

    // Example: warn 5 minutes before expiration
    const warningTime = 5 * 60 * 1000; // 5 minutes in milliseconds
    const timer = setTimeout(() => {
      setShowWarning(true);
      setTimeLeft(warningTime);
    }, warningTime);

    // Clean up timer
    return () => clearTimeout(timer);
  }, [user]);

  // Countdown timer effect
  useEffect(() => {
    let countdown;
    if (showWarning && timeLeft > 0) {
      countdown = setTimeout(() => {
        setTimeLeft(timeLeft - 1000);
      }, 1000);
    } else if (timeLeft <= 0) {
      // Log out user when time is up
      logout();
      setShowWarning(false);
    }

    return () => clearTimeout(countdown);
  }, [showWarning, timeLeft, logout]);

  if (!showWarning) return null;

  return (
    <div className="fixed top-4 right-4 bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-3 rounded z-50">
      <h4 className="font-bold">Session Expiring Soon</h4>
      <p>Your session will expire in {Math.ceil(timeLeft / 1000)} seconds.</p>
      <button
        onClick={() => {
          setShowWarning(false);
          // In a real app, you would refresh the token here
        }}
        className="mt-2 bg-blue-500 hover:bg-blue-700 text-white py-1 px-3 rounded text-sm"
      >
        Extend Session
      </button>
    </div>
  );
};

export default SessionTimeoutWarning;