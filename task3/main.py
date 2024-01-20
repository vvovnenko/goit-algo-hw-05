import timeit
from typing import Callable

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def read_file(filename):
    with open(f'data/{filename}', 'r', encoding='cp1251') as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)


if __name__ == '__main__':
    real_pattern = "структури даних"
    fake_pattern = "довбана русня"

    results = []
    for file in ['article_1.txt', 'article_2.txt']:
        text = read_file(file)
        for pattern in (real_pattern, fake_pattern):
            time = benchmark(boyer_moore_search, text, pattern)
            results.append((file, pattern, boyer_moore_search.__name__, time))
            time = benchmark(kmp_search, text, pattern)
            results.append((file, pattern, kmp_search.__name__, time))
            time = benchmark(rabin_karp_search, text, pattern)
            results.append((file, pattern, rabin_karp_search.__name__, time))

    print('\n')
    print('Загальні результати:')
    print(f"| {'Файл':<30} | {'Підрядок':<30} | {'Алгоритм':<30} | {'Час виконання, сек':<30} |")
    print(f"| :{'-'*29} | :{'-'*29} | :{'-'*29} | :{'-'*29} |")
    for result in results:
        print(f"| {result[0]:<30} | {result[1]:<30} | {result[2]:<30} | {result[3]:<30} |")

    grouped_results = dict()
    for file, pattern, alg, time in results:
        key = (file, pattern)
        value = (alg, time)
        if key not in grouped_results or grouped_results.get(key)[1] > time :
            grouped_results.update({key: (alg, time)})

    print('\n')
    print('Кращі результати для пар file, pattern:')

    print(f"| {'Файл':<30} | {'Підрядок':<30} | {'Алгоритм':<30} | {'Час виконання, сек':<30} |")
    print(f"| :{'-'*29} | :{'-'*29} | :{'-'*29} | :{'-'*29} |")
    for key, value in grouped_results.items():
        print(f"| {key[0]:<30} | {key[1]:<30} | {value[0]:<30} | {value[1]:<30} |")





