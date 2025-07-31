#Estudando linguagem R

#operadores
1+1
2*2
8/4

((20+7)/3)^2

#variaveis
objeto1 <- 3*3
objeto2 <- 2*2
objeto3 <- objeto1 + objeto2

print(objeto3)

(casa <- "todas as letras minusculas")
(Casa <- "primeira letra maiuscula")

print(casa)
print(Casa)

#bibliotecas "automaticas"
pi
month.name

#operadores logicos
X <-21
Y <-28

X>Y

letra <-'a'
letra2 <-'b'

letra == letra2

#vetores
(primeiro.vetor <- c(1,2,3,4,5,6,7,8,9,10))
(segundo.vetor <- c(1,2,3,4,5,6,7,8,9,10))
(terceuro.vetor <- c(primeiro.vetor, segundo.vetor))

length(primeiro.vetor)

#matrizes
A <- matrix(c(1,2,2,22,2,32,56,65,34), nrow = 3, ncol = 3, byrow = TRUE)
B <- matrix(c(1,2,2,22,2,32,56,65,34), nrow = 3, ncol = 3, byrow = TRUE)
print(A*B)

#estátisca básica
x <- c(8,4,4,4,6,30)

media <- mean(x)
print(media)

mediana <- median(x)
print(mediana)