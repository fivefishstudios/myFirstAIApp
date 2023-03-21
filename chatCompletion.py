# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai

openai.api_key_path = ".api-key"

system = """ 
you are a very knowledgeable and helpful language expert
"""
# Answer briefly in first paragraph, 
# and explain like I'm five on second paragraph, 

prompt = """
Compose a poem about resistors and transistors
"""

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": prompt},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
    ],
    max_tokens=1000,
)


# print(response)
print(prompt)
print(response.choices[0].message.content)
print('\n')