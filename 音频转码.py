from pydub import AudioSegment
import os
import easygui as eg
def convert_aodio(input_path,output_path,output_format):
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
def main():
    while True:
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
if __name__ == '__main__':
    main()