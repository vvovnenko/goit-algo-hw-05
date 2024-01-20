
## Загальні результати тестування
    
| Файл                           | Підрядок                       | Алгоритм                       | Час виконання, сек             |
| :----------------------------- | :----------------------------- | :----------------------------- | :----------------------------- |
| article_1.txt                  | структури даних                | boyer_moore_search             | 0.00042359199142083526         |
| article_1.txt                  | структури даних                | kmp_search                     | 0.001118162996135652           |
| article_1.txt                  | структури даних                | rabin_karp_search              | 0.002013810008065775           |
| article_1.txt                  | довбана русня                  | boyer_moore_search             | 0.006856050982605666           |
| article_1.txt                  | довбана русня                  | kmp_search                     | 0.021370775008108467           |
| article_1.txt                  | довбана русня                  | rabin_karp_search              | 0.06541892001405358            |
| article_2.txt                  | структури даних                | boyer_moore_search             | 0.00010191102046519518         |
| article_2.txt                  | структури даних                | kmp_search                     | 0.00011932398774661124         |
| article_2.txt                  | структури даних                | rabin_karp_search              | 0.0002980190038215369          |
| article_2.txt                  | довбана русня                  | boyer_moore_search             | 0.016646770993247628           |
| article_2.txt                  | довбана русня                  | kmp_search                     | 0.042593877005856484           |
| article_2.txt                  | довбана русня                  | rabin_karp_search              | 0.09528484198381193            |

## Кращі результати для пар Файл, Підрядок:

| Файл                           | Підрядок                       | Алгоритм                       | Час виконання, сек             |
| :----------------------------- | :----------------------------- | :----------------------------- | :----------------------------- |
| article_1.txt                  | структури даних                | boyer_moore_search             | 0.00042359199142083526         |
| article_1.txt                  | довбана русня                  | boyer_moore_search             | 0.006856050982605666           |
| article_2.txt                  | структури даних                | boyer_moore_search             | 0.00010191102046519518         |
| article_2.txt                  | довбана русня                  | boyer_moore_search             | 0.016646770993247628           |

## Висновки
Результати тестування показали що алгоритм пошуку Боєра-Мура найбільш придатний для використання,
так як час виконання пошуку цим алгоритмом показав найменший час як для кожного тексту окремо так і в цілому