from gradio_client import Client

# qwen1572_client = Client("https://qwen-qwen1-5-72b-chat.hf.space/--replicas/3kh1x/")
qwen1572_client = None


def call_qwen1572_client(message):
    result = qwen1572_client.predict(
        message,  # str  in 'Input' Textbox component
        [[message, "null"]],
        # Tuple[str | Dict(file: filepath, alt_text: str | None) | None, str | Dict(file: filepath, alt_text: str | None) | None]  in 'Qwen1.5-72B-Chat' Chatbot component
        message,  # str  in 'parameter_9' Textbox component
        api_name="/model_chat"
    )
    return result[1][1]


from openai import OpenAI
client = OpenAI(
    api_key=''
)


messages = [{"role": "system", "content":
    "شما یک دستیار هوشمند از شرکت aihub هستید"}]


def call_with_gpt_3_5(message):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
                                                      messages=[{"role": "user", "content": message}])
    return completion.choices[0].message.content



import anthropic

anthropic_client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="",
)
def call_with_claude_3_opus(message):
    message = anthropic_client.messages.create(
        model="claude-3-haiku-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return message.content