# Entrada
material = input()
p_fusao = float(input())
p_ebul = float(input())
temp_f = float(input())

# Conversao
temp_c = round(((temp_f - 32) / 1.8), 2)

print("Material:", material)
print("Ponto de fusao (Celsius):", format(p_fusao, ".2f"))
print("Ponto de ebulicao (Celsius):", format(p_ebul, ".2f"))
print("Temperatura atual (Celsius):", format(temp_c, ".2f"))

# Teste do estado fisico
if temp_c < p_fusao:
    ESTADO = "Solido"
elif temp_c >= p_ebul:
    ESTADO = "Gasoso"
else:
    ESTADO = "Liquido"
print("Estado fisico do material:", ESTADO)
