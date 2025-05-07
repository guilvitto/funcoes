def imprimir_nome(nome):
    print(f"Nome : {nome}")

def piramide(n):
    for i in range(1,n+1,1):
        for j in range(0,i):
            print(i,end=" ")
        print()

def cont_vogal(texto):
    cont=0
    for i in texto.lower(): #i= ao conteúdo do texo, não o indice:
        if i in "aeiou":
            cont+=1
    print(cont)

def estoque(nome,qtd,valor_unitario):
    valor_total= float(int(qtd) * valor_unitario)
    #print(f" Existem {qtd} de {nome} e o valor total no estoque é : R$ {valor_total:.2f}")
    return valor_total
    #atribuir uma nova variável para receber a função, pois assim o return funcionará
        #EXEMPLO: r=estoque("nescau",5,10)
                # print(r)

def sinal(num):
    if num==0:
        #resposta="Z"
        return "Z"
    elif num>0:
        #resposta="P"
        return "P"
    else:
        #resposta="N"
        return "N"
    #return resposta
#resposta = sinal(-50)
#print(resposta)

def soma(n1,n2):
    soma=int(n1+n2)
    print(soma)

def somar_tupla(*itens):
    soma=0
    for i in itens:
        soma=soma+i
    print(itens)
    print(soma)
    #somar_tupla(7,3,10)
    #soma=sum(itens)
    #print(soma)

def letras(texto):
    cont=0
    for i in range(len(texto)-1,-1,-1):
        if texto[i]!=" ":
            cont+=1
        print(texto[i],end=" ")
    print(cont)

#letras("E o cara vai endoidar?")

def num_unicos(lista):
    lista_nova=[]
    for i in lista:
        if i not in lista_nova:
            lista_nova.append(i)
    print(lista_nova)
    #num_unicos([10,12,12,31,4,4,5,31,6,7,6,8])