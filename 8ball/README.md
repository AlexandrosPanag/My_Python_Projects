# Magic 8-Ball Simulator

A simple Python script that simulates a Magic 8-Ball, the classic fortune-telling toy. Ask any yes/no question and receive a random, whimsical answer!

## Features

- Asks the user for a yes/no question.
- Returns a random response from a set of classic Magic 8-Ball answers.
- Easy to use and modify.

## Usage

1. **Clone or download this repository.**
2. Make sure you have Python 3 installed.
3. Run the script:

    ```bash
    python 8ball.py
    ```

4. When prompted, type your question and press Enter.
5. The Magic 8-Ball will reveal your fortune!

## Example

```
Ask the Magic 8-Ball a question: Will I ace my exam?
🎱 Question: Will I ace my exam?
Answer: Most likely.
```

## Code Example

```python
import random

def eight_ball(question):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes – definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.",
        "Don't count on it.", "My reply is no.", "My sources say no.",
        "Outlook not so good.", "Very doubtful."
    ]
    answer = random.choice(responses)
    return f"🎱 Question: {question}\nAnswer: {answer}"

if __name__ == "__main__":
    user_question = input("Ask the Magic 8-Ball a question: ")
    print(eight_ball(user_question))
```

## License

This project is licensed under the [MIT License](LICENSE).

---

Created by Alexandros Panagiotakopoulos - [alexandrospanag.github.io](https://alexandrospanag.github.io)
