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


def thread(func): #Функция запуска нового потока
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper


@thread
def SendMessageCode(ToMail,  Code, name):
    addr_from = "ting@ru-ting.ru"                # Адресат
    password  = "TESTPASSMAIL12"                 # Пароль
    addr_to   = ToMail                            # Получатель

    msg = MIMEMultipart()                               # Создаем сообщение
    msg['From']    = addr_from                          # Адресат
    msg['To']      = addr_to                            # Получатель
    msg['Subject'] = 'TING подтверждение почты'                   # Тема сообщения

    body = ""
    msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

    urlMail = Code
    html = f"""\
    <html>
        <head></head>
        <body>
            <div style="background-color:#f7f7f8;">
                <div style="margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                            <tr>
                                <td style="border:0px solid #ffffff;direction:ltr;font-size:0px;padding:20px 0px 20px 0px;padding-bottom:20px;padding-left:0px;padding-right:0px;padding-top:20px;text-align:center;">
                                    <div class="mj-column-per-33-333333333333336_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"></table>
                                    </div>
                                    <div class="mj-column-per-33-333333333333336_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                            <tbody>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px; margin: auto;">
                                                            <tbody>
                                                                <tr>
                                                                    <td style="width:150px;">
                                                                        <a href="https://ru-ting.ru" target="_blank" rel=" noopener noreferrer"><img alt="Logo" height="auto" src="https://firstgirls.ru/TingICons.png" style="border:none;border-radius:0px;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="150"></a>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                    <div class="mj-column-per-33-333333333333336_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"></table>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
                        <tbody>
                            <tr>
                                <td style="border:1px solid #ECECEC;direction:ltr;font-size:0px;padding:40px 0px 40px 0px;padding-bottom:40px;padding-left:0px;padding-right:0px;padding-top:40px;text-align:center;">
                                    <div class="mj-column-per-100_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                            <tbody>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:0px 40px 0px 40px;padding-top:0px;padding-right:40px;padding-bottom:0px;padding-left:40px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:26px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <h1 class="text-build-content_mr_css_attr" style="text-align:center;line-height:40px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;font-weight: normal;"><span style="color:#000;font-size:40px;line-height:40px;font-family:Inter, Helvetica, Arial, sans-serif;"><b>Welcome on board!</b></span></h1></div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:0px 40px 10px 40px;padding-top:0px;padding-right:40px;padding-bottom:10px;padding-left:40px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:13px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <p class="text-build-content_mr_css_attr" style="text-align: center;line-height: 25px;margin: 10px 0;margin-top: 10px;margin-bottom: 10px;"><span style="color:#7d7c83;font-size:18px;line-height:25px;font-family:Inter, Helvetica, Arial, sans-serif;">Hello {name},<br>Please confirm your email to activate your new account.</span></p>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="font-size:0px;padding:20px 40px 20px 40px;padding-top:20px;padding-right:40px;padding-bottom:20px;padding-left:40px;word-break:break-word;">
                                                        <p style="border-top:solid 1px #ECECEC;font-size:1;margin:0px auto;width:100%;"></p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:10px 40px 10px 40px;padding-top:10px;padding-right:40px;padding-bottom:10px;padding-left:40px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:16px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <p class="text-build-content_mr_css_attr" style="line-height: 25px;margin: 10px 0;margin-top: 10px;margin-bottom: 10px;"><span style="color:#7d7c83;font-size:16px;line-height:25px;font-family:Inter, Helvetica, Arial, sans-serif;">Confirm by using this color code:</span></p>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="font-size:0px;padding:0px;padding-top:0px;padding-bottom:0px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:13px;letter-spacing:normal;line-height:24px;color:#000000;">
                                                            <div style="background:#{urlMail};color: black;box-shadow:inset rgba(0,0,0,0.2) 0 0 1px;margin:0 40px;padding:40px 30px 20px;text-align:center;border-radius: 8px;font-family: Inter, sans-serif;">
                                                                <div style="font-size: 36px;vertical-align:middle;font-weight:600;text-transform: uppercase;letter-spacing:0.05em;"><span style="user-select: none;"># </span>{urlMail}</div>
                                                                <div style="margin-top: 20px;color: black;">TING</div>
                                                            </div>>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                </tr>
                                                <tr>
                                                    <td style="font-size:0px;padding:40px 40px 40px 40px;padding-top:40px;padding-right:40px;padding-bottom:40px;padding-left:40px;word-break:break-word;">
                                                        <p style="border-top:solid 1px #ECECEC;font-size:1;margin:0px auto;width:100%;"></p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:0px 40px 0px 40px;padding-top:0px;padding-right:40px;padding-bottom:0px;padding-left:40px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:15px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <p class="text-build-content_mr_css_attr" style="text-align: center;line-height: 25px;margin: 10px 0;margin-top: 10px;margin-bottom: 10px;"><span style="color:#7d7c83;font-size:15px;line-height:25px;font-family:Inter, Helvetica, Arial, sans-serif;">Your friends at Coolors. 💙</span></p>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div style="margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                            <tr>
                                <td style="border:0px solid #ffffff;direction:ltr;font-size:0px;padding:20px 0px 10px 0px;padding-bottom:10px;padding-left:0px;padding-right:0px;padding-top:20px;text-align:center;">
                                    <div class="mj-column-per-100_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                            <tbody>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-bottom:0px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:13px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <p class="text-build-content_mr_css_attr" style="text-align: center;margin: 10px 0;margin-top: 10px;margin-bottom: 10px;"><span style="color:#7d7c83;font-size:13px;line-height:20px;font-family:Inter, Helvetica, Arial, sans-serif;">© 2020 TING from @WT_Tini</span></p>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </body>
    </html>
    """

    
    msg.attach(MIMEText(html, 'html', 'utf-8'))         # Добавляем в сообщение HTML-фрагмент

    server = smtplib.SMTP('mail.hosting.reg.ru', 587)           # Создаем объект SMTP                     # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    server.starttls()                                   # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                   # Получаем доступ
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()                                       # Выходим




@thread
def SendMessageReloginPass(ToMail,  CodeMail, name):
    addr_from = "ting@ru-ting.ru"                # Адресат
    password  = "TESTPASSMAIL12"                 # Пароль
    addr_to   = ToMail                            # Получатель

    msg = MIMEMultipart()                               # Создаем сообщение
    msg['From']    = addr_from                          # Адресат
    msg['To']      = addr_to                            # Получатель
    msg['Subject'] = 'TING сброс пароля'                   # Тема сообщения

    body = ""
    msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст
    html = f"""\
    <html>
    <head></head>
        <body>
            <div style="background-color:#f7f7f8;">
                <div style="margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                            <tr>
                                <td style="border:0px solid #ffffff;direction:ltr;font-size:0px;padding:20px 0px 20px 0px;padding-bottom:20px;padding-left:0px;padding-right:0px;padding-top:20px;text-align:center;">
                                    <div class="mj-column-per-33-333333333333336_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"></table>
                                    </div>
                                    <div class="mj-column-per-33-333333333333336_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                            <tbody>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px; margin: auto;">
                                                            <tbody>
                                                                <tr>
                                                                    <td style="width:150px;">
                                                                        <a href="https://ru-ting.ru" target="_blank" rel=" noopener noreferrer"><img alt="Logo" height="auto" src="https://firstgirls.ru/TingICons.png" style="border:none;border-radius:0px;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="150"></a>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                    <div class="mj-column-per-33-333333333333336_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"></table>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
                        <tbody>
                            <tr>
                                <td style="border:1px solid #ECECEC;direction:ltr;font-size:0px;padding:40px 0px 40px 0px;padding-bottom:40px;padding-left:0px;padding-right:0px;padding-top:40px;text-align:center;">
                                    <div class="mj-column-per-100_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                            <tbody>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:0px 40px 0px 40px;padding-top:0px;padding-right:40px;padding-bottom:0px;padding-left:40px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:26px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <h1 class="text-build-content_mr_css_attr" style="text-align:center;line-height:40px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;margin-top: 10px;margin-bottom: 10px;font-weight: normal;"><span style="color:#000;font-size:40px;line-height:40px;font-family:Inter, Helvetica, Arial, sans-serif;"><b>Hey stranger!</b></span></h1></div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:0px 40px 10px 40px;padding-top:0px;padding-right:40px;padding-bottom:10px;padding-left:40px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:13px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <p class="text-build-content_mr_css_attr" style="text-align: center;line-height: 25px;margin: 10px 0;margin-top: 10px;margin-bottom: 10px;"><span style="color:#7d7c83;font-size:18px;line-height:25px;font-family:Inter, Helvetica, Arial, sans-serif;">Hello {name}.<br></span></p>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="font-size:0px;padding:20px 40px 20px 40px;padding-top:20px;padding-right:40px;padding-bottom:20px;padding-left:40px;word-break:break-word;">
                                                        <p style="border-top:solid 1px #ECECEC;font-size:1;margin:0px auto;width:100%;"></p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:10px 40px 10px 40px;padding-top:10px;padding-right:40px;padding-bottom:10px;padding-left:40px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:16px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <p class="text-build-content_mr_css_attr" style="line-height: 25px;margin: 10px 0;margin-top: 10px;margin-bottom: 10px;"><span style="color:#7d7c83;font-size:16px;line-height:25px;font-family:Inter, Helvetica, Arial, sans-serif;">Для сброса пароля нажмите на текст снизу</span></p>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="font-size:0px;padding:0px;padding-top:0px;padding-bottom:0px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:13px;letter-spacing:normal;line-height:24px;color:#000000;">
                                                            <div style="background: #555555;;color: black;box-shadow:inset rgba(0,0,0,0.2) 0 0 1px;margin:0 40px;text-align:center;border-radius: 8px;font-family: Inter, sans-serif;">
                                                                <div style="font-size: 36px;vertical-align:middle;font-weight:600;text-transform: uppercase;letter-spacing:0.05em;"><span style="user-select: none;"></span>
                                                                    <a href="{CodeMail}" target="_blank" rel=" noopener noreferrer"><img alt="Нажмите для сброса пароля" height="auto" src="https://firstgirls.ru/TingICons.png" style="margin: 0 auto; border:none;border-radius:0px;display:block;outline:none;text-decoration:none;height:52%;width:52%;font-size:13px;" width="150"></a>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                </tr>
                                                <tr>
                                                    <td style="font-size:0px;padding:40px 40px 40px 40px;padding-top:40px;padding-right:40px;padding-bottom:40px;padding-left:40px;word-break:break-word;">
                                                        <p style="border-top:solid 1px #ECECEC;font-size:1;margin:0px auto;width:100%;"></p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:0px 40px 0px 40px;padding-top:0px;padding-right:40px;padding-bottom:0px;padding-left:40px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:15px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <p class="text-build-content_mr_css_attr" style="text-align: center;line-height: 25px;margin: 10px 0;margin-top: 10px;margin-bottom: 10px;"><span style="color:#7d7c83;font-size:15px;line-height:25px;font-family:Inter, Helvetica, Arial, sans-serif;">Your friends at Coolors. 💙</span></p>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div style="margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                            <tr>
                                <td style="border:0px solid #ffffff;direction:ltr;font-size:0px;padding:20px 0px 10px 0px;padding-bottom:10px;padding-left:0px;padding-right:0px;padding-top:20px;text-align:center;">
                                    <div class="mj-column-per-100_mr_css_attr mj-outlook-group-fix_mr_css_attr" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                            <tbody>
                                                <tr>
                                                    <td align="left" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-bottom:0px;word-break:break-word;">
                                                        <div style="font-family:Arial, sans-serif;font-size:13px;letter-spacing:normal;line-height:1;text-align:left;color:#000000;">
                                                            <p class="text-build-content_mr_css_attr" style="text-align: center;margin: 10px 0;margin-top: 10px;margin-bottom: 10px;"><span style="color:#7d7c83;font-size:13px;line-height:20px;font-family:Inter, Helvetica, Arial, sans-serif;">© 2020 TING from @WT_Tini</span></p>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </body>
    </html>
    """

    
    msg.attach(MIMEText(html, 'html', 'utf-8'))         # Добавляем в сообщение HTML-фрагмент

    server = smtplib.SMTP('mail.hosting.reg.ru', 587)             # Создаем объект SMTP                     # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    server.starttls()                                   # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                   # Получаем доступ
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()                                       # Выходим






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
    

def GenerateCodeGame():
    GameCode = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    return(GameCode)

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
                'datauser': None,
                'information': None,
                'set': 0,
                'game': {
                    
                    'status': False,
                    'code_in_game': None,
                    'typeGame': None,
                    'questions_id': '0',
                    'true_otv': None,
                    'count_true': 0,
                    'to_win': None,
                    'мultiplier':None
                }
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


def GetQuestiions(Type, questions):
    questions_c = questions['game']['questions_id']
    print(Type, questions, questions_c)
    texts = f'SELECT * FROM Questions where id NOT IN ({questions_c}) AND fromTest = {Type} ORDER BY rand() LIMIT 1'
    print(texts)
    
    mass = DB.GET(texts)
    T_a = ''
    for a in mass:
        T_a += str(a[0])+','
    T_a = T_a[:-1]
    print(T_a)
    
    questions['game']['questions_id'] =  str(questions['game']['questions_id']) + ',' + str(T_a)
    return(mass)


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
                print(user_.GetUserDate(user_cashe))
                DB.POST(f'UPDATE users set mailCheck = 1 where id = {user_.GetUserDate(user_cashe)["id_in_db"]}')
                user_.login(user_cashe,  user_.GetUserDate(user_cashe)['id_in_db'] )
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
                
                
                
                print(req)
                print(datetime.datetime.now())
                te = (f"""INSERT INTO users VALUES  
                        (Null, '{req['name']}', '{req['lastName']}', '{req['login']}', '{req['password']}', '{req['year']}-{req['mouth']}-{req['day']}', '{req['sex']}', '{req['email']}', 0, Null, 0, 'user', '{datetime.datetime.now()}')    
                        
                        """)
                print(te)
                DB.POST(te) # Создание аккаунта с флагом (не подтвержден)
                idq = DB.GET('select max(id) from users')[0][0]
                a['id_in_db'] = idq
                DB.POST(f""" INSERT INTO userStats VALUES (Null, {idq}, 0, 0, 0, 0, 0) """)
                
                
                #Отправить на почту
                SendMessageCode(req['email'],str(a['codeEmail']).replace('#',''),req['login'])

            return(error)
        
    
    else:
        returnValue['status'] = 408
        
    return(returnValue)
    
    

@application.route('/tingAPI/game/<method>', methods=["POST"])
def tingAPI_Game(method):
    if not request.cookies.get('TING'):
        return ('FalseAPI')
    user_cashe = CACHE.Check(request)
    userdata = user_.GetUserDate(user_cashe)

    returnValue = {
        'status': 200,
        'method': method
        }
    TN = str(time.time())
    TN = TN[:TN.find('.')]
    TM = str(request.form['timeN'])[0:-3]

    RZ = (int(TN) - int(TM))
    
    if(RZ <= 10 and RZ >= -5):
        if(method == 'StartNewGame'):
            print(userdata)

            if(userdata['game']['code_in_game'] == None and userdata['game']['status'] == False):
                # Проверка монет
                stavka = 5
                balance = DB.GET(f'select balance from users where id = {userdata["id_in_db"]}')[0][0]
                if(balance >= stavka):
                    userdata['set'] = stavka
                    DB.POST(f'UPDATE users set balance = {balance - 5} where id = {userdata["id_in_db"]}')
                elif(balance == 0):
                    userdata['set'] = 1
                else:
                    userdata['set'] = balance
                    DB.POST(f'UPDATE users set balance = {0} where id = {userdata["id_in_db"]}')
                gameCode = GenerateCodeGame()
                userdata['game']['code_in_game'] = gameCode
                userdata['game']['typeGame'] = request.form['TypeGame']
                userdata = user_.GetUserDate(user_cashe)
                print(userdata)
                userdata['game']['questions_id'] = 0
                userdata['game']['count_true'] = 0
                
                daq = DB.GET(f'SELECT toWin, мultiplier FROM tests where id = {request.form["TypeGame"]}')[0]
                print('daqdaq', daq)
                userdata['game']['to_win'] = daq[0]
                userdata['game']['мultiplier'] = daq[1]
                userdata['game']['status'] = False
                
                
                RV = {
                    'status': 200,
                    'method': method,
                    'data': {
                        'CodeGame': gameCode
                    }
                }
            else:
                RV = {
                    'status': 208,
                    'method': method,
                }
            return(RV)
    
        elif(method =='Check'):
            returnValue = {
                    'status': 200,
                    'method': method
                    }
            if(request.form['code_in_game'] == userdata['game']['code_in_game']):
                print('Коды верные')
                print(request.form['otv'] , userdata['game']['true_otv'])
                
                if(request.form['otv'] == userdata['game']['true_otv']):
                    print('Верно')   
                    userdata['game']['count_true'] =  userdata['game']['count_true'] + 1 
                    # 
                    # 
                    #  
                    
                    # 
                    # 
                    # 
                    if(userdata['game']['to_win'] <= userdata['game']['count_true']):
                        bonus = 0 
                        print('Win')
                        c = DB.GET(f'SELECT countVictor, {userdata["game"]["typeGame"]+"_test_victory"}, {userdata["game"]["typeGame"]+"_test_now"} FROM userStats where fromUser = {userdata["id_in_db"]}')[0]
                        if(c[2] >= 5):
                            DB.POST(f'UPDATE userStats set countVictor = {c[0]+1}, {userdata["game"]["typeGame"]+"_test_victory"} = {c[1]+1}, {userdata["game"]["typeGame"]+"_test_now"} = 0 where fromUser = {userdata["id_in_db"]}')
                            print('Дать приз и победу')
                            bonus = 50
                        else:
                            DB.POST(f'UPDATE userStats set countVictor = {c[0]+1}, {userdata["game"]["typeGame"]+"_test_victory"} = {c[1]+1}, {userdata["game"]["typeGame"]+"_test_now"} = {c[2]+1} where fromUser = {userdata["id_in_db"]}')

                        c = DB.GET(f'SELECT balance FROM users where id = {userdata["id_in_db"]}')[0][0] + (userdata['set'] * userdata['game']['мultiplier'] + bonus) 
                        DB.POST(f'UPDATE users set balance = {c} where id = {userdata["id_in_db"]}')
                        
                        
                        returnValue['status'] = 202
                else:
                    returnValue['status'] = 204
                    print('Не верно')
                    c = DB.GET(f'SELECT countLoss, {userdata["game"]["typeGame"]+"_test_loss"} FROM userStats where fromUser = {userdata["id_in_db"]}')[0]
                    DB.POST(f'UPDATE userStats set countLoss ={c[0]+1},{userdata["game"]["typeGame"]+"_test_loss"} = {c[1]+1} where fromUser = {userdata["id_in_db"]}')
                        
                    userdata['game']['count_true'] = 0

                return(returnValue)
                
            else:
                userdata['game']['code_in_game'] = None
                returnValue['status'] = 208
                return(returnValue)
            
        elif(method =='get_question'):
            returnValue = {
                    'status': 200,
                    'method': method
                    }
            if(request.form['code_in_game'] == userdata['game']['code_in_game']):
                print('Коды верные')
                a = GetQuestiions(userdata['game']['typeGame'], userdata)[0]
                userdata['game']['true_otv'] = a[6]
                Questions_Var = [a[2],a[3],a[4],a[5]]
                # Questions_Var = sorted(Questions_Var, key=lambda A: random.random()) #без него всегда верна первая
                print(Questions_Var)
                returnValue['data'] = {'questions_Var': Questions_Var,
                                       'question': a[1],
                                       'count_true': userdata['game']['count_true'],
                                       'count_to_win':userdata['game']['to_win']}
                return(returnValue)
                
            else:
                userdata['game']['code_in_game'] = None
                returnValue['status'] = 208
                return(returnValue)

    
    else:
        returnValue['status'] = 406

    return(returnValue)


#Игровые ссылки
@application.route('/game')
def game_start():
    if not request.cookies.get('TING'):
        return redirect('/')
    user_cashe = CACHE.Check(request)
    lg = user_.GetUserAuth(user_cashe)
    userdata = user_.GetUserDate(user_cashe)
    if lg == False:
        res = make_response(redirect('/'))
        res.set_cookie('TING', f'{user_cashe}') 
        return(res)
    else:
        if(userdata['game']['status'] == False):
            print('ud',userdata)
            Questions_Var = ['0', '1', '2', '3']
            userdata['game']['status'] = True
        else:
            userdata['game']['code_in_game'] = None
            userdata['game']['count_true'] = 0
            
            userdata['information'] = 'При перезагрузки страницы, игры считается проигранной'
            userdata['game']['status'] = False
            return redirect('/')
    return render_template('/Game.html', Questions_Var = Questions_Var, Question = 'q')


#Пасивные ссылки


@application.route('/stats')
def stats():
    user_cashe = CACHE.Check(request)
    lg = user_.GetUserAuth(user_cashe)
    res = ''
    if lg == False:
        res = make_response(redirect('/'))
        res.set_cookie('TING', f'{user_cashe}') 
    else:
        tests = DB.GET('select * from tests')
        print(tests,lg)
        idUss = user_.GetUserDate(user_cashe)
        idUs = idUss['id_in_db']
        print(idUs)
        data = DB.GET(f'select * from users where id = {idUs}')[0]
        stats = DB.GET(f'select * from userStats where fromUser = {idUs}')[0]
        # el = [[stats[2], stats[3]]] Общая статистика
        el =[]
        sc = 4
        for a in range(len(tests)):
            qqe = []
            for es in range(3):
                qqe.append(stats[sc])
                sc += 1
            qqe.append(tests[a][1])
            el.append(qqe)
        try:    

            res = make_response(render_template('st.html',data = data, login = lg, stats = el))

            res.set_cookie('TING', f'{user_cashe}') 
        except:
            user_.GetUserDate(user_cashe)['auth'] = False
            res = redirect('/')

        
    return (res)

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
    print('LGG',lg)
    if lg == False:
        res = make_response(redirect('/'))
        res.set_cookie('TING', f'{user_cashe}') 
    else:
        tests = DB.GET('select * from tests')
        print(tests)
        idUss = user_.GetUserDate(user_cashe)
        idUs = idUss['id_in_db']
        print(idUs)
        data = DB.GET(f'select * from users where id = {idUs}')
        stats = DB.GET(f'select * from userStats where fromUser = {idUs}')
        try:     
            datad = data[0]
            statsd = stats[0]
            print(datad, statsd)
            print(lg)
            idUss['game']['code_in_game'] = None
            idUss['game']['status'] = False
            res = make_response(render_template('index.html', data=datad, login = lg, stats = statsd, tests=tests, information = idUss['information']))
            idUss['information'] = None
            print('das')
            res.set_cookie('TING', f'{user_cashe}') 
        except:
            print('exp')
            user_.GetUserDate(user_cashe)['auth'] = False
            res = redirect('/')

        
    return (res)


@application.errorhandler(404)
def page_not_found(e):
    return render_template('errors.html') #('404.html')

@application.route('/test')
def test():
    return render_template('231')
    return('/data')


if __name__=="__main__":
    application.run(debug=True, host='192.168.3.2',port='80')