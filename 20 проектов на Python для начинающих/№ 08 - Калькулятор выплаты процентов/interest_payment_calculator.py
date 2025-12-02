def main():
	print("Это калькулятор ежемесячных платежей по кредиту")
	print("")

	principal = float(input("Введите сумму кредита: "))
	apr = float(input("Введите годовую процентную ставку: "))
	years = float(input("Введите срок кредита в годах: "))

	monthly_interest_rate = apr / 1200
	amount_of_months = years * 12
	monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

	# Если хотите выводить округлённо (до 2 знаков):
	print("Ежемесячный платёж по этому кредиту составляет: %.2f" % monthly_payment)

	# # Если хотите выводить всё число полностью (без округления):
	# print("Ежемесячный платёж по этому кредиту составляет:", monthly_payment)

main()