def begin():
    print("WELCOME TO WAR GAMES\nPLEASE LOGON WITH USER PASSWORD")
    print("> ", end="")
    count = 1
    while count <4:
        count = count+1
        i = input()
        if i == "JOSHUA":
            break;
        else:
            print ("WRONG PASSWORD\n"+str(4-count)+" TRIES LEFT")
    if count == 4:
        lose()   
    else: 
        print ("WELCOME DR. FALKEN")
        while True:
            print("> ", end="")
            i = input()
            if i == "hello":
                print ("HELLO DR. FALKEN")
            elif i == "how are you?":
                print ("I AM WELL, SHALL WE PLAY A GAME?")
            elif i == "what game?":
                print ("\nCHESS\nPOKER\nFIGHTER COMBAT\nGUERRILLA ENGAGEMENT\nDESERT WARFARE\nAIR-TO-GROUND ACTIONS\nTHEATERWIDE TACTICAL WARFARE\nTHEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n\nGLOBAL THERMONUCLEAR WAR")
            elif i == "bye":
                lose()
                break;
            else:
                print ("you said:" + i)


def lose():
    print("GAME OVER")


begin()

