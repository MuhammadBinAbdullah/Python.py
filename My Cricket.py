class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__player = score

    def info(self):
        print(f"Cricket - Player : {self.__player}, Score : {self.__score}")

    def play(self):
        print(f"{self.__player} Hits A Six !")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >=
    