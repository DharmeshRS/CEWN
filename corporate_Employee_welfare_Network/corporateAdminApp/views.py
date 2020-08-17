from django.shortcuts import render, redirect

# Create your views here.
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



def pendingUser(request):
    reg = NewRegistrationModel.objects.all()
    return render(request,"Admin/ShortlistedUsers.html",{"reg":reg})


def acceptedusers(request):
    id=request.GET["x"]
    print(id)
    NewRegistrationModel.objects.filter(EmployeeID=id).update(status="accept")

    return render(request, "Admin/ShortlistedUsers.html", {"reg": NewRegistrationModel.objects.all()})


def rejectedusers(request):
    id = request.GET["x"]
    print(id)
    NewRegistrationModel.objects.filter(EmployeeID=id).update(status="reject")
    return render(request, "Admin/ShortlistedUsers.html", {"reg": NewRegistrationModel.objects.all()})


def viewacceptedusers(request):
    regaccept=NewRegistrationModel.objects.filter(status="accept")
    return render(request, "Admin/AcceptedUsers.html", {"reg": regaccept})

def viewrejectedusers(request):
    regaccept = NewRegistrationModel.objects.filter(status="reject")
    return render(request, "Admin/rejectedUsers.html", {"reg": regaccept})


def viewthoughtAdmin(request):
    thought = UserThoughtModel.objects.all()
    return render(request, "Admin/ViewDetails/Viewthought.html", {"reg": thought})


def vieweventAdmin(request):
    thought = UserEventModel.objects.all()
    return render(request, "Admin/ViewDetails/ViewEvents.html", {"reg": thought})


def viewtechAdmin(request):
    thought = UserTechnicalDetailsModel.objects.all()
    return render(request, "Admin/ViewDetails/ViewTS.html", {"reg": thought})


def viewtWorkExpAdmin(request):
    thought = UserWorkExperienceModel.objects.all()
    return render(request, "Admin/ViewDetails/ViewWorkExp.html", {"reg": thought})


def viewpropertyAdmin(request):
    thought = UserPropertyModel.objects.all()
    return render(request, "Admin/ViewDetails/Viewproperty.html", {"reg": thought})


def viewShareMarketAdmin(request):
    thought = UserShareMarketModel.objects.all()
    return render(request, "Admin/ViewDetails/ViewshareMarket.html", {"reg": thought})


def viewreferenceAdmin(request):
    thought = UserReferenceModel.objects.all()
    return render(request, "Admin/ViewDetails/Viewreference.html", {"reg": thought})


def viewmatrimonialAdmin(request):
    thought = UserMatrimonialModel.objects.all()
    return render(request, "Admin/ViewDetails/Viewmatrimonial.html", {"reg": thought})


def viewcelebrationsAdmin(request):
    thought = UserCelebrationModel.objects.all()
    return render(request, "Admin/ViewDetails/ViewCelebrations.html", {"reg": thought})


def viewTravelAdmin(request):
    thought = UserTravelModel.objects.all()
    return render(request, "Admin/ViewDetails/ViewTravel.html", {"reg": thought})


def logoutAdmin(request):
    return redirect('homepage')