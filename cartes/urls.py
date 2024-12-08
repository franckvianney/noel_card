from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Associez l'URL de la racine au template 'index.html'
    path('welcome/', views.welcome, name='welcome'),            # Page d'accueil
    path('loading/', views.loading, name='loading'),  # Page de chargement
    path('choisir/', views.choisir, name='choisir'),  # Page de chargement
    
    path('friends_loading/', views.friends_loading, name='friends_loading'),  # Page de chargement
    path('friends/', views.friends, name='friends'),  # Page de chargement
    
    path('family/', views.family, name='family'),  # Page de chargement
    path('family_loading/', views.family_loading, name='family_loading'), 
    # Page de chargement
    path('card/', views.generate_card, name='generate_card'),
    # path('card/', views.card, name='card'),      # Carte finale
    
    path('footer/', views.footer, name='footer'),
    path('mentions-legales/', views.mentions_legales, name='mentions_legales'),
    path('politique-confidentialite/', views.politique_confidentialite, name='privacy_policy'),
    path('contact/', views.contact, name='contact'),
]
