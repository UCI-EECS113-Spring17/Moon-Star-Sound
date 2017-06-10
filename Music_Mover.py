import os,time
import random
import shutil

Path = ""
Path2 = ""
def File_Mov(Path1: str,Path2: str,NumF: int):
    DL = os.listdir(Path1)
    RL = []
    RL2 = []
    while(True):
        M = random.choice(DL)
        print(M)
        if(M[-3:] in ["mp3","mp4","m4a"]):
            if(len(RL) == 0):
                RL.append(M)
            else:
                print("The length of RL is: "+str(len(RL))+"\n")
                if(M not in RL):
                    RL.append(M)
                    if(len(RL) == NumF):
                        break
    for x in RL:
        shutil.copyfile(Path1+"\\"+x,Path2+"\\"+x)
    for v in RL:
        RL2.append(Path2+"\\"+v)
    return RL2

if __name__ == "__main__":
    print(file_Check(Path,Path2))
