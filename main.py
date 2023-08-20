import random

# rolls the x num of dice and displays their outcome and the sum
def roll_dice(num_dice):
    rolls = []
    for i in range(num_dice):
        rolls += [random.randint(1, 6)]
    total = sum(rolls)
    return print(str(rolls)[1:-1], 'sum =', total)

# asks user how many dice they would like to roll and checks value
def main():
    while True:
        try:
            num_dice = input("How many dice would you like to roll?\n")
            num_dice = num_dice.lower()
            if num_dice == 'exit':
                print("Thanks for playing!")
                break
            num_dice = int(num_dice)
            if num_dice == 0:
                raise ValueError
        except ValueError:
            print("Please input a valid number.")
            continue
        roll_dice(num_dice)


main()
