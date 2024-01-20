def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    if arr[-1] < x:
        return 0, None

    upper_bound = arr[-1]
    iter_count = 0

    while low <= high:
        iter_count += 1

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            upper_bound = mid
            break

    # якщо елемент не знайдений
    return iter_count, upper_bound
