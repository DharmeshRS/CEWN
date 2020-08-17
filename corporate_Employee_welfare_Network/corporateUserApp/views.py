from django.shortcuts import render, redirect,HttpResponse
from corporateUserApp.forms import NewRegistrationForm
from corporateUserApp.models import NewRegistrationModel
from corporateUserApp.models import UserEventModel
from corporateUserApp.models import UserThoughtModel
from corporateUserApp.models import UserTechnicalDetailsModel
from corporateUserApp.models import UserWorkExperienceModel
from corporateUserApp.models import UserPropertyModel
from corporateUserApp.models import UserShareMarketModel
from corporateUserApp.models import UserReferenceModel
from corporateUserApp.models import UserCelebrationModel
from corporateUserApp.models import UserTravelModel
from corporateUserApp.models import UserMatrimonialModel


# from corporateUserApp.models import UserEventModel
# from corporateUserApp.models import UserEventModel


from django.contrib import messages
# Create your views here.
def newRegistration(request):
    return render(request, "commom/registrationform.html")


def saveregistration(request):
    username=request.POST["username"]
    password=request.POST["password"]
    address=request.POST["address"]
    email=request.POST["email"]
    contact=request.POST["contact"]
    dob=request.POST["dob"]
    company=request.POST["company"]
    status="Pending"
    usertype="User"
    NewRegistrationModel(Username=username,Password=password,Address=address,
                         EmailID=email,ContactNo=contact,DOB=dob,Company_Name=company,
                         status=status,usertype=usertype).save()
    messages.success(request,"Registration Successfully....!Note:plz note your Username and Password")
    return redirect('login')


def userlogin_validate(request):
    username=request.POST["username"]
    password=request.POST["password"]
    usertype=request.POST["usertype"]
    accept="accept"
    reject="reject"
    print(username,password,usertype)
    try:
        if NewRegistrationModel.objects.get(Username=username,Password=password,usertype=usertype,status=accept):
            if usertype=="User":
                #session take place
                messages.success(request, "Login Successfully By User.")
                return render(request,"userhomepage.html")
            else:
                messages.success(request, "Login Successfully By Admin.")
                return render(request,"adminhomepage.html")
    except NewRegistrationModel.DoesNotExist:
        try:
            nr=NewRegistrationModel.objects.get(Username=username)
            abc=nr.status
            print(abc)
            if abc=="reject":
                messages.error(request, "Sorry..!Your Application Is Rejected")
            else:
                messages.error(request, "Ohh..!Your Application Is Pending Now")
            return redirect("login")
        except NewRegistrationModel.DoesNotExist:
            messages.error(request, "Invalid Username/Password")
            return redirect("login")



def addThought(request):
    reg=NewRegistrationModel.objects.all()
    return render(request,"User/thought/addthought.html")

def saveThought(request):
    username=request.POST["username"]
    desc=request.POST["description"]
    contact=request.POST["contact"]
    status="Pending"
    UserThoughtModel(Username=username,Description=desc,Contact_no=contact,status=status).save()
    messages.success(request,"Thought Saved")
    return render(request, "User/thought/addthought.html")


def viewThought(request):
    thought=UserThoughtModel.objects.all()
    print(thought)
    return render(request,"User/thought/Viewthought.html",{"reg":thought})


def addEvent(request):
    return render(request, "User/Events/AddEvent.html")


def viewEvents(request):
    reg= UserEventModel.objects.all()
    return render(request, "User/Events/ViewEvents.html",{"reg":reg})


def saveEvent(request):
    username = request.POST["username"]
    sdate = request.POST["startdate"]
    enddate = request.POST["enddate"]
    desc = request.POST["desciption"]
    contact = request.POST["contact"]
    status = "Pending"
    UserEventModel(Username=username, start_date=sdate, end_date=enddate,
                   Description=desc, Contact_no=contact,status=status).save()
    messages.success(request, "Event Saved")
    return render(request, "User/Events/AddEvent.html")


def addtechskills(request):
    return render(request, "User/Technical Skills/addTechSkill.html")


def savetechskills(request):
    username = request.POST["username"]
    tech = request.POST["technology"]
    desc = request.POST["desciption"]
    contact = request.POST["contact"]
    UserTechnicalDetailsModel(Username=username, Technology=tech,
                   Description=desc, Contact_no=contact).save()
    messages.success(request, "Technical Details Are Saved")
    return render(request, "User/Technical Skills/addTechSkill.html")


def viewtechskills(request):
    reg= UserTechnicalDetailsModel.objects.all()
    return render(request, "User/Technical Skills/ViewTS.html",{"reg":reg})



def addworkexp(request):
    return render(request, "User/work Exp/addWorkExp.html")


def saveworkexp(request):
    username = request.POST["username"]
    tech = request.POST["technology"]
    workexp = request.POST["workexp"]
    desc = request.POST["desciption"]
    contact = request.POST["contact"]
    UserWorkExperienceModel(Username=username, Technology=tech,work_exp=workexp,
                              Description=desc, Contact_no=contact).save()
    messages.success(request, "Experience Saved")
    return render(request, "User/work Exp/addWorkExp.html")


def viewworkexp(request):
    reg=UserWorkExperienceModel.objects.all()
    return render(request, "User/work Exp/ViewWorkExp.html",{"reg":reg})


def addPropertyDetails(request):
    return render(request,"User/Property/addproperty.html")


def savePropertyDetails(request):
    username = request.POST["username"]
    ptype = request.POST["propertyType"]
    ptitle = request.POST["propertytitle"]
    area = request.POST["area"]
    price = request.POST["price"]
    address = request.POST["address"]
    contact = request.POST["contact"]
    email = request.POST["email"]
    UserPropertyModel(Username=username,PropertType=ptype,Proprty_title=ptitle,
                      Area_in_size=area,price=price,Address=address,Contact_no=contact,EmailID=email).save()
    messages.success(request,"Property Details Saved")
    return render(request,"User/Property/addproperty.html")



def viewPropertyDetails(request):
    reg=UserPropertyModel.objects.all()
    return render(request,"User/Property/Viewproperty.html",{"reg":reg})


def addsharemarket(request):
    return render(request,"User/shareMarket/addsharemarket.html")


def savesharemarket(request):
    username=request.POST["username"]
    company_name=request.POST["companyname"]
    sharevalue=request.POST["sharevalue"]
    desc=request.POST["desciption"]
    status = "Pending"
    UserShareMarketModel(Username=username,Company_name=company_name,ShareValue=sharevalue,Description=desc,status=status).save()
    messages.success(request, "Details Saved")
    return render(request, "User/shareMarket/addsharemarket.html")


def viewsharemarket(request):
    reg=UserShareMarketModel.objects.all()
    return render(request, "User/shareMarket/ViewshareMarket.html",{"reg":reg})


def addreference(request):

    return render(request,"User/reference/addreference.html")


def savereference(request):
    username = request.POST["username"]
    jobtitle = request.POST["jobtitle"]
    desc = request.POST["desciption"]
    lastdate = request.POST["lastdate"]
    status = "Pending"
    UserReferenceModel(Username=username, job_title=jobtitle, Description=desc, last_date=lastdate,status=status).save()
    messages.success(request, "User Reference Saved")
    return render(request,"User/reference/addreference.html")


def viewreference(request):
    reg=UserReferenceModel.objects.all()
    return render(request,"User/reference/Viewreference.html",{"reg":reg})


def addcelebration(request):
    return render(request,"User/celebrations/AddCelebrations.html")


def savecelebration(request):
    username=request.POST["username"]
    address=request.POST["address"]
    contact=request.POST["contact"]
    email=request.POST["email"]
    dob=request.POST["date"]
    status = "Pending"
    UserCelebrationModel(Username=username,DOB=dob,Address=address,Contact_no=contact,EmailID=email,status=status).save()
    messages.success(request, "User celebration Saved")
    return render(request,"User/celebrations/AddCelebrations.html")


def viewcelebration(request):
    reg=UserCelebrationModel.objects.all()
    return render(request,"User/celebrations/ViewCelebrations.html",{"reg":reg})


def addTravel(request):
    return render(request,"User/Travel/addTravel.html")


def saveTravel(request):
    username=request.POST["username"]
    traveldate=request.POST["traveldate"]
    location=request.POST["location"]
    desc=request.POST["desciption"]
    contact=request.POST["contact"]
    status = "Pending"
    UserTravelModel(Username=username,Traveldate=traveldate,location=location,
                    Description=desc,Contact_no=contact,status=status).save()
    messages.success(request, "User Travel Information Saved")
    return render(request,"User/Travel/addTravel.html")


def viewTravel(request):
    reg=UserTravelModel.objects.all()
    return render(request,"User/Travel/ViewTravel.html",{"reg":reg})


def addmatrimonial(request):

    return render(request,"User/matrimonial/addmatrimonial.html")


def savematrimonial(request):
    username=request.POST["username"]
    gender=request.POST["gender"]
    dob=request.POST["dob"]
    desc=request.POST["desciption"]
    contact=request.POST["contact"]
    status = "Pending"
    UserMatrimonialModel(Username=username,gender=gender,dob=dob,description=desc,contactno=contact,status=status).save()
    messages.success(request,"Details Saved")
    return render(request,"User/matrimonial/addmatrimonial.html")


def viewmatrimonial(request):
    reg=UserMatrimonialModel.objects.all()
    return render(request,"User/matrimonial/Viewmatrimonial.html",{"reg":reg})
#
# def logoutUser(request):
#     return render(request,"commom/homepage.html")