"""
URL configuration for studmanage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from studmanage import settings
import app1.views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app1.views.home_page,name='home'),
    path('log/',app1.views.login_page,name='log'),
    path('reg/',app1.views.form_page,name='reg'),

    path('a_page',app1.views.admin_page,name='a_page'),
    path('student',app1.views.student_page,name='student'),
    path('staff_p',app1.views.staff_page,name='staff_p'),

    path('a_view',app1.views.aview_page,name='a_view'),
    path('staff_v',app1.views.sview_page,name='staff_v'),
    path('student_v',app1.views.studview_page,name='student_v'),

    path('d_user/<id>',app1.views.delete,name='d_user'),
    path('detail/',app1.views.edit_detail,name='detail'),
    path('stud_del/',app1.views.stud_detail,name='stud_del')

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
