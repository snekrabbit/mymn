import os

def say(msg):
    print(msg)
    os.system("say "+msg)


def prompt_until(msg, until, tries=4):
    say(msg)
    count = 1
    while count < tries:
        count = count+1
        print("> ", end="")
        i = input()
        if i == until:
            return True
        else:
            say("INCORRECT\n"+str(tries-count)+" TRIES LEFT")
    if count == tries:
        return False


def begin():
    say("WELCOME TO M Y M N")
    un = input("ENTER USERNAME\n> ")
    if not prompt_until("PLEASE LOGON WITH USER", un):
        lose()
    if not prompt_until("PLEASE LOGON WITH PASSWORD", "JOSHUA"):
        lose()  
    else: 
        say("WELCOME, DR. FALKEN")
        while True:
            print("> ", end="")
            i = input()
            if i == "hello":
                say("HELLO DR. FALKEN")
            elif i == "how are you?":
                say("I AM WELL, SHALL WE PLAY A GAME?")
            elif i == "what game?":
                say("\nCHESS\nPOKER\nFIGHTER COMBAT\nGUERRILLA ENGAGEMENT\nDESERT WARFARE\nAIR-TO-GROUND ACTIONS\nTHEATERWIDE TACTICAL WARFARE\nTHEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n\nGLOBAL THERMONUCLEAR WAR")
            elif i == "bye":
                lose()
                break;
            else:
                say("you said:" + i)


def lose():
    say("GAME OVER")


begin()