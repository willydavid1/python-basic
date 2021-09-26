def is_prime(number):
    # for i in range(1, number + 1):
    #     if i == 1 or i == number:
    #         print(f'i {i}')
    #         continue
    #     if number % i == 0:
    #         return False
    # return True

    # Teorema de Wilson ((n-1)! + 1) % n == 0
    def factorial(n):
        value = 1
        for i in range(1, n):
            value = (value * (i + 1))
        return value
    return (((factorial(number - 1) + 1) % number) == 0)

def run():
    number = int(input('Write a number: '))
    if is_prime(number):
        print('The number is prime')
    else:
        print('The number is not prime')

# This file is being executed directly by python
if __name__ == '__main__':
    run()
