n = input("n = ")
p_list = []
for x in range (1,n+1):
    if x > 1:
        for i in range(2, x):
            if (x%i) == 0:
                break
        else:
            p_list.append(x)    

print(p_list)


