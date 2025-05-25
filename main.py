class ColorRGB:
    def __init__(self, red: int, green: int, blue: int):
        """
        Ініціалізація кольору RGB.

        Args:
            red (int): Червоний  (0–255)
            green (int): Зелений  (0–255)
            blue (int): Синій  (0–255)
        """
        if type(red) != int or type(green) != int or type(blue) != int:
            raise TypeError("Усі значення мають бути цілими числами (int)")

        if red < 0 or red > 255:
            raise ValueError("red має бути в межах 0–255")
        if green < 0 or green > 255:
            raise ValueError("green має бути в межах 0–255")
        if blue < 0 or blue > 255:
            raise ValueError("blue має бути в межах 0–255")

        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        """
        Повертає рядкове представлення кольору у форматі RGB.

        Returns:
            str: Рядок типу "RGB(255, 100, 50)"
        """
        return f"RGB({self.red}, {self.green}, {self.blue})"

    def to_hex(self):
        """
        Перетворює RGB в HEX.

        Returns:
            str: Наприклад "#FF6400"
        """
        return "#{:02X}{:02X}{:02X}".format(self.red, self.green, self.blue)

    def grayscale(self):
        """
        Повертає відтінок сірого (усереднення компонентів).

        Returns:
            int: Значення сірого (0–255)
        """
        return (self.red + self.green + self.blue) // 3

    def is_black(self):
        """
        Перевіряє, чи це чорний колір.

        Returns:
            bool: True, якщо всі компоненти рівні 0
        """
        return self.red == 0 and self.green == 0 and self.blue == 0

    def __eq__(self, other):
        """
        Перевіряє, чи два кольори однакові.

        Returns:
            bool
        """
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __add__(self, other):
        """
        Додає два кольори (обмежує до 255).

        Returns:
            ColorRGB
        """
        r = min(self.red + other.red, 255)
        g = min(self.green + other.green, 255)
        b = min(self.blue + other.blue, 255)
        return ColorRGB(r, g, b)

    def __lt__(self, other):
        """
        Порівнює кольори за яскравістю.

        Returns:
            bool
        """
        return self.grayscale() < other.grayscale()

    def __gt__(self, other):
        """
        Порівнює кольори за яскравістю.

        Returns:
            bool
        """
        return self.grayscale() > other.grayscale()


if __name__ == "__main__":
    try:
        c1 = ColorRGB(100, 150, 200)
        c2 = ColorRGB(255, 255, 255)
        c3 = ColorRGB(300, 0, 0)
    except Exception as e:
        print("Помилка:", e)

    print(c1)
    print("HEX:", c1.to_hex())
    print("Grayscale:", c1.grayscale())
    print("c1 == c2?", c1 == c2)
    print("c1 < c2?", c1 < c2)
    print("Сума c1 + c2:", c1 + c2)

