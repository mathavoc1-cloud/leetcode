def palindrome():
    num = int(input('Type a number: '))

    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


resultado  = palindrome()

if resultado:
    print('true')
else:
    print('false!')