# https://pypi.org/project/gradio/
# https://zhuanlan.zhihu.com/p/624712372
import gradio as gr

def greet(name):
  return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
