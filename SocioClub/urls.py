
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name = "index"),
    path('login/', views.login , name = "login"),
    path('logout/', views.log_out , name = "logout"),
    path('signup/', views.signup , name = "signup"),
    path('maintenance/', views.maintenance , name = "maintenance"),
    path('event/', views.event , name = "event"),
    path('contact_us/', views.contact_us , name = "contact_us"),
    path('complain/', views.complain_view , name = "complain"),
    path('add_complain/', views.add_complain , name = "add_complain"),
    path('test/', views.test , name = "test"),
    path('sec_main/', views.sec_main, name = "sec_main"),
    path('sec_complain/', views.sec_complain , name = "sec_complain"),
    path('sec_event/', views.sec_event , name = "sec_event"),
    path('delete_main/<int:id>/', views.delete_main , name = "delete_main"),
    # path('user/', include("user_data.urls")),
]
