import os
import requests
import sys
from datetime import datetime


def getGoogleSeet(spreadsheet_id, outDir, outFile):
  url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv'
  response = requests.get(url)
  if response.status_code == 200:
    filepath = os.path.join(outDir, outFile)
    with open(filepath, 'wb') as f:
      f.write(response.content)
      print(f'CSV file from [ {url} ] saved to:'.format(filepath))    
  else:
    print(f'Error downloading Google Sheet [ {url} ]: {response.status_code}')


cwd = os.getcwd()
outDir = os.path.join(cwd, 'data')
todayDt = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')

os.makedirs(outDir, exist_ok = True)
filepath = getGoogleSeet('10lV-j8zQ38j9HKrSeGp9bLW1p6_dYjqsl0aQ4rtZvDw', outDir, f'kaderle_sels_{todayDt}.csv')
