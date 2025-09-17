def vence(n):
    if n == 0:
        return False
    
    for i in [1, 2, 3]:
        if n - i >= 0:
            if not vence(n - i):
                return True
    return False

print(vence(4))   
print(vence(5))   
print(vence(7))   
print(vence(8))
