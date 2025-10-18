from FlawlessXmusic.core.bot import Anony
from FlawlessXmusic.core.dir import dirr
from FlawlessXmusic.core.git import git
from FlawlessXmusic.core.userbot import Userbot
from FlawlessXmusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
