from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .form import PdfForm
import PyPDF2
import numpy as np
import pandas as pd


class Pricings(View):
    def get(self, request):
        form = PdfForm()
        return render(request, 'main.html', {'form': form})

    def post(self, request):
        form = PdfForm(request.POST, request.FILES)
        # files -> list of memory uploaded file
        files = request.FILES.getlist('file')

        # pricing
        bw_price = 1000
        colored_price = 2000

        total_pages = 0
        bw_pages = 0
        total_bw_price = 0
        colored_pages = 0
        total_colored_price = 0
        total_price = 0

        for file in files:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            total_pages += num_pages
            file.close()

        return render(request, 'pricing.html', {
            'total_pages': total_pages,
            'bw_pages': bw_pages,
            'bw_price': bw_price,
            'total_bw_price': total_bw_price,
            'colored_pages': colored_pages,
            'colored_price': colored_price,
            'total_colored_price': total_colored_price,
            'total_price': total_price,
        })
