import os
import os.path
import sys
import subprocess
import random
#OUTPUT_DIR = '/Users/matt/Desktop/mp3/'
Path2 = ""
Path3 = ""

def Music_conv(path: str,Diff: str, NS: int):
    #path = os.getcwd()
    Filters = ["-qscale:a 0 -filter:a "+""" " """.strip()+"atempo= 1.7"+""" " """.strip(),"-qscale:a 0 -filter:a "+""" " """.strip()+"aecho=0.8:0.88:60:0.4"+""" " """.strip(),
               "-qscale:a 0 -filter:a "+""" " """.strip()+"chorus=0.5:0.9:50|60|40:0.4|0.32|0.3:0.25|0.4|0.3:2|2.3|1.3"+""" " """.strip(),"-qscale:a 0 -filter:a "+""" " """.strip()+"compand=0|0:1|1:-90/-900|-70/-70|-30/-9|0/-3:6:0:0:0"+""" " """.strip(),"-qscale:a 0 -filter:a "+""" " """.strip()+"atempo= 0.5"+""" " """.strip()]
    filenames = []
    filenames2 = []
    filenames3 = []
    Volume = " -af "+""" " """.strip()+"volume=5dB"+""" " """.strip()+" "
    count = 0
    Len_Count = 0
    for filename in os.listdir(path):
        if(filename.endswith(".m4a")):
            filenames.append(filename)
            
    for filename in filenames:
        print(filename)
        filenames2.append(""" " """.strip()+path+"\\"+filename[:-4]+".mp3"+""" " """.strip())
        
    for filename in filenames:
        filenames3.append(""" " """.strip()+os.path.join(path, filename)+""" " """.strip())
    
    if(Diff == "Easy"):
        for x in range(len(filenames3)):
            S = "ffmpeg -i "+filenames3[x]+" -codec:v copy -codec:a libmp3lame -q:a 0 -map_metadata 0 -id3v2_version 3 "+filenames2[x]
            print(S)
            subprocess.run(S,shell=True)
    elif(Diff == "Normal"):
        if(NS == 10):
            F = random.choices(Filters,k=4)
        elif(NS == 15):
            F = random.choices(Filters,k=8)
        elif(NS == 20):
            F = random.choices(Filters,k=10)
        for x in range(len(filenames3)):
            if(count != len(F)):
                R = random.choice(F)
                S = "ffmpeg -i "+filenames3[x]+" -codec:v copy -codec:a libmp3lame -q:a 0 -map_metadata 0 -id3v2_version 3 "+R+Volume+filenames2[x]
                count += 1
                print(S)
            else:
                S = "ffmpeg -i "+filenames3[x]+" -codec:v copy -codec:a libmp3lame -q:a 0 -map_metadata 0 -id3v2_version 3 "+filenames2[x]
                print(S)
            subprocess.run(S,shell=True)
    elif(Diff == "Hard"):
        for x in range(len(filenames3)):
            R = random.choice(Filters)
            S = "ffmpeg -i "+filenames3[x]+" -codec:v copy -codec:a libmp3lame -q:a 0 -map_metadata 0 -id3v2_version 3 "+R+Volume+filenames2[x]
            print(S)
            subprocess.run(S,shell=True)
    return (0,filenames2)
def Convert_Music_Filters(Music_List: list,Diff: str):
    if(Diff == "Easy"):
        return Music_List
    elif(Diff == "Normal"):
        pass
    elif(Diff == "Hard"):
        pass
if __name__ == '__main__':
    status = Music_conv(Path2)
    sys.exit(status[0])
