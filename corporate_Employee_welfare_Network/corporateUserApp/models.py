from django.db import models
class NewRegistrationModel(models.Model):
    EmployeeID=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=20,unique=True)
    Password=models.CharField(max_length=30)
    Address=models.CharField(max_length=100)
    EmailID=models.EmailField(unique=True)
    ContactNo=models.IntegerField(unique=True)
    DOB=models.DateField()
    Company_Name=models.CharField(max_length=30)
    status=models.CharField(max_length=10)
    usertype=models.CharField(max_length=30)



class UserThoughtModel(models.Model):
    # EmployeeID=models.ForeignKey(NewRegistrationModel,on_delete=models.CASCADE)
    Username=models.CharField(max_length=30)
    Description=models.TextField(max_length=100)
    Contact_no=models.IntegerField()
    status=models.CharField(max_length=10,default=True)

class UserEventModel(models.Model):
#     EmployeeID=models.ForeignKey(NewRegistrationModel,on_delete=models.CASCADE)
    Username=models.CharField(max_length=30)
    start_date=models.DateField()
    end_date=models.DateField()
    Description=models.TextField(max_length=100)
    Contact_no=models.IntegerField()
    status=models.CharField(max_length=10,default=True)

class UserTechnicalDetailsModel(models.Model):
    Username = models.CharField(max_length=30)
    Technology=models.CharField(max_length=30)
    Description = models.TextField(max_length=100)
    Contact_no = models.IntegerField()

class UserWorkExperienceModel(models.Model):
    Username = models.CharField(max_length=30)
    Technology=models.CharField(max_length=30)
    work_exp=models.IntegerField()
    Description = models.TextField(max_length=100)
    Contact_no = models.IntegerField()


class UserPropertyModel(models.Model):
    Username = models.CharField(max_length=30)
    PropertType=models.CharField(max_length=20)
    Proprty_title=models.CharField(max_length=20)
    Area_in_size=models.IntegerField()
    price=models.FloatField()
    Address = models.TextField(max_length=100)
    Contact_no = models.IntegerField()
    EmailID=models.EmailField()


class UserShareMarketModel(models.Model):
    Username = models.CharField(max_length=30)
    Company_name=models.CharField(max_length=30)
    ShareValue=models.DecimalField(max_digits=10,decimal_places=2)
    Description = models.TextField(max_length=100)
    status = models.CharField(max_length=10,default=True)


class UserReferenceModel(models.Model):
    Username = models.CharField(max_length=30)
    job_title=models.CharField(max_length=30)
    Description = models.TextField(max_length=100)
    last_date= models.DateField()
    status = models.CharField(max_length=10,default=True)

class UserCelebrationModel(models.Model):
    Username = models.CharField(max_length=30)
    Address = models.TextField(max_length=100)
    DOB= models.DateField()
    Contact_no = models.IntegerField()
    EmailID = models.EmailField()
    status = models.CharField(max_length=10,default=True)

class UserTravelModel(models.Model):
    Username = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    Description = models.TextField(max_length=100)
    Traveldate= models.DateField()
    Contact_no = models.IntegerField()
    status = models.CharField(max_length=10,default=True)

class UserMatrimonialModel(models.Model):
    Username=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    description=models.CharField(max_length=100)
    contactno=models.IntegerField()
    status = models.CharField(max_length=10,default=True)







