import requests


class GitHub:
    accept_header = {"Accept": "application/vnd.github+json"}

    def get_user(self, username):
        r = requests.get(
            f"https://api.github.com/users/{username}", headers=self.accept_header
        )
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name},
            headers=self.accept_header,
        )
        body = r.json()

        return body

    # Additional methods

    # link to documentation
    # https://docs.github.com/en/rest/emojis/emojis?apiVersion=2022-11-28

    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis", headers=self.accept_header)
        body = r.json()

        return body

    # link to documentation
    # https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28#list-commits

    def get_commits(self, owner, repo):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            headers=self.accept_header,
        )
        body = r.json()

        return body

    def get_commits_by_sha(self, owner, repo, sha):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}",
            headers=self.accept_header,
        )
        body = r.json()

        return body

    def get_commits_by_sha_as_param(self, owner, repo, sha):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            params={"sha": sha},
            headers=self.accept_header,
        )
        body = r.json()

        return body

    def get_commits_by_author(self, owner, repo, author):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            params={"author": author},
            headers=self.accept_header,
        )
        body = r.json()

        return body

    def get_commits_by_committer(self, owner, repo, committer):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            params={"committer": committer},
            headers=self.accept_header,
        )
        body = r.json()

        return body

    # link to documentation
    # https://docs.github.com/en/rest/issues/comments?apiVersion=2022-11-28

    def update_comment(self, owner, repo, id_comment):
        r = requests.patch(
            f"https://api.github.com/repos/{owner}/{repo}/issues/comments/{id_comment}",
            headers=self.accept_header,
            json={"body": "Me too"},
        )
        body = r.json()
        status_code = r.status_code
        return body, status_code
