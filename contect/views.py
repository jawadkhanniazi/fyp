from django.shortcuts import render
from contect.models import Contact
# Create your views here.
def home(request):
    
    return render(request, 'contact.html')

    
def contactUs(request):
    name = request.GET['name']
    email = request.GET['email']
    phone = request.GET['phone']
    cName = request.GET['cName']
    subject = request.GET['subject']
    message = request.GET['message']
   
    ins = Contact(name=name,email=email,phone=phone,cName=cName,sub=subject,message=message)
    ins.save()
    
        #print(name,email,phone,cName,subject,message)
    
    return render(request, 'contact.html')

