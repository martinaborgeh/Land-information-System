from .views import (DisplayMaptemplate,
LoginAdmin,
Createparceldetails,
RemoveParcel,
EditParcel,
SearchParcelforreadonlyMapdisplay,
SearchParcelforreadwriteedit
)

from django.urls import path



urlpatterns = [
    path('DisplayMap/',DisplayMaptemplate , name='DisplayMaptemplate'),
    path('Login/', LoginAdmin, name='LoginAdmin'),
    path('Createparceldetails/', Createparceldetails, name='Createparceldetails'),
    path('RemoveParcel/', RemoveParcel, name='RemoveParcel'),
    path('EditParcel/', EditParcel, name='EditParcel'),
    path('SearchParcelforreadonlyMapdisplay/', SearchParcelforreadonlyMapdisplay, name='SearchParcelforreadonlyMapdisplay'),
    path('SearchParcelforreadwriteedit/', SearchParcelforreadwriteedit, name='SearchParcelforreadwriteedit'),
]
