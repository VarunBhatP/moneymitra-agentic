import openai
import os
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv()

class SimpleFinancialAgent:
    def __init__(self):
        # Configure Cerebras OpenAI client
        self.client = openai.OpenAI(
            api_key=os.getenv("CEREBRAS_API_KEY"),
            base_url="https://api.cerebras.ai/v1"
        )
        
    def quick_chat(self, question, context={}):
        """Quick financial advice using Cerebras"""
        try:
            # Build context string
            income = context.get('income', 'N/A')
            expenses = context.get('expenses', 'N/A')
            occupation = context.get('occupation', 'gig worker')
            location = context.get('location', 'India')
        
            context_prompt = f"""User Profile:
- Occupation: {occupation}
- Monthly Income: ₹{income}
- Monthly Expenses: ₹{expenses}
- Location: {location}"""
        
            system_prompt = """You are MoneyMitra, a friendly AI financial coach specializing in helping Indian gig workers, delivery drivers, auto drivers, and people with irregular income. 

Key Guidelines:
- Give practical, actionable advice in simple Hindi/English
- Understand Indian financial tools (UPI, digital wallets, bank accounts)
- Consider irregular income challenges
- Be encouraging and supportive
- Keep responses concise but helpful (3-5 sentences)
- Include specific amount suggestions when relevant"""

            # Create OpenAI client for this request
            client = openai.OpenAI(
                api_key=os.getenv("CEREBRAS_API_KEY"),
                base_url="https://api.cerebras.ai/v1"
            )

            response = client.chat.completions.create(
                model="llama3.1-8b",  # CHANGED FROM llama3.1-70b
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"{context_prompt}\n\nQuestion: {question}"}
                ],
                max_tokens=500,
                temperature=0.1
            )
        
            return {
                'success': True,
                'response': response.choices[0].message.content,
                'model': 'Cerebras Llama3.1-8B'  # UPDATED DISPLAY NAME
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'fallback_response': f"I understand you're asking about: {question}. While I'm experiencing technical issues, here's basic advice: Track your daily earnings and expenses, save 10-15% when possible, and build an emergency fund gradually."
            }

    def get_financial_advice(self, user_data):
        """Comprehensive financial analysis using Cerebras"""
        try:
            # Extract user data
            income_pattern = user_data.get('income_pattern', 'irregular')
            income_range = user_data.get('income_range', '15000-25000')
            occupation = user_data.get('occupation', 'gig worker')
            monthly_expenses = user_data.get('monthly_expenses', '15000')
            current_savings = user_data.get('current_savings', '2000')
            goals = user_data.get('goals', 'save money')
            family_size = user_data.get('family_size', '3-4 members')
            location = user_data.get('location', 'urban India')
            transactions = user_data.get('recent_transactions', [])
            
            # Build comprehensive prompt
            prompt = f"""As MoneyMitra, provide comprehensive financial coaching for this Indian user:

USER PROFILE:
- Occupation: {occupation}
- Income Pattern: {income_pattern}
- Monthly Income Range: ₹{income_range}
- Monthly Expenses: ₹{monthly_expenses}
- Current Savings: ₹{current_savings}
- Financial Goals: {goals}
- Family Size: {family_size}
- Location: {location}

RECENT TRANSACTIONS:
{json.dumps(transactions, indent=2) if transactions else 'No recent transaction data provided'}

Please provide a detailed analysis covering:

1. FINANCIAL HEALTH ASSESSMENT
   - Current financial position analysis
   - Income vs expenses evaluation
   - Savings rate assessment

2. RISK ANALYSIS
   - Identify immediate financial risks (next 30 days)
   - Medium-term concerns (3-6 months)
   - Emergency fund adequacy

3. PERSONALIZED RECOMMENDATIONS
   - 3 immediate actions (this week)
   - 3 short-term strategies (next 3 months)
   - 2 long-term goals (6+ months)

4. PRACTICAL TIPS
   - Specific to {occupation} and irregular income
   - Include Indian financial tools and cultural context
   - Realistic amount targets based on their income level

Keep advice practical, encouraging, and culturally relevant for Indian users."""

            response = self.client.chat.completions.create(
                model="llama3.1-8b",  # CHANGED FROM llama3.1-70b
                messages=[
                    {"role": "system", "content": "You are MoneyMitra, an expert financial coach for Indian gig workers and people with irregular income. Provide detailed, practical, and culturally relevant financial advice."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.1
            )
            
            return {
                'success': True,
                'advice': response.choices[0].message.content,
                'model_used': 'Cerebras Llama3.1-8B',  # UPDATED DISPLAY NAME
                'user_profile': {
                    'occupation': occupation,
                    'income_pattern': income_pattern,
                    'risk_level': self._assess_risk_level(current_savings, monthly_expenses)
                }
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'fallback_advice': f"Financial coaching for {occupation}: Focus on tracking daily earnings, saving 10-15% when possible, and building emergency fund gradually. Consider your irregular income pattern when planning expenses."
            }
    
    def analyze_spending_with_ai(self, transactions, user_context={}):
        """AI-powered spending analysis"""
        try:
            if not transactions:
                return {'success': False, 'error': 'No transactions provided'}
            
            # Calculate basic metrics
            total_spent = sum(float(t.get('amount', 0)) for t in transactions)
            categories = {}
            for t in transactions:
                cat = t.get('category', 'other').lower()
                categories[cat] = categories.get(cat, 0) + float(t.get('amount', 0))
            
            # Get AI insights
            prompt = f"""Analyze this spending pattern for an Indian gig worker:

TRANSACTIONS DATA:
{json.dumps(transactions, indent=2)}

SPENDING SUMMARY:
- Total Spent: ₹{total_spent}
- Category Breakdown: {categories}

USER CONTEXT:
- Occupation: {user_context.get('occupation', 'gig worker')}
- Monthly Income: ₹{user_context.get('income', 'irregular')}

Provide:
1. SPENDING INSIGHTS (3-4 key observations)
2. RISK WARNINGS (if any category is too high)
3. OPTIMIZATION SUGGESTIONS (2-3 specific recommendations)
4. MONEY-SAVING TIPS (tailored to their occupation)

Keep response concise and actionable."""

            response = self.client.chat.completions.create(
                model="llama3.1-8b",  # CHANGED FROM llama3.1-70b
                messages=[
                    {"role": "system", "content": "You are MoneyMitra, analyzing spending patterns for Indian gig workers. Provide practical insights and actionable recommendations."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=0.1
            )
            
            return {
                'success': True,
                'ai_insights': response.choices[0].message.content,
                'basic_analysis': {
                    'total_spent': total_spent,
                    'categories': categories,
                    'transaction_count': len(transactions)
                }
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _assess_risk_level(self, savings, monthly_expenses):
        """Simple risk assessment"""
        try:
            savings_ratio = float(savings) / float(monthly_expenses)
            if savings_ratio < 0.1:
                return "High Risk"
            elif savings_ratio < 0.3:
                return "Medium Risk"
            else:
                return "Low Risk"
        except:
            return "Unknown"

# Test function
def test_cerebras_connection():
    """Test Cerebras API connection"""
    try:
        agent = SimpleFinancialAgent()
        result = agent.quick_chat(
            "How can I save money as a delivery driver?", 
            {"income": "20000", "occupation": "delivery driver"}
        )
        print("✅ Cerebras connection successful!")
        if result.get('success'):
            print(f"Response: {result.get('response', 'No response content')}")
        else:
            print(f"Response error: {result.get('error', 'Unknown error')}")
        return True
    except Exception as e:
        print(f"❌ Cerebras connection failed: {e}")
        return False

if __name__ == "__main__":
    test_cerebras_connection()
