import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import os
import easygui as eg
import ffmpeg


def browse_file():      # 浏览文件函数
    global input_file, original_info
    input_file = filedialog.askopenfilename()     #选择文件
    if input_file:
        try:
            original_info = f"原文件: {os.path.basename(input_file)}\n" \
                        f"时长: {AudioSegment.from_file(input_file).duration_seconds} 秒\n" \
                        f"大小: {os.path.getsize(input_file)} 字节"
            file_info_label.config(text=original_info)    # 将文件信息显示在窗口上
        
        except Exception as e:
            return
    
        else:
            messagebox.showerror("错误", f"无法打开文件: {e}")
    else:
        messagebox.showerror("错误", f"请选择一个{file}文件！")
       

def convert_audio(selected_format, output_path):      # 转码函数
    output_format = selected_format.get()         # 获取选择的转码格式
    if not input_file:                         #判定用户操作
        messagebox.showerror("错误", "请选择一个音频文件！")
        return
        
    if not output_format:            
        messagebox.showerror("错误", "请选择一个转码格式！")
        return
        
    if not output_path:
        messagebox.showerror("错误", "请输入输出路径！")
        return
    
    if os.path.exists(output_path):
        choice = eg.choicebox("文件已存在，是否覆盖？", "警告", ["是", "否"])
        if choice == "否":
            return
        
    try:
        AudioSegment.from_file(input_file).export(output_path, format=output_format)  #转码文件
        converted_info = f"转码后文件: {os.path.basename(output_path)}\n" \
                        f"时长: {AudioSegment.from_file(output_path).duration_seconds} 秒\n" \
                        f"大小: {os.path.getsize(output_path)} 字节"
        
        file_info_label.config(text=f"{original_info}\n\n{converted_info}")    # 显示文件信息
        messagebox.showinfo("成功", f"音频转码完成！\n 音频已被保存到 {output_path}")  

    except Exception as e:
        messagebox.showerror("错误", f"转码失败: {e}")


def convert_video(selected_format, output_path):      # 转码函数
    output_format = selected_format.get()         # 获取选择的转码格式
    if not input_file:                         #判定用户操作
        messagebox.showerror("错误", "请选择一个视频文件！")
        return
        
    if not output_format:            
        messagebox.showerror("错误", "请选择一个转码格式！")
        return
        
    if not output_path:
        messagebox.showerror("错误", "请输入输出路径！")
        return
    
    if os.path.exists(output_path):
        choice = eg.choicebox("文件已存在，是否覆盖？", "警告", ["是", "否"])
        if choice == "否":
            return
        
    try:
        stream=ffmpeg.input(input_file)
        ffmpeg.output(stream, output_path, format=output_format).run()      #转码文件
        ffmpeg.run(stream)

        converted_info = f"转码后文件: {os.path.basename(output_path)}\n" \
                        f"时长: {AudioSegment.from_file(output_path).duration_seconds} 秒\n" \
                        f"大小: {os.path.getsize(output_path)} 字节"
        
        file_info_label.config(text=f"{original_info}\n\n{converted_info}")    # 显示文件信息
        messagebox.showinfo("成功", f"音频转码完成！\n 视频已被保存到 {output_path}")  

    except Exception as e:
        messagebox.showerror("错误", f"转码失败: {e}")
    

while True:
    choice = eg.buttonbox("选择功能", "音视频转码器", ["音频转码", "视频转码", "退出"])
    if choice == "音频转码":
        file = '音频'
        root = tk.Tk()    #创建窗口并设置标题和大小
        root.title("音频转码器")
        root.geometry("400x500")

        frame = tk.Frame(root)    #创建框架并放置
        frame.pack(padx=20, pady=20)


        browse_button = tk.Button(frame, text="选择音频文件", command=browse_file)    # 创建一个按钮，用于浏览文件
        browse_button.pack(pady=10)

        format_label = tk.Label(frame, text="选择转码后的格式:")      # 创建一个标签，用于显示转码格式
        format_label.pack()

    
        format_var = tk.StringVar()   # 创建一个变量，用于存储选择的转码格式
        format_var.set("mp3")
        format_options = ["mp3", "wav", "ogg", "wma", "aac", "flac", "m4a"]

    
        format_menu = tk.OptionMenu(frame, format_var, *format_options)   # 创建一个下拉菜单，用于选择转码格式
        format_menu.pack(pady=10)

    
        output_path_label = tk.Label(frame, text="输入文件输出的路径:（注：\n务必在路径中使用英文字符，否则可能无法正常转换\n例：D:\*.mp3")   # 创建一个标签，用于显示输出路径
        output_path_label.pack()

    
        output_path_entry = tk.Entry(frame, width=40)    # 创建一个文本框，用于输入输出路径
        output_path_entry.pack(pady=5)

    
        file_info_label = tk.Label(frame, text="")    # 创建一个标签，用于显示文件信息
        file_info_label.pack(pady=20)

        
        convert_button = tk.Button(frame, text="转换", command=lambda: convert_audio(format_var, output_path_entry.get().strip('""')))   # 创建一个按钮，用于执行转码操作
        convert_button.pack(pady=10)

        # 进入主循环
        root.mainloop()

        root = tk.Tk()
        root.geometry('0x0+999999+0')
        if messagebox.askquestion("退出视频转码？", "确定要退出吗？") == "yes":
            tk.messagebox.showinfo("退出", "退出成功！")
            continue
        

    elif choice == "视频转码":
        file = '视频'
        root = tk.Tk()    #创建窗口并设置标题和大小
        root.title("音频转码器")
        root.geometry("400x500")

        frame = tk.Frame(root)    #创建框架并放置
        frame.pack(padx=20, pady=20)


        browse_button = tk.Button(frame, text="选择视频文件", command=browse_file)    # 创建一个按钮，用于浏览文件
        browse_button.pack(pady=10)

        format_label = tk.Label(frame, text="选择转码后的格式:")      # 创建一个标签，用于显示转码格式
        format_label.pack()

    
        format_var = tk.StringVar()   # 创建一个变量，用于存储选择的转码格式
        format_var.set("mp4")
        format_options = ["mp4", "avi", "mov", "mkv", "flv", "wmv", "mpeg", "webm", "3gp", "m4v","aac","m4a"]

    
        format_menu = tk.OptionMenu(frame, format_var, *format_options)   # 创建一个下拉菜单，用于选择转码格式
        format_menu.pack(pady=10)

    
        output_path_label = tk.Label(frame, text="输入文件输出的路径:（注：\n务必在路径中使用英文字符，否则可能无法正常转换)\n例：D:\*.mp4")   # 创建一个标签，用于显示输出路径
        output_path_label.pack()

    
        output_path_entry = tk.Entry(frame, width=40)    # 创建一个文本框，用于输入输出路径
        output_path_entry.pack(pady=5)

    
        file_info_label = tk.Label(frame, text="")    # 创建一个标签，用于显示文件信息
        file_info_label.pack(pady=20)

        
        convert_button = tk.Button(frame, text="转换", command=lambda: convert_audio(format_var, output_path_entry.get().strip('""')))   # 创建一个按钮，用于执行转码操作
        convert_button.pack(pady=10)

        # 进入主循环
        root.mainloop()

        root = tk.Tk()
        root.geometry('0x0+999999+0')
        if messagebox.askquestion("退出视频转码？", "确定要退出吗？") == "yes":
            tk.messagebox.showinfo("退出", "退出成功！")
            continue
        
    elif choice == "退出":
        root = tk.Tk()
        root.geometry('0x0+999999+0')
        tk.messagebox.showinfo("退出", "感谢使用音视频转码器！")
        break

    else:
        continue


