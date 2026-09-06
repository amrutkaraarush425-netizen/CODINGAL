class Cricket:
    def __init__(self, player, score):
        self.__player = player         # private attribute
        self.__score = score           # private attribute

    def info(self):                    # same method name as Football
        print(f"Cricket - player: {self._player}, Score: {self.__score}")   
        
    def play(self):                    # same method name, different output
        print(f"{self.__player} hits a six! ")

    def get_score(self):               # getter - read private data
        return self.__score

    def set_score(self, new_score):    # setter - update private data safely
        if new_score >= 0:
            self._score = new_score
            print(f"score updated to {self.__score}")
        else:
            print("Score cannot be negative")


class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):                    # same name , different output
        print(f"Football - Player : {self.__player}, Score : {self.score}")

    def play(self):                    # same name , diffetent behaviour
        print(f"self.__player" scores a goal!)
              
    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
        self.__score = new_score
        print(f"Score updated to{self.__score}")
        else: