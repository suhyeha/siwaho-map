
D_sungjuk = {}



def f1():
    for subject in ["국어", "영어", "수학"]:
        score = int(input(f"{subject} 점수는? "))
        D_sungjuk[subject] = score



def f2():
    if len(D_sungjuk) == 0:
        return 0
    return sum(D_sungjuk.values()) / len(D_sungjuk)



def f3():
    print("\n성적계산 :")
    for subject, score in D_sungjuk.items():
        print(f"{subject} : {score}점")
    avg = f2()
    print("평균점수 : %.2f 점" % avg)


# 메인 메뉴
while True:
    menu = int(input("\n성적을 입력하세요.\n1) 점수입력 2) 점수 수정 3) 종료(0입력) : "))

    if menu == 1:
        f1()

    elif menu == 2:
        subject = input("수정할 과목은? ")
        if subject in D_sungjuk:
            new_score = int(input("몇 점으로 수정할까요? "))
            D_sungjuk[subject] = new_score
        else:
            print("해당 과목이 없습니다.")

    elif menu == 0 or menu == 3:
        f3()
        break
    else:
        print("잘못 입력하셨습니다.")
