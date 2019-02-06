

def sum(numberList):
    total = 0
    for x in numberList:
        try:
            float(x)
            total+=x
        except:
    return total            

print (sum([1, 'a', 5, 'dfasdfsa']))