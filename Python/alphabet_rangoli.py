#size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----


def print_rangoli(size):
    data = [chr(97 + el) for el in range(size)]
    items = list(range(size))
    items = items[:-1] + items[::-1]
    for el in items:
        temp = data[-(el + 1):]
        row = temp[::-1] + temp[1:]
        print("-".join(row).center(size * 4 - 3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
