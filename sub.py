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

req=urllib.request.Request("http://api.thesubdb.com/?action=search&hash="+get_hash(sys.argv[1])+"[&versions]",headers={"User-Agent" : "SubDB/1.0 (subdb/0.1; http://github.com/JulianHurst/subdb"})
data=urllib.request.urlopen(req)
print(data)
