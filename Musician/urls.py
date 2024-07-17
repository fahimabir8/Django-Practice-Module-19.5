from django.urls import path
from . import views 
urlpatterns = [
    # path('add/',views.add_musician , name= 'add_musician'),
    path('add/',views.AddMusicianView.as_view() , name= 'add_musician'),
    path('del/<int:id>',views.DeleteMusicianView.as_view(), name ='delete_musician'),
    path('edit/<int:id>',views.MusicianUpdateView.as_view(), name ='edit_musician'),
    path('signup/',views.RegisterView.as_view(), name = 'register'),
    path('login/',views.UserLoginView.as_view(), name = 'login'),
    path('logout/',views.UserLogoutView.as_view(), name = 'logout'),
    
    
    
    
]