import os
import sys
import shutil
from zipfile import ZipFile
from rich.progress import track

levels = ["EZ", "HD", "IN", "AT"]

infos = {}

shutil.rmtree("phira", ignore_errors=True)
os.makedirs("phira", exist_ok=True)
for level in levels:
    os.makedirs(os.path.join("phira", level), exist_ok=True)

with open("info.tsv", encoding="utf8") as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        parts = line.split("\t")
        infos[parts[0]] = {
            "Name": parts[1],
            "Composer": parts[2],
            "Illustrator": parts[3],
            "Chater": parts[4:]
        }

with open("difficulty.tsv", encoding="utf8") as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        parts = line.split("\t")
        infos[parts[0]]["difficulty"] = parts[1:]

for id, info in track(infos.items(), description="WritingPez..."):
    for level_index, difficulty in enumerate(info["difficulty"]):
        level = levels[level_index]
        chart_path = os.path.join("Chart_%s" % level, "%s.0.json" % id)
        ill_path = os.path.join("Illustration", "%s.png" % id)
        music_path = os.path.join("music", "%s.ogg" % id)
        
        if not all(os.path.exists(path) for path in [chart_path, music_path, ill_path]):
            print(f'[{level}] "{id}" does not exist and has been skipped')
            continue
        
        pez_filename = os.path.join("phira", level, f"{id}-{level}.pez")
        with ZipFile(pez_filename, "w") as pez:
            pez_info = (
                "#\nName: %s\nSong: %s.ogg\nPicture: %s.png\nChart: %s.json\nLevel: %s Lv.%s\n"
                "Composer: %s\nIllustrator: %s\nCharter: %s" % (
                    info["Name"], id, id, id, level, difficulty,
                    info["Composer"], info["Illustrator"], info["Chater"][level_index]
                )
            )
            pez.writestr("info.txt", pez_info)
            pez.write(chart_path, f"{id}.json")
            pez.write(ill_path, f"{id}.png")
            pez.write(music_path, f"{id}.ogg")

if len(sys.argv) > 1 and sys.argv[1] == '--phira':
    for id, info in track(infos.items(), description="WritingPhiraPez..."):
        for level_index, difficulty in enumerate(info["difficulty"]):
            level = levels[level_index]
            chart_path = os.path.join("Chart_%s" % level, "%s.0.rpe.official.json" % id)
            ill_path = os.path.join("Illustration", "%s.png" % id)
            music_path = os.path.join("music", "%s.ogg" % id)
            
            if not all(os.path.exists(path) for path in [chart_path, music_path, ill_path]):
                print(f'[{level}] "{id}" does not exist and has been skipped')
                continue
            
            pez_filename = os.path.join("phira", level, f"{id}-{level}(Phira ver.).pez")
            with ZipFile(pez_filename, "w") as pez:
                pez_info = (
                    "#\nName: %s\nSong: %s.ogg\nPicture: %s.png\nChart: %s.json\nLevel: %s Lv.%s\n"
                    "Composer: %s\nIllustrator: %s\nCharter: %s" % (
                        info["Name"], id, id, id, level, difficulty,
                        info["Composer"], info["Illustrator"], info["Chater"][level_index]
                    )
                )
                pez.writestr("info.txt", pez_info)
                pez.write(chart_path, f"{id}.json")
                pez.write(ill_path, f"{id}.png")
                pez.write(music_path, f"{id}.ogg")