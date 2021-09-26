def run():
    LIMIT = 1000
    counter = 0
    potency = 2 ** counter

    while potency < LIMIT:
        print(f'2 elevado a {counter} es igual {potency}')
        counter = counter + 1
        potency = 2 ** counter

# This file is being executed directly by python
if __name__ == '__main__':
    run()
