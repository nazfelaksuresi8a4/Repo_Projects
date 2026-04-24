class MyExc(Exception):
    def __init__(self, msg, code=None):
        super().__init__(f"msg: {msg}\ncode:{code}") 

def divisor(x, y):
    try:
        raise x / y
    
    except Exception as e:
        raise MyExc(str(e), 404) 
 
try:
    divisor(2, 0) 
    
except Exception as e:
    print(e) 