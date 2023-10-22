from emoji import demojize, emojize, is_emoji

HELP = 'Convert emoji to text and text to emoji.'

HELP_SYNTAX = '''
    *Syntax :*
        1. Convert emoji to text :
           ```convert emoji 🤣 to text ```
        2. Convert text to emoji : 
           ```convert emoji :check_mark_button: to emoji ```
\n'''


_error = ValueError(f"I don't understand.")

def _clean_inputs(from_:list, to_:list) -> [str, str]:
    return from_[0], to_[0]

def convert_emoji(from_:str, to_:str) -> str|None:
    if is_emoji(from_):
        if to_ == "emoji":
            return from_
        elif to_ == "text":
            return demojize(from_)
        else:
            raise _error
    else:
        if to_ == "emoji":
            return emojize(from_)
        elif to_ == "text":
            return from_
        else:
            raise _error

def wrapper(from_:list, bot, to_:list) -> str:
    return f"Sure. {' '.join(from_)}, is {bot(*_clean_inputs(from_, to_))}"
        
MICRO_BOTS = {
    'emoji'  : lambda from_, to_ : wrapper( from_, convert_emoji, to_ )
}

for bot in MICRO_BOTS:
    MICRO_BOTS[bot].HELP = HELP
    MICRO_BOTS[bot].HELP_SYNTAX = HELP_SYNTAX
