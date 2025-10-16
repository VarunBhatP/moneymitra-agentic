import React, { useState, useEffect, useCallback } from 'react';
import ChatInterface from './components/ChatInterface';
import ProfileSetup from './components/ProfileSetup';
import Header from './components/Header'; // <-- Import the new component
import { api } from './utils/api';
import { Zap, Shield, Users, Heart } from 'lucide-react';
import './App.css';

// Initial state for the profile
const INITIAL_PROFILE = {
  occupation: 'Delivery driver (Zomato/Swiggy)',
  income: '20000-25000',
  expenses: '18000',
  location: 'Mumbai'
};

function App() {
  const [isSetupComplete, setIsSetupComplete] = useState(false);
  const [userProfile, setUserProfile] = useState(INITIAL_PROFILE);
  const [systemHealth, setSystemHealth] = useState(null);

  // Use useCallback for stable function reference
  const handleStartChat = useCallback(() => {
    setIsSetupComplete(true);
  }, []);

  const handleResetProfile = useCallback(() => {
    setIsSetupComplete(false);
    // Optional: Reset profile to initial state here if desired
    // setUserProfile(INITIAL_PROFILE);
  }, []);

  useEffect(() => {
    const checkBackendHealth = async () => {
      try {
        const health = await api.checkHealth();
        setSystemHealth(health);
        // Removed console.log for cleaner production code, but kept for development
        // console.log('Backend health:', health); 
      } catch (error) {
        console.error('Backend health check failed:', error);
        setSystemHealth({ status: 'error', message: 'Backend unavailable' });
      }
    };

    // Use a robust polling mechanism in a real app, but single call is fine here
    checkBackendHealth();
  }, []);
  
  // --- Rendering Logic ---

  if (!isSetupComplete) {
    return (
      <div className="app">
        {/* Pass props to the new component for DRYness */}
        <Header 
          isChatMode={false} 
          systemHealth={systemHealth} 
          onResetProfile={handleResetProfile} // Passed for completeness
        />

        <main className="main-content">
          <ProfileSetup
            userProfile={userProfile}
            setUserProfile={setUserProfile}
            onStart={handleStartChat}
          />
        </main>

        <footer className="app-footer">
          <div className="footer-content">
            {/* ... Footer features remain the same ... */}
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

  // Chat Mode
  return (
    <div className="app">
      {/* Re-use the Header component */}
      <Header 
        isChatMode={true} 
        systemHealth={systemHealth} 
        onResetProfile={handleResetProfile} 
      />

      <main className="main-content chat-mode">
        <ChatInterface userProfile={userProfile} />
      </main>
      
      {/* Footer is typically omitted in chat views for focus, but can be kept if necessary */}
      {/* <footer className="app-footer">...</footer> */}
    </div>
  );
}

export default App;