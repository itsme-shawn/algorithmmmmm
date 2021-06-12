import random


class Character:
    def __init__(self, speed):
        self.speed = speed


class Item:
    def __init__(self, item_type, speed_change):
        self.item_type = item_type
        self.speed_change = speed_change


class Player:
    def __init__(self, name):
        self.name = name  # 플레이어의 이름 저장
        self.speed = 0  # 플레이어의 속도: 선택한 character의 속도!
        self.round_speed = 0  # 아이템 적용 후 플레이어의 속도
        self.play_records = []  # 플레이어의 경기 기록: 라운드별 주행 시간[초]

    def add_play_record(self, record_in_hr):
        """
        - 플레이어의 경기 기록을 받아 저장합니다.
        - 시간 단위로 들어온 기록을 초 단위의 기록으로 변환해 저장해야합니다.
        - Game 클래스의 play_round() 함수에서 호출됩니다.
        """
        # TODO : 플레이어의 경기 기록을 초 단위로 변환해 저장해주세요.
        self.play_records.append(record_in_hr * 3600)
        return record_in_hr * 3600


class Game:
    def __init__(self):
        self.num_rounds = 3
        self.player_list = []  # 플레이어의 목록. 이후에 set_players를 이용해 수정
        self.item_list = []  # 아이템의 목록. 이후에 set_item_list를 이용해 수정
        self.character_list = []

    def set_players(self):
        """
        - 5명의 플레이어를 생성하는 함수입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        # TODO : 사용자로부터 플레이어의 이름을 입력받아 Player 객체를 생성하고 플레이어 목록(self.player_list)에 추가해주세요.
        print("*** 게임 접속 ***")
        for i in range(5):
            while True:
                name = input("Player " + str(i + 1) + " 의 이름을 입력해주세요: ")
                if name:
                    break
                else:
                    print("잘못된 입력값입니다. 다시 입력해주세요")
            self.player_list.append(Player(name))

    def start_game(self):
        """
        - 게임 규칙의 [게임 시작 전] 부분을 담당하는 함수입니다.
        - 3 종류의 캐릭터와 2 종류의 아이템을 초기화하고, 사용자의 입력을 받아 각 플레이어의 속도를 설정합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        # TODO (1): 범위 내의 속도를 가진 세 종류의 캐릭터를 생성해주세요.
        for _ in range(3):
            character = Character(random.randint(100, 180))
            self.character_list.append(character)

        # TODO (2): 사용자의 입력을 받아 플레이어의 고유 속도를 설정하고, 선택된 캐릭터의 속도를 출력해주세요.
        print("*** 캐릭터 선택 ***")
        for i in range(5):
            player = self.player_list[i]
            while True:
                characterNumber = int(
                    input(player.name + "의 캐릭터 선택 차례입니다. 1, 2, 3 중 하나의 값을 입력해주세요. ")
                )
                if characterNumber == 1 or characterNumber == 2 or characterNumber == 3:
                    break
                else:
                    print("잘못된 입력값입니다. 1, 2, 3 중 하나의 값을 입력해주세요.")
            player.speed = self.character_list[characterNumber - 1].speed
            print(f"{player.name}의 고유 속도는 시속 {player.speed}입니다.")

        # TODO (3): 두 종류의 아이템을 생성해 아이템 목록(self.item_list)에 추가해주세요.
        itemBanana = Item("banana_slip", random.randint(-40, -20))
        itemBooster = Item("booster", random.randint(30, 60))
        self.item_list.extend([itemBanana, itemBooster])

    def play_round(self):
        """
        - 게임 규칙의 [라운드 시작 전], [라운드 진행], [라운드 종료 후] 부분을 담당하는 함수입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        #### [라운드 시작 전]
        # TODO (1) - 1: 트랙의 길이를 결정해 변수에 저장하고, 출력해주세요.
        trackLength = random.randint(5, 30)
        print(f"이번 라운드의 트랙 길이는 {trackLength}km 입니다.")

        # TODO (1) - 2: 5명의 플레이어에게 아이템을 랜덤하게 적용시키고, 적용된 아이템과 적용 후 플레이어의 속도를 출력해주세요.
        print("[아이템 적용]")
        for i in range(5):
            playerItem = random.choice(self.item_list)
            player = self.player_list[i]
            player.round_speed = player.speed + playerItem.speed_change
            if playerItem.item_type == "banana_slip":
                print(
                    f"Player {player.name} 는 banana_slip 때문에 시속 {player.round_speed} 로 이번 트랙을 질주합니다! 화이팅 ㅠㅠ"
                )
            else:
                print(
                    f"Player {player.name} 는 booster 덕분에 시속 {player.round_speed} 로 이번 트랙을 질주합니다! 화이팅 ~~"
                )

        #### [라운드 진행] , [라운드 종료 후]
        # TODO (2) : 플레이어가 트랙을 도는 데 걸린 시간을 초 단위로 출력하고, 플레이어의 경기 기록에 추가해주세요. Player 클래스의 함수를 사용해야합니다.
        print("[경기 진행중...]")
        print("[라운드 결과]")
        for i in range(5):
            player = self.player_list[i]
            playerRecord = player.add_play_record(trackLength / player.round_speed)
            print(f"Player {player.name}의 주행시간: {playerRecord}")

    def game_result(self):
        """
        - 게임 규칙의 [게임 종료 후] 부분을 담당하는 함수입니다.
        - 1, 2, 3순위까지 플레이어의 이름과 합산기록을 출력합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        - 파이썬의 sorted() 함수와 sort() 함수를 잘 이용하시면 편합니다. sorting key 등을 검색해보시기를 추천합니다.
        """
        # TODO : 사용자를 합산 기록 순으로 정렬하고, 상위 3명의 경기 기록 합산을 출력합니다.
        print("*** 명예의 전당 ***")
        sumList = {}
        for i in range(5):
            player = self.player_list[i]
            sumList[i] = player.play_records[0] + player.play_records[1] + player.play_records[2]
        AfterSort = sorted(sumList.items(), key=lambda x: x[1])
        for i in range(3):
            print(
                f"{i+1}위: {self.player_list[AfterSort[i][0]].name} (총 주행 시간: {AfterSort[i][1]} 초)"
            )

    def game(self):
        """
        - 게임 운영을 위한 함수입니다.
        - 별도의 코드 작성이 필요 없습니다.
        """
        self.set_players()
        self.start_game()

        print("******************* 게임 시작 *******************")
        for i in range(3):
            print(f"============= ROUND {i+1} =============")
            self.play_round()
            print()
        print()

        print("******************* 명예의 전당 *******************")
        self.game_result()


if __name__ == "__main__":
    """
    - 코드를 실행하는 부분입니다.
    - 역시 별도의 코드 작성이 필요 없습니다.
    """
    game = Game()
    game.game()
