import random
import Music_Mover
import music_convertor
import Music_Test
import os
import Player
import time
Path1 = ""
Path2 = ""
def Create_All_Song_List():
    DL1 = os.listdir(Path1)
    DL2 = []
    for x in DL1:
        if(x[-3:] in ["mp3","mp4","m4a"]):
            DL2.append(x[:-4])
    
    return DL2
def Selected_Song_Names(Music_List: list):
    NML = []
    for x in Music_List:
        x = x.strip('"')
        NML.append(x[46:-4])
    return NML
def Game_Question_list(All_music_names: list, Correct_Song: str):
    Question_List = []
    while(True):
        if(len(Question_List) == 4):
            break
        Song = random.choice(All_music_names)
        if(Song != Correct_Song):
            if(Song not in Question_List):
                Question_List.append(Song)
    
    #Question_List = random.choices(All_music_names,k=4)
    Question_List.append(Correct_Song)
    print("Question List: ",Question_List)
    random.shuffle(Question_List)
    return Question_List
def Game_Set_NP():
    p = 0
    while(True):
        NP = input("Number of Players: ")
        if(NP in ['1','2','3','4']):
            p = int(NP)
            break
        else:
            print("Invalid Input: "+NP+" is not between 1 - 4 \n")
    return p
def Game_Set_Num_Rounds():
    R = 0
    while(True):
        GS = input("Select the game's speed: \n 1: Fast \n 2: Normal \n 3: Slow \n")
        if(GS == '1'):
            R = 2
            break
        elif(GS == '2'):
            R = 3
            break
        elif(GS == "3"):
            R = 5
            break
        else:
            print(GS+" is not a valid input.")
    return R
def Game_Set_Num_of_Songs(Number_of_Rounds: int):
    if(Number_of_Rounds == 2):
        return 10
    elif(Number_of_Rounds == 3):
        return 15
    elif(Number_of_Rounds == 5):
        return 20
def Game_Set_Difficulty():
    D = ""
    while(True):
        Diff = input("Select Difficulty: \n 1: Easy \n 2: Normal \n 3: Hard \n")
        if(Diff == '1'):
            D = "Easy"
            break
        elif(Diff == '2'):
            D = "Normal"
            break
        elif(Diff == '3'):
            D = "Hard"
            break
        else:
            print("Invalid input")
    return D
def Load_Music(P1: str, P2: str, Num_of_Songs: int):
    L = Music_Mover.File_Mov(P1,P2,Num_of_Songs)
    return L
def Create_Round_Playlist(Music_List: list,Num_of_Rounds: int):
    RoundsPL = []
    CML = Music_List.copy()
    print("CML: ",CML)
    for x in range(Num_of_Rounds):
        Rounds = []
        for y in range(5):
            S = random.choice(Music_List)
            if(S not in Rounds):
                Rounds.append(S)
                CML.remove(S)
            else:
                while(True):
                    S = random.choice(Music_List)
                    if(S not in Rounds):
                        Rounds.append(S)
                        break
                CML.remove(S)
        RoundsPL.append(Rounds)
        Music_List = CML
##    for x in range(Num_of_Rounds):
##        RL = random.choices(Music_List,k=5)
##        RoundsPL.append(RL)
##        for y in RL:
##            print(y)
##            CML.remove(y)
##        Music_List = CML
    return RoundsPL
def Convert_Music_to_MP3(File_Path: str, Diff: str, NS: int):
    return music_convertor.Music_conv(File_Path,Diff,NS)[1]
def Select_MP3_Files(Music_names1: list, Music_names2: list):
    for y in Music_names2:
        for index, item in enumerate(Music_names1):
            if(item.endswith(".m4a")):
                Music_names1[index] = y
                break
    return Music_names1
##def Alter_Music_With_Filters(Music_List: list, Diff: str):
##        music_convertor.Convert_Music_Filters(Music_list,Diff)
def Create_Player_List(Num_of_Players: int, Num_of_Rounds: int, Diff: str):
    PL = []
    for x in range(Num_of_Players):
        P = Player.Player(x+1)
        P.Set_Replay_Count(Diff,Num_of_Rounds)
        PL.append(P)
    return PL
def Question_Layout(Section: int, Section_Answers: list):
    print("Select the correct Song name for Song "+str(Section+1)+" \n")
    if(Section == 0):
        print("1: "+Section_Answers[Section][0]+"\n 2: "+Section_Answers[Section][1]
              +"\n 3: "+Section_Answers[Section][2]+"\n 4: "+Section_Answers[Section][3]
              +"\n 5: "+Section_Answers[Section][4]+"    A:Replay")
    elif(Section == 4):
        print("1: "+Section_Answers[Section][0]+"\n 2: "+Section_Answers[Section][1]
              +"\n 3: "+Section_Answers[Section][2]+"\n 4: "+Section_Answers[Section][3]
              +"\n 5: "+Section_Answers[Section][4]+"      A:Replay   B: Back   C: End Turn")
    else:
        print("1: "+Section_Answers[Section][0]+"\n 2: "+Section_Answers[Section][1]
              +"\n 3: "+Section_Answers[Section][2]+"\n 4: "+Section_Answers[Section][3]
              +"\n 5: "+Section_Answers[Section][4]+"          A:Replay  B: Back")
def Check_Answer(Player_Answers: list, Answers: list, Player_Obj):
    Index = 0
    Songs_Missed = []
    Player_Points = 0
    for x in Player_Answers:
        if(x == Answers[Index]):
            Player_Obj.update_score()
            Player_Obj.correct_Songs.append(Answers[Index])
            Player_Points += 1
            Index += 1
        else:
            Songs_Missed.append(Answers[Index])
            Index += 1
    
    return (Player_Points,Songs_Missed)
def Round_Results(RoundR: list, Round_Num: int, Playerlist: list):
    print("Round "+str(Round_Num)+" Results")
    p = 1
    rankings = []
    for x in Playerlist:
        rankings.append((p,x.Total_Points()))
        p += 1
    p = 1
    for Play in RoundR:
        print("Player "+str(p)+" results")
        print("Player "+str(p)+" got "+str(Play[0])+" points this round.")
        print("Player "+str(p)+" missed these songs: "+str(Play[1]))
        p += 1
        
    print("Current Rankings:")
    rankings.sort(key = lambda play : play[1], reverse = True)
    print("Player       Points")
    for R in rankings:
        print("Player "+str(R[0])+"      "+str(R[1]))
    time.sleep(10)
def Final_Results(PlayerList: list):
    p = 1
    rankings = []
    winners = []
    W = ""
    for x in PlayerList:
        rankings.append((p,x.Total_Points()))
        p += 1
    print("Final Rankings:")
    rankings.sort(key = lambda play : play[1], reverse = True)
    print("Player       Points")
    for R in rankings:
        print("Player "+str(R[0])+"      "+str(R[1]))
    winners.append(rankings[0][0])
    if(len(rankings) == 1):
        print("Player 1's score is "+str(rankings[0][1]))
    elif(len(rankings) == 2):
        if(rankings[0][1] == rankings[1][1]):
            print("Draw")
        else:
            if(rankings[0][1] > rankings[1][1]):
                print("Player 1 Wins!")
            else:
                print("Player 2 Wins!")
    elif(len(rankings) == 3):
        if(rankings[0][1] == rankings[1][1] and (rankings[0][1] == rankings[2][1])):
            print("Draw")
        elif(rankings[0][1] == rankings[1][1]):
            print("The Winneers are: Player "+str(rankings[0][1])+" Player "+str(rankings[1][0]))
        else:
            print("The Winner is Player "+str(rankings[0][0]))
    elif(len(rankings) == 4):
        if(rankings[0][1] == rankings[1][1] and (rankings[0][1] == rankings[2][1]) and (rankings[0][1] == rankings[3][1])):
            print("Draw")
        elif(rankings[0][1] == rankings[1][1] and (rankings[0][1] == rankings[2][1])):
            print("The Winneers are: Player "+str(rankings[0][1])+" Player "+str(rankings[1][0])+" Player "+str(rankings[2][0]))
        elif(rankings[0][1] == rankings[1][1]):
            print("The Winneers are: Player "+str(rankings[0][1])+" Player "+str(rankings[1][0]))
        else:
            print("The Winner is Player "+str(rankings[0][0]))

def Main_Game():
    print("Welcome to Moon & Star Sound Music Game\n")
    Number_of_Players = Game_Set_NP()
    Number_of_Rounds = Game_Set_Num_Rounds()
    Number_of_Songs = Game_Set_Num_of_Songs(Number_of_Rounds)
    Game_Difficulty = Game_Set_Difficulty()
    Playerlist = Create_Player_List(Number_of_Players,Number_of_Rounds,Game_Difficulty)
    Music_List = Load_Music(Path1,Path2,Number_of_Songs)
    print("OG Music_List: ",Music_List)
    Music_List2 = Convert_Music_to_MP3(Path2,Game_Difficulty,Number_of_Songs)
    print("Music List 2: ",Music_List2)
    Music_List = Select_MP3_Files(Music_List,Music_List2)
    print("New Music List: ",Music_List)
    Round_Playlist = Create_Round_Playlist(Music_List,Number_of_Rounds)
    print("Round Playlist: ",Round_Playlist)
    for x in range(Number_of_Rounds):
        print("Round "+str(x+1))
        Song_Names = Selected_Song_Names(Round_Playlist[x])
        print(Song_Names)
        All_Songs = Create_All_Song_List()
        Section_Answers = []
        Player_Answers = [0,0,0,0,0]
        All_Players_Round_Results = []
        for y in Song_Names:
            print("y is "+y)
            Section_Answers.append(Game_Question_list(All_Songs,y))
        PI = Music_Test.Play_Music(Round_Playlist[x])
        print(Section_Answers)
        pos = 1
        Sec = 0
        while(True):
            print("Its Player "+str(pos)+"'s turn\n")
            while(True):
                Question_Layout(Sec,Section_Answers)
                Player_Input = input()
                if(Player_Input == "1"):
                    Player_Answers[Sec] = Section_Answers[Sec][0]
                    if(Sec != 4):
                        Sec += 1
                elif(Player_Input == "2"):
                    Player_Answers[Sec] = Section_Answers[Sec][1]
                    if(Sec != 4):
                        Sec += 1
                elif(Player_Input == "3"):
                    Player_Answers[Sec] = Section_Answers[Sec][2]
                    if(Sec != 4):
                        Sec += 1
                elif(Player_Input == "4"):
                    Player_Answers[Sec] = Section_Answers[Sec][3]
                    if(Sec != 4):
                        Sec += 1
                elif(Player_Input == "5"):
                    Player_Answers[Sec] = Section_Answers[Sec][4]
                    if(Sec != 4):
                        Sec += 1
                elif(Player_Input == "A"):
                    if(Playerlist[pos-1].Replay_Count[x] != 0):
                        Playerlist[pos-1].Update_Replay_Count(x)
                        Music_Test.Replay_Song(PI[Sec][0],PI[Sec][1])
                        print("Player "+str(pos)+" has "+str(Playerlist[pos-1].Replay_Count[x])+" left.")
                    else:
                        print("Player "+str(pos)+" has no replays left.")
                elif(Player_Input == "B" and Sec != 0):
                    Sec -= 1
                elif(Player_Input == "C" and Sec == 4):
                    Results = Check_Answer(Player_Answers,Song_Names,Playerlist[pos-1])
                    All_Players_Round_Results.append(Results)
                    pos += 1
                    Sec = 0
                    #All_Player_Answer.append(Player_Answers)
                    #pos += 1
                    break
                else:
                    print("Invalid Input")
                
            if(pos > Number_of_Players):
                break
        Round_Results(All_Players_Round_Results,x+1,Playerlist)
        
    Final_Results(Playerlist)
def Music_Game_Wrap_around():
    Main_Game()
    while(True):
        PI = input("Do you want to play again A: Yes   B: No \n")
        if(PI == "A"):
            Main_Game()
        elif(PI == "B"):
            print("Goodbye!")
            break

    
    
