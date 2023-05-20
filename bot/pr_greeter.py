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


@router.register("pull_request", action="opened")
async def opened_pr(event, gh, *arg, **kwargs):

    installation_id = event.data["installation"]["id"]

    installation_access_token = await apps.get_installation_access_token(
        gh,
        installation_id=installation_id,
        app_id=os.environ.get("APP_ID"),
        private_key=os.environ.get("PRIVATE_KEY")
    )

    author = event.data['pull_request']['user']['login']
    ur = event.data['pull_request']['comments_url']

    messag = f"<b> Hi @author 👋<br>Thanks for opening this pull request. :octocat: </b><br>We will look into it really soon till then keep improving your and show some love by starring  [Repo]()💗. <br><i>By contributing, you are expected to uphold this [code of conduct]()."
    await gh.post(ur, data={
        'body': messag,
        },
        oauth_token=installation_access_token["token"]
                 )
            