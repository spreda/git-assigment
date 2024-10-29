def main(n):
    numbers = range(1, n+1)
    print("Среднее чисел от 1 до {n}:", sum(numbers)/len(numbers))

if __name__ == '__main__':
    main(10)