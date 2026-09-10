"""
URL configuration for govt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from public import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.showindex, name='home'),
    path('showindex',views.showindex, name='showindex'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('insertuserlogin', views.insertuserlogin, name='insertuserlogin'),
    path('insertregister',views.insertregister, name='insertregister'),
    path('insertdepartment',views.insertdepartment, name='insertdepartment'),
    path('insertgrevcat',views.insertgrevcat, name='insertgrevcat'),
    path('insertgrievance',views.insertgrievance, name='insertgrievance'),
    path('insertinfrasset',views.insertinfrasset, name='insertinfrasset'),
    path('insertgrievassign',views.insertgrievassign, name='insertgrievassign'),
    path('insertgrievupdate', views.insertgrievupdate, name='insertgrievupdate'),
    path('insertinframonitor',views.insertinframonitor, name='insertinframonitor'),
    path('insertfeedback',views.insertfeedback, name='insertfeedback'),
    path('insertnotify',views.insertnotify, name='insertnotify'),
    path('insertdocument',views.insertdocument, name='insertdocument'),

    path('viewuserlogin',views.viewuserlogin, name='viewuserlogin'),
    path('viewregister',views.viewregister, name='viewregister'),
    path('viewdepartment',views.viewdepartment, name='viewdepartment'),
    path('viewgrevcat',views.viewgrevcat, name='viewgrevcat'),
    path('viewgriev',views.viewgriev, name='viewgriev'),
    path('viewinasset',views.viewinasset, name='viewinasset'),
    path('viewgassign',views.viewgassign, name='viewgassign'),
    path('viewgupdate',views.viewgupdate, name='viewgupdate'),
    path('viewinmonitor',views.viewinmonitor, name='viewinmonitor'),
    path('viewfeed',views.viewfeed, name='viewfeed'),
    path('viewnotify',views.viewnotify, name='viewnotify'),
    path('viewdocument',views.viewdocument, name='viewdocument'),

    path('delreg/<int:pk>',views.delreg,name='delreg'),
    path('deldept/<int:pk>',views.deldept, name='deldept'),
    path('delgcat/<int:pk>',views.delgcat, name='delgcat'),
    path('delgriev/<int:pk>',views.delgriev, name='delgriev'),
    path('delinasset/<int:pk>',views.delinasset, name='delinasset'),
    path('delgassign/<int:pk>',views.delgassign, name='delgassign'),
    path('delgupdate/<int:pk>',views.delgupdate, name='delgupdate'),
    path('delinmonitor/<int:pk>',views.delinmonitor, name='delinmonitor'),
    path('delfeed/<int:pk>',views.delfeed, name='delfeed'),
    path('delnotify/<int:pk>',views.delnotify, name='delnotify'),
    path('deldoc/<int:pk>',views.deldoc, name='deldoc'),

    path('logcheck',views.logcheck,name='logcheck'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),

    path('public_home',views.public_home,name='public_home'),
    path('officer_home',views.officer_home,name='officer_home'),
    path('govt_home',views.govt_home,name='govt_home'),

    path('r_depart',views.r_depart,name='r_depart'),
    path('water_depart',views.water_depart,name='water_depart'),
    path('elect_depart',views.elect_depart,name='elect_depart'),
    path('san_depart',views.san_depart,name='san_depart'),

    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatbot-message/', views.chatbot_message, name='chatbot_message'),
    path('clear-chat/', views.clear_chat, name='clear_chat'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
