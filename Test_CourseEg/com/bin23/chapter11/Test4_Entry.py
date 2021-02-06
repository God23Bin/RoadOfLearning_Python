import tkinter as tk
import tkinter.messagebox

def bindFun_addExperience():
    tk.messagebox.showinfo('刷经验', '成功增加50经验值~')

# 创建顶层窗口
topwin = tk.Tk()
# 初始化窗口大小
topwin.geometry('820x638')
# 设置标题
topwin.title('刷经验升级利器，卢本伟修改版')

# t = "免责声明:\n" + \
#     '一旦您使用本软件，即表示您愿意接受以下条约。 \n' + \
#     '1、如果软件损害了您的利益，请联系作者，我将立刻停止发布 \n' + \
#     '2、您同意尽您最大的努力来防止和保护未经授权的发表和使用本程序及其文件内容，我们将保留所有无明确说明的权利。 \n' + \
#     '3、您应该对使用该程式的结果自行承担风险，若运行该程式后出现不良后果时，作者对其概不负责，亦不承担任何法律责任。 \n' + \
#     '4、本软件仅供学习与交流使用,请勿用于任何商业用途!下载后请于24小时内删除，运行该程式出现的一切责任与作者本人无关! \n' + \
#     '5、本说明不能在任何版本中被删除或更改，本软件严禁用于任何形式的商业用途，本软件免责声明最终解释权归本修改版作者所有。 \n'
#     # ' \n' + \
#
# m = tk.Message(topwin, text = t, width = 820)
# m.config(bg = 'lightgreen', font = ('times', 11, 'italic'))
# m.pack()


# 不支持jpg，png
# bg = tk.PhotoImage(file = 'PanD.gif')
#
# label = tk.Label(topwin,
#                  text = "欢迎进入刷经验升级利器",
#                  image = bg,
#                  font = 'Helvetica',
#                  # 设置字体颜色
#                  fg = 'white',
#                  # 设置文本和图像的混合模式
#                  compound = tk.CENTER
#                  )
# label.pack()
#
# button_addExperience = tk.Button(topwin, text = "刷经验", command = bindFun_addExperience)
# # 如果command = bindFun_addExperience  多了个括号  command = bindFun_addExperience()
# # 则会在一开始就会执行函数
# # button_addExperience = tk.Button(topwin, text = "刷经验", command = bindFun_addExperience())
# button_addExperience.pack(side = tk.LEFT)
#
# button_ban = tk.Button(topwin, text = "禁止使用，该功能待实现", state = tk.DISABLED)
# button_ban.pack(side = tk.LEFT)
#
# button_quit = tk.Button(topwin, text = "退出卢本伟修改版", command = topwin.quit)
# button_quit.pack(side = tk.RIGHT)

# 创建标签
tk.Label(topwin, text = "昵称").grid(row = 0)
tk.Label(topwin, text = "等级").grid(row = 1, column = 0)
tk.Label(topwin, text = "经验").grid(row = 2)

e1 = tk.Entry(topwin)
e2 = tk.Entry(topwin)
e3 = tk.Entry(topwin, state = tk.DISABLED)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
e3.grid(row = 2, column = 1)

# 进入主循环
topwin.mainloop()
