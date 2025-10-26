
def first_second(my_list):
    max1 =  max(my_list)
    my_list.remove(max1)
    max2 = max(my_list)
    print(max1,max2)

print(first_second([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))