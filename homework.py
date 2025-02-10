class Match:
    def __init__(self,name,rank):
        self.name=name
        self.rank = rank
    def hi(self):
        print(f"Hello,welcome game {self.name} mening uruvinim {self.rank}")


class playerstats(Match):
    def __init__(self,name,rank,goals,assists,points):
        super().__init__(name,rank)
        self.goals = goals
        self.assists = assists
        self.points = points
        self.name = name
        self.rank = rank


    def hi(self):
        print(f"Hello,welcome to game {self.name}, mening uruvinim {self.rank}")
        return self.hi

    def playerstats(self):
        print(f"men o'yindaman {self.name} levelim {self.rank}, golim {self.goals}, assistlarim{self.assists}, pazitsiyam {self.points}.")
        return self.playerstats

p = playerstats("shuhrat",120,50,13,4)
p.hi()
p.playerstats()
