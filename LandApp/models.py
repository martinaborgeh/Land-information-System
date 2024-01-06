
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField

class PolygonModels(models.Model):
    polygon = models.PolygonField()
    def __str__(self):
       return f'{self.polygon}'


class ParcelOwnerDetails(models.Model):
    Parcel_Owner_ID =  models.CharField(max_length=100, blank = False, null = False,unique=True)
    Parcel_Owner_Surname = models.CharField(max_length=100, blank = False, null = False)
    Parcel_Owner_FirstName = models.CharField(max_length=100, blank = False, null = False)
    Parcel_Owner_Location = models.CharField(max_length=100,blank = False, null = False)
    Parcel_Owner_Image = models.TextField(null=True, default=None, blank=True)
    Parcel_Owner_Gender = models.CharField(max_length=100,blank = False, null = False)
    Parcel_Owner_Age = models.PositiveIntegerField(blank = False, null = False)
    Parcel_Owner_Marital_Status = models.CharField(max_length = 100,blank = False, null = False)
    Parcel_Owner_Next_of_Kin = models.CharField(max_length =100,blank = False, null = False)
    Parcel_Owner_Contact = models.CharField(max_length=100,blank = False, null = False)
    Parcel_Owner_Next_of_Kin_Contact = models.CharField(max_length=100,blank = False, null = False)
    Parcel_Owner_Ghana_Card_Id = models.CharField(max_length =100,blank = False, null = False)
    Parcel_Owner_Qualification = models.CharField(max_length=100,blank = True, null = True)
    Parcel_Owner_EmailField = models.EmailField(max_length=100,blank = True, null = True)
    def __str__(self):
       return f'{self.Parcel_Owner_ID}'


class ChiefDetails(models.Model):
    Chief_ID = models.CharField(max_length=100,blank = False, null = False)
    Chief_Surname = models.CharField(max_length=100,blank = False, null = False)
    Chief_FirstName = models.CharField(max_length=100,blank = False, null = False)
    Chief_Location = models.CharField(max_length=100,blank = False, null = False)
    Chief_Image = models.TextField(null=True, default=None, blank=True)
    Chief_Gender = models.CharField(max_length=100,blank = False, null = False)
    Chief_Marital_Status = models.CharField(max_length = 100,blank = False, null = False)
    Chief_Contact = models.CharField(max_length=100,blank = False, null = False)
    Chief_Ghana_Card_Id = models.CharField(max_length =100,blank = False, null = False)
    Chief_Region = models.CharField(max_length=100,blank = False, null = False)
    Chief_District = models.CharField(max_length = 100,blank = False, null = False)
    Chief_Rank_of_Chieftaincy = models.CharField(max_length=100,blank = False, null = False)
    Chief_Year_of_Enstoolment = models.CharField(max_length=100,blank = False, null = False)
    Chief_Year_of_Chieftancy_End = models.CharField(max_length =100,blank = False, null = False)
    Chief_Qualification = models.CharField(max_length=100,blank = False, null = False)
    Chief_EmailField = models.EmailField(default = 0,max_length=100,blank = False, null = False)
    def __str__(self):
       return f'{self.Chief_ID}'

class SurveyorDetails(models.Model):
    Survey_Licence_Number = models.CharField(max_length=100,blank = False, null = False)
    Survey_Surname = models.CharField(max_length=100,blank = False, null = False)
    Survey_FirstName = models.CharField(max_length=100,blank = False, null = False)
    Survey_Location = models.CharField(max_length=100,blank = False, null = False)
    Survey_Image = models.TextField(null=True, default=None, blank=True)
    Survey_Gender = models.CharField(blank = False, null = False)
    Survey_Age = models.PositiveIntegerField(blank = False, null = False)
    Survey_Marital_Status = models.CharField(max_length = 100,blank = False, null = False)
    Survey_Contact = models.CharField(max_length=100,blank = False, null = False)
    Survey_Ghana_Card_Id = models.CharField(max_length =100,blank = False, null = False)
    Survey_Qualification = models.CharField(max_length=100,blank = False, null = False)
    Survey_Year_Of_Completions = models.CharField(max_length=100,blank = False, null = False)
    Survey_Institution_of_Completion = models.CharField(max_length=100,blank = False, null = False)
    Survey_Professional_Body =  models.CharField(max_length=100)
    Survey_EmailField = models.EmailField(default = 0,max_length=100)

    def __str__(self):
       return f'{self.Survey_Licence_Number}'


class ParcelDetails(models.Model):
   Parcel_Owner = models.OneToOneField(ParcelOwnerDetails,on_delete=models.CASCADE,default=0)
   Parcel_ID = models.CharField(blank=False,null = False,unique = True)
   Parcel_Boundary = models.OneToOneField(PolygonModels,on_delete=models.CASCADE,default=0)
   Parcel_District = models.CharField(max_length = 100,blank = False, null = False)
   Parcel_Region = models.CharField(max_length = 100, blank = False)
   parcel_Locality = models.CharField(max_length = 100, blank = False , null = False)
   Parcel_Status = models.CharField(max_length =100, blank = False, null = False)
   Parcel_land_interest_type = models.CharField(max_length = 100 , blank = False, null = False)
   Parcel_surveyor_who_demarcated = models.ForeignKey(SurveyorDetails,on_delete=models.CASCADE,default=0)
   Parcel_Chief_Involved = models.ForeignKey(ChiefDetails,on_delete=models.CASCADE,default=0) 
   Northings = ArrayField(models.CharField(max_length =255, blank = False, null = False))
   Eastings = ArrayField(models.CharField(max_length =255, blank = False, null = False))
   Longitude = ArrayField(models.CharField(max_length =255, blank = False, null = False))
   Latitude = ArrayField(models.CharField(max_length =255, blank = False, null = False))
  
   def __str__(self):
       return f'{self.Parcel_ID}'


