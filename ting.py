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

def generate_Color_hex():
    """Генерирует цвет
    """
    r = lambda: random.randint(0,255)
    return('#%02X%02X%02X' % (r(),r(),r()))
    
    
    
class DB():
    """Работа с Базой данных
    получить данные::
    
        DB.GET('Текст запроса SQL')   
    отправить данные::
    
        DB.POST('Текст запроса SQL')
    """
    

    def GET(self):
        """Получает данные с Базы данных
        """
        connection = pymysql.connect(host="37.140.192.90", user='u1102095_ting', password='S7x6U9j2', database='u1102095_ting_v2', charset="utf8")
        cursor = connection.cursor()
        cursor.execute(self)
        OTV = cursor.fetchall()
        return(OTV)
        
    def POST(self):
        """Отправляет данные в Базу данных
        """
        connection = pymysql.connect(host="37.140.192.90", user='u1102095_ting', password='S7x6U9j2', database='u1102095_ting_v2', charset="utf8")
        cursor = connection.cursor()  
        cursor.execute(self) 
        connection.commit()
        return('True')
    
    def Check_user_in_db(self, login, password):
        connection = pymysql.connect(host="37.140.192.90", user='u1102095_ting', password='S7x6U9j2', database='u1102095_ting_v2', charset="utf8")
        cursor = connection.cursor()
        cursor.execute(f'select password, id from users where login = "{login}" or email = "{login}"')
        OTV = cursor.fetchall()
        error = 0
        ids = 0
        try:
            if(str(OTV[0][0]) == password):
                error = 0
                ids = OTV[0][1]
            else:
                error = 2
        except:
            error = 1
        return(error, ids)
        


class user_():
    """Работа с локальными данными пользователей"""
    
    def GetUserDate(self):
        """Получение локальных данных пользователя
        """
        if not self in AllClient: # Создание локальных данных пользователя
            AllClient[self] = {
                'auth': False,
                'authCode': None,
                'id_in_db': None,
                'codeEmail': None,
                'datauser': None
            }     
        return(AllClient[self])
    
    def GetUserAuth(self):
        userData = user_.GetUserDate(self)
        print(userData)
        
        return(userData['auth'])
    
    def login(self, idss = None):
        """
        Выдаёт флаг `auth`, чтобы убрать флаг используйте::
        
            user_.logout(user_cashe)

        """
        userData = user_.GetUserDate(self)
        userData['auth'] = True
        userData['id_in_db'] = int(idss)
        return(True)
        
    def logout(self):
        """
        Убирает флаг `auth`, чтобы вернуть флаг используйте::
        
            user_.login(user_cashe)

        """
        userData = user_.GetUserDate(self)
        userData['auth'] = False
        userData['id_in_db'] = None
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
                
                codeE, ids = DB.Check_user_in_db(None, request.form['login'], request.form['password'])
                print(codeE, ids)
                
                if codeE == 1:
                    rt['ErrorL'] = True
                    rt['ErrorP'] = True
            
                if(codeE == 2):
                    rt['ErrorP'] = True
                
                if(codeE == 0):
                    user_.login(user_cashe, idss = ids)
                
            else:
                rt['status'] = False
                rt['info'] = 'API NOT FOUND'
            
            returnValue = rt
    
        elif(method == 'mailcheck'):
            
            code = '#'+str(request.form['code'])
            codeEmail = user_.GetUserDate(user_cashe)['codeEmail']
            
            print(code, codeEmail)
            
            error =  {
                'status':200,
                'error': None
            }
            
            if(str(code) == str(codeEmail)):
                error['error'] = False       
            else:
                error['error'] = True
            
            return(error)

        elif(method == 'create'):
            req = request.form
            text = (f'select login, email from users where login = "{req["login"]}" or email = "{req["email"]}"')
            print(req)
            mails = DB.GET(text)
            print('create', req,'\n',mails,'\n')
            error = {'login':None,
                     'mail':None,
                     'status':200}
            
            if not(('@mail.ru' in req["email"]) or 
                ('@gmail.com' in req["email"]) or 
                ('@bk.ru' in req["email"]) or 
                ('@outlook.com' in req["email"]) or 
                ('@list.ru' in req["email"]) or 
                ('@list.ru' in req["email"]) or 
                ('@yandex.ru' in req["email"]) or 
                ('@inbox.ru' in req["email"])):error['mail'] = True
            
            try:
                em = mails[0][1]
                if(mails[0][0] == req["login"]):error['login'] = True
                if(mails[0][1] == req["email"]):error['email'] = True
            except:
                pass
            
            print(error)
            if(error['login'] == None and error['mail'] == None):
                a = user_.GetUserDate(user_cashe)
                a['codeEmail'] = generate_Color_hex()
                
                
                ##
                ##### Создание аккаунта с флагом (не подтвержден)
                ##
            return(error)
        
    
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


@application.route('/email_confirmation')
def email_confirmation():
    if not request.cookies.get('TING'):
        return redirect('/')
    user_cashe = CACHE.Check(request)
    if(user_.GetUserDate(user_cashe)['codeEmail'] != None):
        return render_template('mail_code.html')
    else:
        return redirect('/')


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
        tests = DB.GET('select * from tests')
        print(tests)
        idUs = user_.GetUserDate(user_cashe)['id_in_db']
        print(idUs)
        data = DB.GET(f'select * from users where id = {idUs}')
        stats = DB.GET(f'select * from userStats where fromUser = {idUs}')
        try:     
            data = data[0]
            stats = stats[0]
            res = make_response(render_template('index.html', data=data, login = lg, stats = stats, tests=tests))
            res.set_cookie('TING', f'{user_cashe}') 
        except:
            res = redirect('/')

        
    return (res)


@application.errorhandler(404)
def page_not_found(e):
    return ("errors") #('404.html')

if __name__=="__main__":
    application.run(debug=True, host='192.168.3.2',port='80')