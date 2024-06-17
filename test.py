n = int(input("入力したい回数を入力してください: "))
last_value = ""
for i in range(n):
    last_value = input(f"{i + 1} 番目の値を入力してください: ")
print(f"最後に入力された値は: {last_value}")
