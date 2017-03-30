# SubDB  
Python script for downloading subtitles for a given video using the subDB api.  
  
The script searches for the available languages for a given video file. You may then choose amongst the languages and the subtitles will download in the same folder as your video file (same name but with the extension .srt).

# Command Line Usage  
This script does not have a gui... yet ! So to download subtitles for your favorite movies simply open a terminal and type :  
```bash
subdb yourfavoritemovie  
```
To get a list of languages available and then download the one you choose or :
```bash
subdb -l en yourfavoritemovie  
```
To directly download english subtitles (if available).  
The list of all languages on subDB is : 
* en (English)
* es (Español)
* fr (Français)
* it (Italiano)
* nl (Nederlands)
* pl (Polski)
* pt (Poruguês (Brazil))
* ro (Român)
* sv (Svenska)
* tr (Türkçe)
