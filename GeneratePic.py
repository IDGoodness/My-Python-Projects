import os
import openai

# Your API Key Here: <img draggable="false" role="img" class="emoji" alt="👇" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f447.svg">
openai.api_key = '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'

# Your Image Prompt Here: <img draggable="false" role="img" class="emoji" alt="👇" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f447.svg">
prompt = "An oil painting of a dancing robot in the style of Monet"

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"])