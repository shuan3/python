def ran_rank(num, low, high):
    if num > low and num < high:
        print(f" {num} is in the range between {low} and {high}")  # type: ignore
    return


ran_rank = lambda num, low, high: num in range(low, high + 1)
print(ran_rank(1, 0, 5))


def ran_bool(num, low, high):
    if num > low and num < high:
        return True
    return False


def up_low(s):
    u = 0
    l = 0
    for idx, ss in enumerate(s):
        if ss.isupper():
            u += 1
        elif ss.islower():
            l += 1
        else:
            continue
    print(f"No. of Upper case characters : {u}")
    print(f"No. of Lower case characters : {l}")
    return


def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1]))


def multiply(numbers):
    s = 1
    for i in numbers:
        s = s * i
    return s


def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


def ispangram(s: str, alphabet):
    alphaset = set(alphabet)
    s = s.replace(" ", "")
    s = s.lower()
    s = set(s)
    return s == alphaset
