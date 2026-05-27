def mulreturn():
    return 1, 2


x, y = mulreturn()
print(f"x = {x}, y = {y}")
print(mulreturn())
