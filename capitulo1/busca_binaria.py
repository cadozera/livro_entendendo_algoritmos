class BuscaBinaria:
    """
    Busca interativa ela executa o processo do inicio ao fim sem chamar a propria funcao para execucao
    """

    def busca_interativa(self, lista, item):
        # Baixo e alto acompanham a parte da listaque voce esta procurando.
        baixo = 0
        alto = len(lista) - 1
        tentativas = 0

        # Enquanto ainda nao conseguiu chegar a um unico elemento.
        while baixo <= alto:
            tentativas += 1
            # ... verificando o elemento do meio
            meio = (baixo + alto) // 2
            chute = lista[meio]
            # Encontrou o item.
            if chute == item:
                return f"Quantidade de tentativas {tentativas}..."
            # Chute muito alto.
            if chute > item:
                alto = meio - 1
            # Chute muito baixo.
            else:
                baixo = meio + 1

        # Quando o item nao existir...
        return None

    """
        Busca recursiva ela executa o processo em passos...
        Ela executa o primeiro passo,
        Se encontrar o resultado retorna o dado,
        Senao retorna para o inicio da funcao com novos argumentos, chamando ela mesma para execucao...
    """

    def busca_recursiva(self, lista, baixo, alto, item):
        # Check base case
        if alto >= baixo:

            meio = (alto + baixo) // 2
            chute = lista[meio]

            # If element is present at the meiodle itself
            if chute == item:
                return meio

                # If element is smaller than meio, then it can only
            # be present in left subarray
            elif chute > item:
                return self.busca_recursiva(lista, baixo, meio - 1, item)

                # Else the element can only be present in right subarray
            else:
                return self.busca_recursiva(lista, meio + 1, alto, item)

        else:
            # Element is not present in the array
            return None

    """
    A principal diferenca entre elas esta na performance do algoritmo, que no caso da iterativa e mais rapido pois,
    nao precisa chamar novamente a mesma funcao e mandar novos argumentos, porem entao porque usar a busca recursiva?
    Ela deixa o codigo mais simples e muito menor dependendo do caso.
    """


if __name__ == "__main__":
    # Inicializando a classe...
    bs = BuscaBinaria()

    my_list = [1, 3, 5, 7, 9]
    mylist2 = [i + 1 for i in range(128)]

    print(bs.busca_interativa(mylist2, 52))  # => 1
    # 'None' means nil in Python. We use to indicate that the item wasn't found.
    print(bs.busca_interativa(my_list, -1))  # => None
