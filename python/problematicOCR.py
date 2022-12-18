# parse the string and convert all numeric value to numeric value * "?"
def parser(name):
    res = ""
    for i in range(len(name)):
        res += ("?" * int(name[i])) if name[i].isnumeric() else name[i]
    return res

def solution(string_one, string_two):
    string_one = parser(string_one)
    string_two = parser(string_two)

    # check equal length after parsing
    if len(string_one) != len(string_two):
        return False

    # check alphabet by alphabet
        # if string_one[i] is "?", means string_two[i] can be anything
        # vice versa
    for i in range(0, len(string_one)):
        if string_one[i] == "?" or string_two[i] == "?":
            continue
        elif string_one[i] != string_two[i]:
            return False
    return True

if __name__ == '__main__':
    print(solution('a2Le', "2pL1"))
    print(solution('a10', "10a"))
    print(solution('ba1', "1Ad"))
    print(solution('3x2x', "8"))