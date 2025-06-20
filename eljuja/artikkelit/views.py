from django.shortcuts import render, redirect
from .models import Artikkeli
from django.http import HttpResponseForbidden
from . import forms
import pandas as pd
from django.http import HttpResponse
from .models import Myynti


def artikkeli_uusi(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Kirjaudu ensin sisään.")
    if not request.user.is_superuser:
        return HttpResponseForbidden("Sinulla ei ole oikeuksia käyttää tätä sivua.")
    if request.method == 'POST': 
        form = forms.CreateArtikkeli(request.POST, request.FILES) 
        if form.is_valid():
            newartikkeli = form.save(commit=False) 
            newartikkeli.author = request.user 
            newartikkeli.save()
            return  render(request, 'artikkelit/artikkeli_uusi.html', { 'form': form })
    else:
        form = forms.CreateArtikkeli()
    return render(request, 'artikkelit/artikkeli_uusi.html', { 'form': form })



def export_myynnit_to_excel(request):
    # Query the Person model to get all records
    myynnit = Myynti.objects.all().values()
    
    # Convert the QuerySet to a DataFrame
    df = pd.DataFrame(list(myynnit))

    # Define the Excel file response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=myynti.xlsx'

    # Use Pandas to write the DataFrame to an Excel file
    df.to_excel(response, index=False, engine='openpyxl')

    return response