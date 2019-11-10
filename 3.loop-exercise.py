# Create a function that return the largest number in the list

def get_largest_number(item_list):
    largest_number = None
    
    for item in item_list:
        if(largest_number is None):
            largest_number = item
        elif(largest_number < item):
            largest_number = item
        ##Get the item
        ## if it is bigger than largest_number variable
        ## Put it in the largest_number    
            
    return largest_number

result = get_largest_number([-1,-2,-5,-7])
print(result) #500


