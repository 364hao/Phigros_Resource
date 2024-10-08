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

for id, info in track(infos.items(), description = "WritePez..."):
    for level in range(len(info["difficulty"])):
        try:
            with ZipFile("phira/%s/%s-%s.pez" % (levels[level], id, levels[level]), "w") as pez:
                pez.writestr("info.txt", "#\nName: %s\nSong: %s.ogg\nPicture: %s.png\nChart: %s.json\nLevel: %s Lv.%s\nComposer: %s\nIllustrator: %s\nCharter: %s" % (info["Name"], id, id, id, levels[level], info["difficulty"][level], info["Composer"], info["Illustrator"], info["Chater"][level]))
                pez.write("Chart_%s/%s.0.json" % (levels[level], id), "%s.json" % id)
                pez.write("Illustration/%s.png" % id, "%s.png" % id)
                pez.write("music/%s.ogg" % id, "%s.ogg" % id)
        except:
            pass

if len(sys.argv) > 1 and sys.argv[1] == '--phira':
    for id, info in track(infos.items(), description = "WritePhiraPez..."):
        for level in range(len(info["difficulty"])):
            try:
                with ZipFile("phira/%s/%s-%s(Phira ver.).pez" % (levels[level], id, levels[level]), "w") as pez:
                    pez.writestr("info.txt", "#\nName: %s\nSong: %s.ogg\nPicture: %s.png\nChart: %s.rpe.official.json\nLevel: %s Lv.%s\nComposer: %s\nIllustrator: %s\nCharter: %s" % (info["Name"], id, id, id, levels[level], info["difficulty"][level], info["Composer"], info["Illustrator"], info["Chater"][level]))
                    pez.write("Chart_%s/%s.0.json" % (levels[level], id), "%s.rpe.official.json" % id)
                    pez.write("Illustration/%s.png" % id, "%s.png" % id)
                    pez.write("music/%s.ogg" % id, "%s.ogg" % id)
            except:
                pass
    for id, info in track(infos.items(), description = "WriteRPEPez..."):
        for level in range(len(info["difficulty"])):
            try:
                with ZipFile("phira/%s/%s-%s(RPE ver.).pez" % (levels[level], id, levels[level]), "w") as pez:
                    pez.writestr("info.txt", "#\nName: %s\nSong: %s.ogg\nPicture: %s.png\nChart: %s.rpe.json\nLevel: %s Lv.%s\nComposer: %s\nIllustrator: %s\nCharter: %s" % (info["Name"], id, id, id, levels[level], info["difficulty"][level], info["Composer"], info["Illustrator"], info["Chater"][level]))
                    pez.write("Chart_%s/%s.0.json" % (levels[level], id), "%s.rpe.json" % id)
                    pez.write("Illustration/%s.png" % id, "%s.png" % id)
                    pez.write("music/%s.ogg" % id, "%s.ogg" % id)
            except:
                pass