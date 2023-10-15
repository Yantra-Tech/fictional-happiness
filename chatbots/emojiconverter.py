from emoji import demojize, emojize

def textToEmoji(msg:str):
    return "Converting text to emoji - " + emojize(msg)

def emojiToText(msg:str):
    return "Converting emoji to text - " + demojize(msg)

BOTS = {
    'emojitext' : emojiToText,
    'textemoji' : textToEmoji
}
