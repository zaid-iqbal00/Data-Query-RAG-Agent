import React, { useState, useEffect } from 'react';
import './App.css';
import { Send, Database, MessageCircle, BarChart3, Users, CreditCard, UserCheck } from 'lucide-react';
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

function App() {
  const [activeTab, setActiveTab] = useState('chat');
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(false);
  const [profiles, setProfiles] = useState([]);
  const [transactions, setTransactions] = useState([]);
  const [managers, setManagers] = useState([]);

  // Fetch data on component mount
  useEffect(() => {
    fetchProfiles();
    fetchTransactions();
    fetchManagers();
  }, []);

  const fetchProfiles = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/profiles`);
      setProfiles(response.data.profiles || []);
    } catch (error) {
      console.error('Error fetching profiles:', error);
    }
  };

  const fetchTransactions = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/transactions`);
      setTransactions(response.data.transactions || []);
    } catch (error) {
      console.error('Error fetching transactions:', error);
    }
  };

  const fetchManagers = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/relationship_managers`);
      setManagers(response.data.relationship_managers || []);
    } catch (error) {
      console.error('Error fetching managers:', error);
    }
  };

  const sendMessage = async () => {
    if (!inputValue.trim()) return;

    const userMessage = { type: 'user', content: inputValue };
    setMessages(prev => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await axios.post(`${API_BASE_URL}/ask`, {
        query: inputValue
      });

      const botMessage = { type: 'bot', content: response.data.response };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = { type: 'bot', content: 'Sorry, there was an error processing your request.' };
      setMessages(prev => [...prev, errorMessage]);
    }

    setInputValue('');
    setLoading(false);
  };

  const ChatInterface = () => (
    <div className="chat-container">
      <div className="chat-header">
        <MessageCircle className="icon" />
        <h2>RAG Agent Chat</h2>
        <p>Ask questions about profiles, transactions, and relationship managers</p>
      </div>

      <div className="messages-container">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <h3>Welcome to your RAG Agent!</h3>
            <p>Try asking questions like:</p>
            <ul>
              <li>"What is the total portfolio value?"</li>
              <li>"Show me all transactions"</li>
              <li>"Who are the relationship managers?"</li>
              <li>"Find profiles with high net worth"</li>
            </ul>
          </div>
        ) : (
          messages.map((message, index) => (
            <div key={index} className={`message ${message.type}`}>
              <div className="message-content">
                {message.content}
              </div>
            </div>
          ))
        )}
        {loading && (
          <div className="message bot">
            <div className="message-content loading">
              <div className="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}
      </div>

      <div className="chat-input">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Ask a question about your data..."
          disabled={loading}
        />
        <button onClick={sendMessage} disabled={loading || !inputValue.trim()}>
          <Send className="icon" />
        </button>
      </div>
    </div>
  );

  const DataExplorer = () => (
    <div className="data-explorer">
      <div className="data-section">
        <div className="section-header">
          <Users className="icon" />
          <h3>Profiles ({profiles.length})</h3>
        </div>
        <div className="data-grid">
          {profiles.slice(0, 5).map((profile, index) => (
            <div key={index} className="data-card">
              <h4>{profile.name || 'Unknown'}</h4>
              <p><strong>Age:</strong> {profile.age || 'N/A'}</p>
              <p><strong>Net Worth:</strong> ${profile.net_worth?.toLocaleString() || 'N/A'}</p>
              <p><strong>Risk Tolerance:</strong> {profile.risk_tolerance || 'N/A'}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="data-section">
        <div className="section-header">
          <CreditCard className="icon" />
          <h3>Transactions ({transactions.length})</h3>
        </div>
        <div className="data-grid">
          {transactions.slice(0, 5).map((transaction, index) => (
            <div key={index} className="data-card">
              <h4>Account: {transaction.account_number || 'Unknown'}</h4>
              <p><strong>Amount:</strong> ${transaction.amount?.toLocaleString() || 'N/A'}</p>
              <p><strong>Type:</strong> {transaction.transaction_type || 'N/A'}</p>
              <p><strong>Date:</strong> {transaction.date || 'N/A'}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="data-section">
        <div className="section-header">
          <UserCheck className="icon" />
          <h3>Relationship Managers ({managers.length})</h3>
        </div>
        <div className="data-grid">
          {managers.slice(0, 5).map((manager, index) => (
            <div key={index} className="data-card">
              <h4>{manager.name || 'Unknown'}</h4>
              <p><strong>Region:</strong> {manager.region || 'N/A'}</p>
              <p><strong>Clients:</strong> {manager.clients_count || 'N/A'}</p>
              <p><strong>Experience:</strong> {manager.experience_years || 'N/A'} years</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  const Dashboard = () => (
    <div className="dashboard">
      <div className="dashboard-header">
        <BarChart3 className="icon" />
        <h2>Dashboard Overview</h2>
      </div>
      
      <div className="stats-grid">
        <div className="stat-card">
          <Users className="stat-icon" />
          <div className="stat-content">
            <h3>{profiles.length}</h3>
            <p>Total Profiles</p>
          </div>
        </div>
        
        <div className="stat-card">
          <CreditCard className="stat-icon" />
          <div className="stat-content">
            <h3>{transactions.length}</h3>
            <p>Total Transactions</p>
          </div>
        </div>
        
        <div className="stat-card">
          <UserCheck className="stat-icon" />
          <div className="stat-content">
            <h3>{managers.length}</h3>
            <p>Relationship Managers</p>
          </div>
        </div>
        
        <div className="stat-card">
          <Database className="stat-icon" />
          <div className="stat-content">
            <h3>{transactions.reduce((sum, t) => sum + (t.amount || 0), 0).toLocaleString()}</h3>
            <p>Total Transaction Volume</p>
          </div>
        </div>
      </div>

      <div className="recent-activity">
        <h3>Recent Activity</h3>
        <div className="activity-list">
          {transactions.slice(0, 10).map((transaction, index) => (
            <div key={index} className="activity-item">
              <div className="activity-icon">
                <CreditCard />
              </div>
              <div className="activity-content">
                <p><strong>{transaction.transaction_type || 'Transaction'}</strong></p>
                <p>Account: {transaction.account_number} - ${transaction.amount?.toLocaleString()}</p>
                <small>{transaction.date}</small>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  return (
    <div className="App">
      <header className="app-header">
        <div className="header-content">
          <h1>🤖 RAG Agent</h1>
          <p>Intelligent Data Query System</p>
        </div>
      </header>

      <nav className="app-nav">
        <button 
          className={activeTab === 'chat' ? 'active' : ''} 
          onClick={() => setActiveTab('chat')}
        >
          <MessageCircle className="icon" />
          Chat
        </button>
        <button 
          className={activeTab === 'data' ? 'active' : ''} 
          onClick={() => setActiveTab('data')}
        >
          <Database className="icon" />
          Data Explorer
        </button>
        <button 
          className={activeTab === 'dashboard' ? 'active' : ''} 
          onClick={() => setActiveTab('dashboard')}
        >
          <BarChart3 className="icon" />
          Dashboard
        </button>
      </nav>

      <main className="app-main">
        {activeTab === 'chat' && <ChatInterface />}
        {activeTab === 'data' && <DataExplorer />}
        {activeTab === 'dashboard' && <Dashboard />}
      </main>
    </div>
  );
}

export default App;
