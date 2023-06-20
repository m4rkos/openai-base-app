import openai
from tools import Tools
from dotenv import dotenv_values

env_data = dotenv_values(".env")

"""
-- AUTHENTICATION --
"""

credentials = {
    'org' : env_data.get("YOUR_ORG_ID"),
    'key' : env_data.get("OPENAI_API_KEY")
}

openai.organization = credentials.get('org')
openai.api_key = credentials.get('key')
info = openai.Model.list()

"""
-- To USE --
"""

tools = Tools()
# tools.save_info(info)


# Create chat
def create_chat(model_type: str = "gpt-3.5-turbo"):
    completion = openai.ChatCompletion.create(
        model = model_type,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ] # chat example
    )

    print(completion.choices[0].message)
    print(completion)


# Create images
def create_images(prompt: str = "A cute baby sea otter"):
    result = openai.Image.create(
        prompt=prompt,
        n=2,
        size="1024x1024"
    )

    a = result
    tools.save_prompt_images(result, a['data'], prompt)

def start():
    result = input("What kind of thing do you want to do: \n1 : chat\n2 : create an image \n\nanswer: ")
    while tools.is_number(result) != True:
        start()
    return result


choice = start()
if int(choice) in (1, 2):
    match choice:
        case '1':
            create_chat()
    
        case '2':
            create_images(input("type your prompt: "))
    
        # case _:
        #     print("Wrong choice 🤣 !!")

    start()

else:
    print("Wrong choice 🤣 !!")
    start()

