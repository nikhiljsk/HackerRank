def minion_game(word):
    word = word.lower()
    n = len(word)
    count_stuart, count_kevin = 0, 0

    for i in range(n):
        if word[i] in ['a', 'e', 'i', 'o', 'u']:
            count_kevin += (n-i)
        else:
            count_stuart += (n-i)
    
    if count_stuart > count_kevin:
        print("Stuart", count_stuart)
    elif count_stuart < count_kevin:
        print("Kevin", count_kevin)
    else:
        print("Draw")
    return

