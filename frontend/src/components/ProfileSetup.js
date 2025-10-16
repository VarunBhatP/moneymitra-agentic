import React, { useState } from 'react';
import { MapPin, DollarSign, Briefcase } from 'lucide-react';

const ProfileSetup = ({ userProfile, setUserProfile, onStart }) => {
  const [profile, setProfile] = useState(userProfile);

  const handleChange = (field, value) => {
    setProfile(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setUserProfile(profile);
    onStart();
  };

  const occupationOptions = [
    'Delivery driver (Zomato/Swiggy)',
    'Auto rickshaw driver', 
    'Uber/Ola driver',
    'Freelancer/Consultant',
    'Small business owner',
    'Construction worker',
    'Gig worker (other)'
  ];

  return (
    <div className="profile-setup">
      <div className="profile-setup-container">
        <div className="profile-header">
          <h2>Welcome to MoneyMitra! </h2>
          <p>Let's personalize your financial coaching experience</p>
        </div>

        <form onSubmit={handleSubmit} className="profile-form">
          <div className="form-group">
            <label>
              <Briefcase size={18} />
              What's your occupation?
            </label>
            <select
              value={profile.occupation}
              onChange={(e) => handleChange('occupation', e.target.value)}
              required
            >
              {occupationOptions.map(option => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>
              <DollarSign size={18} />
              Monthly Income Range (₹)
            </label>
            <select
              value={profile.income}
              onChange={(e) => handleChange('income', e.target.value)}
              required
            >
              <option value="8000-12000">₹8,000 - ₹12,000</option>
              <option value="12000-18000">₹12,000 - ₹18,000</option>
              <option value="18000-25000">₹18,000 - ₹25,000</option>
              <option value="25000-35000">₹25,000 - ₹35,000</option>
              <option value="35000-50000">₹35,000 - ₹50,000</option>
              <option value="50000+">₹50,000+</option>
            </select>
          </div>

          <div className="form-group">
            <label>
              <DollarSign size={18} />
              Monthly Expenses (₹)
            </label>
            <input
              type="number"
              value={profile.expenses}
              onChange={(e) => handleChange('expenses', e.target.value)}
              placeholder="e.g., 15000"
              required
            />
          </div>

          <div className="form-group">
            <label>
              <MapPin size={18} />
              Location
            </label>
            <input
              type="text"
              value={profile.location}
              onChange={(e) => handleChange('location', e.target.value)}
              placeholder="e.g., Mumbai, Delhi"
              required
            />
          </div>

          <button type="submit" className="start-button">
            Start Financial Coaching 
          </button>
        </form>

        <div className="features-preview">
          <h3>What you'll get:</h3>
          <ul>
            <li>⚡ Ultra-fast AI responses (powered by Cerebras)</li>
            <li>🎯 Personalized advice for irregular income</li>
            <li>💡 Practical tips for Indian financial tools</li>
            <li>📊 Smart spending analysis</li>
            <li>🔒 Private and secure conversations</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default ProfileSetup;
