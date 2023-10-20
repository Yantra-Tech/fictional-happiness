from . import helloworld
# from . import emojiconverter
from . import convert

# Register Bots like this :
BOTS = {
    **helloworld.BOTS,
    # **emojiconverter.BOTS,
    **convert.BOTS,
    "unknown": lambda *args, **kwargs: "This is an unkown command.",
}
