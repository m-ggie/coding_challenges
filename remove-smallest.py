def remove_smallest(numbers):
    if numbers:
        temp = numbers[0]
        for n in numbers:
            if n < temp:
                temp = n
        numbers.remove(temp)
    return numbers