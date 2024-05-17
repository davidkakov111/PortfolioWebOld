# Imports
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib.auth import views as auth_views

#Home view
def homepage(request):
    return render(request, 'index.html')

#Game view
def game(request):
    return render(request, 'game.html')

#About me view
def aboutme(request):
    return render(request, 'aboutme.html')

#Web3shop view
def web3shop(request):
    return render(request, 'web3shop.html')

#Movie Catalog view
def MovieCatalog(request):
    return render(request, 'moviecatalog.html')

#Handling 404 error view
def handler404(request, exception):
    return render(request, 'handler404.html')

#Sign Up view
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        try:
            #Against multiple registrations.
            email = request.POST.get("email")
            if User.objects.filter(email=email).exists():
                return render(request, "response.html", {"data":"existing account"})
            #Check for identical passwords.
            password = request.POST.get("password")
            password1 = request.POST.get("pasword")
            if password != password1:
                return render(request, "response.html", {"data":"invalid password"})
            #Registration save.
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            #Automatic login.
            UseR = authenticate(request, username=email, password=password)
            login(request, UseR)
            return render(request, "index.html")
        except:
            #Formal error handing.
            return render(request, 'index.html')

#Log In view
def Login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        try:    
            #User authentication.
            username = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                #User login.
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, "response.html", {"data":"unsuccessfullogin"})
        except:
            #Formal error handing.
            return render(request, 'index.html')

#Log Out view
@login_required
def Logout(request):
    logout(request)
    auth_views.LogoutView.as_view()
    return render(request, 'index.html')

#Contact view
@login_required
def contact(request):
    form = ContactForm()
    if request.method == "POST":
        try:
            form = ContactForm(request.POST)
            #Form check.
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                theme = form.cleaned_data['themes']
                message = form.cleaned_data['message']
                #Organizing datas.
                contents1 = [
                    "Name:", name, "Message:", message
                ]
                message_body1 = "\n".join(contents1)
                #Datas send to me.
                email_to_send1 = EmailMessage(
                    subject = theme,
                    body = message_body1,
                    from_email= email, 
                    to = ['kovacsdavid648@gmail.com'],
                    reply_to= [email],
                )
                email_to_send1.send()
                #Instant auto reply in email to user.
                contents2 = [
                    f'Dear {name},', 'I have received your message, and I will respond shortly from the email address kovacsdavid648@gmail.com. Thank you in advance for your patience and understanding!', 'Best regards,', 'Kovács Dávid'
                ]
                message_body2 = "\n".join(contents2)
                email_to_send2 = EmailMessage(
                    subject = "Auto-reply",
                    body =   message_body2,
                    from_email= 'kovacsdavid648@gmail.com', 
                    to = [email],
                    reply_to= ['kovacsdavid648@gmail.com'],
                )
                email_to_send2.send()
                #Finish.
                return render(request, 'contact_response.html', {"name":name})
            else:
                # Formal error handing.
                return render(request, "index.html")
        except:
            # Formal error handing.
            return render(request, "index.html")
    else:
        return render(request, "contact.html", {'form':form})
