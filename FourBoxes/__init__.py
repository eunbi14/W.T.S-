
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:08:40 2019
@author: 은비
"""

from flask import Flask, render_template
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd, numpy as np
import openpyxl

book = openpyxl.load_workbook("total경복궁.xlsx")

sheet8 = book.get_sheet_by_name("2018경복궁") # Matirx[7]
sheet7 = book.get_sheet_by_name("2017경복궁") # Matrix[6]
sheet6 = book.get_sheet_by_name("2016경복궁") # Matrix[5]
sheet5 = book.get_sheet_by_name("2015경복궁") # Matrix[4]
sheet4 = book.get_sheet_by_name("2014경복궁") # Matrix[3]
sheet3 = book.get_sheet_by_name("2013경복궁") # Matrix[2]
sheet2 = book.get_sheet_by_name("2012경복궁") # Matrix[1]
sheet1 = book.get_sheet_by_name("2011경복궁") # Matrix[0]

Matrix = [[0]*31 for i in range(12)]
Matrix2012 = [[0]*31 for i in range(12)]
Matrix2013 = [[0]*31 for i in range(12)]
Matrix2014 = [[0]*31 for i in range(12)]
Matrix2015 = [[0]*31 for i in range(12)]
Matrix2016 = [[0]*31 for i in range(12)]
Matrix2017 = [[0]*31 for i in range(12)]
Matrix2018 = [[0]*31 for i in range(12)]

r = 2
now = datetime.now()
year = now.year

j = 0
for i in range(365):
    month = sheet1.cell(row=r, column=7).value - 1
    month2 = sheet1.cell(row=r-1, column=7).value
    if i!=0:
        if month != month2 -1:
            j=0
        else:
            j=j+1
    Matrix[month][j] = sheet1.cell(row=r,column=3).value
    r = r+1
    
r = 2
j = 0
for i in range(365):
    month = sheet2.cell(row=r, column=7).value - 1
    month2 = sheet2.cell(row=r-1, column=7).value
    if i!=0:
        if month != month2 -1:
            j=0
        else:
            j=j+1
    Matrix2012[month][j] = sheet2.cell(row=r,column=3).value
    r = r+1
    
r = 2
j = 0
for i in range(365):
    month = sheet3.cell(row=r, column=7).value - 1
    month2 = sheet3.cell(row=r-1, column=7).value
    if i!=0:
        if month != month2 -1:
            j=0
        else:
            j=j+1
    Matrix2013[month][j] = sheet3.cell(row=r,column=3).value
    r = r+1
    
r = 2
j = 0
for i in range(365):
    month = sheet4.cell(row=r, column=7).value - 1
    month2 = sheet4.cell(row=r-1, column=7).value
    if i!=0:
        if month != month2 -1:
            j=0
        else:
            j=j+1
    Matrix2014[month][j] = sheet4.cell(row=r,column=3).value
    r = r+1
    
r = 2
j = 0
for i in range(365):
    month = sheet5.cell(row=r, column=7).value - 1
    month2 = sheet5.cell(row=r-1, column=7).value
    if i!=0:
        if month != month2 -1:
            j=0
        else:
            j=j+1
    Matrix2015[month][j] = sheet5.cell(row=r,column=3).value
    r = r+1
    
r = 2
j = 0
for i in range(365):
    month = sheet6.cell(row=r, column=7).value - 1
    month2 = sheet6.cell(row=r-1, column=7).value
    if i!=0:
        if month != month2 -1:
            j=0
        else:
            j=j+1
    Matrix2016[month][j] = sheet6.cell(row=r,column=3).value
    r = r+1
    
r = 2
j = 0
for i in range(365):
    month = sheet7.cell(row=r, column=7).value - 1
    month2 = sheet7.cell(row=r-1, column=7).value
    if i!=0:
        if month != month2 -1:
            j=0
        else:
            j=j+1
    Matrix2017[month][j] = sheet7.cell(row=r,column=3).value
    r = r+1
    
r = 2
j = 0
for i in range(365):
    month = sheet8.cell(row=r, column=7).value - 1
    month2 = sheet8.cell(row=r-1, column=7).value
    if i!=0:
        if month != month2 -1:
            j=0
        else:
            j=j+1
    Matrix2018[month][j] = sheet8.cell(row=r,column=3).value
    r = r+1
    
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/preview')
def preview():

    return render_template('preview.html', test=Matrix, test2012 = Matrix2012, test2013 = Matrix2013, test2014 = Matrix2014, test2015 = Matrix2015, test2016 = Matrix2016, test2017 = Matrix2017, test2018 = Matrix2018)

@app.route('/index.html')
def home2():
    return render_template('index.html')