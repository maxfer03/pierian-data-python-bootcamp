def ran_check(num,low,high):
    nums = range(low,high+1)
    is_num = num in nums    
    return is_num


print(ran_check(1,2,7))