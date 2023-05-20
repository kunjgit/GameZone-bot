import asyncio
import os
import sys
import traceback
import aiohttp
from aiohttp import web
from gidgethub import aiohttp as gh_aiohttp
from gidgethub import routing
from gidgethub import sansio
from gidgethub import apps

router = routing.Router()

@router.register("issues", action="opened")
async def issue_opened_event(event, gh, *args, **kwargs):

    installation_id = event.data["installation"]["id"]

    installation_access_token = await apps.get_installation_access_token(
        gh,
        installation_id=installation_id,
        app_id=os.environ.get("APP_ID"),
        private_key=os.environ.get("PRIVATE_KEY")
    )

    url = event.data['issue']['comments_url']
    
    author = event.data['issue']['user']['login']
    
    avatar = event.data['issue']['user']['avatar_url']

    message = f"<b> Hi @{author} 👋<br>Thanks for opening this issue. :octocat: </b><br>Someone will look into it soon! Till then show your love by staring [Repo](). 💗<br>You can assign this issue to you by commenting `/assign`.👀 <br><i>By contributing, you are expected to uphold this [Guide](). Check this [guide]() before contributing.</i>"
    await gh.post(url, data={
        'body': message,
        },
        oauth_token=installation_access_token["token"]
                 )
