import random

def run():
    numberRandom = random.randint(1, 100)
    entryNumber = int(input('Choose a number from 1 to 100: '))
    lives = 11

    while numberRandom != entryNumber:
        if entryNumber < numberRandom:
            print('Look for a higher number ↑')
        else:
            print('Look for a lower number ↓')
        lives -= 1
        if lives == 0:
            return print(f'You lost =( - The number was {numberRandom}')
        entryNumber = int(input(f'You have {lives} lives - choose a number: '))
    print(f'You win! the number was {numberRandom}')

if __name__ == '__main__':
    run()
