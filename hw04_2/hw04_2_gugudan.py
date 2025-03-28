def gugudan(dan):
    for i in range(9):
         print(dan * (i + 1))

def main():
    numbers = int(input("몇 단을 출력하나요? =>"))
    gugu = gugudan(numbers)
    print(gugu)
if __name__ == "__main__":
    main()
