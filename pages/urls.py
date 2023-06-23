
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.Delete_record, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('joiners/', views.create_joiner, name='joiners'),
    path('privacy/', views.privacy, name='privacy'),
    path('project/', views.project, name='project'),
    path('service/', views.service, name='service'),
    path('terms/', views.terms, name='terms'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('owner/', views.owner, name='owner'),
    path('download-records/', views.download, name='download_records'),
    

    
    #path('joiners/create/', views.joiners_create, name='joiners_create'),
]



