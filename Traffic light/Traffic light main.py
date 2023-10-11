import itertools
import time


# def Time():
#     user_input = input("Enter a word or phrase: ")
#     for letter in user_input:
#         print(letter, end='', flush=True)
#         time.sleep(2)

#     print()


# if __name__ == "__main__":
#     Time()
light = [
    ("green", 5),
    ("yellow", 3),
    ("red", 8)
]


def traffic_light():
    color = itertools.cycle(light)
    red_count = 0  # Initialize the red light counter
    while True:
        c, s = next(color)
        print(c)
        print(red_count)
        time.sleep(s)
        if c == "red":
            red_count += 1
            if red_count >= 3:
                break  #


traffic_light()
