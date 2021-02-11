# -*- coding: utf-8 -*-
# 문제12 : 게임 캐릭터 클래스 만들기
# 다음 소스코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '파이어볼'이 출력되게 만드시오.

# **주어진 소스 코드를 수정해선 안됩니다.**

# ```python
# <여기에 class를 작성하세요.>

# x = Wizard(health = 545, mana = 210, armor = 10)
# print(x.health, x.mana, x.armor)
# x.attack()
# ```

# >> 출력예시

# ```python
# 545 210 10
# 파이어볼
# ```


# 답안
class Wizard(object):
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    def attack(self):
        print('파이어볼')
    # def __str__(self):
    #     return "hello world"

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()

print(x) # <__main__.Wizard object at 0x108f953d0>
# print(type(x)) # <class '__main__.Wizard'>
# print(dir(x))