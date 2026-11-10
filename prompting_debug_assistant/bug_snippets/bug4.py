def sum_items(items):
    total = 0
    for index in range(len(items) + 1):
        total += items[index]
    return total


def main():
    items = [10, 20, 30]
    result = sum_items(items)
    print(f"Sum: {result}")


if __name__ == "__main__":
    main()
