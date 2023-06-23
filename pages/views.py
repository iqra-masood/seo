
from .models import Order, joiners
from .forms import OrderForm
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as  auth_login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout as auth_logout
import csv





def home(req):
    return render(req,'index.html')

def about(req):
    return render(req,'about.html')

def career(req):
    return render(req,'career.html')



def privacy(req):
     return render(req,'privacy.html')


def project(req):
    return render(req,'project.html')

def service(req):
    return render(req,'service.html')

def team(req):
    return render(req,'team.html')

def terms(req):
    return render(req,'terms.html')

def testimonial(req):
    return render(req,'testimonial.html')

#owner pannel data  
def owner(req):
    datao = '' # Default value for the datao variable
    if req.method == "POST":
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        company = req.POST['company']
        service = req.POST['service']
        subject = req.POST['subject']
        message = req.POST['message']
        datao = Order(name=name, email=email, phone=phone, company=company, service=service, subject=subject, message=message)
        datao.save()
       
    data= Order.objects.all()
    context = {
        'datao': datao,
        'dataall' : data,
    }


    return render(req, 'owner.html', context)







def contact(req):
    datao = '' # Default value for the datao variable
    if req.method == "POST":
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        company = req.POST['company']
        service = req.POST['service']
        subject = req.POST['subject']
        message = req.POST['message']
        datao = Order(name=name, email=email, phone=phone, company=company, service=service, subject=subject, message=message)
        datao.save()
        messages.success(req,"Your Form submitted sucessfully!")
    data= Order.objects.all()
    context = {
        'datao': datao,
        'dataall' : data,
    }

    return render(req, "contact.html", context)



def create_joiner(request):
    dataj=''
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        domain = request.POST['domain']
        file = request.FILES['file']
        subject = request.POST['subject']
        message = request.POST['message']
        dataj = joiners(name=name, email=email, phone=phone, domain=domain, file=file, subject=subject, message=message)
        dataj.save()
        messages.success(request,"Your application submitted sucessfully!")
    data2= joiners.objects.all()
    context = {
        'dataj': dataj,
        'dataall' : data2,
    }
    return render(request, "joiners.html", context)



def signup(request):
    if request.method =='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render (request,'signup.html')

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use .get() instead of [] for QueryDict
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            auth_login(request, user)  # Rename the function to auth_login to avoid conflict
            
            # Redirect to the user panel based on user type
            if user.is_superuser:
                return redirect('owner')  # Update the redirect URL
            else:
                return redirect('login')  # Update the redirect URL
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password. Please try again.'})
    else:
        return render(request, 'login.html')
    
    


def logout(request):
     auth_logout(request)
     request.session.flush()
     request.session.set_expiry(-1)
     
     return redirect('login') 



# Delete View
def Delete_record(request,id):
    a=Order.objects.get(pk=id)
    a.delete()
    return redirect('/contact')
    

# Update View
def update(request,id):
    if request.method=='POST':
        data=Order.objects.get(pk=id)
        form=OrderForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:

        data=Order.objects.get(pk=id)
        form=OrderForm(instance=data)
    context={
        'form':form,
    }

    
    return render (request,'update.html',context)


    
#download record

def download(request):
    # Retrieve the data for the CSV file (replace with your data retrieval logic)
    data = Order.objects.all()
    
    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="records.csv"'

    # Write the data to the CSV file
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Email', 'Phone', 'Company', 'Service', 'Subject', 'Message'])
    for record in data:
        writer.writerow([record.id, record.name, record.email, record.phone, record.company, record.service, record.subject, record.message])

    return response





