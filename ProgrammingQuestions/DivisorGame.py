def divisorGame(n: int) -> bool:
    winning = [0] * (n + 1)  # dictionary of win/lose

    for i in range(1, n + 1):
        # find divisors
        for j in range(1, int(i / 2)+1):
            if i % j == 0 and winning[i - j] == 0:
                winning[i] = 1
    print(winning)
    print(winning[2::2]==[1]*len(winning[2::2]))
    print(winning[1::2]==[0]*len(winning[1::2]))



    return winning[n]


divisorGame(10000)
