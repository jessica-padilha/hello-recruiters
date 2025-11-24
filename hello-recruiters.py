def oportunity():
    while True:
        question = str(input('Are you a tech recruiter?\n answer "yes" or "no":\n'))
        case_question=question.casefold()
        if case_question == "no":
                print("Ok. Thanks for being here.\n \"Let\'s connect on LinkedIn: https://www.linkedin.com/in/jéssica-padilha-23833b179'?") 
                print('Thanks for participating!')    
                break
        elif case_question == "yes":
            print("I am looking for an opportunity as a junior cloud engineer." "\nLet\'s connect on LinkedIn: 'https://www.linkedin.com/in/jéssica-padilha-23833b179'?")
            print('Thanks for participating!')       
            break
        else:
                print('Please try again and enter a valid answer.')
                # break

oportunity()    