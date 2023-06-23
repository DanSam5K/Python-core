import math


radius = 5
area = math.pi * math.pow(radius, 2)

def print_area():
        print(area)

print("I can run in main") # not protected by`__name__ == "__main__"`

if __name__ == "__main__":
    print("I will on run here") # I am covered by `if __name__ == "__main__":`

    print(radius)

    