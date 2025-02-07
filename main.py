class Swimmer:
    def swim(self):\
        print("Swimming")


class Pilot:
    def fly(self):
        print("Men uchamaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaan")

class Holder(Swimmer,Pilot):
    pass

h = Holder()
h.fly()
h.swim()