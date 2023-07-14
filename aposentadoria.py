def calcular_aposentadoria(idade, sexo, tempo_contribuicao, salario_atual):
    if sexo == 'masculino':
        idade_aposentadoria = 65
    else:
        idade_aposentadoria = 60

    anos_contribuicao = idade - tempo_contribuicao

    if anos_contribuicao >= 35:
        valor_aposentadoria = salario_atual * 0.8
    else:
        valor_aposentadoria = salario_atual * 0.6

    return idade_aposentadoria, anos_contribuicao, valor_aposentadoria

# Exemplo de uso da função:
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo (masculino ou feminino): ")
tempo_contribuicao = int(input("Digite seu tempo de contribuição (em anos): "))
salario_atual = float(input("Digite seu salário atual: "))

aposentadoria = calcular_aposentadoria(idade, sexo, tempo_contribuicao, salario_atual)
idade_aposentadoria, anos_contribuicao, valor_aposentadoria = aposentadoria

print(f"Você poderá se aposentar aos {idade_aposentadoria} anos.")
print(f"Você já contribuiu por {anos_contribuicao} anos.")
print(f"O valor estimado da sua aposentadoria é R$ {valor_aposentadoria:.2f}.")
