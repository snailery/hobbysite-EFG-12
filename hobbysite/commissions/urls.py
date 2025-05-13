from django.urls import path
from .views import CommissionListView, CommissionDetailView, commission_create, commission_update

urlpatterns = [
    path('list', CommissionListView.as_view(), name='commissions'),
    path('detail/<int:pk>', CommissionDetailView.as_view(), name='commission'),
    path('add', commission_create, name='commission-create'),
    path('<int:pk>/edit', commission_update, name='commission-edit')
]

app_name = "commissions"
