# 💰 MoneyMitra - Agentic AI Financial Coach

**Your AI financial friend that never sleeps, never judges**

[![Mumbai Hacks 2025](https://img.shields.io/badge/Mumbai_Hacks-2025-blue.svg)](https://devfolio.co)
[![Cerebras AI](https://img.shields.io/badge/Powered_by-Cerebras_AI-green.svg)](https://cerebras.ai)
[![Django](https://img.shields.io/badge/Backend-Django-darkgreen.svg)](https://djangoproject.com)
[![React](https://img.shields.io/badge/Frontend-React-blue.svg)](https://reactjs.org)

## 🎯 Problem Statement
400+ million Indians with irregular income struggle with financial planning. Traditional financial advice doesn't work for gig workers, delivery drivers, and informal sector employees earning ₹8,000-₹50,000/month with unpredictable income patterns.

## 💡 Our Solution
MoneyMitra is an **agentic AI system** that provides personalized financial coaching in <200ms, specifically designed for irregular income patterns common in India's gig economy.

## 🏆 Hackathon Submission
**Mumbai Hacks 2025 - Fintech Track**
- **Team:** Nirvana coders 
- **Track:** Fintech Innovation
- **Target:** Underserved financial markets

## ⚡ Key Differentiators
- **🚀 Sub-second responses** using Cerebras Llama3.1-8B
- **🇮🇳 Culturally intelligent** (Hindi/English, UPI, Indian context)
- **🧠 Agentic architecture** (3 specialized AI agents)
- **🎯 Gig worker focused** (delivery, auto, freelance)
- **⚡ Production ready** with enterprise error handling

## 🛠️ Tech Stack

### **Backend** (`/backend`)
- **Framework:** Django + Django REST Framework
- **AI Engine:** Cerebras Llama3.1-8B via OpenAI-compatible API
- **Architecture:** Agentic system with specialized financial agents
- **Database:** SQLite (dev), PostgreSQL ready
- **APIs:** 3 specialized endpoints for different use cases

### **Frontend** (`/frontend`)
- **Framework:** React 18+ with modern hooks
- **Styling:** Custom CSS with responsive design
- **UI/UX:** Professional chat interface with real-time metrics
- **State Management:** React useState + useEffect
- **HTTP Client:** Axios for API communication

## 📊 System Architecture

┌───────────────────────────────────────────────────────────────┐
│                  MONEYMITRA AGENTIC AI SYSTEM                 │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐  │
│   │  FRONTEND    │◄──► │   BACKEND    │◄──► │   AI ENGINE  │  │
│   │   (React)    │     │  (Django)    │     │  (Cerebras)  │  │
│   ├──────────────┤     ├──────────────┤     ├──────────────┤  │
│   │ - Profile UI │     │ - REST APIs  │     │ - 3 AI Agents│  │
│   │ - Chat UI    │     │ - Error Mgmt │     │ - Llama3.1-8B│  │
│   │ - Real-time  │     │ - Production │     │ - <200ms Rsp │  │
│   │ - Responsive │     │ - Context Mgt│     │ - OpenAI API │  │
│   └──────────────┘     └──────────────┘     └──────────────┘  │
│                                                               │
├───────────────────────────────────────────────────────────────┤
│                        LOGICAL COMPONENTS                     │
│                                                               │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐  │
│   │USER INTERFACE│     │   API LAYER  │     │   AI AGENTS  │  │
│   ├──────────────┤     ├──────────────┤     ├──────────────┤  │
│   │ - Chat Msgs  │     │ /api/health/ │     │ quick_chat() │  │
│   │ - Profiles   │     │ /api/advice/ │     │ advice_agent │  │
│   │ - Analytics  │     │ /api/analyze/│     │ spend_agent  │  │
│   │ - Errors     │     │ /api/chat/   │     │ context_build│  │
│   └──────────────┘     └──────────────┘     └──────────────┘  │
│                                                               │
├───────────────────────────────────────────────────────────────┤
│                           DATA FLOW                           │
│                                                               │
│ User Input → Profile Context → AI Agent → Cerebras API → Smart│
│ Response → React UI → Django Logic → LLM Processing → JSON Out│
└───────────────────────────────────────────────────────────────┘



## **🔄 Request Flow**

USER INTERACTION
├── Profile Setup (Occupation, Income, Goals)
└── Chat Message

FRONTEND PROCESSING
├── Form Validation
├── Context Building
└── API Request (Axios)

BACKEND PROCESSING
├── Request Validation
├── Agent Selection
└── Context Enhancement

AI PROCESSING
├── Prompt Engineering
├── Cerebras API Call
└── Response Formatting

RESPONSE DELIVERY
├── Error Handling
├── Performance Metrics
└── UI Update


## **🧠 AI Agent Architecture**

┌──────────────────────────────────────────────┐
│             SIMPLE FINANCIAL AGENT           │
├──────────────────────────────────────────────┤
│                                              │
│   ┌──────────────┐        ┌──────────────┐   │
│   │  QUICK CHAT  │        │  FULL ADVICE │   │
│   ├──────────────┤        ├──────────────┤   │
│   │ - Real-time  │        │ - Deep       │   │
│   │ - Contextual │        │   Analysis   │   │
│   │ - <200ms Rsp │        │ - Planning   │   │
│   └──────────────┘        └──────────────┘   │
│             │                    │           │
│             └──────────┬─────────┘           │
│                        │                     │
│        ┌────────────────────────────────┐    │
│        │        SPENDING ANALYZER       │    │
│        ├────────────────────────────────┤    │
│        │ - Transaction Processing       │    │
│        │ - Pattern Recognition          |    │
│        │ - Actionable Insights          │    │
│        └────────────────────────────────┘    │
│                                              │
└──────────────────────────────────────────────┘


## 🚀 Quick Start

### **Prerequisites**
- Python 3.8+
- Node.js 16+
- Cerebras API Key

### **Backend Setup**
- cd backend/django_services
- python -m venv env
- source env/bin/activate # Windows: .\env\Scripts\activate
- pip install -r requirements.txt
- python manage.py runserver 8000

### **Frontend Setup**
- cd frontend
- npm init -y
- npm install react react-dom react-scripts axios lucide-react
- npm install --save-dev eslint prettier
- npm install
- npm start # Runs on http://localhost:3000

### **Environment Configuration**
- backend/django_services/.env
- CEREBRAS_API_KEY=your_cerebras_api_key_here
- DEBUG=True

## 💡 Demo Scenarios

### **Delivery Driver**
- **Income:** ₹18,000-25,000/month (irregular)
- **Question:** "How can I save ₹5000 in 3 months?"
- **Response:** Route optimization, daily savings targets, UPI tracking

### **Auto Driver**
- **Income:** ₹12,000-20,000/month (daily variation)
- **Question:** "Emergency fund strategy for irregular income?"
- **Response:** CNG cost management, festival planning, medical fund

### **Freelancer**
- **Income:** ₹25,000-40,000/month (project-based)
- **Question:** "Investment options for ₹10,000 surplus?"
- **Response:** SIP planning, risk assessment, tax-saving instruments

## 📈 Impact Metrics
- **Target Users:** 400M+ Indians with irregular income
- **Response Time:** <200ms (3x faster than traditional solutions)
- **Market Size:** $50B+ underserved financial services market
- **Languages:** Hindi + English cultural context

## 👥 Team
- **Varun Bhat P** - AI/ML Engineer & Team Lead
- **Pavan A Kustagi** - Full-stack Developer
- **Prateek Bhat** - UI/UX Designer

## 📞 Contact
- **Demo:** [Live Demo Link]
- **Pitch Deck:** [Presentation Link]
- **Video:** [Demo Video Link]

---
*Making financial coaching accessible to those who need it most. 🇮🇳*

