from django.shortcuts import render
from django.contrib.gis.geos import Polygon
import pyproj as prj
from django.db.models import Q
from django.contrib.gis.serializers import geojson
from django.http import JsonResponse
from .models import ParcelDetails,PolygonModels,ParcelOwnerDetails,ChiefDetails,SurveyorDetails
import json
import os
import mimetypes
import base64
import imghdr
from django.core.files.base import ContentFile
from uuid import uuid4


# Create your views here
def LoginAdmin(request):
    response_data = {'msg': None, 'status': None}

    if request.method == 'POST':
        data_from_post = json.load(request)
        username = data_from_post.get('username')
        password = data_from_post.get('password')
        admin_username = os.environ.get("ADMIN_USERNAME")
        admin_password = os.environ.get("ADMIN_PASSWORD")
        if admin_username ==username and admin_password == password:
            response_data['status'] = 200
            response_data['msg'] = 'Success:You have logged in successfully'
        else:
            response_data['status'] = 404
            response_data['msg'] = 'You are not a valid Admin'

    else:
        response_data['status'] = 404
        response_data['msg'] = 'Failed: Invalid request method.'

    return JsonResponse(response_data, status=response_data['status'])


def getddetails(formdata,formitem):
    try:
        return formdata.get(formitem)
    except Exception as e:
       print(f"{e} exception occured")
       return False



#This initially projects from Ghana National Grid to WGS84
def project_coordinates(coordinates, from_srid=None,to_srid=None):
    projection = prj.Transformer.from_crs(from_srid,to_srid)
    coordinates = coordinates.split(',') 
    Northings = coordinates[0::2]
    Northings.append(Northings[0])
    Eastings = coordinates[1::2]
    Eastings.append(Eastings[0])
    zipped = zip(Northings,Eastings)
    
    return Northings,Eastings,[list(projection.transform(float(values[0]),float(values[1]))) for values in zipped]

def createpolygon(projectedcoordinates):
  
    polygon = Polygon(projectedcoordinates)
    return polygon

def decodebinary(base64_string):
    try:
        # Split the base64 string
        format, imgstr = base64_string.split(';base64,')
        
        # Determine the image format using imghdr
        ext = imghdr.what(None, h=imgstr)
        
        # If the format is not recognized, default to 'png'
        if not ext:
            ext = 'png'

        # Decode the base64-encoded image data
        img_data = base64.b64decode(imgstr)

        # Create a ContentFile with a unique name
        file_name = f"{uuid4().hex}.{ext}"
        content_file = ContentFile(img_data, name=file_name)
        print(content_file)

        return content_file
    except Exception as e:
        # Handle exceptions (e.g., invalid base64 string)
        print(f"Error converting base64 to image: {e}")
        return None



def createsurveyordetails(modelname,formdata):
    if formdata:
        surveyor_license =  getddetails(formdata,'surveyor_license')
        surname = getddetails(formdata,'surveyor_surname')
        firstname =  getddetails(formdata,'surveyor_firstname')
        location = getddetails(formdata,'surveyor_location')
        image = getddetails(formdata,'surveyor_image')
        gender = getddetails(formdata,'surveyor_gender')
        age = getddetails(formdata,'surveyor_age')
        marital_status =  getddetails(formdata,'surveyor_marital_status')
        contact =  getddetails(formdata,'surveyor_contact')
        ghana_card_id = getddetails(formdata,'surveyor_ghana_card_id')
        qualification = getddetails(formdata,'surveyor_qualification')
        year_of_completion = getddetails(formdata,'surveyor_year_of_completion')
        institution_of_completion = getddetails(formdata,'surveyor_institution_of_completion')
        professional_body = getddetails(formdata,'surveyor_professional_body')
        email = getddetails(formdata,'surveyor_email')
        if surveyor_license and surname and  firstname and image and location and  gender and  age and marital_status and contact and  ghana_card_id and qualification and year_of_completion and institution_of_completion and professional_body and email:
            surveyor_model = modelname.objects.create(
            Survey_Licence_Number = surveyor_license,
            Survey_Surname =   surname,
            Survey_FirstName =  firstname,
            Survey_Location =  location,
           Survey_Image =  image,
            Survey_Gender = gender,
            Survey_Age = age,
            Survey_Marital_Status =  marital_status,
            Survey_Contact =  contact,
            Survey_Ghana_Card_Id =  ghana_card_id,
            Survey_Qualification = qualification,
            Survey_Year_Of_Completions =  year_of_completion,
            Survey_Institution_of_Completion = year_of_completion,
            Survey_Professional_Body = professional_body,
            Survey_EmailField = email
            )
            return surveyor_model



def createchiefdetails(modelname,formdata):
 
    if formdata:
        chief_id =  getddetails(formdata,'chief_id')
        surname = getddetails(formdata,'chief_surname')
        firstname = getddetails(formdata,'chief_firstname')
        location =  getddetails(formdata,'chief_location')
        image =    getddetails(formdata,'chief_image')
        gender = getddetails(formdata,'chief_gender')
        marital_status = getddetails(formdata,'chief_marital_status')
        contact= getddetails(formdata,'chief_contact')
        ghana_card_id =  getddetails(formdata,'chief_ghana_card_id')
        region =  getddetails(formdata,'chief_region')
        district = getddetails(formdata,'chief_district')
        rank_of_chieftancy = getddetails(formdata,'chief_rank_of_chieftancy')
        year_of_enstoolment = getddetails(formdata,'chief_year_of_enstoolment')
        year_of_chieftancy_end = getddetails(formdata,'chief_year_of_chieftancy_end')
        qualification = getddetails(formdata,'chief_qualification')
        email = getddetails(formdata,'chief_email')
        if chief_id and surname and  firstname and image and location and   gender and  marital_status and contact and ghana_card_id and region and district and rank_of_chieftancy and year_of_enstoolment and year_of_chieftancy_end and qualification and  email:
            chief_model = modelname.objects.create(
                Chief_ID = chief_id,
                Chief_Surname =  surname,
                Chief_FirstName =  firstname,
                Chief_Location =  location,
                Chief_Image =  image,
                Chief_Gender = gender,
                Chief_Marital_Status = marital_status,
                Chief_Contact =  contact,
                Chief_Ghana_Card_Id =  ghana_card_id,
                Chief_Region =  region,
                Chief_District = district,
                Chief_Rank_of_Chieftaincy =  rank_of_chieftancy,
                Chief_Year_of_Enstoolment=year_of_enstoolment,
                Chief_Year_of_Chieftancy_End =  year_of_chieftancy_end,
                Chief_Qualification = qualification,
                Chief_EmailField = email
                )
            return chief_model



def createparcelownerdetail(modelname,formdata):
    if formdata:
        parcel_owner_id =  getddetails(formdata,'parcel_owner_id')
        surname = getddetails(formdata,'parcel_owner_surname')
        firstname =  getddetails(formdata,'parcel_owner_firstname')
        location = getddetails(formdata,'parcel_owner_location')
        image =getddetails(formdata,'parcel_owner_image')

        gender = getddetails(formdata,'parcel_owner_gender')
        age = getddetails(formdata,'parcel_owner_age')
        marital_status =  getddetails(formdata,'parcel_owner_marital_status')
        next_of_kin =  getddetails(formdata,'parcel_owner_next_of_kin')
        contact = getddetails(formdata,'parcel_owner_contact')
        next_of_kin_contact = getddetails(formdata,'parcel_owner_next_of_kin_contact')
        ghana_card_id = getddetails(formdata,'parcel_owner_ghana_card_id')
        qualification = getddetails(formdata,'parcel_owner_qualification')
        email = getddetails(formdata,'parcel_owner_email')
        
        if parcel_owner_id and surname and  firstname and image and location and   gender and  age and marital_status and next_of_kin and contact and next_of_kin_contact and ghana_card_id and qualification and email:
            parcel_owner_model = modelname.objects.create(
                       Parcel_Owner_ID = parcel_owner_id,
                       Parcel_Owner_Surname =  surname,
                       Parcel_Owner_FirstName =  firstname,
                       Parcel_Owner_Location =  location,
                      Parcel_Owner_Image=  image,
                       Parcel_Owner_Gender = gender,
                       Parcel_Owner_Age = age,
                       Parcel_Owner_Marital_Status =  marital_status,
                       Parcel_Owner_Next_of_Kin =   next_of_kin,
                       Parcel_Owner_Contact =  contact,
                       Parcel_Owner_Next_of_Kin_Contact = next_of_kin_contact,
                       Parcel_Owner_Ghana_Card_Id = ghana_card_id,
                       Parcel_Owner_Qualification = qualification,
                       Parcel_Owner_EmailField = email
                     )
            return parcel_owner_model


def Createparceldetails(request):
    response_data  = {'msg': None, 'status': None}
    print(request.POST)
   
    formdata = json.load(request)
   
    if formdata:
        coordinates = getddetails(formdata,'coordinates')
        projected_coordinates = project_coordinates(coordinates, from_srid=2136,to_srid=4326)
        northings = projected_coordinates[0]
        eastings = projected_coordinates[1]
        longitudes = [coord[0] for coord in projected_coordinates[2]]
        latitude = [coord[1] for coord in projected_coordinates[2]]
        print(northings)
        print(eastings)
        print(longitudes)
        print(latitude)
        polygon = createpolygon(projected_coordinates[2])
        parcel_id = getddetails(formdata,'parcel_id')
        Parcel_Boundary =  PolygonModels.objects.create(polygon=polygon)
        parcel_district = getddetails(formdata,'parcel_district')
        parcel_region = getddetails(formdata,'parcel_region')
        parcel_locality = getddetails(formdata,'parcel_locality')
        parcel_status = getddetails(formdata,'parcel_status')
        land_interest_type =  getddetails(formdata,'parcel_interest')

        if parcel_id and  Parcel_Boundary and  parcel_district and  parcel_region and  parcel_locality and parcel_status and land_interest_type:
            ParcelDetails.objects.create(
            Northings = northings,
            Eastings = eastings,
            Longitude = longitudes,
            Latitude = latitude,
            Parcel_ID =  parcel_id,
            Parcel_Boundary =  Parcel_Boundary,
            Parcel_District =  parcel_district,
            Parcel_Region =  parcel_region,
            parcel_Locality = parcel_locality,
            Parcel_Status = parcel_status,
            Parcel_land_interest_type =  land_interest_type,
            Parcel_Owner = createparcelownerdetail(ParcelOwnerDetails,formdata),
            Parcel_surveyor_who_demarcated = createsurveyordetails(SurveyorDetails,formdata),
            Parcel_Chief_Involved =  createchiefdetails(ChiefDetails,formdata)
            
                     )
            response_data['msg'] = "Parcel Owner Details Successfuly Saved"
            response_data['status'] =  200

        else:
            response_data['msg'] = "Make sure not to leave any Parcel field empty"
            response_data['status'] =  404
    else:
         response_data['msg'] = "Parcel Forms cannot be submitted empty"
         response_data['status'] =  404

    return JsonResponse(response_data, status=response_data['status'])





def RemoveParcel(request):
   response_data = {'msg': None, 'status': None}
   
   if request.method == 'POST':
       data_from_post = json.load(request) 
       getitemfrompost = getddetails(data_from_post,'old_parcel_id')
       print('parcel id',getitemfrompost)
       if getitemfrompost:
           parcel = ParcelDetails.objects.get(Parcel_ID=getitemfrompost)
           if parcel:
               parcel.delete()
               response_data['msg'] = "Parcel deleted successfully"
               response_data['status'] =  200
           else:
               response_data['msg'] = "Parcel does not exist"
               response_data['status'] =  404
       else:
           response_data['msg'] = "Entry cannot be empty"
           response_data['status'] =  404
   else:
       response_data['msg'] = "Invalid request method"
       response_data['status'] =  404
   return JsonResponse(response_data, status=response_data['status'])



def EditParcel(request):
    response_data = {'msg': None, 'status': None}
    if request.method == 'POST':
        data_from_post = json.load(request)
        
        parcel_id = getddetails(data_from_post,'old_parcel_id')
        print(parcel_id)
        if(parcel_id):
            parcel =  ParcelDetails.objects.get(Parcel_ID =  parcel_id)
            parcel_owner_instance = parcel.Parcel_Owner
            coordinates = getddetails(data_from_post,'coordinates')
            projected_coordinates = project_coordinates(coordinates, from_srid=2136,to_srid=4326)
            northings = projected_coordinates[0]
            eastings = projected_coordinates[1]
            longitudes = [coord[0] for coord in projected_coordinates[2]]
            latitude = [coord[1] for coord in projected_coordinates[2]]
            polygon = createpolygon(projected_coordinates[2])
            Parcel_Boundary =  PolygonModels.objects.create(polygon=polygon)
            Parcel_surveyor_who_demarcated = createsurveyordetails(SurveyorDetails,data_from_post)

            parcel_owner_instance.Parcel_Owner_ID=getddetails(data_from_post,'parcel_owner_id')
            parcel_owner_instance.Parcel_Owner_Surname=getddetails(data_from_post,'parcel_owner_surname')
            parcel_owner_instance.Parcel_Owner_FirstName=getddetails(data_from_post,'parcel_owner_firstname')
            parcel_owner_instance.Parcel_Owner_Location=getddetails(data_from_post,'parcel_owner_location')
            parcel_owner_instance.Parcel_Owner_Image=getddetails(data_from_post,'parcel_owner_image')
            parcel_owner_instance.Parcel_Owner_Gender=getddetails(data_from_post,'parcel_owner_gender')
            parcel_owner_instance.Parcel_Owner_Age=getddetails(data_from_post,'parcel_owner_age')
            parcel_owner_instance.Parcel_Owner_Marital_Status=getddetails(data_from_post,'parcel_owner_marital_status')
            parcel_owner_instance.Parcel_Owner_Contact=getddetails(data_from_post,'parcel_owner_contact')
            parcel_owner_instance.Parcel_Owner_Next_of_Kin=getddetails(data_from_post,'parcel_owner_next_of_kin')
            parcel_owner_instance.Parcel_Owner_Next_of_Kin_Contact=getddetails(data_from_post,'parcel_owner_next_of_kin_contact')
            parcel_owner_instance.Parcel_Owner_Ghana_Card_Id=getddetails(data_from_post,'parcel_owner_ghana_card_id')
            parcel_owner_instance.Parcel_Owner_Qualification=getddetails(data_from_post,'parcel_owner_qualification')
            parcel_owner_instance.Parcel_Owner_EmailField=getddetails(data_from_post,'parcel_owner_email')
            parcel.Parcel_Chief_Involved = createchiefdetails(ChiefDetails,data_from_post)
           #parcel.Parcel_ID = getddetails(data_from_post,'parcel_id')
            parcel.Parcel_Boundary = Parcel_Boundary
            parcel.Northings = northings
            parcel.Eastings = eastings
            parcel.Longitude = longitudes
            parcel.Latitude = latitude
            parcel.Parcel_District = getddetails(data_from_post,'parcel_district')
            parcel.Parcel_Region = getddetails(data_from_post,'parcel_region')
            parcel.parcel_Locality = getddetails(data_from_post,'parcel_locality')
            parcel.Parcel_Status = getddetails(data_from_post,'parcel_status')
            parcel.Parcel_land_interest_type = getddetails(data_from_post,'parcel_interest')
            parcel_owner_instance.save()
            parcel.save()

            response_data['msg'] = "Land details Form Successfully edited"
            response_data['status'] =  200
        else:
            response_data['msg'] = "Make sure you edit all necessary fields before sending"
            response_data['status'] =  404
    else:
         response_data['msg'] = "Cannot submit empty Land details Form"
         response_data['status'] =  404
    return JsonResponse(response_data, status=response_data['status'])



def retrievesearchresult(itemtoretrieve):
    response_data = {'msg': None, 'status': None,'data':None}
    try:
        retrieveddata = ParcelDetails.objects.filter(
       Q(Parcel_Owner__Parcel_Owner_ID=itemtoretrieve) | 
       Q(Parcel_ID=itemtoretrieve) |
       Q(Parcel_surveyor_who_demarcated__Survey_Licence_Number=itemtoretrieve) | 
       Q(Parcel_Chief_Involved__Chief_Qualification=itemtoretrieve)| 
       Q(Parcel_District=itemtoretrieve) |  
       Q(Parcel_Region=itemtoretrieve) | 
       Q(parcel_Locality=itemtoretrieve) | 
       Q(Parcel_Status=itemtoretrieve) |
       Q(Parcel_land_interest_type=itemtoretrieve) 
       
        ).values('id',
            'Parcel_Owner__Parcel_Owner_ID',
             'Parcel_Owner__Parcel_Owner_Surname',
             'Parcel_Owner__Parcel_Owner_FirstName',
             'Parcel_Owner__Parcel_Owner_Location',
              'Parcel_Owner__Parcel_Owner_Image',
              'Parcel_Owner__Parcel_Owner_Gender',
              'Parcel_Owner__Parcel_Owner_Age',
              'Parcel_Owner__Parcel_Owner_Marital_Status',
              'Parcel_Owner__Parcel_Owner_Next_of_Kin',
              'Parcel_Owner__Parcel_Owner_Contact',
               'Parcel_Owner__Parcel_Owner_Next_of_Kin_Contact',
              'Parcel_Owner__Parcel_Owner_Ghana_Card_Id',
              'Parcel_Owner__Parcel_Owner_Qualification',
               'Parcel_Owner__Parcel_Owner_EmailField',
            'Parcel_ID',
            'Parcel_Boundary__polygon',  # Replace 'your_field_name' with the actual field you want
            'Parcel_District',
            'Parcel_Region',
            'parcel_Locality',
            'Parcel_Status',
            'Northings',
             'Eastings',
             'Longitude',
             'Latitude',
            'Parcel_land_interest_type',
            'Parcel_surveyor_who_demarcated__Survey_Licence_Number',
             'Parcel_surveyor_who_demarcated__Survey_Surname',
             'Parcel_surveyor_who_demarcated__Survey_FirstName',
             'Parcel_surveyor_who_demarcated__Survey_Location',
             'Parcel_surveyor_who_demarcated__Survey_Image',
              'Parcel_surveyor_who_demarcated__Survey_Marital_Status',
             'Parcel_surveyor_who_demarcated__Survey_Gender',
             'Parcel_surveyor_who_demarcated__Survey_Age',
             'Parcel_surveyor_who_demarcated__Survey_Contact',
             'Parcel_surveyor_who_demarcated__Survey_Ghana_Card_Id',
             'Parcel_surveyor_who_demarcated__Survey_Qualification',
             'Parcel_surveyor_who_demarcated__Survey_Year_Of_Completions',
              'Parcel_surveyor_who_demarcated__Survey_Institution_of_Completion',
              'Parcel_surveyor_who_demarcated__Survey_Professional_Body',
              'Parcel_surveyor_who_demarcated__Survey_EmailField',
            'Parcel_Chief_Involved__Chief_ID',
            'Parcel_Chief_Involved__Chief_Surname',
            'Parcel_Chief_Involved__Chief_FirstName',
            'Parcel_Chief_Involved__Chief_Location',
             'Parcel_Chief_Involved__Chief_Image',
             'Parcel_Chief_Involved__Chief_Gender',
             'Parcel_Chief_Involved__Chief_Marital_Status',
             'Parcel_Chief_Involved__Chief_Contact',
              'Parcel_Chief_Involved__Chief_Ghana_Card_Id',
              'Parcel_Chief_Involved__Chief_Region',
              'Parcel_Chief_Involved__Chief_District',
              'Parcel_Chief_Involved__Chief_Rank_of_Chieftaincy',
              'Parcel_Chief_Involved__Chief_Year_of_Enstoolment',
               'Parcel_Chief_Involved__Chief_Year_of_Chieftancy_End',
               'Parcel_Chief_Involved__Chief_Qualification',
               'Parcel_Chief_Involved__Chief_EmailField')
        
            # Convert Polygon objects to GeoJSON
        #print(retrieveddata) 
        if retrieveddata:
            # Convert Polygon objects to string representation
            for item in retrieveddata:
                if 'Parcel_Boundary__polygon' in item:
                    item['Parcel_Boundary__polygon'] = str(item['Parcel_Boundary__polygon'])
                
                    

            response_data['status'] = 200
            response_data['data'] = list(retrieveddata)
            response_data['message'] = 'Items retrieved successfully'
        
   
    except Exception as e:
        print(e)
        response_data['status'] = 500
        response_data['message'] = f'An error occurred: {e}'
    response_data['data']
    return response_data
 
        

def SearchParcelforreadonlyMapdisplay(request):
    response_data = {'msg': None, 'status': None,'data':None}
    if request.method == 'POST':
        data_from_post = json.load(request)
        get_item_from_post=getddetails(data_from_post,'searchdata')
        print('hjj',get_item_from_post)
        get_item_from_db =  retrievesearchresult(get_item_from_post)
        

        if get_item_from_db :
            
            response_data = get_item_from_db
            

        else:
            response_data['msg'] = "Incorrect entry"
            response_data['status'] =  404
    else:
        response_data['msg'] = "Invalid request method"
        response_data['status'] =  404
    print(response_data['data'])
    print(len(response_data['data']))
    return JsonResponse(response_data, status=response_data['status'],safe=False)

def SearchParcelforreadwriteedit(request):
    response_data = {'msg': None, 'status': None,'data':None}
    if request.method == 'POST':
        data_from_post = json.load(request)
        get_item_from_post=getddetails(data_from_post,'searchdata')
        get_item_from_db =  retrievesearchresult(get_item_from_post)
        

        if get_item_from_db :
            
            response_data = get_item_from_db

        else:
            response_data['msg'] = "data not found"
            response_data['status'] =  404
    else:
        response_data['msg'] = "Invalid request method"
        response_data['status'] =  404

    return JsonResponse(response_data, status=response_data['status'],safe=False)


def DisplayMaptemplate(request):
    return render(request,'Mapdisplay.html')




