class Player:
    def __init__(self,Pos):
        self.position = Pos
        self.points = 0
        self.correct_Songs = []
        self.Replay_Count = []
    def update_score(self):
        self.points += 1
    def Set_Replay_Count(self, Diff: str, Num_Rounds: int):
        if(Diff == "Easy"):
            self.Replay_Count = [5 for x in range(Num_Rounds)]
        elif(Diff == "Normal"):
            self.Replay_Count = [3 for x in range(Num_Rounds)]
        elif(Diff == "Hard"):
            self.Replay_Count = [1 for x in range(Num_Rounds)]
    def Update_Replay_Count(self,Round: int):
        self.Replay_Count[Round]-= 1
    def Total_Points(self):
        return self.points
    def check_position(self,Pos):
        if(pos == self.Position):
            return True
        else:
            return False
    def update_song_list(self,Song_Name):
        self.correct_songs.append(Song_Name)
