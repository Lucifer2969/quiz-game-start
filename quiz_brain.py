class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, u_answer, r_answer):
        if u_answer.lower() == r_answer.lower():
            self.score += 1
            print ("Correct answer")
        else:
            print("You got it wrong")
        print(f"The correct answer was {r_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    
