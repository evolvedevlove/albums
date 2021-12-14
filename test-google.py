# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:24:23 2021

@author: Patty Whack
"""
from google.oauth2 import service_account
import pygsheets

# connect to google sheets with sheets api

#
gs_auth = pygsheets.authorize(service_file='C:\\Users\\Patty Whack.000\Documents\\patrickcrosmandotcom.json')
sheet_id = '12jyNNamJp43Qe80OocEM5qa0r1umLPksNNvEkiCQpAQ'
#spreadsheet_url = "https://docs.google.com/spreadsheets/d/12jyNNamJp43Qe80OocEM5qa0r1umLPksNNvEkiCQpAQ/edit?usp=sharing"
sheet = gs_auth.open_by_key(sheet_id)
worksheet = sheet.worksheet_by_title('test')

print(worksheet)
# add a value