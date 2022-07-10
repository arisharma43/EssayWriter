import open_ai
import openai

api_response = open_ai.openai_request(
    "Write an essay about the different types of media and their role in the modern world."
)

with open("output/output.txt", "w+") as file:
    # file = open(completeName, "w")
    file.write(api_response)
