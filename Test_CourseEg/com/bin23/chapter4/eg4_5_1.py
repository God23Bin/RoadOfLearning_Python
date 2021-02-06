player = {"LeBron":23, "Kobe":24, "Durant":35, "Ivring":2 ,"Love":0}
print("原始字典：", player)
player["Russell"] = 0
player["LeBron"] = 6
del player["Kobe"]
print("现有字典：", player, "总人数：", len(player))
name = input("请输入名字，可找其号码：")

if name in player:
    print("该球员号码为：", player[name])
else:
    print("没找到该球员")