from django.urls import path, include
from .views import DashboardView, KPIDetailView, Ibyakozwe

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('kpi/<int:pk>', KPIDetailView.as_view(), name='kpi-detail'),
    path('ibyakozwe', Ibyakozwe.as_view(), name='ibyakozwe'),
    path('ibisigaye', Ibyakozwe.as_view(), name='ibisigaye'),
]