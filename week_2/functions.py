

# my_sort is
num_list = input("input list (ex: [5, 3, 12, 4]): ")

def my_sort(list):
    for i in range(1, len(num_list)):
        copy = num_list[i]
        j = i-1
        while j >= 0 and copy < num_list[j]:
            num_list[j+1] = num_list[j]
            j -= 1
        num_list[j+1] = copy      
my_sort(list)
for i in range(len(num_list)): 
    print ("%d" %num_list[i])     
