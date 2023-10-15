from . import helloworld
from . import emojiconverter

# Register Bots like this :
BOTS = {
    **helloworld.BOTS,
    **emojiconverter.BOTS,
    "unknown": lambda *args, **kwargs: "This is an unkown command.",
}
