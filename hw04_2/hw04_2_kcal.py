def main():
    print("마라탕에 들어간 재료를 얼마나 넣었는지 입력하세요.(g 기준)")
    print()
    calories = {"청경채":11/100, "팽이버섯":20/100 ,"배추":17/100 ,"숙주":12/100 ,"당면":375/100, "유부":363/100 ,"마라탕소스":260/100 }

    ingredients = ["청경채","팽이버섯","배추","숙주","당면","유부","마라탕소스"]
    weight = []
    for item in ingredients:
     weight.append(int(input(f"{item}의 무게를 입력하세요 =>")))

    total_calories = 0
    for i in range(len(ingredients)):
        total_calories += weight[i] * calories[ingredients[i]]

    print("-"*30)
    print(f"마라탕의 칼로리는 {total_calories}kcal이다")
if __name__ == "__main__":
    main()