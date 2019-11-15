from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proposals/', views.all_proposal_details, name='prop_all'),
    path('proposals/<int:proposal_no>/', views.proposal_details, name='prop_detail'),
    path('society/', views.all_society_details, name='soc_all'),
    path('society/<str:soc_id>/', views.society_details, name='soc_detail'),
    path('secretary/', views.all_secretaries_details, name='sec_all'),
    path('secretary/<str:sec_id>/', views.secretary_details, name='sec_detail'),
    path('new_society/', views.soc_new, name='soc_new'),
    path('new_sec/', views.sec_new, name='sec_new'),
    path('new_proposal/', views.proposal_new, name='prop_new')
]