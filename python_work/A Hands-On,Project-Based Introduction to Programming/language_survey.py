from survey import AnonymousSurvey

question = "What is your favorite language?"
my_survey = AnonymousSurvey(question)

print("Enter 'q' to quit at any time")
my_survey.show_question()
while True:
	language = input("Language : ")
	if language == 'q':
		break
	my_survey.store_response(language)
	
my_survey.show_results()
