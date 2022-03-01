# importing the required libraries

import sys
import os
import csv
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
#import traceback

font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import winsound

# google api stuff
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credential_key_file_pomodoro.json', scope)
gc = gspread.authorize(credentials)
# sheet1
wks = gc.open('Pomodoro').get_worksheet(0)

# read old vaues from last tme

filename = "log.csv"  # log file to check previous data

f = open(filename, 'r')
csv_f = csv.reader(f)

for row in csv_f:
    A1old = row[0]
    A2old = row[1]
    A3old = row[2]
    A4old = row[3]
    A5old = row[4]
    A6old = row[5]
    A7old = row[6]
    A8old = row[7]
    A9old = row[8]
    A10old = row[9]
    A11old = row[10]
    A12old = row[11]
    A13old = row[12]
    A14old = row[13]
    A15old = row[14]
    
print("getting data from sheet")

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

# get the cells in the first column

A1 = (sheet_instance.acell('A1').value)
A2 = (sheet_instance.acell('A2').value)
A3 = (sheet_instance.acell('A3').value)
A4 = (sheet_instance.acell('A4').value)
A5 = (sheet_instance.acell('A5').value)
A6 = (sheet_instance.acell('A6').value)
A7 = (sheet_instance.acell('A7').value)
A8 = (sheet_instance.acell('A8').value)
A9 = (sheet_instance.acell('A9').value)
A10 = (sheet_instance.acell('A10').value)
A11 = (sheet_instance.acell('A11').value)
A12 = (sheet_instance.acell('A12').value)
A13 = (sheet_instance.acell('A13').value)
A14 = (sheet_instance.acell('A14').value)
A15 = (sheet_instance.acell('A15').value)

# write values to text log file
csv = open(filename, 'w')
csv.write(A1)
csv.write(",")
csv.write(A2)
csv.write(",")
csv.write(A3)
csv.write(",")
csv.write(A4)
csv.write(",")
csv.write(A5)
csv.write(",")
csv.write(A6)
csv.write(",")
csv.write(A7)
csv.write(",")
csv.write(A8)
csv.write(",")
csv.write(A9)
csv.write(",")
csv.write(A10)
csv.write(",")
csv.write(A11)
csv.write(",")
csv.write(A12)
csv.write(",")
csv.write(A13)
csv.write(",")
csv.write(A14)
csv.write(",")
csv.write(A15)
csv.write(",")
csv.close

# check if there is any new data since last time

if (A1old != A1 or A2old != A2 or A3old != A3 or A4old != A4 or A5old != A5 or A6old != A6 or A7old != A7 or A8old != A8 or A9old != A9 or A10old != A10 or A11old != A11 or A12old != A12 or A13old != A13 or A14old != A14 or A15old != A15):
	# e-Paper display stuff

    epd = epd7in5_V2.EPD()
    epd.init()
    epd.Clear()
    # Drawing on the Vertical image
    Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Limage)
    print ("rendering display")
    draw.text((2, 0), A1, font = font35, fill = 0)
    draw.text((2, 50), A2, font = font35, fill = 0)
    draw.text((2, 100), A3, font = font35, fill = 0)
    draw.text((2, 150), A4, font = font35, fill = 0)
    draw.text((2, 200), A5, font = font35, fill = 0)
    draw.text((2, 250), A6, font = font35, fill = 0)
    draw.text((2, 300), A7, font = font35, fill = 0)
    draw.text((2, 350), A8, font = font35, fill = 0)
    draw.text((2, 400), A9, font = font35, fill = 0)
    draw.text((2, 450), A10, font = font35, fill = 0)
    draw.text((2, 500), A11, font = font35, fill = 0)
    draw.text((2, 550), A12, font = font35, fill = 0)
    draw.text((2, 600), A13, font = font35, fill = 0)
    draw.text((2, 650), A14, font = font35, fill = 0)
    draw.text((2, 700), A15, font = font35, fill = 0)
    
    #print(var1, ":", var2, "     ", var3, ":", var4)

    epd.display(epd.getbuffer(Limage))
    epd.sleep()
    print("sleeping")
    
else:
    print("there was no new data")
