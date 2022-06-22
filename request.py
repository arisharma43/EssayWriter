import constants
import openai

essay_prompt = input("Enter a prompt to be answered:\n")
response = openai.Completion.create(
    api_key=constants.API_KEY,
    engine="text-davinci-002",
    prompt=essay_prompt,
    temperature=0.7,
    max_tokens=1000,
    frequency_penalty=0,
    presence_penalty=0,
)
print(response)

essay = essay_prompt + response.choices[0].text

print(essay)
