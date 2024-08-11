def square(num):
    return num**2
nums=[1,2,3,4,5]
# for item in map(square,nums):
#     print(item)
new_num=list(map(square,nums))
print(new_num)


def splicer(s):
    if len(s)%2==0:
        return 'EVEN'
    else:
        return s[0]
    
names=['lol','ironman','captain china']
print(list(map(splicer,names)))


def check_even(num):
    return num%2==0

nums=[1,2,3,4,5,6]
print(list(filter(check_even,nums)))



for n in filter(check_even,nums):
    print(n)




def square(num):
    return num**2
square=lambda num:num**2
print(square(5))

print(list(map(lambda num:num**2, nums)))

print(list(map(lambda num:num%2==0, nums)))
