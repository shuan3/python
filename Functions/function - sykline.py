def mufunc(s):
    n = []
    for idx, ss in enumerate(s):
        if idx % 2 == 0:
            n.append(ss.lower())
        else:
            n.append(ss.upper())
    return "".join(n)


print(mufunc("lolololololol"))


# a=[0,0,7]
# b=[0,0,0,7]
# aa='007'
# bb='00007'
# print(aa,bb)
# if aa in bb:
#     print("yes")
def spy_game(l):
    s = ""
    for i in l:
        if i == 0 or i == 7:
            s = s + str(i)
    if "007" in s:
        return True
    else:
        return False


print(spy_game([1, 2, 30, 0, 0, 7, 0, 0, 0]))


def spy_game(nums):
    code = [0, 0, 7, "x"]
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


def count_prime(num):
    if num < 2:
        return 0
    primes = [2]
    x = 3
    while x <= num:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
