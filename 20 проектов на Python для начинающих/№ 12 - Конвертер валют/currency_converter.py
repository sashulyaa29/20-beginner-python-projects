def main():
    print("Эта программа конвертирует доллары США в фунты стерлингов")
    print()

    dollars = eval(input("Введите сумму в долларах: "))
    pounds = convert_to_pounds(dollars)
    print("Это", pounds, "фунтов.")

convert_to_pounds = lambda dollars: dollars * 0.82

main()