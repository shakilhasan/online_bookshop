"""online_bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings # new
from django.conf.urls.static import static
from . import views

from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.usignup, name='signup'),
    path('login/', views.ulogin, name='login'),
    path('logout/', views.ulogout, name='logout'),
    path('', include('book_info.urls'), name='book_info'),
    path('', include('buy.urls'), name='buy'),
    path('', include('cgpa.urls'), name='cgpa'),

    path("graphql/", csrf_exempt(PrivateGraphQLView.as_view(graphiql=True))),

    path("update_server/", views.update, name="update"),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
