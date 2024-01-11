from django.urls import path
from . import views

urlpatterns = [
    # We anticipate a home function within views.py
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('balls/', views.balls_index, name='index'),
    path('balls/<int:ball_id>/', views.balls_detail, name='detail'),
    path('balls/create', views.BallCreate.as_view(), name='create_ball'),
    path('balls/<int:pk>/update', views.BallUpdate.as_view(), name='update_ball'),
    path('balls/<int:pk>/delete', views.BallDelete.as_view(), name='delete_ball'),
]