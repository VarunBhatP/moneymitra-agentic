from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
import json
import os
import time

# Import Cerebras agent
try:
    from agents.financial_crew import SimpleFinancialAgent
    AGENT_AVAILABLE = True
except ImportError:
    AGENT_AVAILABLE = False
    print("⚠️ SimpleFinancialAgent not available - using mock mode")

@api_view(['GET'])
def health_check(request):
    """Enhanced health check with Cerebras status"""
    cerebras_status = "unknown"
    
    if AGENT_AVAILABLE:
        try:
            from agents.financial_crew import test_cerebras_connection
            if test_cerebras_connection():
                cerebras_status = "connected"
            else:
                cerebras_status = "connection_failed"
        except:
            cerebras_status = "error"
    
    return Response({
        'status': 'healthy',
        'service': 'MoneyMitra Financial Coaching API - Production Ready',
        'timestamp': datetime.now().isoformat(),
        'version': '2.0.0',
        'cerebras_status': cerebras_status,
        'endpoints': [
            '/api/health/',
            '/api/quick-chat/',
            '/api/financial-advice/',
            '/api/analyze-spending/',
            '/api/test/'
        ]
    })

@api_view(['POST'])
@csrf_exempt
def quick_financial_chat(request):
    """Quick chat with Cerebras-powered financial agent"""
    start_time = time.time()
    
    try:
        question = request.data.get('question', '')
        context = request.data.get('context', {})
        
        if not question:
            return Response({
                'success': False,
                'error': 'No question provided',
                'example': {
                    'question': 'How can I save money as a delivery driver?',
                    'context': {'income': '20000', 'expenses': '18000', 'occupation': 'delivery driver'}
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if AGENT_AVAILABLE:
            try:
                agent = SimpleFinancialAgent()
                result = agent.quick_chat(question, context)
                
                response_time = round((time.time() - start_time) * 1000, 2)  # ms
                
                if result['success']:
                    return Response({
                        'success': True,
                        'response': result['response'],
                        'timestamp': datetime.now().isoformat(),
                        'model': result.get('model', 'Cerebras Llama3.1-8B'),  # ✅ CHANGED HERE
                        'response_time_ms': response_time,
                        'powered_by': 'Cerebras AI'
                    })
                else:
                    # Use fallback response if Cerebras fails
                    return Response({
                        'success': True,
                        'response': result.get('fallback_response', 'Technical issue occurred. Please try again.'),
                        'timestamp': datetime.now().isoformat(),
                        'model': 'Fallback Mode',
                        'error_details': result.get('error', 'Unknown error')
                    })
                    
            except Exception as e:
                return Response({
                    'success': False,
                    'error': f'Agent error: {str(e)}',
                    'timestamp': datetime.now().isoformat()
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({
                'success': False,
                'error': 'Financial agent not available. Please check configuration.',
                'timestamp': datetime.now().isoformat()
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
    except Exception as e:
        return Response({
            'success': False,
            'error': f'Request processing error: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@csrf_exempt
def get_financial_advice(request):
    """Comprehensive financial coaching using Cerebras AI"""
    start_time = time.time()
    
    try:
        user_data = request.data
        
        if not user_data:
            return Response({
                'success': False,
                'error': 'No user data provided',
                'required_fields': ['income_pattern', 'income_range', 'occupation', 'monthly_expenses', 'current_savings', 'goals']
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if AGENT_AVAILABLE:
            try:
                agent = SimpleFinancialAgent()
                advice_result = agent.get_financial_advice(user_data)
                
                response_time = round((time.time() - start_time) * 1000, 2)
                
                if advice_result['success']:
                    return Response({
                        'success': True,
                        'advice': advice_result['advice'],
                        'user_profile': advice_result.get('user_profile', {}),
                        'timestamp': datetime.now().isoformat(),
                        'model': advice_result.get('model_used', 'Cerebras Llama3.1-8B'),  # ✅ CHANGED HERE
                        'response_time_ms': response_time,
                        'analysis_type': 'comprehensive'
                    })
                else:
                    return Response({
                        'success': True,
                        'advice': advice_result.get('fallback_advice', 'Basic financial advice provided due to technical issues.'),
                        'timestamp': datetime.now().isoformat(),
                        'model': 'Fallback Mode',
                        'error_details': advice_result.get('error')
                    })
                    
            except Exception as e:
                return Response({
                    'success': False,
                    'error': f'Financial analysis error: {str(e)}',
                    'timestamp': datetime.now().isoformat()
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({
                'success': False,
                'error': 'Financial agent not available',
                'timestamp': datetime.now().isoformat()
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
    except Exception as e:
        return Response({
            'success': False,
            'error': f'Request error: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@csrf_exempt
def analyze_spending_pattern(request):
    """AI-powered spending pattern analysis"""
    start_time = time.time()
    
    try:
        transactions = request.data.get('transactions', [])
        user_context = request.data.get('user_context', {})
        
        if not transactions:
            return Response({
                'success': False,
                'error': 'No transaction data provided',
                'example': {
                    'transactions': [
                        {'amount': '500', 'category': 'food', 'date': '2025-10-14'},
                        {'amount': '200', 'category': 'fuel', 'date': '2025-10-14'}
                    ],
                    'user_context': {'occupation': 'delivery driver', 'income': '20000'}
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Basic analysis (always available)
        total_spent = 0
        categories = {}
        daily_spending = {}
        
        for transaction in transactions:
            try:
                amount = float(transaction.get('amount', 0))
                category = transaction.get('category', 'other').lower()
                date = transaction.get('date', 'unknown')
                
                total_spent += amount
                categories[category] = categories.get(category, 0) + amount
                daily_spending[date] = daily_spending.get(date, 0) + amount
                
            except (ValueError, TypeError):
                continue
        
        basic_analysis = {
            'total_spent': total_spent,
            'category_breakdown': categories,
            'transaction_count': len(transactions),
            'average_transaction': round(total_spent / len(transactions), 2) if transactions else 0,
            'top_categories': sorted(categories.items(), key=lambda x: x[1], reverse=True)[:3]
        }
        
        response_time = round((time.time() - start_time) * 1000, 2)
        
        if AGENT_AVAILABLE:
            try:
                agent = SimpleFinancialAgent()
                ai_result = agent.analyze_spending_with_ai(transactions, user_context)
                
                if ai_result['success']:
                    return Response({
                        'success': True,
                        'basic_analysis': basic_analysis,
                        'ai_insights': ai_result['ai_insights'],
                        'timestamp': datetime.now().isoformat(),
                        'response_time_ms': response_time,
                        'analysis_type': 'ai_powered'
                    })
                else:
                    # Return basic analysis if AI fails
                    return Response({
                        'success': True,
                        'basic_analysis': basic_analysis,
                        'ai_insights': 'AI analysis temporarily unavailable. Basic analysis provided.',
                        'timestamp': datetime.now().isoformat(),
                        'response_time_ms': response_time,
                        'analysis_type': 'basic'
                    })
                    
            except Exception as e:
                return Response({
                    'success': True,
                    'basic_analysis': basic_analysis,
                    'ai_insights': f'AI analysis error: {str(e)}. Basic analysis provided.',
                    'timestamp': datetime.now().isoformat(),
                    'response_time_ms': response_time,
                    'analysis_type': 'basic_fallback'
                })
        else:
            return Response({
                'success': True,
                'basic_analysis': basic_analysis,
                'ai_insights': 'AI analysis not available. Showing basic spending breakdown.',
                'timestamp': datetime.now().isoformat(),
                'response_time_ms': response_time,
                'analysis_type': 'basic_only'
            })
        
    except Exception as e:
        return Response({
            'success': False,
            'error': f'Analysis error: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def test_endpoint(request):
    """Enhanced test endpoint"""
    cerebras_test = False
    
    if AGENT_AVAILABLE and request.method == 'POST':
        try:
            from agents.financial_crew import test_cerebras_connection
            cerebras_test = test_cerebras_connection()
        except:
            pass
    
    return Response({
        'message': 'MoneyMitra API - Production Ready! 🚀',
        'method': request.method,
        'timestamp': datetime.now().isoformat(),
        'agent_available': AGENT_AVAILABLE,
        'cerebras_test': cerebras_test if request.method == 'POST' else 'run POST to test',
        'data_received': request.data if request.method == 'POST' else None,
        'status': 'All systems operational'
    })
