def calcu(l):
    # initialize results
    r = []
    for i in range(len(l)):
        x = l[i]
        r.append(x * x)
    return r

def unused():
    pass

# execution
data = [1, 2, 3]
print(calcu(data))
