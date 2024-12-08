from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
def welcome(request):
    return render(request, 'cartes/welcome.html')  # Affiche le fichier `home.html`

def choisir(request):
    return render(request, 'cartes/choisir.html')  # Affiche le fichier `home.html`

def friends_loading(request):
    return render(request, 'cartes/friends/friends_loading.html') 

def friends(request):
    return render(request, 'cartes/friends/friends.html') 

def family_loading(request):
    return render(request, 'cartes/family/family_loading.html') 

def family(request):
    return render(request, 'cartes/family/family.html') 

def loading(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            request.session['user_name'] = name  # Stocker dans la session
            return render(request, 'cartes/loading.html', {'name': name})
    return redirect('welcome')


def generate_card(request):
    # Récupérer le nom depuis la session ou directement depuis une requête GET/POST
    name = request.session.get('user_name', 'Inconnu')  # Valeur par défaut si aucun nom n'est trouvé
    return render(request, 'cartes/card.html', {'name': name})


def footer(request):
    return render(request, 'cartes/common/footer.html')
def mentions_legales(request):
    return render(request, 'cartes/common/mentions_legales.html')

def politique_confidentialite(request):
    return render(request, 'cartes/common/politique_confidentialite.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Sujet et contenu de l'email
        subject = f"Message de {name}"
        email_message = f"Nom : {name}\nEmail : {email}\n\nMessage :\n{message}"

        try:
            # Envoi de l'email
            send_mail(
                subject,
                email_message,
                email,  # Adresse de l'expéditeur
                ['votre_email_de_reception@example.com'],  # Adresse(s) de destination
            )
            messages.success(request, "Votre message a été envoyé avec succès.")
        except Exception as e:
            messages.error(request, "Une erreur est survenue lors de l'envoi du message.")
    
    return render(request, 'cartes/common/contact.html')