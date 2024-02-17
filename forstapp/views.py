from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .models import Image
from .forms import ImageForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid(): 
         form.save()
    form = ImageForm()
    img = Image.objects.all()
#     send_mail(
#     "Subject here",
#     "Here is the message.",
#     "abrarqureshi790@gmail.com",
#     ["abrarquresi4462@gmail.com"],
#     fail_silently=False,
# )
    return render (request , 'home.html' , { 'img': img,'form': form})

# def send_mail(request):
#     subject = 'welcome this is django mail'
#     message = 'Hi  This is check mail by ABrar dontworry.'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['najeebtareen00@gmail.com' , 'abrarqureshi4462@gmail.com' ]
#     send_mail( subject, message, email_from, recipient_list )
#     return render(request , 'home.html')
    