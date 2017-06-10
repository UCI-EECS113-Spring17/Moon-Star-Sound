import pygame
import mutagen
import math
import random
import threading
import time
import Music_Mover
import music_convertor

Path = "C:\\Users\\KrystopherM\\Music"
Path2 = "C:\\Users\\KrystopherM\\Music\\EECS113_Test_Music"

FFMPEG_Filter_List = []
def mstop():
    pygame.mixer.music.stop()
def music_names(Path01: str, Path02: str, Rounds: int):
    
    return Music_Mover.File_Mov(Path01,Path02, Rounds)

def convert_M(Path: str):
    return music_convertor.Music_conv(Path)[1]
def Play_Music(Music_List: list):
    pygame.mixer.init()
    Play_information = []
    for M in Music_List:
        M = M.strip('"')
        print(M)
        audio = mutagen.File(M)
        print(audio.info.length)
        newL = math.floor(audio.info.length)
        print(newL)
        Lower = random.randrange(0,newL,20)
        print(Lower)
        Higher = 20+Lower
        while(Higher > newL):
            print("Bad Higher: "+str(Higher))
            Lower = random.randrange(0,newL,20)
            print("New Lower: "+str(Lower))
            Higher = Lower + 20
        Play_information.append((M,Lower))
        pygame.mixer.music.load(M)
        pygame.mixer.music.play(start = Lower)
        t = threading.Timer(20.0,mstop)
        t.start()
        time.sleep(20)
    time.sleep(5)
    pygame.mixer.quit()
    return Play_information
def Replay_Song(Song: str, Play_location: int):
    print("Replaying Song...")
    pygame.mixer.init()
    pygame.mixer.music.load(Song)
    pygame.mixer.music.play(start = Play_location)
    t = threading.Timer(20.0,mstop)
    t.start()
    time.sleep(20)
    time.sleep(5)
    pygame.mixer.quit()
    print("Finsihed Replaying Song.")
if __name__ == "__main__":
    #pygame.mixer.init()
    #pygame.mixer.music.load
    x = music_names(Path,Path2,5)
    x2 = convert_M(Path2)
    for y in x2:
        for index, item in enumerate(x):
            if(item.endswith(".m4a")):
                x[index] = y
                break
    print(x)
    random.shuffle(x)
    pygame.mixer.init()
    for M in x:
        M = M.strip('"')
        print(M)
        audio = mutagen.File(M)
        print(audio.info.length)
        newL = math.floor(audio.info.length)
        print(newL)
        Lower = random.randrange(0,newL,20)
        print(Lower)
        Higher = 20+Lower
        while(Higher > newL):
            print("Bad Higher: "+str(Higher))
            Lower = random.randrange(0,newL,20)
            print("New Lower: "+str(Lower))
            Higher = Lower + 20

        pygame.mixer.music.load(M)
        pygame.mixer.music.play(start = Lower)
        t = threading.Timer(20.0,mstop)
        t.start()
        time.sleep(20)
    time.sleep(5)
    pygame.mixer.quit()
        
