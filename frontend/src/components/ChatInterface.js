import React, { useState, useRef, useEffect } from 'react';
import { Send, MessageCircle, Zap } from 'lucide-react';
import { api } from '../utils/api';

const ChatInterface = ({ userProfile }) => {
  const [messages, setMessages] = useState([
    {
      type: 'bot',
      content: 'Hi! I am MoneyMitra, your AI financial coach. I am here to help with budgeting, saving, and financial planning. Ask me anything! 💰',
      timestamp: new Date()
    }
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!inputMessage.trim() || isLoading) return;

    const userMessage = {
      type: 'user',
      content: inputMessage,
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const startTime = Date.now();
      const response = await api.quickChat(inputMessage, userProfile);
      const responseTime = Date.now() - startTime;

      const botMessage = {
        type: 'bot',
        content: response.response,
        timestamp: new Date(),
        responseTime: responseTime,
        model: response.model || 'AI'
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        type: 'bot',
        content: 'Sorry, I encountered an error. Please make sure the backend is running on localhost:8000.',
        timestamp: new Date(),
        isError: true
      };
      setMessages(prev => [...prev, errorMessage]);
      console.error('Chat error:', error);
    }

    setInputMessage('');
    setIsLoading(false);
  };

  const quickQuestions = [
    'How can I save ₹5000 in 3 months?',
    'Emergency fund tips for irregular income?',
    'Best way to track daily expenses?',
    'Investment options for ₹10,000?'
  ];

  return (
    <div className="chat-container">
      <div className="profile-bar">
        <div className="profile-info">
          <MessageCircle size={22} />
          <span>Chatting as: {userProfile.occupation} (₹{userProfile.income}/month)</span>
        </div>
        <div className="status-indicator">
          <div className="status-dot"></div>
          <span>AI Ready</span>
        </div>
      </div>

      <div className="messages-container">
        {messages.map((message, index) => (
          <div key={index} className={"message " + message.type}>
            <div className="message-content">
              <div className="message-text">
                {message.content}
              </div>
              <div className="message-meta">
                <span className="timestamp">
                  {message.timestamp.toLocaleTimeString()}
                </span>
                {message.responseTime && (
                  <span className="response-time">
                    <Zap size={13} />
                    {message.responseTime}ms
                  </span>
                )}
                {message.model && (
                  <span className="model-info">
                    {message.model}
                  </span>
                )}
              </div>
            </div>
          </div>
        ))}
        
        {isLoading && (
          <div className="message bot">
            <div className="message-content">
              <div className="typing-indicator">
                <div className="typing-dot"></div>
                <div className="typing-dot"></div>
                <div className="typing-dot"></div>
              </div>
              <div className="message-meta">
                <span className="timestamp">MoneyMitra is thinking...</span>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {messages.length <= 1 && (
        <div className="quick-questions">
          <h4>Try asking:</h4>
          <div className="quick-questions-grid">
            {quickQuestions.map((question, index) => (
              <button
                key={index}
                className="quick-question-btn"
                onClick={() => setInputMessage(question)}
              >
                {question}
              </button>
            ))}
          </div>
        </div>
      )}

      <form onSubmit={handleSendMessage} className="chat-input-form">
        <div className="input-container">
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            placeholder="Ask about saving, budgeting, investments, or any financial question..."
            disabled={isLoading}
            className="chat-input"
          />
          <button 
            type="submit" 
            disabled={isLoading || !inputMessage.trim()}
            className="send-button"
          >
            <Send size={20} />
          </button>
        </div>
      </form>
    </div>
  );
};

export default ChatInterface;
