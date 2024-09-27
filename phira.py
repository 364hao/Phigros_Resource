import os
import sys
import shutil
from zipfile import ZipFile
from rich.progress import track

levels = ["EZ", "HD", "IN", "AT"]

infos = {}

shutil.rmtree("phira", True)
os.mkdir("phira")
for level in levels:
    os.mkdir("phira/%s" %level)

with open("info.tsv", encoding="utf8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line[:-1].split("\t")
        infos[line[0]] = {"Name": line[1], "Composer": line[2], "Illustrator": line[3], "Chater": line[4:]}
        
with open("difficulty.tsv", encoding="utf8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line[:-1].split("\t")
        infos[line[0]]["difficulty"] = line[1:]

for id, info in track(infos.items(), description = "WritingPez..."):
    for level in range(len(info["difficulty"])):
        chart_path = "Chart_%s/%s.0.json" % (levels[level], id)
        ill_path = "IllustrationLowRes/%s.png" % id
        music_path = "music/%s.ogg" % id
            
        if not any(os.path.exists(path) for path in {chart_path, music_path, ill_path}):
            print(f'[{levels[level]}]"{id}" does not exist and has been skipped')
            continue
        
        with ZipFile("phira/%s/%s-%s.pez" % (levels[level], id, levels[level]), "x") as pez:
            pez.writestr("info.txt", "#\nName: %s\nSong: %s.ogg\nPicture: %s.png\nChart: %s.json\nLevel: %s Lv.%s\nComposer: %s\nIllustrator: %s\nCharter: %s" % (info["Name"], id, id, id, levels[level], info["difficulty"][level], info["Composer"], info["Illustrator"], info["Chater"][level]))
            
            pez.write(chart_path, "%s.json" % id)
            pez.write(ill_path, "%s.png" % id)
            pez.write(music_path, "%s.ogg" % id)

if len(sys.argv) > 1 and sys.argv[1] == '--phira':
    for id, info in track(infos.items(), description = "WritingPhiraPez..."):
        for level in range(len(info["difficulty"])):
            chart_path = "Chart_%s/%s.rpe.0.json" % (levels[level], id)
            ill_path = "Illustration/%s.png" % id
            music_path = "music/%s.ogg" % id
                
            if not any(os.path.exists(path) for path in {chart_path, music_path, ill_path}):
                print(f'[{levels[level]}]"{id}" does not exist and has been skipped')
                continue
            
            with ZipFile("phira/%s/%s-%s(Phira ver.).pez" % (levels[level], id, levels[level]), "x") as pez:
                pez.writestr("info.txt", "#\nName: %s\nSong: %s.ogg\nPicture: %s.png\nChart: %s.json\nLevel: %s Lv.%s\nComposer: %s\nIllustrator: %s\nCharter: %s" % (info["Name"], id, id, id, levels[level], info["difficulty"][level], info["Composer"], info["Illustrator"], info["Chater"][level]))
                
                pez.write(chart_path, "%s.json" % id)
                pez.write(ill_path, "%s.png" % id)
                pez.write(music_path, "%s.ogg" % id)