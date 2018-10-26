class Tile:

    def __init__(self, pos_x, pos_y, width, height, number):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._width = width
        self._height = height
        self._number = number

    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value):
        self._pos_x = value

    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        self._pos_y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    def get_properties(self):
        return (self.pos_x, self.pos_y, self.width, self.height, self.number)
