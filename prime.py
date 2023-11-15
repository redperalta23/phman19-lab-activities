for number in range(1, 251):
    if number > 1:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                break
        else:
            print(number)
