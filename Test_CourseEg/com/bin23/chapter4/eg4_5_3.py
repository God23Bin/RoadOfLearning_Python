player = {"LeBron":23, "Kobe":24, "Durant":35, "Ivring":2 ,"Love":0}
print("原始字典：", player)
player.update({"Russell":0, "LeBron":6})
player.pop("Kobe")
print("现有字典：", player, "总人数：", len(player))
name = input("请输入名字，可找其号码：")

while name in player.keys():
    print("该球员号码为：", player[name])
    name = input("请输入名字，可找其号码：")
else:
    print("没找到该球员")