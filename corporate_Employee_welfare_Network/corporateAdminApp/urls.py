"""corporate_Employee_welfare_Network URL Configuration

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
from django.contrib import admin
from django.urls import path

from corporateAdminApp import views

urlpatterns =[
    # path('admin/', admin.site.urls),
    path('shortlistedUsers/', views.pendingUser, name="pendingusers"),
    path('acceptedusers/', views.acceptedusers, name="acceptedusers"),
    path('rejectedusers/', views.rejectedusers, name="rejectedusers"),
    path('viewacceptedusers/', views.viewacceptedusers, name="viewacceptedusers"),
    path('viewrejectedusers/', views.viewrejectedusers, name="viewrejectedusers"),
    path('viewthoughtAdmin/', views.viewthoughtAdmin, name="viewthoughtAdmin"),
    path('vieweventAdmin/', views.vieweventAdmin, name="vieweventAdmin"),
    path('viewtechAdmin/', views.viewtechAdmin, name="viewtechAdmin"),
    path('viewWorkExpAdmin/', views.viewtWorkExpAdmin, name="viewWorkExpAdmin"),
    path('viewpropertyAdmin/', views.viewpropertyAdmin, name="viewpropertyAdmin"),
    path('viewShareMarketAdmin/', views.viewShareMarketAdmin, name="viewtShareMarketAdmin"),
    path('viewreferenceAdmin/', views.viewreferenceAdmin, name="viewreferenceAdmin"),
    path('viewmatrimonialAdmin/', views.viewmatrimonialAdmin, name="viewmatrimonialAdmin"),
    path('viewcelebrationsAdmin/', views.viewcelebrationsAdmin, name="viewcelebrationsAdmin"),
    path('viewTravelAdmin/', views.viewTravelAdmin, name="viewTravelAdmin"),
    path('logout/',views.logoutAdmin,name="logout")
]