Discord Tureng Sözlük Botu
===

Discord sunucunuz için Tureng Sözlük Botu.


Kullanımı
---------

Botu kullanmak için [discord developer](https://discord.com/developers/) kısmından yeni bir bot oluşturabilir ve **token**'inizi **main.py**'deki gerekli yere koyabilirsiniz.

```py
import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix='.')
TOKEN = 'your token here' # token'ininiz buraya 
```

Ya da var olan botunuza **tureng.py** dosyasını **cog** dosyalarınıza ekleyerek kullanabilirsiniz.



Sunucu İçinde Kullanımı
---

`.tureng {en_tr / tr_en} {kelime}`

![tureng](https://user-images.githubusercontent.com/54121978/90651181-65659b80-e245-11ea-808c-936d62f41600.gif)



Herhangi bir **bug** vs. ile karşılaşırsanız bilgilendirmeyi veya eklemek istediğiniz bir şey varsa **pull request** atmayı unutmayınız ! 
