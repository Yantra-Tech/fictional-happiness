from . import helloworld
# from . import emojiconverter
from . import convert

HELP = '''
Hey there, I am your mitra.
\n'''

USER_CREATED_BOTS = {
    **helloworld.BOTS,
    **convert.BOTS
}

def helpbot(*args, **kwargs):
    output = HELP
    tokens = args[0].split()
    if len(tokens):
        bot = tokens[0]
        print(USER_CREATED_BOTS)
        if bot in USER_CREATED_BOTS:
            output += USER_CREATED_BOTS[bot].HELP
            output += USER_CREATED_BOTS[bot].HELP_SYNTAX
    else:
        output+="Here are the list of things I can do for you.\n"
        for i, bot in enumerate(USER_CREATED_BOTS):
            output += str(i+1)+". "+bot+" : "+USER_CREATED_BOTS[bot].HELP
        output+="\nType ```help <option>``` to know more."
    return output

# Register Bots like this :
BOTS = {
    "help":helpbot,
    **USER_CREATED_BOTS,
    "unknown": lambda *args, **kwargs: "This is an unkown command.",
}
