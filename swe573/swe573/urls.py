"""swe573 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from coLearn.views import (
    learning_space_create_view,
    learning_space_edit_view,
    learning_space_view,
    explore_view,
    sign_up_view,
    sign_in_view,
    profile_view,
    profile_edit_view
)

urlpatterns = [
    path('explore/', explore_view),
    path('signup/', sign_up_view),
    path('signin/', sign_in_view),
    path('user/<int:user_id>/', profile_view),
    path('user/<int:user_id>/edit', profile_edit_view),
    path('learningspace/create/', learning_space_create_view),
    path('learningspace/<int:learning_space_id>/', learning_space_view),
    path('learningspace/<int:learning_space_id>/edit/', learning_space_edit_view),
    path('admin/', admin.site.urls),
]

# If DEBUG is true, the url mapping for the media files
# is appended to the urlpatterns. By doing so, media files
# are accessible during local development. 
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )