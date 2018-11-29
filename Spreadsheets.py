import gspread
from oauth2client.service_account import ServiceAccountCredentials

json_file = 'client_json.json'
spreadsheeturl = 'https://docs.google.com/spreadsheets/d/'

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file,scope)

ssclient = gspread.authorize(credentials)

spreadsheet = ssclient.open_by_url(spreadsheeturl)

worksheet1 = spreadsheet.get_worksheet(0)

worksheet2 = spreadsheet.get_worksheet(1)

#Getting the value of cell 'B2' of worksheet 1
print(worksheet1.acell('B2').value)

#Appending rows to end of worksheet 2
worksheet2.append_row(['Childs',4.00,5.00,6.00])

#Changing value of cell 'C3' to value of 200 of worksheet 1
worksheet1.update_acell('C3',200)

#Insert a row between rows 1 and 2 which will be the new row 2, populated with the values 'Dent',4.00,5.00,6.00 in worksheet 1
worksheet1.insert_row(['Dent',4.00,5.00,6.00],index=2)



