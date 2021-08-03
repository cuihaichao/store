print("--------猜字游戏---------")
import random
import time
game = random.randint(0,100)
a=True
while a:
    guess=input("请输入你猜的数字")
    guess=int(guess)
    if guess>game:
        print("你猜的数字太大"),time.sleep(3)
        continue
    elif guess<game:
        print("你猜的数字太小"),time.sleep(3)
        continue
    else:print("恭喜你答对了")
    a=False