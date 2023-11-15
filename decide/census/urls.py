from django.urls import path, include
from . import views
from .views import *

urlpatterns = [ 
    path('', views.CensusCreate.as_view(), name='census_create'),
    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
    path('reuse/<int:old_voting>/<int:new_voting>/',views.reuseCensus, name='reuse_census'),
    path('showAll/', views.censusShow, name='show_all_census'),
    path('reuseView/',views.reuseview, name='reuse_view'),
]
