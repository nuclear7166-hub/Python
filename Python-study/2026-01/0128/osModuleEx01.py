import os

cwd = os.getcwd()  # cwd=변수
print(cwd)
files = os.listdir()
for name in files:
    if os.path.isfile(name):
        if name.endswith(".txt"):
            print(name)
