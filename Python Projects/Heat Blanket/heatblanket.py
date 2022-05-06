"""
heatblanket.py

Purpose: Created to help wife make a heat blanket with submission of accurate 
average temparatures via scripted automation

Method: Gets historical data from api.worldweatheronline.com and extracts
average temperatures twice per week on Monday and Thursday. Afterwards, it
adds the information to a google sheet. Example photo included in Git repo.
"""

from __future__ import print_function

from googleapiclient.discovery import build

from google.oauth2 import service_account
import requests
import sys
from datetime import datetime, timedelta
import calendar

#
class Parameters():
    lat = "40.782864"
    lon = "-73.965355"
    apikey = "[CHANGE THIS TO YOUR API KEY]"
    units = "standard"
    today = datetime.today()
    dayOfYear = datetime.date(today)
    yesterday = dayOfYear + timedelta(days=-1)
    dayOfWeek = datetime.weekday(today)
    
def _resolveDate(dayOfWeek, dayOfYear):
    global startDay
    if dayOfWeek == 0:
        startDay = dayOfYear + timedelta(days=-4)
    elif dayOfWeek == 3:
        startDay = dayOfYear + timedelta(days=-3)
    else:
        today_is = calendar.day_name[Parameters.today.weekday()]
        sys.exit(f'Today is {today_is}, please run again on Monday or Thursday to submit data!')
    return

def _weatherAPICall():
    latlon = Parameters.lat+","+Parameters.lon
    yesterday = Parameters.yesterday
    apikey = Parameters.apikey

    #sends back historical information
    URL = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx"
    PARAMS = {'q':latlon, 'date':startDay, 'enddate': yesterday, 'key':apikey, 'tp':'24', 'format':'json'}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()

    # print(data)

    tempList = []
    tempListSum = 0

    for objects in data:
        for weather in data['data']['weather']:
            tempList.append(weather['avgtempF'])
                
    for temps in tempList:
        tempListSum = tempListSum + int(temps)
    halfwkAvg = tempListSum/len(data['data']['weather'])
    return halfwkAvg

def _resolveGoog(halfwkAvg):
    today=str(Parameters.today)
    
    # Substitute out these values with the temp ranges and colors used
    if halfwkAvg < 30:
        color = 'Purple'
    elif halfwkAvg < 35:
        color = 'Soft Purple'
    elif halfwkAvg < 40:
        color = 'Medium Rose'
    elif halfwkAvg < 45:
        color = 'Cornflower'
    elif halfwkAvg < 50:
        color = 'Aqua'
    elif halfwkAvg < 55:
        color = 'Teal'
    elif halfwkAvg < 60:
        color = 'Sapphire'
    elif halfwkAvg < 65:
        color = 'Varsity Navy'
    elif halfwkAvg < 70:
        color = 'Emerald Green'
    elif halfwkAvg < 75:
        color = 'Light Green'
    elif halfwkAvg < 80:
        color = 'Pale Yellow'
    elif halfwkAvg < 85:
        color = 'Mustard'
    elif halfwkAvg < 90:
        color = 'DK Coral'
    elif halfwkAvg < 95:
        color = "Deep Red"
    else:
        color = 'Wine'

    googOutput = [[today, halfwkAvg, color]]

    SERVICE_ACCOUNT_FILE = '[CHANGE TO YOUR GOOGLE ACCOUNT KEY FILE]'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)


    SAMPLE_SPREADSHEET_ID = '[CHANGE TO YOUR SPREADSHEETS ID]'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="A3:A").execute()
    values = result.get('values', [])

    datelength = "A" + str(len(values)+3)

    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=datelength, valueInputOption="USER_ENTERED", body={"values":googOutput}).execute()


def _resolveAll():
    _resolveDate(Parameters.dayOfWeek, Parameters.dayOfYear)
    halfwkAvg = _weatherAPICall()
    _resolveGoog(halfwkAvg)

_resolveAll()