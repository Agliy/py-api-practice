from github import Github, Auth
from config import GITHUB_TOKEN, GITHUB_HOSTNAME

auth = Auth.Token(GITHUB_TOKEN)


g = Github(auth=auth, base_url=f"{GITHUB_HOSTNAME}")

for repo in g.get_user().get_repos():
    print(repo.full_name)

g.close()