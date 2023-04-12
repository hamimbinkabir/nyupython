def string_splitter(value):
    length = len(value)
    middle = length // 2
    half1 = value[: middle]
    half2 = value[middle:]

    if length % 2 == 1:
        half2 = value[middle + 1:]
        print("Middle character:", value[middle])

    print("First half:", half1)
    print("Second half:", half2)

string = input("Enter an odd length string:")
string_splitter(string)