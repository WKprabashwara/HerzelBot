## Herzel bot example plugin format here :
You can create your own custom plugin useing this format or use any [pyrogram](http://pyrogram.org) method !


```
from Herzel import app
from Herzel.utils.commands import *

@app.on_message(command("test"))
async def plug(_, message):
    szteambots = await message.reply_text(text="Hello I am herzel"
    )
    supun = """
I'm a group management bot with some useful features.
@Theherzelbot    
    """
    await szteambots.edit_text(supun)

__MODULE__ = "test"
__HELP__ = """  
/test - test cmd here
"""
```

