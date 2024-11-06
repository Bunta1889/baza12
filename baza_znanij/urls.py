
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls)]
from django.urls import include
from django.urls import path
urlpatterns += [
    path('blog/', include('blog.urls')),  # Убедитесь, что это строка присутствует
]
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]
