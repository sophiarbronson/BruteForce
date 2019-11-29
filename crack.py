import itertools
import string
import getpass
import time

def guessPassword(drowssaP, limit):
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    attempts = 0

    for password_length in range((limit-1), limit):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == drowssaP:
                return('password is {}, found in {} guesses.'.format(guess, attempts))
            print(guess, attempts)

start_time = time.time()
drowssaP=getpass.getpass("Your password: ")
limit=(len(drowssaP)+1)

print(guessPassword(drowssaP, limit))
print('It took', float(time.time() - start_time), 'to crack the password')
