import gradio as gr
app=gr.Interface(fn=len,inputs=["text"],outputs=["number"])
app.launch(share=True)