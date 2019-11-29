from django.urls import include, path
from . import views
from .api.v1 import views as api_v1


urlpatterns = [
    # render
    path('', views.index, name='index'),
    path('post/<int:id>', views.post, name='post'),
    path('manage', views.manage, name='manage'),
    path('history', views.history, name='history'),

    # api
    path('api/v1/create_post', api_v1.create_post, name='create_post'),
    path('api/v1/read_post', api_v1.read_post, name='inderead_postx'),
    path('api/v1/update_post', api_v1.update_post, name='update_post'),
    path('api/v1/delete_post', api_v1.delete_post, name='delete_post'),
    path('api/v1/read_history', api_v1.read_history, name='read_history'),
]