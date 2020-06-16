def get_ordered_distinct(word):
    letters = list(word)
    unique = list()
    for letter in letters:
        if letter not in unique:
            unique.append(letter)
    return ''.join(unique)

def merge_the_tools(word, k):
    n = len(word)
    for i in range(0, n, k):
        print(get_ordered_distinct(word[i:i+k]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)