from goog_classes import Create_Service
# import pandas as pd


def run_batchUpdate_request(service, google_sheet_id, request_body_json):
    try:
        response = service.spreadsheets().batchUpdate(
            spreadsheetId=google_sheet_id,
            body=request_body_json
        ).execute()
        return response
    except Exception as e:
        print(e)
        return None


CLIENT_SECRET_FILE = 'kaderle-76571959e669.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
GOOGLE_SHEET_ID = '<Google Sheets Id' # 10lV-j8zQ38j9HKrSeGp9bLW1p6_dYjqsl0aQ4rtZvDw

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

"""
Iterate Worksheets
"""
# gsheets = service.spreadsheets().get(spreadsheetId=GOOGLE_SHEET_ID).execute()
# sheets = gsheets['sheets']

# for sheet in sheets:
#     if sheet['properties']['title'] != 'master':
#         dataset = service.spreadsheets().values().get(
#             spreadsheetId=GOOGLE_SHEET_ID,
#             range=sheet['properties']['title'],
#             majorDimension='ROWS'
#         ).execute()
#         df = pd.DataFrame(dataset['values'])
#         df.columns = df.iloc[0]
#         df.drop(df.index[0], inplace=True)
#         df.to_csv(sheet['properties']['title'] + '.csv', index=False)