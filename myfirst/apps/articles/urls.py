from django.urls import path
from django.conf.urls import include

from . import views
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='articles'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('grappelli/', include('grappelli.urls')),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),

]
