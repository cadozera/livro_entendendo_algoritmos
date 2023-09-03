# Busca Binaria

## Busca Iterativa

### Pontos fortes
- A iteração pode ser usada para executar repetidamente um conjunto de instruções sem a sobrecarga de chamadas de função e sem usar memória de pilha.
- A iteração é mais rápida e eficiente que a recursão.
- É mais fácil otimizar códigos iterativos e eles geralmente possuem complexidade de tempo polinomial.
- Eles são usados para iterar sobre os elementos presentes em estruturas de dados como array, conjunto, mapa, etc.
- Se a contagem de iterações for conhecida, podemos usar loops for; caso contrário, podemos usar loops while, que terminam quando a condição de controle se torna falsa.

### Pontos fracos
- Nos loops, podemos ir apenas em uma direção, ou seja, não podemos ir ou transferir dados do estado atual para o estado anterior que já foi executado.
- É difícil percorrer árvores/gráficos usando loops.
- Apenas informações limitadas podem ser passadas de uma iteração para outra, enquanto na recursão podemos passar quantos parâmetros forem necessários.

## Busca Recursiva

### Pontos fortes
- É mais fácil codificar a solução usando recursão quando a solução do problema atual depende da solução de problemas menores semelhantes.
```
  - fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
  - fatorial(n) = n * fatorial(n-1)
```
- Os códigos recursivos são menores e mais fáceis de entender.
- Podemos passar informações para o próximo estado na forma de parâmetros e retornar informações para o estado anterior na forma de valor de retorno.
- É muito mais fácil realizar operações em árvores e gráficos usando recursão.

### Pontos fracos
- A simplicidade da recursão custa tempo e eficiência de espaço.
- É muito mais lento que a iteração devido à sobrecarga de chamadas de função e à mudança de controle de uma função para outra.
- Requer memória extra na pilha para cada chamada recursiva. Essa memória é desalocada quando a execução da função termina.
- É difícil otimizar um código recursivo e eles geralmente apresentam maior complexidade de tempo do que códigos iterativos devido à sobreposição de subproblemas.


