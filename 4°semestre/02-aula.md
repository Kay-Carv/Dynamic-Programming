### Situações em que recursão é preferível
1. Estruturas de dados hierárquicas
• Ex.: árvores, grafos, diretórios em um sistema de arquivos.
• Navegar ou processar cada nó de uma árvore é naturalmente recursivo.

```
def soma_arvore(no):
    if not no:
        return 0
    return no.valor + soma_arvore(no.esquerda)
soma_arvore(no.direita)
```

2. Problemas definidos matematicamente de forma recursiva
• Ex.: Fibonacci (com memoização), fatorial, sequências definidas por
relações de recorrência.
• O código recursivo reflete diretamente a definição matemática.

3. Divisão e conquista (Divide and Conquer)
• Ex.: mergesort, quicksort, pesquisa binária.
• Recursão permite quebrar um problema grande em subproblemas
menores até atingir casossimples.

4. Expressividade e legibilidade
• Recursão pode gerar código mais curto e mais próximo da lógica humana.
• Isso é útil em contextos didáticos ou quando a clareza é mais importante
que a micro-otimização.


## Quando evitarrecursão

1. Quando o problema exige muitas chamadas profundas (risco de stack
overflow).

2. Quando o mesmo problema pode ser resolvido iterativamente de
forma mais eficiente.

3. Quando a recursão não traz clareza ou simplificação ao código.

4. Cada vez que uma função é chamada, o computador guarda:
• variáveis locais, endereço de retorno, estado da execução, em uma estrutura
chamada pilha de chamadas (call stack).
5. Essa pilha tem tamanho limitado.
3. Se as funções chamarem outras funções continuamente (como em uma recursão sem
fim ou muito profunda), a pilha cresce até ficar cheia.
4. Quando não há mais espaço, ocorre o stack overflow → o programa trava ou encerra
com erro