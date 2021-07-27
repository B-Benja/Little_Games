import requests
import html
from question_model import Question

parameters = {
    "amount": 10,
    "type": "boolean",
}

question_data = requests.get("https://opentdb.com/api.php", params=parameters).json()

question_bank = []
for question in question_data["results"]:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))
