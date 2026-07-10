"""
Store at least 10 questions
Ask questions randomly
Accept user answer
Check if correct
Keep score
Display final percentage
Allow replay
Add three difficulty levels:"""

import random

easy_questions = {
    "What keyword is used to define a function in Python?": "def",
    "Which data type stores whole numbers?": "int",
    "Which function is used to get input from the user?": "input()",
    "Which symbol is used to start a comment in Python?": "#",
    "Which loop runs while a condition is true?" : "while" ,
}

Medium_questions = {
    "Which operator checks if two values are equal?": "==",
    "Which function converts a string to an integer?": "int()",
    "Which data structure allows duplicate values?": "list",
    "What function returns the number of items in a list?": "len()",
    "Which keyword skips the current loop iteration and moves to the next one?" : "continue",
}

hard_questions = {
    "Which keyword immediately exits a loop?": "break",
    "Which data type stores key–value pairs?": "dictionary",
    "Which method adds an item to the end of a list?": "append()",
    "What does range(5) generate?": "The numbers 0, 1, 2, 3, 4",
    "What keyword is used to handle exceptions in Python?": "try"

}

def quiz_game():
    print("Welcome to Quiz game")
    print("enter the level you want to play 1.easy 2. Medium  3. Hard")
    level_choice = input(" Enter your choise: ")

    if level_choice == "1":
        questions  = easy_questions
    elif level_choice == "2":
        questions  = Medium_questions
    elif level_choice == "3":
        questions = hard_questions
    else:
        print("Invalid choice.")
        return

    question_list = list(questions)
    total_questions = 5
    score = 0

    select_questions = random.sample(question_list, total_questions)

    for number, question in enumerate(select_questions, start=1):
        print(f"{number}. {question}")
        answer = input("Enter your answer: ").lower().strip()

        correct_answer = questions[question]

        if answer == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong!. correct answer is {correct_answer}")
    percentage = (score / total_questions) *100
    if percentage == 100:
         print("Excellent")
    elif percentage >= 80:
        print("Great job!")
    elif percentage >= 60:
        print("Good effort.")
    else:
        print("Keep practicing!")
    print(f"Game over!. your final score is {score}/{total_questions}")
    print(f"parcentage: {percentage:.0f}%")

while True:
    quiz_game()

    again = input("Play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break









