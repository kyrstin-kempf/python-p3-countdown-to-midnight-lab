import time

def countdown(i):
    while i <= 10:
        print(f'{i} SECOND(S)!')
        i -= 1
        if i == 0:
            break
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(i):
    while i <= 10:
        print(f'{i} SECOND(S)!')
        time.sleep(1)
        i -= 1
        if i == 0:
            break
    print("HAPPY NEW YEAR!")