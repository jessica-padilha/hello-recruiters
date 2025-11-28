import time

def efeito_digi(parametro):
    for char in parametro:
        print(char, end='', flush=True)
        time.sleep(0.06)
    print() 

def oportunity():
    while True:
        
        efeito_digi ('Are you a tech recruiter?\n answer "yes" or "no":\n')
        question = input()
        case_question=question.casefold()

        if case_question == "no":
                efeito_digi("Ok. Thanks for being here.\n Anyway let\'s connect on LinkedIn: https://www.linkedin.com/in/jéssica-padilha-23833b179'?")
                efeito_digi('Thanks for participating!')    
                break
        elif case_question == "yes":
            efeito_digi("I am looking for an opportunity as a junior cloud engineer." "\nLet\'s connect on LinkedIn: 'https://www.linkedin.com/in/jéssica-padilha-23833b179'?")
            efeito_digi('Thanks for participating!')       
            break
        else:
            efeito_digi('Please try again and enter a valid answer.')
        

oportunity()    
