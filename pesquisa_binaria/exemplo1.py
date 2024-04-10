''' A função pesquisa_binaria pega um array ordenado e um item. Se o item  está no array, 
a função retorna a sua posição. Dessa maneira, você é capaz de  saber por qual ponto do array 
deve continuar procurando. No começo, o  código do array segue assim'''
def pesquisa_binaria(lista, item):
    baixo = 0 #1
    alto = len(lista) - 1 # 1
# a cada tentativa, você testa para o elemento central.
    while baixo <= alto: # 2
        meio = (baixo + alto) / 2   # 3      #meio será arredondado para baixo automaticamente pelo Python se (baixo + alto) não for par.
        chute = lista[meio]
#Se o chute for muito baixo, você atualizará a varíavel baixo proporcionalmente.
        if chute == item: # 4
            return meio
        if chute > item: # 5
            alto = meio - 1
        else: # 6
            baixo = meio + 1
    return None # 7
minha_lista = [1, 3, 5, 7, 9] # 8
print(pesquisa_binaria(minha_lista, 3)) # 1 --> 9 
print(pesquisa_binaria(minha_lista, -1)) # None --> 10
#E se o chute for muito alto, você autalizará a varíavel alto. 

#1 - baixo alto acompanha a parte da lista que você está procurando
#2 - enquanto ainda não conseguiu chegar a um único elemento
#3 - verificar o elemento centar
#4 - acha o item
#5 - o chute foi muito alto
#6 - o chute foi muito baixo
#7 - o item não existe
#8 - vamos testá-lo
#9 - lembre, se as listas começam no 0. O próximo endereço tem índice 1
#10 - "None" significa nulo em Python. Ele indica que o item não foi encontrado.

