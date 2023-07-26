import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    # Additional methods

    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body

    def get_commits(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
        body = r.json()

        return body

    def get_commits_by_sha(self, owner, repo, sha):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}")
        body = r.json()

        return body

    def get_commits_by_sha_as_param(self, owner, repo, sha):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits", params={"sha": sha}
        )
        body = r.json()

        return body

    def get_commits_by_author(self, owner, repo, author):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            params={"author": author},
        )
        body = r.json()

        return body

    def get_commits_by_committer(self, owner, repo, committer):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            params={"committer": committer},
        )
        body = r.json()

        return body
