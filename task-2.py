import turtle

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)


def draw_snowflake(level):
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.color("blue")

    # Малюємо три сторони сніжинки
    for _ in range(3):
        koch_snowflake(t, 400, level)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (наприклад, 3): "))
        if level < 0:
            print("Рівень рекурсії має бути невід'ємним числом.")
        else:
            draw_snowflake(level)
    except ValueError:
        print("Будь ласка, введіть ціле число.")
