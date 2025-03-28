def main():
    print("1부터 n까지의 합을 구해봅시다")
    print()
    def sum_n(n):
        total = 0
        for i in range(1,n+1):
         total +=i
        return total
    n = int(input("n의 값을 입력하세요. =>"))
    print(f"합은 '{sum_n(n)}'입니다.")
if __name__ == "__main__":
    main()