def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total


def main():
    prices = [12.5, 20.0, 7.5]
    total = calculate_total(prices)
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
