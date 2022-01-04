import sys

x, y, w, h = map(int, sys.stdin.readline().split())

y_up = h - y
y_down = y
x_left = x
x_right = w - x

print(min(y_up, y_down, x_left, x_right))
