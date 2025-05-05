#By Alexandros Panagiotakopoulos - alexandrospanag.github.io
# This script simulates a Magic 8-Ball, a toy used for fortune-telling or seeking advice.
# DATE: 5-05-2025

import random

def eight_ball(question):
    """
    Simulates a Magic 8-Ball response to a yes/no question.
    Args:
        question (str): The question to ask the 8-ball.
    Returns:
        str: The 8-ball's answer.
    """
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes – definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.",
        "Don't count on it.", "My reply is no.", "My sources say no.",
        "Outlook not so good.", "Very doubtful."
    ]
    # Choose a random response
    answer = random.choice(responses)
    # Return the formatted answer
    return f"🎱 Question: {question}\nAnswer: {answer}"

# Example usage:
if __name__ == "__main__":
    user_question = input("Ask the Magic 8-Ball a question: ")
    print(eight_ball(user_question))