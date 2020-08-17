from django.urls import path
from . import views

app_name = 'polls'

# path( route, view, kwargs, name )
# urlpatterns = [
#     path('', views.index, name='index'), # /polls/
#     path('<int:question_id>/', views.detail, name='detail'), # /polls/5/
#     path('<int:question_id>/results/', views.results, name='results'), # /polls/5/results/
#     path('<int:question_id>/vote/', views.vote, name='vote'), # /polls/5/vote/
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # /polls/5/vote/
]