def c2f(t_c):
    return((t_c)*9/5+32)
def main():
    temp_c = int(input("변환할 온도를 입력하세요 =>"))
    temp_f = c2f(temp_c)
    print(f"{temp_c}C => {temp_f}F")
if __name__ == "__main__":
    main()