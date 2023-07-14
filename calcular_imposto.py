from imposto import calcular_imposto

faturamento = 5000
ir = calcular_imposto(faturamento, 0.2)
iss = calcular_imposto(faturamento, 0.05)
csll = calcular_imposto(faturamento, 0.0025)

print(ir, iss, csll)
