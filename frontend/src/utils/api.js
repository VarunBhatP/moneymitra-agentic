import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000,
});

export const api = {
  checkHealth: async () => {
    const response = await apiClient.get('/health/');
    return response.data;
  },

  quickChat: async (question, context = {}) => {
    const response = await apiClient.post('/quick-chat/', {
      question,
      context
    });
    return response.data;
  },

  getFinancialAdvice: async (userData) => {
    const response = await apiClient.post('/financial-advice/', userData);
    return response.data;
  },

  analyzeSpending: async (transactions, userContext = {}) => {
    const response = await apiClient.post('/analyze-spending/', {
      transactions,
      user_context: userContext
    });
    return response.data;
  }
};

export default api;
