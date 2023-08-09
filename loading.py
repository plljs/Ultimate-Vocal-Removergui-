import win32gui
import win32con
import sys
args = sys.argv

# 隐藏窗口
win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)



import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import os
import sys
from gui_data.translate import *

def delete_file(file_path):
    if os.path.exists(file_path):
        try:
            print(f"删除文件")
            os.remove(file_path)
        except OSError as e:
            print(f"删除文件时发生错误：{e}")

print(f"{args[1]}")
# 删除文件
delete_file(f"{dir_path}\\gui_data\\tmp\\load.json")
if f"{args[1]}"=='URV5startljs':
    #run_cmd("start UVR5.py")
    # 创建主窗口
    loadbmp_window = tk.Tk()

    # 设置窗口大小
    window_width = 390
    window_height = 245
    screen_width = loadbmp_window.winfo_screenwidth()
    screen_height = loadbmp_window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    loadbmp_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 设置窗口无边框
    loadbmp_window.overrideredirect(True)

    # 加载图片
    dir_path=os.getcwd()
    image_path = f"{dir_path}\\gui_data\\img\\splash.bmp"
    image = Image.open(image_path)
    image = image.resize((window_width, window_height), Image.LANCZOS)  # 使用Image.LANCZOS滤波器
    photo = ImageTk.PhotoImage(image)

    # 创建Canvas
    canvas = Canvas(loadbmp_window, width=window_width, height=window_height, highlightthickness=0)
    canvas.pack()

    # 显示图片
    canvas.create_image(0, 0, anchor="nw", image=photo)

    # 创建标签，使用Canvas模拟
    label_text = "Loading"
    label_x = 2  # 在窗口左边距离为2
    label_y = 235
    label = canvas.create_text(label_x, label_y, text=label_text, font=("楷体", 10), fill="gray", anchor="w")

    # 定义要显示的文本列表
    text_list = [translate("Loading"),translate("Loading."),translate("Loading.."),translate("Loading...")]

    # 定义用于更新文本的索引
    text_index = 0

    # 定义全局变量a，用于控制窗口的结束
    a = 1

    # 定义更新文本的函数

def update_label_text():
    global text_index, a
    filename = f"{dir_path}\\gui_data\\tmp\\load.json"
    if os.path.exists(filename):
      with open(filename, 'r') as f:
            if f.read() == "ok":
                #结束窗口和释放相应组件和内存
                loadbmp_window.destroy()
                sys.exit()  # 退出程序
                return
    canvas.itemconfig(label, text=text_list[text_index])
    text_index = (text_index + 1) % len(text_list)  # 循环更新文本
    loadbmp_window.after(500, update_label_text)  # 0.5秒后再次调用函数更新文本


# 开始动态更新标签文本
update_label_text()

# 显示窗口
loadbmp_window.mainloop()

