def most_frequent():
    str = input("Input a String: ")
    str = str.casefold()
    dict = {}
    for char in str:
        dict[char] = dict.get(char,0)+1
    a = sorted(dict.items(), key=lambda x: x[1], reverse= True)
    print(a)
most_frequent()
