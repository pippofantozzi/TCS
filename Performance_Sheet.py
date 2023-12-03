import pandas as pd
from googleapiclient.discovery import build
import numpy as np

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = 'key.json'
#SERVICE_ACCOUNT_FILE = r'C:\Users\pippo_4wep9xe\OneDrive\VSC\4hour_Programs\Combined\aws\key.json'

def Sheet_Type():
    #ids = {'4hour':"1_r9NAGZha1cy491mDvpuEpJq-1OifwbzmuYEq8zhUpk",'1hour':'1CIIzcSLlAS1MCW1JSXA0A6axd_wBR1GR7fKPg0vEntQ'}
    SPREADSHEET_ID = '1Wa2UU8zZM7a18s2fBuu6X0pJtZ7E_DJ4Aqx9VRqO_b4'

    from google.oauth2 import service_account
    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets','v4',credentials=credentials)
    sheet = service.spreadsheets()
    return sheet, SPREADSHEET_ID


        
def read(sheet_name='Form Responses 3'):
    sheet,SPREADSHEET_ID = Sheet_Type()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=sheet_name).execute()
    values = result.get('values',[])
    import pandas as pd
    if values:
        # Extract column names from the first row
        columns = values[0]
        
        # Create the Pandas dataframe
        df = pd.DataFrame(values[1:], columns=columns)
        return df

    

    
