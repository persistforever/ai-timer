import gradio as gr
import time

def start_countdown(seconds, message):
    """
    函数用于执行倒计时操作。
    :param seconds: int, 倒计时秒数
    :param message: str, 倒计时结束后的提示信息
    """
    for i in range(seconds, 0, -1):
        time.sleep(1)  # 暂停一秒
    return message

# 创建 Gradio 的 Blocks 对象
with gr.Blocks() as demo:
    # 创建输入组件
    input_seconds = gr.Number(label="请输入倒计时时间（秒）")
    input_message = gr.Textbox(label="请输入倒计时提示语")

    # 创建输出组件
    output_message = gr.Textbox(label="倒计时结束提示")

    # 创建按钮并绑定处理函数
    btn_start = gr.Button("开始")
    btn_start.click(start_countdown, inputs=[input_seconds, input_message], outputs=output_message)

# 启动 Gradio 应用
demo.launch()
