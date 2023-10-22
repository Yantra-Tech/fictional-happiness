HELP = '''Say hello to the world.'''

HELP_SYNTAX = '''
1. Simply say hello back to the world.
```hello```
2. Simply say hello back to the world.
```hey```
'''

def hello(*args, **kwargs) -> str:
    return "Hello World"

BOTS = {
    "hey"   : hello,
    "hello"   : hello
}

for bot in BOTS:
    BOTS[bot].HELP = HELP
    BOTS[bot].HELP_SYNTAX = HELP_SYNTAX
