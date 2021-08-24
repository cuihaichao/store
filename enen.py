# 调用模块
import threading
import time

bread = 0
money = 3000


class making_Bread(threading.Thread):
    username = ""
    count = 0

    def run(self) -> None:
        global bread
        while True:
            if bread < 50:
                bread = bread + 1
                self.count = self.count + 1
                print(self.username, "做了", self.count, "个面包")
                time.sleep(0.1)
            else:
                print("共做了{}个面包",format(self.count))
                break


class buy_bread(threading.Thread):
    username = ""
    count = 0  # 面包计数器
    money1 = 0  # 余额计数器

    def run(self) -> None:
        global bread
        global money
        while True:
            if money > 0:
                if bread <= 0:
                    bread = bread + 1
                    money = money - 3
                    self.count = self.count - 1
                    self.money1 = self.money1 - 3
                    print(self.username, "买了", self.count, "个面包花了", money)
                elif bread <= 0:
                    print("面包没了")
            elif money <= 0:
                print(self.username, "共买了", self.count, "个面包共花了", money)
                break


l1 = making_Bread()
l2 = making_Bread()
l3 = making_Bread()
l4 = buy_bread()
l5 = buy_bread()
l6 = buy_bread()
l7 = buy_bread()
l8 = buy_bread()

l1.username = "张三"
l2.username = "李四"
l3.username = "王五"
l4.username = "4"
l5.username = "5"
l6.username = "6"
l7.username = "7"
l8.username = "8"

l1.start()
l2.start()
l3.start()
l4.start()
l5.start()
l6.start()
l7.start()
l8.start()
