""" 1. yöntem """

denklem = "2x^2+3x-5"

nums = {key : num for key, num in enumerate(denklem) if num.isdigit()}
operators = {key : num for key, num in enumerate(denklem) if num.isdigit() != True}

n1, n2 = len(nums), len(operators)

if n1 != n2:
    maxx = max(n1, n2) 
    if maxx == n1:
        while n1 != n2:
            n2 = len(nums) 
            operators["."] = ".."
    
    elif maxx == n2:
        while n2 != n1:
            n1 = len(operators) 
            nums["."] = ".."

ops, num = list(operators.keys()) , list(nums.keys()) 

for opkey, numkey in zip(ops, num):
    print(f"{operators[opkey]} : {nums[numkey]}") 
    

""" 2. yöntem """
denklem = "2x^2+3x-5"

nums = [num for num in denklem if num.isdigit()]
operators = [op for op in denklem if op.isdigit() != True]

n1, n2 = len(nums), len(operators)

maxlen = max(n1, n2) 

nums, operators = list(nums), list(operators) 

operators += [None] * (maxlen - n2)
nums += [None] * (maxlen - n1) 

print(len(operators) == len(nums)) 

for nx, ny in zip(nums ,operators):
    print(f"{nx} : {ny}") 
    