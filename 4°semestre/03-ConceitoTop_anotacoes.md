## FIAP: Dynamic Programming - 06/03/2026
Prof° Francisco


Aula 4 - Top down e Bottom up

São estruturas de baseadas em árvore binária
Pensando no problema de Fibonacci


Conceito de arvore top-down (de cima pra baixo)

            6
        3       3
    1      2 1     2    
1   1   1   1    1    1   

Quero fib(5)
    ->preciso de fib(4) + fib(3)
        ->preciso de fib(3) + fib(2)
            -->....

Conceito de bottom-up (de baixo pra cima)

Sei que fib(0)


1      1     1   1     1   1
    1     2   1     2    
        3       3
            6



| Característica                | De cima para baixo (Top-down / Memoização)                | De baixo para cima (Bottom-up / Tabulação)                    |
| :---                          | :---                                                      | :---                                                          |
| **Estrutura**                 | Recursivo                                                 | Iterativo                                                     |
| **Ponto de partida**          | Problema principal                                        | Casos base / Menores subproblemas                             |
| **Armazenamento**             | Tabela de cache/pesquisa (preenchida sob demanda)         | Tabela (preenchida sistematicamente)                          |
| **Subproblemas resolvidos**   | Apenas os necessários                                     | Todos os subproblemas                                         |
| **Sobrecarga**                | Sobrecarga da pilha de chamadas recursivas                | Sobrecarga mínima (loops)                                     |
| **Implementação**             | Pode ser mais intuitivo para problemas recursivos         | Requer uma ordenação cuidadosa das soluções dos subproblemas  |