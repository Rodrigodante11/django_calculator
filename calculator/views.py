from django.shortcuts import render

from django.http import HttpResponse
from .calculatorTest import *


def calculator_request(request):
    if request.method == 'POST':

        valor1 = request.POST['valor1']
        valor2 = request.POST['valor2']
        valor3 = request.POST['valor3']

        list = [valor1, valor2, valor3]

        tarifa = request.POST['tarifa']
        tipo = request.POST['tipo']

        calculator(list, tarifa, tipo)

        return HttpResponse("teste")

    else:

        return render(request, 'cadastro.html')
