from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_view, name='data'),                     # Home page, punta a views.index
    path('404/', views.error, name='404'),                   # Pagina 404 personalizzata
    path('contact/', views.contact, name='contact'),         # Pagina contatti
    path('login/', views.login, name='login'),               # Pagina di login
    path('password-reset/', views.password_reset, name='password-reset'),  # Pagina reset password
    path('register/', views.register, name='register'),      # Pagina di registrazione

    #path('data/', views.data, name='data'),                  # Pagina iniziale "data"
    path('data/', views.data_view, name='data_view'),   # Pagina che carica i dati per il menu a tendina
   
    path('set-life-expectancy/', views.set_life_expectancy, name='set-life-expectancy'),  # Imposta l'aspettativa di vita

    path('index/', views.index, name='index'),               # Definisci la vista per il template index.html
]

