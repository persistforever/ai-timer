import gradio as gr
import time

def start_countdown(seconds, message):
    """
    倒计时函数，接受秒数和消息作为参数，在控制台中进行倒计时，并在结束后返回消息。
    :param seconds: int, 倒计时的秒数
    :param message: str, 倒计时结束后显示的信息
    :return: str, 返回的提示信息
    """
    for i in range(seconds, 0, -1):
        print(f"Counting down... {i} seconds left")
        time.sleep(1)
    except ValueError:
        return "错误：请输入一个整数秒数"
    return message

# 创建Gradio界面
with gr.Blocks() as demo:
    gr.Markdown("### 倒计时器")
    
    # 输入组件
    input_seconds = gr.Number(label="请输入倒计时秒数", placeholder="例如: 60")
    input_message = gr.Textbox(label="请输入倒计时结束后的提示语", placeholder="例如: 时间到！")
    
    # 按钮
    btn_start = gr.Button("开始")
    
    # 输出组件
    output_text = gr.Textbox(label="倒计时结束后显示的信息")

    # 事件处理
    btn_start.click(start_countdown, inputs=[input_seconds, input_message], outputs=output_text)

# 启动Gradio应用
demo.launch()
