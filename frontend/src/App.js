import React, { useState, useEffect } from 'react';
import ChatInterface from './components/ChatInterface';
import ProfileSetup from './components/ProfileSetup';
import { api } from './utils/api';
import { Zap, Shield, Users, Heart } from 'lucide-react';
import './App.css';

function App() {
  const [isSetupComplete, setIsSetupComplete] = useState(false);
  const [userProfile, setUserProfile] = useState({
    occupation: 'Delivery driver (Zomato/Swiggy)',
    income: '20000-25000',
    expenses: '18000',
    location: 'Mumbai'
  });
  const [systemHealth, setSystemHealth] = useState(null);

  useEffect(() => {
    const checkBackendHealth = async () => {
      try {
        const health = await api.checkHealth();
        setSystemHealth(health);
        console.log('Backend health:', health);
      } catch (error) {
        console.error('Backend health check failed:', error);
        setSystemHealth({ status: 'error', message: 'Backend unavailable' });
      }
    };

    checkBackendHealth();
  }, []);

  if (!isSetupComplete) {
    return (
      <div className="app">
        <header className="app-header">
          <div className="header-content">
            <div className="logo">
              <h1>💰 MoneyMitra</h1>
              <p>Your AI financial friend that never sleeps, never judges</p>
            </div>
            {systemHealth && (
              <div className={"health-status " + systemHealth.status}>
                <div className={"status-dot " + systemHealth.status}></div>
                <span>
                  Backend: {systemHealth.status === 'healthy' ? 'Ready' : 'Error'}
                </span>
              </div>
            )}
          </div>
        </header>

        <main className="main-content">
          <ProfileSetup
            userProfile={userProfile}
            setUserProfile={setUserProfile}
            onStart={() => setIsSetupComplete(true)}
          />
        </main>

        <footer className="app-footer">
          <div className="footer-content">
            <div className="feature">
              <Zap className="feature-icon" />
              <span>Cerebras AI - Sub-second responses</span>
            </div>
            <div className="feature">
              <Users className="feature-icon" />
              <span>Built for 400M+ gig workers</span>
            </div>
            <div className="feature">
              <Shield className="feature-icon" />
              <span>Secure & Private</span>
            </div>
            <div className="feature">
              <Heart className="feature-icon" />
              <span>Mumbai Hacks 2025</span>
            </div>
          </div>
        </footer>
      </div>
    );
  }

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <div className="logo">
            <h1>💰 MoneyMitra</h1>
            <p>AI Financial Coaching</p>
          </div>
          <button 
            className="reset-button"
            onClick={() => setIsSetupComplete(false)}
          >
            Change Profile
          </button>
        </div>
      </header>

      <main className="main-content chat-mode">
        <ChatInterface userProfile={userProfile} />
      </main>
    </div>
  );
}

export default App;
