Introduction :
--------------

NestVideoConverter is a small, simple script written in python to extract x264
video frames from the Nest database. It also combines the extracted frames and
converts the raw video to viewable mp4 file using ffmpeg.

The current version of NestVideoConverter is 1.0 as it currently is a proof of
concept.  The script has only been tested using Windows 7 x64  with 
python 2.7.13.  Python 3.5 will cause an error.

Dependencies :
--------------
You should have the following python libraries installed to use 
NestVideoConverter.

* sys
* sqlite3
* os
* fnmatch
* time

Usage :
-------
NestVideoConvert.py <database> <ffmpeg>

Contact :
---------
This script was written under the guidance and help of the Leahy Center of 
Digital Investigation specifically for the IoT Forensics Project

Author :
--------
You can contact me (Michael Geyer) via 
e-mail: michael.geyer@mymail.champlain.edu

