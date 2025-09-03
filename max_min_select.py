from typing import List, Tuple

def max_min_select(array: List[int]) -> Tuple[int, int]:
    return _max_min_select(array, 0, len(array) - 1)

def _max_min_select(array: List[int], esq: int, dir: int) -> Tuple[int, int]:
    if len(array) == 0:
        raise ValueError("O array está vazio.")

    if esq == dir:
        return (array[esq], array[dir])
    
    if dir == esq + 1:
        if array[esq] < array[dir]:
            return (array[esq], array[dir])
        else:
            return (array[dir], array[esq])
    
    meio = (esq + dir) // 2
    esq_min, esq_max = _max_min_select(array, esq, meio)
    dir_min, dir_max = _max_min_select(array, meio + 1, dir)
    
    min_geral = min(esq_min, dir_min)
    max_geral = max(esq_max, dir_max)
    
    return (min_geral, max_geral)