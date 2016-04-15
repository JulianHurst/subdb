#!/usr/bin/env python3
import urllib.request
import sys
import os.path
import hashlib

def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

def error():
    print("USAGE : "+sys.argv[0]+" [-l lang] file")
    sys.exit(-1)


if len(sys.argv)!=4 and len(sys.argv)!=2:
    error()
if len(sys.argv)==4:
    if sys.argv[1]=="-l":
        lang=sys.argv[2]
        filename=sys.argv[3]
    else:
        error()
else:
    lang="NA"
    filename=sys.argv[1]
req=urllib.request.Request("http://api.thesubdb.com/?action=languages",headers={"User-Agent" : "SubDB/1.0 (subdb/0.1; http://github.com/JulianHurst/subdb"})
data=urllib.request.urlopen(req)
langs=data.read().decode('utf-8')
langs=langs.split(',')
req=urllib.request.Request("http://api.thesubdb.com/?action=search&hash="+get_hash(filename),headers={"User-Agent" : "SubDB/1.0 (subdb/0.1; http://github.com/JulianHurst/subdb"})
data=urllib.request.urlopen(req)
print("available languages : ",data.read().decode('utf-8'))
while lang not in langs[:]:
    lang=input("Choose one of the available languages : ")
req=urllib.request.Request("http://api.thesubdb.com/?action=download&hash="+get_hash(filename)+"&language="+lang,headers={"User-Agent" : "SubDB/1.0 (subdb/0.1; http://github.com/JulianHurst/subdb"})
data=urllib.request.urlopen(req)
with open(os.path.splitext(filename)[0]+".srt","wb") as f:
    f.write(data.read())
