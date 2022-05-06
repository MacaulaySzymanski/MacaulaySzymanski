"""
japaneseSheetLookup_v2.py

Purpose: When trying to prioritize what to learn, and if a specific word 
will be useful in a given context we can refer to frequency lists to ensure
we are focusing on the most used words in said language. This script makes 
parsing the most used words in a language, in this case Japanese, very simple.

Method: Makes use of a 0(n) linear search algorithm (a for loop) to find 
the row in which a queried value exists in a csv then extrapolates information 
from the related columns in the form of a formatted string specifying various
values returned

Requires a csv with frequency information for a given language
"""

import csv
from unicodedata import decimal
import pyperclip
import os

def heyo_donezo():
    
    focusPercent = 95
    usefulPercentage = 100 - focusPercent
    focusNumber = 12020
    percentile = (100 - float(rows[5]))
    usage = rows[4]
    ranking = rows[3]
    if percentile > usefulPercentage:
        useful = "HELPFUL"
    else:
        useful = "SUBJECTIVE"
    txt = """
The word is {0}, 
ranked number {2}, 
used {3} percent of the time,
it's usage is within the {1} percentile of Japanese language. 

Since we are trying to learn the first {5} words,
Learning this word would likely be a {4} addition."""
    print(txt.format(search,percentile,ranking, usage, useful, focusNumber))


with open('C:/Users/Dave/Desktop/Coding and Scripting/Python Projects/Japanese_Sheet_Lookup/word_freq_report - word_freq_report.csv','r',encoding='utf-8') as fd:
    rd = csv.reader(fd, delimiter=",")
    
    search = pyperclip.paste()
    
    # woah = any(e[1] == search for e in rd)
    # print(woah)

    for rows in rd:
        if search != rows[1]:
            continue
        else:
            heyo_donezo()
            
    