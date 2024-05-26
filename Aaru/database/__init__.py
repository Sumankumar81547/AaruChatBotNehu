from pymongo import MongoClient

import config

aaru1 = MongoClient(config.MONGO_URL)
aarubot = aaru1["AaruDB"]["AaruChat"]


from .chats import *
from .users import *
