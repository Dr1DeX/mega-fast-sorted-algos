# mega-fast-sorted-algos
## Самый быстрый алгоритм в мире?

### Сложно сказать, зависит какой класс задач должен решать алгоритм и чем готовы жертвовать(память или время)

----

## Задачу можно разделить на 2 основные категории - это `CPU-bound` и `I/O-bound`
### Так же, например, можно разделить для каждой основной категории, ещё на 2 абстрактные подкатегории - `Online` и `Offline алгоритм`
### Если класс задач `CPU-bound` это один класс алгоритмов, если нужно что-то гонять по сети(`I/O-bound`) то, другой класс алгоритмов

-------

## Для примера возьмем класс задач `I/O-bound/Offline` , с этой задачей справляется алгоритм сортировки слиянием
### Ее асимптотическая сложность по времени - `O(N*logn)`, а по памяти - `O(n)`, если готовы пожертвовать памятью то такое решение сойдет, однако если нужно в real-time проводить какие-то вычисления с большими данными то, тут возникнут сложности

## Та же задача, но я взял другой алгоритм `LSD-сортировка(Radix)`-побитовая сортировка, на бенчмарке в 10000000 элементов он показал себя чуть хуже, чем сортировка слиянием, однако этот класс алгоритмом хорошо работает, если нужно распараллелить вычисления, если данных будет очень-приочень много, то он справится лучше, чем любая другая сортировка 
### Сложность алгоритма по времени - ``O(d * (n + b))``, где `d`-кол-во цифр, `n`-кол-во элементов, `b`-основа используемой системы счисления(10)

### Ответ на вопрос из задания: сортировка слиянием, потому что она быстрая(быстрее и стабильнее пока что ничего ,к сожалению, не придумали), если линейная сложность по памяти не пугает и при условии, что класс задачи не `Online` и не `CPU`, то решение будет соответствовать заданным критериям, иначе уточняем требования

## Bencmark 10000000 elem:

    
    Func radix_sort executor to start
    Func radix_sort complete:
    35.1349664000154
    Func merge_sort executor to start
    Func merge_sort complete:
    33.34970500000054

_______

## Developer: Dr1DeX
