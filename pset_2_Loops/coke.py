def main():
    cokePrice = 50

    coins = [5, 10, 25]

    while cokePrice > 0:
        print(f"Amount Due: {cokePrice}")

        insertCoin = int(input("Insert Coin: "))

        if insertCoin in coins and insertCoin < cokePrice:
            cokePrice -= insertCoin
        elif insertCoin in coins and insertCoin >= cokePrice:
            cokePrice = insertCoin - cokePrice
            print(f"Change Owed: {cokePrice}")
            break


if __name__ == "__main__":
    main()
