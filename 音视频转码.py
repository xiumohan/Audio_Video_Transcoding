from pydub import AudioSegment
import os
import easygui as eg
import ffmpeg
from easygui import fileopenbox
def convert_aodio(input_path,output_path,output_format):     #定义音频转码函数
    try:
        if os.path.exists(output_path):
            choice = eg.buttonbox(f'文件 {output_path} 已存在，是否覆盖？', '音频转码器', ['是', '否'])
            if choice == '否':
                return
        else:
            return
        stream= AudioSegment.from_file(input_path)
        stream.export(output_path, format=output_format)
        
        eg.msgbox(f'文件 {output_path} 转码完成！', '音频转码器')
    except Exception as e:
        eg.msgbox(f'文件 {output_path} 转码失败！\n错误信息：{e}', '音频转码器')
def convert_video(input_path, output_path, target_format):       #定义视频转码函数
    try:
        # 判断输出路径是否存在
        if os.path.exists(output_path):
            # 弹出对话框，询问是否覆盖
            choice = eg.buttonbox(f'文件 {output_path} 已存在，是否覆盖？', '视频转码器', ['是', '否'])
            # 如果选择否，则返回
            if choice == '否':
                return
        else:
            return
        stream = ffmpeg.input(input_path)          # 使用ffmpeg库的input函数，读取输入文件
        stream = ffmpeg.output(stream, output_path, format=target_format)    # 使用ffmpeg库的output函数，将输入文件转换为指定格式，并输出到指定路径
        ffmpeg.run(stream)
    except Exception as e:
        eg.exceptionbox(f'发生错误：{e}')
def main():
    while True:
        choice=eg.buttonbox('请选择要进行的操作：', '音频转码器', ['音频转码', '视频转码', '退出'])
        if choice=='音频转码':
            try:
                input_path = eg.fileopenbox('选择要转码的音频文件', '音频转码器')
                output_format=eg.choicebox(msg='请选择要转码的格式', title='音频转码', choices=['mp3','wav','ogg','wma','aac','flac'])
                if input_path is None:
                    return
            except FileNotFoundError:
                eg.msgbox("没有选择文件，请重新操作。")
                continue
        
            output_path = eg.enterbox('请在后缀名前输入文件路径和文件名，例如E:\**\*.mp3', '音频转码器', default=f'.{output_format}')
            if output_path is None:
                return
            convert_aodio(input_path, output_path, output_format)

            eg.msgbox(f'文件 {output_path} 转码完成！', '音频转码器')
            if eg.buttonbox('是否继续转码？', '音频转码器', ['是', '否']) == '否':
                eg.msgbox('感谢使用音频转码器！', '音频转码器')
                break
            else:
                continue
        elif choice=='视频转码':
            try:
                input_path = fileopenbox("请选择要转换的视频文件", "视频转码器")
                target_format = eg.choicebox('请选择你要转换的编码格式', '视频转码器', ['mp4', 'avi', 'mkv', 'flv', 'wmv', 'mov'])
                if not input_path:
                    return
            except FileNotFoundError:
                eg.msgbox("没有选择文件，请重新操作。")
                continue

            # 打开文件保存框，让用户选择输出文件的路径和格式
            output_path = eg.enterbox("请输入输出文件的路径，例如：E:\**\*.mp4 ", "视频转码器")
            if not output_path and not target_format:
                return
                    
            # 调用convert_video函数进行转码
            convert_video(input_path, output_path, target_format)
    
            eg.msgbox("视频转码完成！", "视频转码器")
            if eg.buttonbox("退出视频转码？", "退出", ["是", "否"]) == "是":
                break
            continue
        elif choice=='退出':
            eg.msgbox('感谢使用音频转码器！', '音频转码器')
if __name__ == '__main__':
    main()