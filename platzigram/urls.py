# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from posts import views as posts_views
from users import views as users_views
from django.views.generic import TemplateView
urlpatterns = [

    path('admin/', admin.site.urls),
    path('posts/', posts_views.list_posts, name='feed'),
    path('posts/new/', posts_views.create_post, name='create'),

    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update'),
    path('users/<str:username>/',  view=TemplateView.as_view(template_name='users/detail.html'),
        name='detail')
   
    # path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    # path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)