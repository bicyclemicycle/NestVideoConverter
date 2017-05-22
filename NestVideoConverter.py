#--------------------------------------
#--- Nest Video Database Converter
#
# File:     NestVideoConverter.py
# Author:   Michael Geyer
# Revision: 1
# Purpose:  Extracts and converts frames from a Nest database to mp4 format
#           files
#
# Usage:    NestVideoConvert.py <database> <ffmpeg.exe>

import sys
import sqlite3
import os
import fnmatch
import time

print "Usage: NestVideoConvert.py <filepath to database> <filepath to ffmpeg.exe>"
print "Note: This has been tested and built using python 2.7.13 on Windows 7 x64"

dbpath = os.path.dirname(os.path.abspath(sys.argv[1]))

DB = sqlite3.connect(sys.argv[1])
cur = DB.cursor()
videoname = "" # name of file
videofile = "" # buffer

# gets everything in table
cur.execute("SELECT * FROM frame_raw_data_table")
rows = cur.fetchall()

for row in rows:
  if row[4] != None:

    # write existing buffer (string) to disk if anything is within buffer
    if videofile != "":
      with open(videoname + ".rawh264", "wb") as file:
        file.write(videofile)
        
    # creation of header info (sps and pps and first frame)
    videofile = str(row[5]) # pps
    videofile = videofile + str(row[4]) # sps
    videofile = videofile + str(row[6]) # frame
    
    # name of file (first timestamp)
    videoname = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(row[0]/1000.0)) # frame_time
    
  # if the row is a part of a video, append to end
  else:
    videofile = videofile + str(row[6]) # frame
    
# Can't forget what is left in the buffer!
if videofile != "":
  with open(videoname + ".rawh264", "wb") as file:
    file.write(videofile)

# convert any video based file extension
for NameOfFile in os.listdir(dbpath): 
  if NameOfFile.endswith('.rawh264'):
    os.system(str(sys.argv[2] + " -f h264 -r 10 -i \"" + dbpath + "\\" + NameOfFile + "\" -c copy \""+ os.path.splitext(NameOfFile)[0] + ".mp4\""))

# Delete olde files
for NameOfFile in os.listdir(dbpath): 
  if fnmatch.fnmatch(NameOfFile, '*.rawh264*'):
    os.remove(dbpath + "\\" + NameOfFile)