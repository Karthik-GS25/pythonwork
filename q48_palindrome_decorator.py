"""48. Use a decorator to report palindrome numbers."""


def palindrome_check(function):
    def wrapper(number):
        return function(number) and str(number) == str(number)[::-1]

    return wrapper


@palindrome_check
def valid_number(number):
    return number >= 0


print(valid_number(121))
