import os
import openai

openai.api_key_path = ".env"


prompt = """
What is the sum of square method? Explain like I'm five. 
"""

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.6,
    max_tokens=1000,
)

result=response.choices[0].text
# print(response.choices)
print("\n")
print(prompt)
print(result)
print("\n")
