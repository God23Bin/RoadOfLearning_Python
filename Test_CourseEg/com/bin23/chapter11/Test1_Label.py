import tkinter as tk

# 创建顶层窗口
topwin = tk.Tk()
# 初始化窗口大小
topwin.geometry('820x638')
# 设置标题
topwin.title('刷经验升级利器，卢本伟修改版')

# 不支持jpg，png
bg = tk.PhotoImage(file = 'PanD.gif')

label = tk.Label(topwin,
                 text = "欢迎进入刷经验升级利器",
                 image = bg,
                 font = 'Helvetica',
                 # 设置字体颜色
                 fg = 'white',
                 # 设置文本和图像的混合模式
                 compound = tk.CENTER
                 )
label.pack()

# 进入主循环
topwin.mainloop()
