from django.urls import path
from django.contrib import admin
from .views import BlogListView, BlogDetailView
from django.urls import include

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('', BlogDetailView.as_view(), name='blog_detail'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
