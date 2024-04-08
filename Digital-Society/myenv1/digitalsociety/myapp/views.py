from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.urls import reverse
import random
"""
    Django ORM(object relational method)

    get() : data retrive karna ho to get method aati hai , fetch data from model and return object but only single records
        if there are multiple record found with given condition it will thrown an exception

"""

# Create your views here.
def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairmen.objects.get(userid = uid)
        context = {
                'uid' : uid,
                'cid' : cid, 
            }
        return render(request,'myapp/index.html',context)
    else:
        return render(request,'myapp/login.html')

def login(request):
    if "email" in request.session:
        return HttpResponseRedirect(reverse("home"))
        """uid = User.objects.get(email = request.session['email'])
        cid = Chairmen.objects.get(userid = uid)
        context = {
                'uid' : uid,
                'cid' : cid, 
            }
        return render(request,'myapp/index.html',context)"""
    else:
        if request.POST:
            try:
                print("------------ page loaded")
                p_email = request.POST["email"]
                print("------------>> email ",p_email)
                p_password = request.POST["password"]
                print("-----> password",p_password)
                uid = User.objects.get(email = p_email ,password = p_password)
                print("=============================>>> object ",uid)
                print("---------->",uid.role)
                cid = Chairmen.objects.get(userid = uid)
                print("------------->firstname",cid.firstname)

                request.session['email'] = uid.email
                return HttpResponseRedirect(reverse("home"))
                #return render(request,"myapp/login.html")
                #context = {
                #    'uid' : uid,
                #    'cid' : cid, 
                #}
                #return render(request,"myapp/index.html",context)
            except Exception as e:
                print("----------------------------->Email",e)
                msg = "Invalid Email or password"
                return render(request,"myapp/login.html",{'e_msg':msg})
                pass
        else:
            print("----> page loaded")
            return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        #return render(request,"myapp/login.html")
        return HttpResponseRedirect(reverse("login"))
    else:
        #return render(request,"myapp/login.html") 
        return HttpResponseRedirect(reverse("login"))   
            
def profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairmen.objects.get(userid = uid)
        context = {
                'uid' : uid,
                'cid' : cid, 
            }
        return render(request,'myapp/profile.html',context)
    else:
        return HttpResponseRedirect(reverse("login"))
    
def change_password(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairmen.objects.get(userid = uid)
        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']

        if uid.password == currentpassword:
            uid.password = newpassword
            uid.save() #update
            s_msg = "Successfully password change"
            del request.session['email']
            return render(request,'myapp/login.html',{'s_msg':s_msg})
        else:
            e_msg = "Invalid Current Password"
            del request.session['email']
            return render(request,'myapp/login.html',{'e_msg':e_msg})

    else:
        return render(request,'myapp/profile.html')

def change_profile(request):
    if 'email' in request.session:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairmen.objects.get(userid = uid)

            cid.firstname = request.POST['firstname']
            cid.lastname = request.POST['lastname']
            cid.contact = request.POST['contact']
            cid.houseno = request.POST['houseno']
            cid.blockno = request.POST['blockno']
            if "pic" in request.FILES:
                cid.pic = request.FILES['pic']
            cid.save()
        else:
            context = {
                    'uid' : uid,
                    'cid' : cid, 
                }
            return render(request,'myapp/profile.html',context)
    else:
        return render(request,'myapp/profile.html')

def add_member(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairmen.objects.get(userid = uid)

        if request.POST:
                print("---> add operation")
                email = request.POST['email']
                contact = request.POST['contact']
                l1 = ['2w334d','43rsd','9as23','34rfd','9y6f7']
                password = random.choice(l1)+email[3:6]+contact[4:7]
                muid = User.objects.create(email = request.POST['email'],password=password , role='member')

                if muid:
                    mid = Member.objects.create(
                            userid = muid,
                            firstname = request.POST['firstname'],
                            lastname = request.POST['lastname'],
                            contact = request.POST['contact'],
                            blockno = request.POST['blockno'],
                            houseno = request.POST['houseno'],
                            occupation = request.POST['occupation'],
                            job_address = request.POST['job_address'],
                            bloodgroup = request.POST['bloodgroup'],
                            vehicle_detail = request.POST['vehicledetails'],
                        )
                    context = {
                    'uid' : uid,
                    'cid' : cid, 
                    's_msg': 'Successfully Member Added'
                    }
                    return render(request,'myapp/addmember.html',context)
        else:
            context = {
                    'uid' : uid,
                    'cid' : cid, 
                }
            return render(request,'myapp/addmember.html',context)
