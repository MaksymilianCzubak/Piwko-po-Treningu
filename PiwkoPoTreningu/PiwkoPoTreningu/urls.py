"""PiwkoPoTreningu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from PortalTreningowy.views import (
    MainView,
    LoginView,
    LogoutView,
    PlanList,
    DetailedPlan,
    EditPlan,
    NoteList,
    Vo2max_View,
    MasaView
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', MainView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name='logout'),
    path('plans', PlanList.as_view(), name='plans'),
    path('detailed_plan/<int:plan_id>', DetailedPlan.as_view(), name='detailed_plan'),
    path('plan_edit/<int:training_session_id>', EditPlan.as_view(), name='edit_plan_details'),
    path('note_list', NoteList.as_view(), name='note_list'),
    path('vo2max_plot', Vo2max_View.as_view(), name='vo2max_view'),
    path('mass', MasaView.as_view(), name='masa_view'),
]

urlpatterns += staticfiles_urlpatterns()