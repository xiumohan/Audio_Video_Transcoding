import os
import ffmpeg
import easygui as eg
from easygui import fileopenbox
import time
# 定义转换格式的函数
def convert_video(input_path, output_path, target_format):
    try:
        # 判断输出路径是否存在
        if os.path.exists(output_path):
            # 弹出对话框，询问是否覆盖
            choice = eg.buttonbox(f'文件 {output_path} 已存在，是否覆盖？', '视频转码器', ['是', '否'])
            # 如果选择否，则返回
            if choice == '否':
                return
        stream = ffmpeg.input(input_path)          # 使用ffmpeg库的input函数，读取输入文件
        stream = ffmpeg.output(stream, output_path, format=target_format)    # 使用ffmpeg库的output函数，将输入文件转换为指定格式，并输出到指定路径
        ffmpeg.run(stream)
    except Exception as e:
        eg.exceptionbox(f'发生错误：{e}')
def main():
    while True:
        try:
            input_path = fileopenbox("请选择要转换的视频文件", "视频转码器")
            target_format = eg.choicebox('请选择你要转换的编码格式', '视频转码器', ['mp4', 'avi', 'mkv', 'flv', 'wmv', 'mov'])
            if not input_path:
                return
        except FileNotFoundError:
            eg.msgbox("没有选择文件，请重新操作。")
            continue

        # 打开文件保存框，让用户选择输出文件的路径和格式
        output_path = eg.enterbox("请输入输出文件的路径，例如：/path/to/output/*.mp4 ", "视频转码器")
        if not output_path and not target_format:
            return
                
        # 调用convert_video函数进行转码
        convert_video(input_path, output_path, target_format)
        time.sleep(1)
        eg.msgbox("视频转码完成！", "视频转码器")
        if eg.buttonbox("退出视频转码？", "退出", ["是", "否"]) == "是":
            break
        continue
        

if __name__ == "__main__":
    main()
