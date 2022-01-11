from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from spweadmin.settings import BASE_DIR
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
        excel_file = request.FILES["excel_file"]

        df_aanwezig = pd.read_excel(excel_file, sheet_name=0)
        path_verwacht = os.path.join(BASE_DIR, 'checkafwezigheden\Data\planning_elke_dag.xlsx')
        df_verwacht = pd.read_excel(path_verwacht, sheet_name=dag)
        df_niet_aanwezig = compare_excel_files(df_aanwezig, df_verwacht)
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
