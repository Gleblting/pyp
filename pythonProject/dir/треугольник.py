def triangle_type(a, b, c):
    if a == b == c:
        return "Равносторонний"
    elif a == b or b == c or a == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"

print(triangle_type(3, 3, 3))  # Output: Равносторонний