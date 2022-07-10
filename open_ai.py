import constants
import openai


def openai_request(user_prompt):
    response = openai.Completion.create(
        api_key=constants.API_KEY,
        engine="text-davinci-002",
        prompt=user_prompt,
        temperature=0.7,
        max_tokens=3000,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].text
