from utils import emojiconverter, unitconverter

_registered_micro_bots = {}
_registered_micro_bots.update(emojiconverter.MICRO_BOTS)
_registered_micro_bots.update(unitconverter.MICRO_BOTS)

_syntax_error = SyntaxError("Incorrect syntax")


def convert(*args:str, **kwargs:str):
    # temp 20 C to F
    # emoji :cake: to text
    tokens = args[0].split()
    if not len(tokens): 
        raise _syntax_error

    bot = _registered_micro_bots.get(tokens.pop(0))
    # print("convert : 18 : ", tokens)
    if not (bot) or not (len(tokens) >= 3): # A to B = 3 tokens minimum remaining
        raise _syntax_error
    
    mid = tokens.index("to")
    from_, to_ = (tokens[:mid]), (tokens[mid+1:])

    try : 
        output = bot(from_, to_)
    except Exception as e:
        output = f"{e}"
    
    return output

BOTS = {
    "convert" : convert
}
