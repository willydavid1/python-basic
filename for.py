# def run():
#     for counter in range(1, 1001):
#         print(counter)

def run():
    name = input('Write your name: ')
    for word in name:
        print(f'=> {word.upper()}')

# This file is being executed directly by python
if __name__ == '__main__':
    run()
