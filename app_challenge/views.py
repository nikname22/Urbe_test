from django.shortcuts import render, redirect
from .models import Usuario, Project
import requests
import yfinance as yf
import pandas_datareader.data as web
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import streamlit as st
import pandas as pd
import numpy as np 
import datetime

# def get_graph():
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     print(image_png)
#     graph = base64.b64decode(image_png)
#     graph = graph.decode('utf-8', errors='ignore')
#     buffer.close()
#     return graph

# def get_plot(x,y):
#     plt.switch_backend('AGG')
#     plt.figure(figsize=(10,5))
#     plt.title('sales of items')
#     plt.plot(x,y)
#     plt.xticks(rotation=45)
#     plt.xlabel('item')
#     plt.ylabel('price')
#     plt.tight_layout()
#     graph = get_graph()
#     return graph

def home(request):    
    usuarios = {
        'usuarios': Usuario.objects.all()
    }    
    novo_usuario = Usuario()  
    # responses = requests.get('https://urbe.me/administracao/api/lista-projetos/').json()

    # for response in responses:       
    #     #print(response['projeto'], response['latitude'])
    #     novo_project = Project()            
    #     novo_project.projeto = response['projeto']
    #     novo_project.latitude = response['latitude']
    #     novo_project.longitude = response['longitude']
    #     novo_project.tir_media = response['tir_media']
    #     novo_project.total_captado = response['total_captado']
    #     novo_project.vgv = response['vgv']
    #     novo_project.save()    
    # usuario = Project.objects.all()
    # usuario.delete()    

    tickers = ["ABEV3.SA"]    
    carteira = yf.download(tickers,period="1mo")['Adj Close']  

    print(carteira.index[0].date().strftime("%d/%m/%Y"), carteira[0])
    print(carteira.index[-1].date().strftime("%d/%m/%Y"), carteira[-1])    

    # data_atual = datetime.datetime.now()
    # ano_atual = data_atual.year
    # sub = ano_atual - 5
    # years = []
    # for i in range(5):
    #      item = sub + (i+1)
    #      years.append(item)         
    
    # answer = []
    # for year in years:
    #     n_stocks = 0
    #     n_days = 0            
    #     soma= 0
    #     for cart in carteira:
    #         if n_stocks < len(carteira):
    #             #print(carteira.index[n_stocks].date().strftime("%Y"), str(year))                
    #             if carteira.index[n_stocks].date().strftime("%Y") == str(year):                    
    #                 n_days = n_days + 1 
    #                 soma = soma + cart
    #         n_stocks = n_stocks + 1
    #     answer.append({'year': year, 'soma':soma, 'n_days':n_days})
    # print(answer)

    for cart in carteira.index:
        print(cart.date().strftime("%d/%m/%Y"))

    for cart in carteira:
        print(cart)    
    

    return render(request,'usuarios/home.html', {'usuarios': Usuario.objects.all(), 'hello':'hello world'})

def create_user(request):
    #salvar os dados da home no banco de dados
    novo_usuario = Usuario()    
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()    
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/home.html', usuarios )

def edit(request, id):    
    usuario = Usuario.objects.get(id_usuario=id)
    return render(request,'usuarios/update.html', {"usuario": usuario})

def update(request,id):
     input_name = request.POST.get('nome')  
     input_age = request.POST.get('idade')
     usuario = Usuario.objects.get(id_usuario=id)
     usuario.nome = input_name
     usuario.idade = input_age
     usuario.save() 
     return redirect(home)   



def delete(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.delete()    
    return redirect(home)
