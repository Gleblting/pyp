def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

print(find_max([1, 3, 5, 7]))  # Output: 7

