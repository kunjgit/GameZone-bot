from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp

@router.register("installation", action="created")
async def repo_installation_added(event, gh, *args, **kwargs):
    installation_id = event.data["installation"]["id"]

    installation_access_token = await apps.get_installation_access_token(
        gh,
        installation_id=installation_id,
        app_id=os.environ.get("APP_ID"),
        private_key=os.environ.get("PRIVATE_KEY")
    )
    repo_name = event.data["repositories"][0]["full_name"]
    url = f"/repos/{repo_name}/issues"
    response = await gh.post(
        url,
                     data={
        'title': 'Thanks you soo much for installing simplifier',
        'body': 'Thanks!',
            },
        oauth_token=installation_access_token["token"]
                             )
    print(response)