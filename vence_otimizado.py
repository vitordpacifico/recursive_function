def vence_iterativa(n):

    dp = [False] * (n + 1)    
    for i in range(1, n + 1):
        jogadas_possiveis = [1, 2, 3]
        if any(not dp[i - jogada] for jogada in jogadas_possiveis if i - jogada >= 0):

            dp[i] = True
            
    return dp[n]

print(f"vence_iterativa(4): {vence_iterativa(4)}")
print(f"vence_iterativa(5): {vence_iterativa(5)}")
print(f"vence_iterativa(7): {vence_iterativa(7)}")
print(f"vence_iterativa(8): {vence_iterativa(8)}")
print(f"vence_iterativa(10000): {vence_iterativa(10000)}")