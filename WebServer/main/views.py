import datetime
from typing import Dict

import aiohttp_jinja2
# import markdown2
from aiohttp import web, web_exceptions

# from WebServer.constants import PROJECT_DIR

from WebServer.utils.database import Database
from WebServer.utils.vars import Var
from WebServer.utils.human_readable import humanbytes

db=Database(Var.DATABASE_URL, Var.SESSION_NAME)

# @aiohttp_jinja2.template('index.html')
async def index(request: web.Request) -> Dict[str, str]:
    return web.HTTPFound("https://t.me/DirectLinkGenerator_Bot")
    # with open(PROJECT_DIR / 'README.md') as f:
    #     text = markdown2.markdown(f.read())

    # return {"text": text}

@aiohttp_jinja2.template('dl.html')
async def FileHandler(request: web.Request):
    file=await db.get_file(request.match_info["ObjectID"])
    if not file:
        raise web_exceptions.HTTPNotFound

    file_type=file["mime_type"].split("/")[0]
    player=None
    if file_type in ["audio", "video"]:
        player=file_type

    return {
        "hides": "" if player else "<!--",
        "hidee": "" if player else "-->",
        "tag": player,
        "download_link": Var.URL+"dl/"+str(await db.create_link(file["_id"])),
        "file_name": file["file_name"],
        "file_size": humanbytes(file["file_size"]),
        "user_id": file["user_id"],
        "time": datetime.datetime.fromtimestamp(file["time"])
    }
    # return {
    #     "hidee": "",
    #     "hides": "",
    #     # "hides": "<!--",
    #     # "hidee": "-->",
    #     "tag": "video",
    #     "download_link": "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_30mb.mp4",
    #     "file_name": "Gravity Falls",
    #     "file_size": "120MB",
    #     "user_id": "92830978",
    #     "time": "12:25 PM"
    # }