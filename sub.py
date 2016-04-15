import urllib.request
import sys
import os
import hashlib
def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

req=urllib.request.Request("http://api.thesubdb.com/?action=search&hash="+get_hash(sys.argv[1]),headers={"User-Agent" : "SubDB/1.0 (subdb/0.1; http://github.com/JulianHurst/subdb"})
data=urllib.request.urlopen(req)
print(data.read().decode('utf-8'))
lang=input("Choose one of the available languages : ")
req=urllib.request.Request("http://api.thesubdb.com/?action=download&hash="+get_hash(sys.argv[1])+"&language="+lang,headers={"User-Agent" : "SubDB/1.0 (subdb/0.1; http://github.com/JulianHurst/subdb"})
data=urllib.request.urlopen(req)
with open(os.path.splitext(sys.argv[1])[0]+".srt","w+") as f:
    f.write(data.read().decode('utf-8'))
