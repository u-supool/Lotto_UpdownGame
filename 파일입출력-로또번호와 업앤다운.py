import random

# 로또 
# num = [] 함수 안에 없으면 계속 초기화 안 돼서 함수 안에서 계속 빈 할당 새로 하게끔 해야됨


# 업앤다운 -  닉네임
name_easy = []
name_normal = []
name_hard = []

# 업앤다운 기록 - 이름:횟수 딕셔너리
game_history_easy = {}  #{'수현': 7, '지민': 6}
game_history_normal = {}
game_history_hard = {}

# 업앤다운 리더보드 - 오름차순 정렬된 리스트
leaderboard_easy = []   #['지민', '수현']
leaderboard_normal = []
leaderboard_hard = []


# 메인메뉴 안내문 함수
def main_menu():
    print("1. 모드 선택")
    print("2. 랭킹/이력 보기")
    print("3. 프로그램 종료")
    select = int(input("메뉴를 선택해주세요: "))
    print()
    return select


# 게임모드 선택 함수
def game_mode():
    print("1. 로또 번호 추천")
    print("2. 업앤다운 게임")
    mode_select = int(input("모드를 선택해주세요: "))
    print()
    return mode_select


# o잘못된 입력 함수
def wrong_input():
    print("잘못된 입력입니다!")
    print()


# o로또 자동 함수
def lotto_auto():
    
    num = [] # 안에서 써야 계속 초기화 함수로 바꿀 땐 밖에서 계속 빈 할당 못 하기 때문..
    
    print("다음의 번호를 추천합니다:", end=' ')

    while True:
        a = random.randint(1,45)

        if a not in num:
            num.append(a)

        if len(num) == 6:
            break

    num.sort()

    for j in range(6):
        print(num[j], end=' ')

    num_history.append(num)
    save_lotto(num)
    print()


# o로또 수동 함수
def lotto_manual(n):

    num = [] # 안에서 써야 계속 초기화 함수로 바꿀 땐 밖에서 계속 빈 할당 못 하기 때문..

    while True:
        pick = int(input("1부터 45까지 중 하나를 고르십시오: "))

        if pick in num:
            print("중복된 숫자입니다!")

        elif 45 < pick or pick < 1:
            print("범위 밖의 숫자입니다!")

        else:
            num.append(pick)

            if len(num) == n:
                break

    while len(num) < 6:
        a = random.randint(1,45)

        if a not in num:
            num.append(a)

    num.sort()

    print("다음의 번호를 추천합니다: ", end=' ')

    for j in range(6):
        print(num[j], end=' ')

    num_history.append(num)
    save_lotto(num)
    print()


# o로또 실행 함수
def lotto_game():

    while True:
        select = input("로또 번호 추천: 자동 또는 수동을 입력하십시오: ")
        print()

        # 자동
        if select == "자동":
            lotto_auto()
            break

        # 수동
        elif select == "수동":

            while True:
                g = int(input("수동으로 뽑을 번호의 개수를 입력하십시오: "))

                if 6 < g or g < 1:
                    wrong_input()

                else:
                    break

            lotto_manual(g)
            break

        # 잘못된 입력
        else:
            wrong_input()


# o업앤다운 난이도 선택 출력문 함수
def difficulty_select():
    print("1. 쉬움")
    print("2. 보통")
    print("3. 어려움")
    difficulty = int(input("난이도를 선택해주세요: "))
    print()
    return difficulty


# o난이도별 이름 입력 함수 - 중복되지 않는 이름 기록하고 값 나오게 함.
def name_input(name_difficulty):

    while True:
        name = input("닉네임을 입력해주세요: ")
        print()

        if name in name_difficulty:
            print("중복된 닉네임입니다!")
            print()

        else:
            name_difficulty.append(name)
            break

    return name


# o난이도별 업앤다운 게임 함수 - 업앤다운 게임 실행 후, 걸린 횟수 값 나오게 함.
def game_pick(n):

    target = random.randint(1, n)
    try_count = 0

    while True:
        pick = int(input(f"1부터 {n}까지 중 하나를 고르세요: "))
        try_count += 1

        if target < pick:
            print("다운!")

        elif target > pick:
            print("업!")

        else:
            print(f"정답입니다! {try_count}회 시도 만에 성공하셨습니다!")
            break

    return try_count


# o게임 기록 및 정렬 함수
def history(name, try_count, history_difficulty, leaderboard_difficulty, file_name):

    # 게임 기록 딕셔너리 저장
    history_difficulty[name] = try_count

    # 리더보드 리스트 오름차순 정렬해서 이름만 저장
    if len(leaderboard_difficulty) == 0:
        leaderboard_difficulty.append(name)

    else:
        for i in range(0, len(leaderboard_difficulty)):

            if try_count < history_difficulty[leaderboard_difficulty[i]]:
                leaderboard_difficulty.insert(i, name)
                break

            # 끝자리까지 다 비교했는데도 작지 않다면, 가장 큰 횟수인거니까 그냥 append 로 끝에 추가
            elif i == len(leaderboard_difficulty) - 1:
                leaderboard_difficulty.append(name)
    save_ranking(file_name, name, try_count)       

    print()


# o업앤다운 실행 함수
def updown_game():

    while True:
        difficulty = difficulty_select()

        # 쉬움
        if difficulty == 1:

            name_difficulty = name_easy
            name = name_input(name_difficulty)

            n = 50
            try_count = game_pick(n)

            history_difficulty = game_history_easy
            leaderboard_difficulty = leaderboard_easy

            history(name, try_count, history_difficulty, leaderboard_difficulty, "ranking_easy.txt")
            break

        # 보통
        elif difficulty == 2:

            name_difficulty = name_normal
            name = name_input(name_difficulty)

            n = 100
            try_count = game_pick(n)

            history_difficulty = game_history_normal
            leaderboard_difficulty = leaderboard_normal

            history(name, try_count, history_difficulty, leaderboard_difficulty, "ranking_normal.txt")
            break

        # 어려움
        elif difficulty == 3:

            name_difficulty = name_hard
            name = name_input(name_difficulty)

            n = 300
            try_count = game_pick(n)

            history_difficulty = game_history_hard
            leaderboard_difficulty = leaderboard_hard

            history(name, try_count, history_difficulty, leaderboard_difficulty, "ranking_hard.txt")
            break

        # 잘못된 입력
        else:
            wrong_input()


# 기록보기 메뉴 출력 함수
def menu_history():
    print("1. 로또 번호 이력")
    print("2. 업앤다운 랭킹")
    history_select = int(input("조회할 항목을 선택해주세요: "))
    print()
    return history_select


# 로또 이력 보기 함수
def history_lotto(k):

    if k > len(num_history):
        print("조회할 기록 수가 부족합니다!")
        print()
        return

    else:
        print(f"최근 {k}회 번호 추천 기록")

        for i in range(-1, -k - 1, -1):
            print(f"최근 {-i}회: ", end="")

            for j in range(6):
                print(num_history[i][j], end=" ")

            print()

        print()


# 난이도별 업앤다운 랭킹 보기 함수 - 몇 순위까지 볼지 난이도별로 받아서 있는 기록까지만 rank 출력
def rank_input(난이도, leaderboard_difficulty):

    rank = int(input("몇 순위까지 보시겠습니까?: "))
    print()
    print(f"<{난이도} 난이도 랭킹>")

    if len(leaderboard_difficulty) == 0:
        print("조회할 랭킹이 없습니다!")

    # 더 큰 수의 기록 요구할 때 그냥 있는 것 까지 보여주기
    elif rank > len(leaderboard_difficulty):
        rank = len(leaderboard_difficulty)

    return rank


# 리더보드 출력 함수
def leaderboard_print(rank, leaderboard_difficulty, history_difficulty):

    if len(leaderboard_difficulty) != 0:

        for i in range(0, rank):
            print(f"{i+1}위: {leaderboard_difficulty[i]} - {history_difficulty[leaderboard_difficulty[i]]}회")

    print()


# 업앤다운 랭킹 실행 함수
def rank_game():

    while True:
        difficulty = difficulty_select()

        # 랭킹 - 쉬움
        if difficulty == 1:

            난이도 = "쉬움"
            leaderboard_difficulty = leaderboard_easy
            history_difficulty = game_history_easy

            rank = rank_input(난이도, leaderboard_difficulty)
            leaderboard_print(rank, leaderboard_difficulty, history_difficulty)
            break

        # 랭킹 - 보통
        elif difficulty == 2:

            난이도 = "보통"
            leaderboard_difficulty = leaderboard_normal
            history_difficulty = game_history_normal

            rank = rank_input(난이도, leaderboard_difficulty)
            leaderboard_print(rank, leaderboard_difficulty, history_difficulty)
            break

        # 랭킹 - 어려움
        elif difficulty == 3:

            난이도 = "어려움"
            leaderboard_difficulty = leaderboard_hard
            history_difficulty = game_history_hard

            rank = rank_input(난이도, leaderboard_difficulty)
            leaderboard_print(rank, leaderboard_difficulty, history_difficulty)
            break

        else:
            wrong_input()

# 메인 함수
def main():
    
    while True:

        # 메인메뉴 함수
        select = main_menu()

        if select == 1:

            while True:

                

                # 게임모드 함수
                mode_select = game_mode()

                # 로또 번호 추천
                if mode_select == 1:

                    lotto_game()
                    
                    
                    break

                # 업앤다운 게임
                elif mode_select == 2:

                    updown_game()
                    break

                # 게임 모드 선택 잘못된 번호
                else:
                    wrong_input()
                    break


        # 랭킹/이력 보기
        elif select == 2:

            while True:

                # 히스토리 메뉴 출력 함수
                history_select = menu_history()

                # 2-1. 로또 이력
                if history_select == 1:
                    k = int(input("조회할 최근 기록 수를 입력하십시오: "))
                    print()

                    history_lotto(k)
                    break

                # 2-2. 업앤다운 랭킹
                elif history_select == 2:
                    rank_game()
                    break

                # 랭킹/이력 보기 잘못된 번호
                else:
                    wrong_input()

                break

        # 프로그램 종료
        elif select == 3:
            print("프로그램을 종료합니다.")
            break

        else:
            wrong_input()

# 로또 번호 저장
def save_lotto(num):
    line = ""

    for i in range(len(num)):
        line += str(num[i])

        if i < len(num) - 1:
            line += ","

    with open("lotto_history.txt", "a", encoding="utf-8") as file:
        file.write(line + "\n")

# 로또 번호 불러오기
def load_lotto_history():
    lotto_history = []

    try:
        with open("lotto_history.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(",")
            lotto = []

            for number in data:
                lotto.append(int(number))

            lotto_history.append(lotto)

    except FileNotFoundError:
        print("아직 저장된 로또 이력이 없습니다.")

    return lotto_history


# 업앤다운 랭킹 저장
def save_ranking(file_name, name, try_count):

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(name + "," + str(try_count) + "\n")
# 수현,5
# 지민,3

# 업앤다운 랭킹 불러오기
def load_ranking(file_name, name_difficulty, history_difficulty, leaderboard_difficulty):

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:

            data = line.strip().split(",")

            name = data[0]
            try_count = int(data[1])

            name_difficulty.append(name)

            history_difficulty[name] = try_count

            if len(leaderboard_difficulty) == 0:
                leaderboard_difficulty.append(name)

            else:
                for i in range(0, len(leaderboard_difficulty)):

                    if try_count < history_difficulty[leaderboard_difficulty[i]]:
                        leaderboard_difficulty.insert(i, name)
                        break

                    elif i == len(leaderboard_difficulty) - 1:
                        leaderboard_difficulty.append(name)

    except FileNotFoundError:
        return

num_history = load_lotto_history()

load_ranking("ranking_easy.txt", name_easy, game_history_easy, leaderboard_easy)
load_ranking("ranking_normal.txt", name_normal, game_history_normal, leaderboard_normal)
load_ranking("ranking_hard.txt", name_hard, game_history_hard, leaderboard_hard)

# 실행
main()