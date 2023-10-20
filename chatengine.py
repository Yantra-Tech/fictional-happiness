from chatbots import BOTS

class _ChatAction:
    def __init__(self, bot, args="") -> None:
        self.bot    = BOTS.get(bot.lower())
        self.bot    = [self.bot, BOTS["unknown"]][self.bot==None]
        self.args   = args
        self.output = None
    
    def _execute(self):
        try :
            self.output = self.bot(self.args)
        except Exception as e:
            self.output = str(e)
        return self.output

class ChatEngine:
    @staticmethod
    def parse(msg:str) -> _ChatAction:
        '''
        Parse the chat received from a user.
        '''
        msg_tokens = msg.lower().split()
        if len(msg_tokens)>=1:
            action = _ChatAction(
                bot=msg_tokens[0],
                args=" ".join(msg_tokens[1:])
            )
        else:
            action = _ChatAction("unknown")
        
        return action

    @staticmethod
    def execute(bot:_ChatAction) -> str:
        output = bot._execute()
        if not output:
            raise Exception("Some Error Occurred -> chatengine.py:29")
        return output 
