def run():
    for i in range(10):
        if i % 2 != 0:
            continue
        print(i)

    counter = 0
    while counter < 10:
        counter += 1
        if counter % 2 != 0:
            continue
        elif counter == 10:
            print(f'BREAK {counter}')
            break
        print(f'counter {counter}')

    text = input('Write a text: ')
    for word in text:
        if word == 'o':
            print('===> BREAK \'o\'')
            break
        print(f'=> {word.upper()}')

if __name__ == '__main__':
    run()
