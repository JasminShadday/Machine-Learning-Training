#int (inteiros)- Números inteiros, positivos ou negativos, sem casas decimais.
idade = 25

#float (ponto flutuante) - Números com casas decimais (números reais).
altura = 1.75

#str (string) - Texto, ou seja, sequência de caracteres.
nome = "Jasmin"

#bool (booleano) - Verdadeiro ou falso.
ativo = True

#list (lista) - Uma coleção ordenada e mutável de itens.
frutas = ["maçã", "banana", "uva"]

#tuple (tupla) - Como uma lista, mas imutável (não pode ser alterada).
coordenadas = (10, 20)

#set (conjunto) - Uma coleção não ordenada e sem itens repetidos.
cores = {"vermelho", "verde", "azul"}

#dict (dicionário) - Coleção de pares chave:valor.
pessoa = {"nome": "Ana", "idade": 30}

#🧠 Extras (menos usados no início, mas importantes mais pra frente):
#Tipo	Exemplo	Pra que serve?
#bytes	b"texto"	Armazenar dados binários
#NoneType	None	Representa “nada”, ou valor vazio
#range	range(0, 10)	Sequência de números (usado em for)

#✅ Dica bônus:
#Você pode usar a função type() para ver o tipo de uma variável:
x = 5
print(type(x))  
# <class 'int'>