from max_min_select import max_min_select

def main():
    array = [2, 7, 4, 5, 1, 8, 6, -31]

    min, max = max_min_select(array)
    print(f"Array: {array}")
    print(f"Menor valor: {min}")
    print(f"Maior valor: {max}")

if __name__ == "__main__":
    main()