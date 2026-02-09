import React from 'react';

const LoadingSpinner = () => {
  return (
    <div className="loading-spinner" style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      padding: '20px'
    }}>
      <div style={{
        width: '40px',
        height: '40px',
        border: '4px solid rgba(0, 0, 0, 0.1)',
        borderRadius: '50%',
        borderTopColor: '#007acc',
        animation: 'spin 1s linear infinite'
      }}></div>
      <style jsx>{`
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
};

export default LoadingSpinner;