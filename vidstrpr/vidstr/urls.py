from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('like_post_profile/<int:pk>', views.like_post_profile, name='like_post_profile'),
    path('like_post_home/<int:pk>', views.like_post_home, name='like_post_home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('message_link/<int:pk>', views.message_link, name='message_link'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
