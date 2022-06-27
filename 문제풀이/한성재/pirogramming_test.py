# Skeleton Code
from multiprocessing.connection import answer_challenge
import string
import random


class Player:
    def __init__(self, name, hp, damage, correct_alp):
        self.name = name      # 이름
        self.hp = hp          # 생명력
        self.damage = damage  # 데미지
        self.correct_alp = 0  # 알파벳 맞춘 횟수

    def introduce(self):
        print("*************")
        print("이름:", self.name)
        print("생명력:", self.hp)
        print("데미지:", self.damage)
        print("*************")


class Game:
    def __init__(self):
        self.player = []  # 캐릭터의 목록. start_game()에서 생성
        self.user_character = ""  # 사용자가 선택한 캐릭터
        self.remain_alp = list(string.ascii_uppercase)  # 남은 알파벳
        self.cur_string = ["_"] * 10  # 현재까지의 글자상태를 저장
        self.answer_string = ""  # 랜덤 10글자 단어

    def start_game(self):
        """
        - [ 게임 시작 전 ] 부분을 담당하는 함수 입니다.
        - 캐릭터들을 초기화 하고, 사용자가 플레이할 캐릭터를 선택합니다.
        - 랜덤 알파벳 10글자로 이루어진 answer_string 을 생성합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        self.player.append(Player("김용빈", 50, 20, 0))
        self.player.append(Player("김규리", 70, 25, 0))
        self.player.append(Player("이승아", 80, 30, 0))
        self.player.append(Player("윤석현", 90, 35, 0))
        print("\n\n###############################################")
        print("###############################################")
        print("           피로그래밍 17기 제출용 게임           ")
        print("       컴퓨터가 되어버린 운영진을 이겨라!       ")
        print("             made by 중앙대 한성재          ")
        print("###############################################")
        print("###############################################\n\n")
        # TODO 1-(1): 사용자로부터 캐릭터를 입력받아 user_character에 저장해주세요.
        # Write code here..
        print("******************* 캐릭터 선택 *******************")
        for i in range(len(self.player)):
            print("\n{}번째 캐릭터".format(i+1))
            self.player[i].introduce()
        while(True):
            try:
                selected_number = int(
                    input("캐릭터를 선택하세요.({}~{}):  ".format(1, len(self.player))))
                selected_character = self.player[selected_number-1].name
            except ValueError:
                print("<<입력 오류>>: 숫자가 입력되지 않았습니다. 1~4를 입력해주세요.")
                continue
            except IndexError:
                print("<<입력 오류>>: 범위가 다릅니다. 1~4 사이의 정수를 입력해주세요.")
                continue
            break
        self.user_character = selected_character
        ##### END OF TODO 1-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####
        # TODO 1-(2) : 랜덤 알파벳 10글자로 이루어진 단어를 만들어 answer_string에 저장해주세요.
        # Write code here..
        alphabet_pool = string.ascii_uppercase
        for i in range(10):
            self.answer_string += random.choice(alphabet_pool)
        # 테스트를 하고 싶다면 밑의 줄을 주석 해제
        # print("테스트 용 문자열 출력", self.answer_string)

        ##### END OF TODO 1-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def sort_data(self, i):
        """
        - [ 게임 진행 ] 부분에서 게임진행 순서를 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        # TODO 2 : 게임진행을 위한 data 를 재정렬해주세요.(ROUND 1 : 이름순, ROUND 2,3 : HP 높은 순)
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        # Write code here..
        if i == 1:
            self.player.sort(key=lambda x: x.name)
        else:
            self.player.sort(key=lambda x: x.hp, reverse=True)
        ##### END OF TODO 2 (문제와 본 라인 사이에 코드를 작성하세요.) #####
        #

    def play_game(self):
        """
        - [ 게임 진행 ] 부분을 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        print(
            f"게임은 {self.player[0].name},{self.player[1].name},{self.player[2].name},{self.player[3].name} 순으로 진행됩니다.\n")
        for i in range(4):
            if self.player[i].name == self.user_character:
                print("***** 내 캐릭터 *****")
            else:
                print(f"***** {i+1} 캐릭터 *****")
            print(f"이름: {self.player[i].name} (HP: {self.player[i].hp})")
            # TODO 3-(1) : 플레이어와 컴퓨터의 차례에서는 랜덤의 알파벳 한글자를 선택하게 해주세요.
            # 단 앞에 나왔던 알파벳과 중복되면 안됩니다.
            # Write code here..
            while True:
                chosen_answer = input("선택 알파벳: ")
                if chosen_answer in self.remain_alp:
                    self.remain_alp.remove(chosen_answer)
                    break
                if chosen_answer == "":
                    print("<<입력 오류>>: 한 글자 입력해주세요")
                    continue
                if chosen_answer not in self.remain_alp and chosen_answer not in string.ascii_uppercase:
                    print("<<입력 오류>>: 영어 대문자를 입력해주세요.\n")
                    continue
                if len(chosen_answer) > 1:
                    print("<<입력 오류>>: 영어 대문자 한글자를 입력해주세요.\n")
                else:
                    print("<<입력 오류>>: 앞에서 이미 나왔던 알파벳입니다.\n")
                    continue
            ##### END OF TODO 3-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####
            # TODO 3-(2) : 정답 시, 현재까지 맞춘 단어의 상태를 출력해주세요.
            # 이 단계에서 플레이어 별 점수 집계도 처리해주셔야 합니다.
            # Write code here..
            if chosen_answer in self.answer_string:
                indexOfAns = []
                for idx in range(len(self.answer_string)):
                    if chosen_answer == self.answer_string[idx]:
                        indexOfAns.append(idx)
                        self.cur_string[idx] = chosen_answer
                self.player[i].correct_alp += 1
                for char in self.cur_string:
                    print(char, end=" ")
                print("\n\n***** 맞았습니다 ᵔεᵔ  *****")
            ##### END OF TODO 3-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####
            # TODO 3-(3) : 오답 시, 생명력을 데미지만큼 감소시켜주고 이를 출력해주세요.
            else:
                self.player[i].hp -= self.player[i].damage
                print("\n***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
                print("{}님은 틀렸기 때문에 HP가 {}남았습니다.".format(
                    self.player[i].name, self.player[i].hp))
            print("\n")
            # Write code here..
            ##### END OF TODO 3-(3)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def game_result(self):
        """
        - [ 게임 종료 후 ] 부분을 담당하는 함수 입니다.
        - 게임의 결과를 생명력순, 알파벳 맞춘 횟수 순 두가지의 경우로 출력해야 합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        print("\n\n******************* 게임이 끝났습니다 *******************")
        # TODO 4-(1) : 생명력 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        # Write code here..
        print("\n정답은 \"{}\" 였습니다! 수고하셨습니다\n".format(self.answer_string))
        print("=============================")
        print("     게임 순위 - 생명력")
        print("=============================")
        self.player.sort(key=lambda x: x.hp, reverse=True)
        for i in range(len(self.player)):
            name = ""
            if self.player[i].name == self.user_character:
                name = "*"+self.player[i].name+"*"
            else:
                name = self.player[i].name
            print("{}등: {} ({})".format(
                i+1, name, "HP: " + str(self.player[i].hp) if self.player[i].hp > 0 else "사망"))
        ##### END OF TODO 4-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####
        # TODO 4-(2) : 알파벳 맞춘 횟수 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print(" 게임 순위 - 알파벳 맞춘 횟수")
        print("=============================")
        # Write code here..
        self.player.sort(key=lambda x: x.correct_alp, reverse=True)
        for i in range(len(self.player)):
            name = ""
            if self.player[i].name == self.user_character:
                name = "*"+self.player[i].name+"*"
            else:
                name = self.player[i].name
            print("{}등: {} {}회".format(
                i+1, name, self.player[i].correct_alp))
        ##### END OF TODO 4-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def game(self):
        """
        - 게임 운영을 위한 함수입니다. 
        - 별도의 코드 작성이 필요 없습니다. 
        """
        self.start_game()
        print("******************* 게임 시작 *******************\n")
        for i in range(1, 4):
            print("===========================")
            print(f"     ROUND {i} - START")
            print("===========================")
            self.sort_data(i)
            self.play_game()
            print("===========================")
            print(f"     ROUND {i} - END")
            print("===========================")
        self.game_result()


if __name__ == '__main__':
    """
    - 코드를 실행하는 부분입니다. 
    - 역시 별도의 코드 작성이 필요 없습니다. 
    """
    game = Game()
    game.game()
