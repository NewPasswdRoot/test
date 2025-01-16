a = int(input())
if a > 0:
	print("Положительное ", end="")
elif a < 0:
	print("Отрицательное ", end="")
if a == 0:
	print("Нулевое число ")
elif a%2 == 0:
	print("четное число ")
else:
	print("нечетное число")
