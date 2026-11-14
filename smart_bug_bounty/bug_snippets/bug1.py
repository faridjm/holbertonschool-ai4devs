def last_items(items: list[str], count: int) -> list[str]:
    if count < 0:
        raise ValueError("Count must be non-negative.")

    start_index = max(0, len(items) - count + 1)
    return items[start_index:]


if __name__ == "__main__":
    items = ["pen", "notebook", "ruler", "eraser"]
    print(last_items(items, 2))
