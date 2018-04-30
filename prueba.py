import gspread 
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('../CajaChica-5a38455e3dd8.json',scope)

gc = gspread.authorize(credentials)

wks = gc.open('Caja Chica y Gastos').sheet1

print(wks.get_all_records())

wks.append_row(['linea nueva col 1','linea nueva col 2'])




print(wks.get_all_records())
