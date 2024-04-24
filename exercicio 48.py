s = 0
for n in range(1,501):
    if (n % 2) == 1:
        if (n % 3) == 0:
            s += n
print(f"A soma dos múltiplos de 3 é {s}")
