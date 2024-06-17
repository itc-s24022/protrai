#s24022
import random

def main():
    print("Hello")

def omikuji():
    kuji = ["大吉", "中吉", "吉", "凶"]
    return random.choice(kuji)

if __name__ == "__main__":
    main()
    kekka = omikuji()
    print("結果は", kekka, "です。")
