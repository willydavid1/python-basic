def palindrome(word):
    word_without_spaces = word.replace(' ', '').strip().lower()
    inverted_word = word_without_spaces[::-1]
    return inverted_word == word_without_spaces

def run():
    word = input('Write a word: ')
    is_palindrome = palindrome(word)

    if is_palindrome:
        print('It\'s palindrome')
    else:
        print('It isn\'t palindrome')


# This file is being executed directly by python
if __name__ == '__main__':
    run()
