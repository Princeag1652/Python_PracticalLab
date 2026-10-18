
import turtle
import math
import colorsys

# Interactive Turtle Pattern Generator and Fractal Renderer

# Screen configuration
screen = turtle.Screen()
screen.title("Turtle Pattern and Fractal Generator")
screen.setup(width=900, height=700)
screen.bgcolor("#101020")
screen.colormode(255)

# Custom drawing pen
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

# RGB color generator
def get_color(index, total):
    hue = index / max(total, 1)
    r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
    return int(r * 255), int(g * 255), int(b * 255)


# Recursive Koch curve
def koch_curve(length, depth):
    if depth == 0:
        pen.forward(length)
    else:
        koch_curve(length / 3, depth - 1)
        pen.left(60)
        koch_curve(length / 3, depth - 1)
        pen.right(120)
        koch_curve(length / 3, depth - 1)
        pen.left(60)
        koch_curve(length / 3, depth - 1)


# Draw Koch snowflake
def draw_snowflake(length, depth):
    pen.penup()
    pen.goto(-length / 2, length / 3)
    pen.setheading(0)
    pen.pendown()

    for side in range(3):
        pen.color(get_color(side, 3))
        koch_curve(length, depth)
        pen.right(120)


# Draw a colorful logarithmic-style spiral
def draw_spiral(turns=5):
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    pen.pendown()

    for step in range(turns * 36):
        pen.color(get_color(step, turns * 36))
        pen.forward(2 + step * 0.12)
        pen.left(10)


# Interactive menu
print("=== Turtle Pattern Generator ===")
print("1. Koch Snowflake")
print("2. Colorful Spiral")
print("3. Both Patterns")

choice = input("Enter your choice (1-3): ").strip()

try:
    depth = int(input("Enter fractal depth (0-4): "))
    depth = max(0, min(depth, 4))
except ValueError:
    depth = 3
    print("Invalid depth. Using default depth 3.")

print("\n=== Rendering Configuration ===")
print("Canvas: 900 x 700")
print("Background: RGB(16, 16, 32)")
print("Maximum fractal depth:", depth)

if choice == "1":
    print("Rendering Koch Snowflake...")
    draw_snowflake(420, depth)

elif choice == "2":
    print("Rendering Colorful Spiral...")
    draw_spiral(5)

elif choice == "3":
    print("Rendering Koch Snowflake...")
    draw_snowflake(300, depth)

    pen.clear()
    print("Rendering Colorful Spiral...")
    draw_spiral(5)

else:
    print("Invalid choice. Rendering Koch Snowflake...")
    draw_snowflake(420, depth)

print("Rendering completed successfully!")
print("Close the graphics window to exit.")

screen.exitonclick()
