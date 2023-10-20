from emoji import demojize, emojize

def textToEmoji(*args, **kwargs):
    msg = args[0]
    return "Converting text to emoji - " + emojize(msg)

def emojiToText(*args, **kwargs):
    msg = args[0]
    return "Converting emoji to text - " + demojize(msg)

BOTS = {
    'emojitext' : emojiToText,
    'textemoji' : textToEmoji
}
