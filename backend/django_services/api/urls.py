from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('quick-chat/', views.quick_financial_chat, name='quick_chat'),
    path('financial-advice/', views.get_financial_advice, name='financial_advice'),
    path('analyze-spending/', views.analyze_spending_pattern, name='analyze_spending'),
    path('test/', views.test_endpoint, name='test_endpoint'),
]
