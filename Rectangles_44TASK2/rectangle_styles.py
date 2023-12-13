class RectangleStyle:

    @property
    def top_left(self):
        raise NotImplementedError()

    @property
    def top_left(self):
        raise NotImplementedError()

    @property
    def top_right(self):
        raise NotImplementedError()

    @property
    def bottom_left(self):
        raise NotImplementedError()

    @property
    def bottom_right(self):
        raise NotImplementedError()

    @property
    def top_horizontal(self):
        raise NotImplementedError()

    @property
    def bottom_horizontal(self):
        raise NotImplementedError()

    @property
    def left_vertical(self):
        raise NotImplementedError()

    @property
    def right_vertical(self):
        raise NotImplementedError()


class DoubleLinesStyle(RectangleStyle):
    @property
    def top_left(self): return '\u2554'

    @property
    def top_right(self): return '\u2557'

    @property
    def bottom_left(self): return '\u255A'

    @property
    def bottom_right(self): return '\u255D'

    @property
    def top_horizontal(self): return '\u2550'

    @property
    def bottom_horizontal(self): return '\u2550'

    @property
    def left_vertical(self): return '\u2551'

    @property
    def right_vertical(self): return '\u2551'


class SingleLineStyle(RectangleStyle):

    @property
    def top_left(self): return '\u250C'

    @property
    def top_right(self): return '\u2510'

    @property
    def bottom_left(self): return '\u2514'

    @property
    def bottom_right(self): return '\u2518'

    @property
    def top_horizontal(self): return '\u2500'

    @property
    def bottom_horizontal(self): return '\u2500'

    @property
    def left_vertical(self): return '\u2502'

    @property
    def right_vertical(self): return '\u2502'
