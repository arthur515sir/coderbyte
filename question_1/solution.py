def BracketMatcher(strParam):
    left = 0
    right = 0

    for cr in strParam:
        if (cr == "("):
            left = left + 1
        elif (cr == ")"):
            right = right + 1

    if (right == left):
        left = 0
        right = 0
        return 1

    else:
        right = 0
        left = 0
        return 0

        # code goes here


# keep this function call here
print(BracketMatcher(input()))