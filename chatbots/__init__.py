from .helloworld import hello
from .emojiconverter import textToEmoji, emojiToText

# Register Bots like this :
BOTS = {
    "unknown": lambda *args, **kwargs: "This is an unkown command.",
    'hello' : hello,
    'emojitext' : emojiToText,
    'textemoji' : textToEmoji
}
