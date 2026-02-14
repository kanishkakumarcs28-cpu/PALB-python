25.
def isPalinArray(arr):
    
    for num in arr:
        original = num
        rev = 0
        
        while num > 0:
            rev = rev * 10 + (num % 10)
            num //= 10
        
        if original != rev:
            return False
    
    return True
