mini = 278384
maxi = 824795

def isdub(x):
    a = str(x)
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return True
    return False

def isinc(x):
    a = str(x)
    for i in range(len(a)-1):
        if int(a[i]) > int(a[i+1]):
            return False
    return True


# part 1
count = 0
for i in range(mini,maxi+1):
    if isdub(i) and isinc(i):
        count += 1
print(count)

# part 2
def isnotgroup(x):
    a = str(x)
    for i in range(len(a)-1):
        if isdub(a[i]+a[i+1]):
            try:
                if not isdub(a[i+1]+a[i+2]):
                    try:
                        if not isdub(a[i-1]+a[i]):
                            return True
                    except:
                        return True
            except:
                if not isdub(a[i-1]+a[i]):
                    return True
    return False

count = 0
for i in range(mini,maxi+1):
    if isnotgroup(i) and isinc(i):
        count += 1
print(count)
