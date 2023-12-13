class Rectangle:

    def __init__(self, length, height, display_char, rectangle_style=None):
        self.length = length
        self.height = height
        self.display_char = display_char
        self.rectangle_style = rectangle_style

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def display_char(self):
        return self.__display_char

    @display_char.setter
    def display_char(self, display_char):
        self.__display_char = display_char

    @property
    def rectangle_style(self):
        return self.__rectangle_style

    @rectangle_style.setter
    def rectangle_style(self, rectangle_style):
        self.__rectangle_style = rectangle_style

    def calculate_area(self):
        return self.height * self.length

    def display(self):
        lines = []

        if self.rectangle_style is not None:
            for i in range(self.height):
                if i == 0:
                    lines.append(
                        self.rectangle_style.top_left
                        + ((self.length * 2)-2) * self.rectangle_style.top_horizontal
                        + self.rectangle_style.top_right
                    )
                elif i == self.height - 1:
                    lines.append(
                        self.rectangle_style.bottom_left
                        + ((self.length * 2)-2) * self.rectangle_style.bottom_horizontal
                        + self.rectangle_style.bottom_right)

                else:
                    lines.append(
                        self.rectangle_style.left_vertical
                        + ((self.length * 2)-2) * " "
                        + self.rectangle_style.right_vertical)
        else:
            for i in range(self.height):
                lines.append(self.display_char * self.length)

        for i in lines:
            print(i)

    def __str__(self):
        return f"('{self.length}', '{self.height}')"
