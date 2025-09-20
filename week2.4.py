def vending_machine():
    total_point = 0  # 누적 포인트

    while True:
        money = int(input("투입한 돈 : "))
        if money == 0:
            print("감사합니다. 안녕히가세요")
            break

        price = int(input("물건값 : "))
        change = money - price
        print(f"거스름돈 : \₩{change} 원")

        # 동전 단위별 계산
        coins = {}
        coins[500] = change // 500
        change %= 500
        coins[100] = change // 100
        change %= 100
        coins[50] = change // 50
        change %= 50
        coins[10] = change // 10

        total_coins = sum(coins.values())

        if total_coins >= 5:
            choice = input("동전의 개수가 많습니다. 포인트로 적립해 드릴까요?(Y or N)").strip().lower()
            if choice == 'y':
                total_point += money - price
                print(f"{money - price} 포인트가 적립되었습니다. 현재까지의 누적포인트 : {total_point}")
            else:
                for coin, cnt in coins.items():
                    if cnt > 0:
                        print(f"{coin}원 동전의 개수 : {cnt}")
        else:
            for coin, cnt in coins.items():
                if cnt > 0:
                    print(f"{coin}원 동전의 개수 : {cnt}")


# 실행
vending_machine()
