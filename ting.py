#!/usr/bin/env python
from flask import Flask, render_template, request, session, Response, make_response, redirect, jsonify, json

import smtplib                                      # Импортируем библиотеку по работе с SMTP
# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML

import datetime
import uuid
import json
import hashlib
import sqlite3
import pymysql
import requests
import time
import string
import random
import threading
application = Flask(__name__)

data = ['да', '123', 'да', '123', 'да', '123', 'да', '123', 'да', '123', 'да', '123']

AllClient = {}

def parse_arg_from_requests(el):
    el = (el.decode("utf-8"))
    el = el.split('&')
    es = []
    for a in el:
        es.append(a.split("=")[-1])
    return(es)


class user_():
    """Работа с локальными данными пользователей"""
    
    def GetUserDate(self):
        """Получение локальных данных пользователя
        """
        if not self in AllClient: # Создание локальных данных пользователя
            AllClient[self] = {
                'auth': False,
                'authCode': None                
            }     
        return(AllClient[self])
    
    def GetUserAuth(self):
        userData = user_.GetUserDate(self)
        print(userData)
        
        return(userData['auth'])
    
    def login(self):
        """
        Выдаёт флаг `auth`, чтобы убрать флаг используйте::
        
            user_.logout(user_cashe)

        """
        userData = user_.GetUserDate(self)
        userData['auth'] = True
        return(True)
        
    def logout(self):
        """
        Убирает флаг `auth`, чтобы вернуть флаг используйте::
        
            user_.login(user_cashe)

        """
        userData = user_.GetUserDate(self)
        userData['auth'] = False
        return(True)

class CACHE():
    """Работа с кэшем"""
    def Generate(self):
        """Генерирует кэш

        Returns:
            string: созданный кэш
        """
        cc = str('_TING_' + str(self) + '_TING_' + str(datetime.datetime.now()))
        bytesvalue = cc.encode('utf-8')
        hash_object = hashlib.md5(bytesvalue)
        Hash_user = (hash_object.hexdigest())
        return(Hash_user)
  
    def Check(self):
        """Проверка кэша

        Returns:
            string: кэш пользователя
        """
        user_cashe = ''
        if not self.cookies.get('TING'):
            user_cashe = CACHE.Generate(str(self.remote_addr))
            print('Генерация')
            # hash = (GENERCASH(str(self.remote_addr)))
        else:
            user_cashe = self.cookies.get('TING')  
            print('Есть')
            # hash = self.cookies.get('TING')    
        # print(user_cashe)
        return(user_cashe)

# Slow API
@application.route('/tingAPI/account/<method>', methods=["POST"])
def tingAPI_account(method):
    if not request.cookies.get('TING'):
        return redirect('/')
    user_cashe = CACHE.Check(request)
    returnValue = {
        'status': 200,
        'method': method
        }
    TN = str(time.time())
    TN = TN[:TN.find('.')]
    TM = str(request.form['timeN'])[0:-3]

    RZ = (int(TN) - int(TM))
    if(RZ <= 10 and RZ >= -5):
        if(method == 'goout'):
            user_.logout(user_cashe)
        
        elif(method == 'check'):
            db = ['123', '55']
            
            rt = {
                'status': None,
                'ErrorP': False,
                'ErrorL': False,
                'info': None
            }
            if(len(request.form) == 3 and (RZ <= 10 and RZ >= -5)):
                rt['status'] = True
                if request.form['login'] != db[0]:
                    rt['ErrorL'] = True
                    rt['ErrorP'] = True
            
                if(request.form['password'] != db[1]):
                    rt['ErrorP'] = True
                
                if(rt['ErrorP'] == False and rt['ErrorL'] == False):
                    user_.login(user_cashe)
                
            else:
                rt['status'] = False
                rt['info'] = 'API NOT FOUND'
            
            returnValue = rt
    else:
        returnValue['status'] = 408
        
    return(returnValue)
    
    






#Пасивные ссылки
@application.route('/about')
def about_us():
    if not request.cookies.get('TING'):
        return redirect('/')
    user_cashe = CACHE.Check(request)
    lg = user_.GetUserAuth(user_cashe)
    
    return render_template('/about.html', data=data, login = lg)

@application.route('/InDeveloper')
def InDeveloper():
    return render_template('InDeveloper.html')


# Сайт основные ссылки
@application.route('/auth', methods=["POST","GET"])
def auth():
    if not request.cookies.get('TING'):
        return redirect('/')
    user_cashe = CACHE.Check(request)
    
    if request.method == "GET":
        
        lg = user_.GetUserAuth(user_cashe)
        
        if lg:
            return redirect('/main')
        else:
            res = make_response(render_template('auth.html'))
            res.set_cookie('TING', f'{user_cashe}') 
            return(res)





@application.route('/')
def index():
    user_cashe = CACHE.Check(request)
    lg = user_.GetUserAuth(user_cashe)
    res = None
    
    data = ['да', '123', 'да', '123', 'да', '123', 'да', '123', 'да', '123', 'да', '123']
    
    # lg = True
    
    if not lg:
        res = make_response(render_template('main.html',data=None, login=lg))
        res.set_cookie('TING', f'{user_cashe}') 
        
    else:
        return redirect('/main')
    
    return(res)

@application.route('/main')
def main():
    user_cashe = CACHE.Check(request)
    lg = user_.GetUserAuth(user_cashe)
    res = ''
    if lg == False:
        res = make_response(redirect('/'))
        res.set_cookie('TING', f'{user_cashe}') 
    else:
        res = make_response(render_template('index.html', data=data, login = lg))
        res.set_cookie('TING', f'{user_cashe}') 
        print('s')
        
    return (res)


@application.errorhandler(404)
def page_not_found(e):
    return ("errors") #('404.html')

if __name__=="__main__":
    application.run(debug=True, host='localhost',port='80')