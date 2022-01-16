from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from spweadmin.settings import BASE_DIR, STATIC_ROOT, STATIC_URL
from .compare_excel_files import compare_excel_files
import pandas as pd
import os
from io import BytesIO
from datetime import date

# Create your views here.
# https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if "GET" == request.method:
        return render(request, 'checkafwezigheden/index.html')
    else:
        data = request.POST
        dag =  data['dag']
        dag = dag.lower()
        print(request.FILES)
        aanwezig = request.FILES["aanwezigheden"]
        verwacht = request.FILES["verwachte_lln"]


        df_aanwezig = pd.read_excel(aanwezig, sheet_name=0)
        df_verwacht = pd.read_excel(verwacht, sheet_name=0, header=2, skiprows=[0,1], usecols=['Klas', 'Naam & Voornaam', 'Maandag', 'Dinsdag', 'Donderdag', 'Vrijdag'])
        df_niet_aanwezig = compare_excel_files(df_aanwezig, df_verwacht, dag)
        with BytesIO() as b:
            # Use the StringIO object as the filehandle.
            writer = pd.ExcelWriter(b, engine='xlsxwriter')
            df_niet_aanwezig.to_excel(writer, sheet_name='Afwezig_' + dag)
            writer.save()
            today = date.today()
            today_string = today.strftime('%d_%m_%y')
            filename = 'afwezigen_' + today_string
            content_type = 'application/vnd.ms-excel'
            response = HttpResponse(b.getvalue(), content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
            return response
