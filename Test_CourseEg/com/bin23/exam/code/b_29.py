# 29.
# 设计一个Game类
# 属性:
# 定义一个类属性top_score记录比赛的历史最高分
# 定义一个实例属性player_name记录当前比赛的运动员姓名
# 方法:
# 静态方法show_help显示比赛帮助信息
# 类方法show_top_score显示历史最高分
# 实例方法start_game开始当前比赛的项目
# 主程序步骤:
# 查看帮助信息
# 查看历史最高分
# 创建比赛对象（李小明）,开始比赛
import random

class Game:
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name
        self.top_score = 0

    @staticmethod
    def show_help():
        print("1. 有静态方法show_help()可用")
        print("2. 有类方法show_top_score()可用")
        print("3. 有实例方法start_game()可用")

    @classmethod
    def show_top_score(cls):
        print(Game.top_score)

    def start_game(self):
        score = random.randint(0, 100)
        if Game.top_score < score:
            Game.top_score = score

if __name__ == '__main__':
    Game.show_help()
    lxm = Game("李小明")
    lxm.start_game()
    Game.show_top_score()

    lxm.start_game()
    lxm.show_top_score()

    lxm.start_game()
    lxm.show_top_score()

    lxm.start_game()
    lxm.show_top_score()

    lxm.start_game()
    lxm.show_top_score()
