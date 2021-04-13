#!/usr/bin/env python
from flask import Flask, render_template, request, session, Response, make_response, redirect, jsonify

import smtplib                                      # Импортируем библиотеку по работе с SMTP
# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML

import datetime
import uuid
import hashlib
import sqlite3
import pymysql
import requests
import time
import string
import random
import threading
application = Flask(__name__)

data = [51,'1525']


def thread(func): #Функция запуска нового потока
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper


@thread
def SendMessageMail(ToMail,  URL, name):
    addr_from = "ting@ru-ting.ru"                # Адресат
    password  = "TESTPASSMAIL12"                 # Пароль
    addr_to   = ToMail                            # Получатель

    msg = MIMEMultipart()                               # Создаем сообщение
    msg['From']    = addr_from                          # Адресат
    msg['To']      = addr_to                            # Получатель
    msg['Subject'] = 'TING подтверждение почты'                   # Тема сообщения

    body = ""
    msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

    urlMail = URL
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
def SendMessageCodeToMail(ToMail,  CodeMail, name):
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


class DataClass():
    MNData = {}
    mailDates = {}
    DataMain = {}
    DataInfo = {}
    IDUserLogins = {}
    RegInfo = {}
    GameInfo = {}
    GameDatas = {}
    StartGames = {}
    

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

#Пароль чекерс
def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 

def GENERCASH(IPs):
    cc = str('_TING_' + str(IPs) + '_TING_' + str(datetime.datetime.now()))
    bytesvalue = cc.encode('utf-8')
    hash_object = hashlib.md5(bytesvalue)
    Hash_user = (hash_object.hexdigest())
    return(Hash_user)


class CheckData(object):
    def Check_L(self):
        try:
            login = DataClass.DataMain[self]['Login']
        except:
            DataClass.DataMain[self] = {'Login':"False"}
            login = (DataClass.DataMain[self]['Login'])
        print(login)
        return(login)
    
    
    def SetLoginTrue(self):
        try:
            DataClass.DataMain[self] = {'Login':"True"}
            login = DataClass.DataMain[self]['Login']
            print(login)
        except:
            login = False
        return(login)

        
class DB(object):
    def GetAdmin():
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Settings")
        OTV = cursor.fetchall()[0]
        return(OTV)
        
    def CheckLogin(self):
        print('sas ', self)
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE Login = '{self[0]}' or Email = '{self[0]}'")
        OTV = cursor.fetchall()
        print(OTV)
        try:
            a = (OTV[0])
            print('Есть ',a)
            if check_password(a[4], self[1]):
                print('Вы ввели правильный пароль')
                DataClass.IDUserLogins[self[2]] = a[0]
                return('')
            else:
                print('Извините, но пароли не совпадают')
                return('1')
        except:
            return('0 1')

    def TakeData(self):
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Users u, Stats s WHERE s.id = u.id and s.id = '{self}'")
        OTV = cursor.fetchall()
        try:
            b = (OTV[0])
        except:
            b = 'Такого нет'
        return(b)

    def CreateNewAccount(self):
        #self ([Name1R, Name2R, Email, Login, Pass])
        print(self)
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Users WHERE Login = '{self[3]}' or Email = '{self[2]}'")
        OTV = cursor.fetchall()
        try:
            P = OTV[0][0]
            print(OTV)
            print('Такой есть')
            return('False')
        except:
            b = DB.GetAdmin()
            cursor.execute(f"INSERT INTO Users (`id`, `FirstName`, `SecondName`, `Login`, `Password`, `Email`, `Balance`, `Bonus`, ForgMail, mailСheck) VALUES (null, '{self[0]}', '{self[1]}', '{self[3]}', '{self[4]}', '{self[2]}', {b[3]}, {b[3]}, '', 1)")
            connection.commit()
            LastID = cursor.lastrowid
            cursor.execute(f"INSERT INTO Stats (`id`) VALUES ({LastID})") 
            connection.commit()
            return('True')

    def CheckRegister(self):
        #self ([Mail, Login])
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Users WHERE Login = '{self[1]}' or Email = '{self[0]}'")
        OTV = cursor.fetchall()
        print(OTV)
        ErrorList = ''
        try:
            a = OTV[0][0]
            if (str(self[0]) in str(OTV)):
                ErrorList += '2 '
            if (str(self[1]) in str(OTV)):
                ErrorList += '3 '   
        except:
            ErrorList = ''
        return (ErrorList)    

    def GetBag_1in6(self):
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()

        cursor.execute(f'SELECT SeeWord FROM Stats where id = {self}')
        mm = str(cursor.fetchall()[0][0])
        cursor.execute(f'SELECT * FROM 1In6 WHERE id NOT IN ({mm}) ORDER BY RAND() limit 6') #без повторов
        OTV = cursor.fetchall()
        try:
            d = OTV[5][0]
            mm += (", " + str(OTV[0][0]))
            cursor.execute(f"UPDATE Stats SET SeeWord = '{mm}' WHERE id={self}")
            connection.commit()
            g = OTV
            v = True
            return(g)
        except:
            cursor.execute(f"UPDATE Stats SET SeeWord = '0' WHERE id={self}")
            connection.commit()
            cursor.execute(f'SELECT SeeWord FROM Stats where id = {self}')
            mm = str(cursor.fetchall()[0][0])
            cursor.execute(f'SELECT * FROM 1In6 WHERE id NOT IN ({mm}) ORDER BY RAND() limit 6') #без повторов
            OTV = cursor.fetchall()
            d = OTV[5][0]
            mm += (", " + str(OTV[0][0]))
            cursor.execute(f"UPDATE Stats SET SeeWord = '{mm}' WHERE id={self}")
            connection.commit()
            g = OTV
            return(g)
            
    def GetBag_Questions(self):
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()

        cursor.execute(f'SELECT SeeQuestionsAll FROM Stats where id = {self}')
        mm = str(cursor.fetchall()[0][0])
        cursor.execute(f'SELECT * FROM Question WHERE id NOT IN ({mm}) ORDER BY RAND() limit 1') #без повторов
        OTV = cursor.fetchall()
        try:
            d = OTV[0][0]
            mm += (", " + str(OTV[0][0]))
            cursor.execute(f"UPDATE Stats SET SeeQuestionsAll = '{mm}' WHERE id={self}")
            connection.commit()
            g = OTV
            v = True
            return(g)
        except:
            cursor.execute(f"UPDATE Stats SET SeeQuestionsAll = '0' WHERE id={self}")
            connection.commit()
            cursor.execute(f'SELECT SeeQuestionsAll FROM Stats where id = {self}')
            mm = str(cursor.fetchall()[0][0])
            cursor.execute(f'SELECT * FROM Question WHERE id NOT IN ({mm}) ORDER BY RAND() limit 1') #без повторов
            OTV = cursor.fetchall()
            d = OTV[0][0]
            mm += (", " + str(OTV[0][0]))
            cursor.execute(f"UPDATE Stats SET SeeQuestionsAll = '{mm}' WHERE id={self}")
            connection.commit()
            g = OTV
            return(g)

    def AddContinueGame(self):
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM Stats where id = {self[0]}')
        OTV = (cursor.fetchall()[0])
        cursor.execute(f'SELECT 1in6Prize, QuestionsPrise FROM Settings')
        OTVPrise = (cursor.fetchall()[0])
        if(self[1] == '1in6'):
            if(int(OTV[4]) <= 3):
                T = int(OTV[4]) + 1
                cursor.execute(f'UPDATE Stats SET 1in6Seria = {T}, AllScore1In6 = {int(OTV[3]) + 1} where id = {self[0]}')
                connection.commit()
                return("True")
            else:
                if(adminPPTest == False):
                    cursor.execute(f'SELECT Balance, winsMoney FROM Users where id = {self[0]}')
                    OTVUsers = (cursor.fetchall()[0])

                    b = float(OTVUsers[0]) + float(OTVPrise[0])
                    WM = float(OTVUsers[1]) + float(OTVPrise[0])
                    cursor.execute(f'UPDATE Users SET Balance = {b}, winsMoney = {WM} where id = {self[0]}')
                    connection.commit()


                


                cursor.execute(f'UPDATE Stats SET 1in6Seria = 0, Score1In6 = {int(OTV[2]) + 1} where id = {self[0]}')
                connection.commit()
                return("Max")



        elif(self[1] == 'Que'):
            if(int(OTV[8]) <= 4):
                T = int(OTV[8]) + 1
                cursor.execute(f'UPDATE Stats SET QuestionsSeria = {T}, AllScoreQuestions = {int(OTV[7]) + 1}  where id = {self[0]}')
                connection.commit()
                return("True")
            else:
                if(adminPPTest == False):
                    cursor.execute(f'SELECT Balance, winsMoney FROM Users where id = {self[0]}')
                    OTVUsers = (cursor.fetchall()[0])
                    b = float(OTVUsers[0]) + float(OTVPrise[1])
                    WM = float(OTVUsers[1]) + float(OTVPrise[1])
                    cursor.execute(f'UPDATE Users SET Balance = {b}, winsMoney = {WM} where id = {self[0]}')
                    connection.commit()
                    
                cursor.execute(f'UPDATE Stats SET QuestionsSeria = 0, ScoreQuestions = {int(OTV[6]) + 1} where id = {self[0]}')
                connection.commit()
                return("Max")

    def ClearTrueSer(self):
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        if (self[1] == 1):
            cursor.execute(f'UPDATE Stats SET 1in6Seria = 0 where id = {self[0]}')
            connection.commit()
        elif (self[1] == 2):
            print('d')
            cursor.execute(f'UPDATE Stats SET QuestionsSeria = 0 where id = {self[0]}')
            connection.commit()

    def GetUpdate():
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Updates")
        OTV = cursor.fetchall()
        return(OTV)

    def GetVideo():
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM TINGVideo")
        OTV = cursor.fetchall()
        return(OTV)

    def ReturnMail(self):
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE Login = '{self}' or Email = '{self}'")
        OTV = cursor.fetchall()
        try:
            a = OTV[0]
            data = True
        except:
            data = False
        return(OTV, data)

    def ForgettenMailDB(self):
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE ForgMail = '{self}'")
        OTV = cursor.fetchall()
        print(OTV)
        if (len(OTV) == 0):
            return("False")
        else:
            return("True")
    
    def CreateForgetenMailCode(self):
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE Login = '{self}' or Email = '{self}'")
        OTVS = cursor.fetchall()
        MailCodeRes = ''
        
        while(True):
            MailCodeRes = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))
            cursor.execute(f"SELECT * FROM Users WHERE ForgMail = '{MailCodeRes}'")
            OTV = cursor.fetchall()
            if(len(OTV) != 0):
                pass
            else:
                cursor.execute(f'UPDATE Users SET ForgMail = "{MailCodeRes}" where id = {OTVS[0][0]}')
                connection.commit()
                break
        return(MailCodeRes, OTVS[0][3], OTVS[0][5])        

    def SetNewPass(self):
        connection = pymysql.connect("37.140.192.90", 'u1102095_root', 'rootpass!', 'u1102095_ting', charset="utf8", port=3306)
        cursor = connection.cursor()
        Passwords = hash_password(self[0])
        cursor.execute(f'UPDATE Users SET ForgMail = "", Password = "{Passwords}" where ForgMail = "{self[1]}"')
        connection.commit()


@application.route('/CheckDataRegister', methods=["POST","GET"])
def CheckDataRegister():
    if request.method == "POST": 
        try:
            print(request.args)
            Mail = request.args.get('email')
            Login = request.args.get('Login')
            P1 = request.args.get('PassFirst')
            P2 = request.args.get('PassSecond')
            Erors = ''
            print(Mail, Login, P1, P2)
            MailChec = str(Mail) + " !"
            print(MailChec)
            if (('@mail.ru !' in MailChec) or 
                ('@gmail.com !' in MailChec) or 
                ('@bk.ru !' in MailChec) or 
                ('@outlook.com !' in MailChec) or 
                ('@list.ru !' in MailChec) or 
                ('@list.ru !' in MailChec) or 
                ('@yandex.ru !' in MailChec) or 
                ('@inbox.ru !' in MailChec)):
                print('TRUE')
                
                if(str(P2) != str(P1)):
                    Erors += ('4 5 ')
                else:
                    if(len(str(P2)) < 8):
                        Erors += ('4 5 ')
                        
                #Проверка ошибка может, занята почта (ErrMail), занят логин (ErrLog), и то и то(ErrAlls) пароли (ErrPass)
                Erors += DB.CheckRegister([Mail, Login])
                print('Erors ', Erors)
                return(Erors)
            else:
                return('2 3 ')
        except:
            return redirect('/')
    else:
        return redirect('/')


@application.route('/CheckDataLogin', methods=["POST","GET"])
def CheckDataLogin():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')
    if request.method == "POST": 
        try:
            print(request.args)
            Pass = request.args.get('Pass')
            Login = request.args.get('Login')

            Erors = DB.CheckLogin([Login, Pass, hash])
            return(Erors)
        except:
            return redirect('/')
    else:
        return redirect('/')


@application.route('/userSTR', methods=["POST","GET"])
def gg():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')
    print('dd')
    if(request.method == 'POST'):
        TT_REBR = request.args.get('TT_RRBR')
        if(TT_REBR == 'register'):
            try:
                print(request.form)
                Name1R = request.form['validationName']
                Name2R = request.form['validationName2']
                Email =  request.form['validationEmail']
                Login =  request.form['validationLogin']
                Pass  =  request.form['validationPass']
                CodeColor = requests.post('http://megagenerator.ru/color/',data = {'con':""})
                CodeColor = ((str(CodeColor.content).replace('"','').replace("b'        <div class=color_id>\\r\\n            ",'').replace('</div>\\r\\n ',''))[:10]).replace(' ','')
                DataClass.mailDates[hash] = {'Email':Email,
                                             'CodeColor': CodeColor.upper()} 

                sdawd = CodeColor.replace('#','')
                SendMessageMail(Email, sdawd, Login)

                DataClass.MNData[hash]={'Name1R': Name1R,
                                        'Name2R': Name2R,
                                        'Email': Email,
                                        'Login': Login,
                                        'Pass': Pass}                      
                return redirect(f'/ConnectMail?Email={Email}')
            except:
                return redirect('/')
        elif(TT_REBR == 'login'):
            OTV_Check = (CheckData.SetLoginTrue(str(hash)))
            return redirect('/main')
    else:
        return redirect('/')


@application.route('/dob', methods=["POST","GET"])
def dob():
    if request.method == "POST": 
        a = str(request.args.get('Dt'))
        a = a[0:-3]
        p = str(time.time())
        p = p[:p.find('.')]
        print(int(a) - int(p))
        if(int(a) - int(p) >= -1):
            if not request.cookies.get('TING'):
                hash = (GENERCASH(str(request.remote_addr)))
            else:
                hash = request.cookies.get('TING')  
            DataClass.DataMain[hash] = {'Login': "False"}
            DataClass.RegInfo[hash] = {'RegInfo': 'False'} 
        else:
            return('False')
        return ('True')  
    else:
        return redirect('/')


@application.route('/endGame', methods=["POST","GET"])
def EndGame():
    if request.method == "GET":
        try:
            if not request.cookies.get('TING'):
                hash = (GENERCASH(str(request.remote_addr)))
            else:
                hash = request.cookies.get('TING')  
            dataA = (DB.TakeData(DataClass.IDUserLogins[hash])) 
            SettingsAdmin = DB.GetAdmin()
            absdas = DataClass.GameDatas[hash]
        
            OTV_Check = (CheckData.Check_L(str(hash)))
            if(OTV_Check == 'False'):
                return redirect("/")
            else:
                AB =(DataClass.GameDatas[hash]) #{'TrueOtv': 'Относительная высота', 'ScoreT': 1, 'StartGames': True}

                BB = (DataClass.GameInfo[hash]) #{'IDGame': '2', 'InGame': True, 'DataStart': '1606047833851', 'GameCode': '40XK5BVB'}
                TrueOTV = AB['TrueOtv']
                Proc = int(DataClass.GameDatas[hash]['ScoreT'])
                if(BB['IDGame'] == '1'):
                    GameID = ['1 in 6', 'Тест на знания английского языка']
                    Procs = Proc * 16.7
                elif(BB['IDGame'] == '2'):
                    GameID = ['Questions', 'Тест на различные темы']
                    Procs = Proc * 20
                #######################
                
                return render_template('EndGame.html',GameID = GameID, Proc = Proc, TrueOTV = TrueOTV, login = str(OTV_Check), Procs = Procs, data = dataA, AS = SettingsAdmin)
        except:
            return redirect('/')
    else:
        return redirect("/")


@application.route('/SetGameAPI', methods=["POST","GET"])
def SetGameAPI():
    if request.method == "POST": 
        # ?GameID=" + GameId + "&Data=" + begin
        GameID = str(request.args.get('GameID'))
        Data = str(request.args.get('Data'))
        a = Data[0:-3]
        p = str(time.time())
        p = p[:p.find('.')]
        print(int(a) - int(p))
        if(int(a) - int(p) >= -1):
            if not request.cookies.get('TING'):
                hash = (GENERCASH(str(request.remote_addr)))
            else:
                hash = request.cookies.get('TING')  
            OTV_Check = (CheckData.Check_L(str(hash)))
            if(OTV_Check == 'False'):
                return ("False")
            else:
                # Проверка денег
                moneyCheck = 'True'
                if(moneyCheck == 'True'):
                    GameCode = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        
                    DataClass.GameInfo[hash] = {'IDGame': GameID,
                                                'InGame': True,
                                                'DataStart': Data,
                                                'GameCode': GameCode}
                                                
                    return(GameCode)
                else:
                    return('False')
        else:
            return('False')
        return ('False')  
    else:
        return redirect('/')


@application.route('/StartGame', methods=["POST","GET"])
def StartGame():
    if request.method == "GET": 
        try:
            GameToken = str(request.args.get('GameToken'))
            Data = str(request.args.get('Data'))
            a = Data[0:-3]
            p = str(time.time())
            p = p[:p.find('.')]
            print(int(a) - int(p))
            if(int(a) - int(p) >= -1):
                if not request.cookies.get('TING'):
                    hash = (GENERCASH(str(request.remote_addr)))
                else:
                    hash = request.cookies.get('TING')  
                OTV_Check = (CheckData.Check_L(str(hash)))
                if(OTV_Check == 'False'):
                    return redirect("/")
                else:
                    try:
                        GameCode = DataClass.GameInfo[hash]['GameCode']
                        print(GameCode, GameToken)
                        if (GameToken == GameCode):
                            idG = DataClass.GameInfo[hash]['IDGame']
                            print('tt ',idG)
                            if(int(idG) == 1):
                                return redirect('/StartGame1')     
                            elif(int(idG) == 2):
                                return redirect('/StartGame2')
                    except:
                        return redirect('/')
            else:
                return redirect('/')
        except:
            return redirect('/')
        return redirect('/')  
    else:
        return redirect('/')


@application.route('/StartGame1', methods=["POST","GET"])
def StartGame1():
    if request.method == "GET":
        try:
            if(True):
                if not request.cookies.get('TING'):
                    hash = (GENERCASH(str(request.remote_addr)))
                else: 
                    hash = request.cookies.get('TING')
                try:
                    GameD = DataClass.GameInfo[hash]
                except:
                    return redirect('/')

                try:
                    if (DataClass.GameDatas[hash]['ScoreT'] >= 0):
                        if (DataClass.GameDatas[hash]['StartGames'] == True):
                            DataClass.GameDatas[hash] = {}
                            DataClass.GameInfo[hash] = {}
                            DataClass.StartGames[hash] = {}
                            print('Обновил игру')
                            return  redirect('/')
                except:
                    print('первый заход игру')
                OTV_Check = (CheckData.Check_L(str(hash)))
                if(OTV_Check == 'False'):
                    return redirect('/')
                else:
                    data = (DB.TakeData(DataClass.IDUserLogins[hash])) 
            print('data', data)
            VP = list(DB.GetBag_1in6(data[0]))
            print('vP1', VP)
            VPTrue = (VP[0][1])
            print(VP[0][2])
            
            try:
                DataClass.GameDatas[hash] = {"TrueOtv": VP[0][2], "ScoreT": int(DataClass.GameDatas[hash]['ScoreT']) + 1, 'StartGames': True}
            except:
                DataClass.GameDatas[hash] = {"TrueOtv": VP[0][2], "ScoreT": 1, 'StartGames': True}
            v = DataClass.GameInfo[hash]['GameCode']
            random.shuffle(VP)
            print('vP2', VP)
            SettingsAdmin = DB.GetAdmin()
            if(int(DataClass.GameDatas[hash]['ScoreT']) + 1 <= 7):
                return render_template('Game1.html',GameD = GameD, Proc = int(DataClass.GameDatas[hash]['ScoreT']), VP = VP, VPTrue = VPTrue, data = data, login = str(OTV_Check),  AS = SettingsAdmin)
            else:
                OT = DB.AddContinueGame([data[0],'1in6'])
                return redirect('/')
        except:
            print('Ош')
            return redirect('/')
    
    else:
        GameToken = str(request.args.get('GameToken'))
        Word = str(request.args.get('Word'))
        Data = str(request.args.get('Data'))
        a = Data[0:-3]
        p = str(time.time())
        p = p[:p.find('.')]
        print(int(a) - int(p))
        if(int(a) - int(p) >= -1):
            if not request.cookies.get('TING'):
                hash = (GENERCASH(str(request.remote_addr)))
            else:
                hash = request.cookies.get('TING')  
            OTV_Check = (CheckData.Check_L(str(hash)))
            if(OTV_Check == 'False'):
                return redirect("/")
            else:
                try:
                    print('Тут')
                    GameCode = DataClass.GameInfo[hash]['GameCode']
                    print(GameCode, GameToken)
                    if (GameToken == GameCode):
                        GWord = DataClass.GameDatas[hash]['TrueOtv']
                        if(str(Word) == str(GWord)):
                            d = [1,2,3,4,5]
                            print('True', Word, GWord)
                            DataClass.GameDatas[hash]['StartGames'] = False
                            return('True') 
                        else:
                            return("False")       
                except:
                    return redirect('/')
        else:
            return redirect('/')


@application.route('/StartGame2', methods=["POST","GET"])
def StartGame2():
    if request.method == "GET":
        try:
            if(True):
                if not request.cookies.get('TING'):
                    hash = (GENERCASH(str(request.remote_addr)))
                else: 
                    hash = request.cookies.get('TING')
                try:
                    GameD = DataClass.GameInfo[hash]
                except:
                    return redirect('/')

                try:
                    if (DataClass.GameDatas[hash]['ScoreT'] >= 0):
                        if (DataClass.GameDatas[hash]['StartGames'] == True):
                            DataClass.GameDatas[hash] = {}
                            DataClass.GameInfo[hash] = {}
                            DataClass.StartGames[hash] = {}
                            print('Обновил игру')
                            return  redirect('/')
                except:
                    print('первый заход игру')
                OTV_Check = (CheckData.Check_L(str(hash)))
                if(OTV_Check == 'False'):
                    return redirect('/')
                else:
                    data = (DB.TakeData(DataClass.IDUserLogins[hash])) 
            VP = list(DB.GetBag_Questions(data[0]))
            print('vP1', VP)
            VPTrue = (VP[0][1])
            print(VP[0][6])
            VPS = [VP[0][3], VP[0][4], VP[0][5], VP[0][2]]
            
            try:
                DataClass.GameDatas[hash] = {"TrueOtv": VP[0][6], "ScoreT": int(DataClass.GameDatas[hash]['ScoreT']) + 1, 'StartGames': True}
            except:
                DataClass.GameDatas[hash] = {"TrueOtv": VP[0][6], "ScoreT": 1, 'StartGames': True}
            v = DataClass.GameInfo[hash]['GameCode']
            random.shuffle(VPS)
            print('vP2', VPS)
            SettingsAdmin = DB.GetAdmin()
            if(int(DataClass.GameDatas[hash]['ScoreT']) + 1 <= 6):
                return render_template('Game2.html', GameD = GameD, Proc = int(DataClass.GameDatas[hash]['ScoreT']), VP = VPS, VPTrue = VPTrue, data = data, login = str(OTV_Check),  AS = SettingsAdmin)
            else:
                OT = DB.AddContinueGame([data[0],'Que'])
                return redirect('/')
        except:
            print('Ош')
            return redirect('/')
    
    else:
        GameToken = str(request.args.get('GameToken'))
        Word = str(request.args.get('Word'))
        Data = str(request.args.get('Data'))
        a = Data[0:-3]
        p = str(time.time())
        p = p[:p.find('.')]
        print(int(a) - int(p))
        if(int(a) - int(p) >= -1):
            if not request.cookies.get('TING'):
                hash = (GENERCASH(str(request.remote_addr)))
            else:
                hash = request.cookies.get('TING')  
            OTV_Check = (CheckData.Check_L(str(hash)))
            if(OTV_Check == 'False'):
                return redirect("/")
            else:
                try:
                    print('Тут POST')
                    GameCode = DataClass.GameInfo[hash]['GameCode']
                    print(GameCode, GameToken)
                    if (GameToken == GameCode):
                        GWord = DataClass.GameDatas[hash]['TrueOtv']
                        if(str(Word) == str(GWord)):
                            d = [1,2,3,4,5]
                            print('True', Word, GWord)
                            DataClass.GameDatas[hash]['StartGames'] = False
                            return('True') 
                        else:
                            print('True', Word, GWord)
                            return("False")       
                except:
                    return redirect('/')
        else:
            return redirect('/')


@application.route('/APIBLOCK', methods=["POST","GET"])
def APIBLOCK():
    print("Пришёл")
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')
    if request.method == "POST":
        APIBLOCK = str(request.args.get('APIBLOCK'))
        Data = str(request.args.get('Data'))
        
        a = Data[0:-3]
        p = str(time.time())
        p = p[:p.find('.')]
        if(int(a) - int(p) >= -1):
            OTV_Check = (CheckData.Check_L(str(hash)))
            if(OTV_Check == 'False'):
                return('False')
            else:
                data = (DB.TakeData(DataClass.IDUserLogins[hash]))
                DB.ClearTrueSer([data[0], int(APIBLOCK)])
                return('True')


@application.route('/')
def index():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')     
    DataClass.GameInfo[hash] = {}
    SettingsAdmin = DB.GetAdmin()
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        try:
            g = DataClass.RegInfo[hash]['RegInfo']
        except:
            g = "False"
        res = make_response(render_template('main.html',data=data, login=OTV_Check, QQ = g, AS = SettingsAdmin))
        DataClass.RegInfo[hash] = {'RegInfo': 'False'}
        res.set_cookie('TING', f'{hash}') 
        return (res)
    else:
        res = make_response(redirect ('/main'))
        res.set_cookie('TING', f'{hash}') 
        return (res)


@application.route('/main')
def main():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')  

    SettingsAdmin = DB.GetAdmin()
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        res = make_response(redirect('/'))
        res.set_cookie('TING', f'{hash}') 
        return (res)
    else:
        data = (DB.TakeData(DataClass.IDUserLogins[hash]))
        print(data)

        res = make_response(render_template('index.html', data=data, login = str(OTV_Check), AS = SettingsAdmin))
        res.set_cookie('TING', f'{hash}') 
        return (res)


@application.route('/news')
def News():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING') 
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        data = 'N'
    else:
        data = (DB.TakeData(DataClass.IDUserLogins[hash]))
    SettingsAdmin = DB.GetAdmin()
    updatess = DB.GetUpdate()
    return render_template('News.html', data = data, login = str(OTV_Check), updates = updatess, AS = SettingsAdmin)


@application.route('/stats')
def stats():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')  
    SettingsAdmin = DB.GetAdmin()
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        res = make_response(redirect('/'))
        res.set_cookie('TING', f'{hash}') 
        return (res)
    else:
        data = (DB.TakeData(DataClass.IDUserLogins[hash]))
        print(data)
        s = (data[9] + data[10])
        a = toFixed(s, 2)
        
        data = list(data)
        data.append(a)
        print(data)
       
        res = make_response(render_template('stats.html', data=data, login = str(OTV_Check), AS = SettingsAdmin))
        res.set_cookie('TING', f'{hash}') 
        return (res)


@application.route('/prvate-policy')
def PP():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')  
    SettingsAdmin = DB.GetAdmin()
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        data = ''
    else:
        data = (DB.TakeData(DataClass.IDUserLogins[hash]))
        print(data)

    return render_template('/privacy-policy.html', data=data, login = str(OTV_Check), AS = SettingsAdmin)


@application.route('/about')
def about_us():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')  
    SettingsAdmin = DB.GetAdmin()
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        data = ''
    else:
        data = (DB.TakeData(DataClass.IDUserLogins[hash]))
        print(data)

    return render_template('/about.html', data=data, login = str(OTV_Check), AS = SettingsAdmin)


@application.route('/video')
def Video():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')  
    SettingsAdmin = DB.GetAdmin()
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        data = ''
    else:
        data = (DB.TakeData(DataClass.IDUserLogins[hash]))
    VideoData = DB.GetVideo()
    return render_template('/video.html', data=data, login = str(OTV_Check), AS = SettingsAdmin, VideoData = VideoData)
    

@application.route('/ConnectMail', methods=["POST","GET"])
def ConnectMail():
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')  
    SettingsAdmin = DB.GetAdmin()
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        data = ''
    else:
        data = (DB.TakeData(DataClass.IDUserLogins[hash]))
    
    if request.method == "GET":
        Email = str(request.args.get('Email'))
        try:
            MailInClass = DataClass.mailDates[hash]['Email']
        except:
            MailInClass = ''
        print(Email, MailInClass)
        TeT = ''
        if(Email == MailInClass):
            return render_template('TrueMail.html', data=data, login = str(OTV_Check), AS = SettingsAdmin, TeT = TeT)
            return(Email,MailInClass)
        else:
            return redirect('/')
    

    if request.method == "POST":
        MailCodeIn = str(request.form.get('MailCodeIn'))
        try:
            CodeColor = str(DataClass.mailDates[hash]['CodeColor']).replace('#','')
        except:
            return redirect('/')
        print('CodeColor - ',CodeColor , 'MailCodeIn - ', MailCodeIn)

        TeT = CodeColor == MailCodeIn

        if not(TeT):
            return render_template('/TrueMail.html', data=data, login = str(OTV_Check), AS = SettingsAdmin, TeT = TeT)
        else:
            MND = DataClass.MNData[hash]

            OTV = DB.CreateNewAccount([MND['Name1R'], MND['Name2R'], MND['Email'], MND['Login'], hash_password(MND['Pass'])])
            print(OTV)
            ########################        
            ErorsS = DB.CheckLogin([MND['Login'], MND['Pass'], hash])
            print('Erors ', ErorsS)
            OTV_CheckS = (CheckData.SetLoginTrue(str(hash)))
            ########################
            if(OTV == 'True'):
                DataClass.RegInfo[hash]= {'RegInfo':'True'}
                return render_template('/TrueMail.html', data=data, login = 'True', AS = SettingsAdmin, TeT = TeT)
            else:
                DataClass.RegInfo[hash]= {'RegInfo':'False'}
                return redirect('/')


@application.route('/ForgottenPassword', methods=["POST","GET"])
def ForgottenPassword():
    #return redirect('/InDeveloper')
    if not request.cookies.get('TING'):
        hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')  
    SettingsAdmin = DB.GetAdmin()
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        data = ''
    else:
        data = (DB.TakeData(DataClass.IDUserLogins[hash]))
    if(request.method == 'POST'):
        LoginMain = request.form.get('LMLogin')
        OTV, TeT = DB.ReturnMail(str(LoginMain))
        
        if not(TeT):
            return render_template('/ForgottenPassword.html', data=data, login = str(OTV_Check), AS = SettingsAdmin, TeT = TeT)
        else:
            Code, na, mai = DB.CreateForgetenMailCode(LoginMain)
            print(Code)
            Codes = f'http://localhost/ForgettenMail/{Code}'
            SendMessageCodeToMail(mai, Codes, na)
            return render_template('/ForgottenPassword.html', data=data, login = str(OTV_Check), AS = SettingsAdmin, TeT = TeT)
        
        
    if(request.method == 'GET'):
        return render_template('/ForgottenPassword.html', data=data, login = str(OTV_Check), AS = SettingsAdmin, TeT = '')


@application.route('/ForgettenMail/', methods=["POST","GET"])
def ForgettenMails():
    return redirect('/')


@application.route('/ForgettenMail/<string:token>', methods=["POST","GET"])
def ForgettenMail(token):
    if not request.cookies.get('TING'):
            hash = (GENERCASH(str(request.remote_addr)))
    else:
        hash = request.cookies.get('TING')  
    SettingsAdmin = DB.GetAdmin()
    OTV_Check = (CheckData.Check_L(str(hash)))
    if(OTV_Check == 'False'):
        data = ''
    else:
        data = (DB.TakeData(DataClass.IDUserLogins[hash]))



    if(request.method == 'GET'):
        print(token)
        t = (DB.ForgettenMailDB(token))
        print(t)
        if (t == 'False'):
            return redirect('/')
        else:
            return render_template('NewPass.html', data=data, login = str(OTV_Check), AS = SettingsAdmin, TeT = '', Toc = token)
    
    if(request.method == 'POST'):
        print(token)
        t = (DB.ForgettenMailDB(token))
        print(t)
        if (t == 'False'):
            return redirect('/')
        else:
            PPsss1 = request.form.get('P1')
            PPsss2 = request.form.get('P2')
            if(PPsss2 != PPsss1 or len(PPsss2) < 8 or len(PPsss1) < 8):
                return render_template('NewPass.html', data=data, login = str(OTV_Check), AS = SettingsAdmin, TeT = False, Toc = '')
            else:
                DB.SetNewPass([PPsss1, token])
                return render_template('NewPass.html', data=data, login = str(OTV_Check), AS = SettingsAdmin, TeT = True, Toc = '')


@application.route('/InDeveloper')
def InDeveloper():
    return render_template('/InDeveloper.html')

@application.errorhandler(404)
def page_not_found(e):
    return ("errors") #('404.html')


if __name__=="__main__":
    application.run(debug=True, host='localhost',port='80')
