class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print("starting to draw")


class Pen(Stationery):
    def __init__(self):
        Stationery.__init__(self, "pen")

    def draw(self):
        print("pen is drawing")


class Pencil(Stationery):
    def __init__(self):
        Stationery.__init__(self, "pencil")

    def draw(self):
        print("pencil is drawing")


class Handle(Stationery):
    def __init__(self):
        Stationery.__init__(self, "handle")

    def draw(self):
        print("handle is drawing")


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()