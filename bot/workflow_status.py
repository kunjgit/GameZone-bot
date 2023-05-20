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

@router.register("workflow_run", action="completed")
async def workflow_job(event, gh, *arg, **kwargs):

	installation_id = event.data["installation"]["id"]

	installation_access_token = await apps.get_installation_access_token(
		gh,
		installation_id=installation_id,
		app_id=os.environ.get("APP_ID"),
		private_key=os.environ.get("PRIVATE_KEY")
	)

	status = event.data['workflow_run']['conclusion']
	ur = event.data['pull_request']['comments_url']

	pass
	
