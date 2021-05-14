"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from products.views import MainPageView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('users/', include('users.urls', namespace='users')),
    path('subscribes/', include('subscribes.urls', namespace='subscribes')),
    path('favorites/', include('favorites.urls', namespace='favorites')),
    path('infopages/', include('infopages.urls', namespace='infopages')),
    path('feedback/', include('feedback.urls', namespace="feedback")),

    # ################  password_reset #####################

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/passwd/reset.html'), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/passwd/reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/passwd/reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/passwd/reset_complete.html'), name='password_reset_complete'),

    # ################ end password_reset ##################
]

urlpatterns += i18n_patterns(
    path('products/', include('products.urls', namespace='products')),
    path('', MainPageView.as_view(), name='index'),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
