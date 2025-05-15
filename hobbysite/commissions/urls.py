from django.urls import path
from .views import CommissionListView, commission_detail, commission_create, commission_update

urlpatterns = [
    path('list', CommissionListView.as_view(), name='commissions'),
    path('detail/<int:pk>', commission_detail, name='commission'),
    path('add', commission_create, name='commission-create'),
    path('<int:pk>/edit', commission_update, name='commission-edit')
]

app_name = "commissions"
