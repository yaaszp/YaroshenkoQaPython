import pytest


# The required tests from the course


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 13
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# The additional tests


@pytest.mark.api_additional
def test_user_exists(github_api):
    user = github_api.get_user("yaaszp")
    assert user["login"] == "yaaszp"
    assert user["name"] == "Oleksii Yaroshenko"


@pytest.mark.api_additional
def test_repo_can_be_found(github_api):
    body = github_api.search_repo("YaroshenkoQaPython")
    values_of_items = body["items"]
    dic = values_of_items[0]
    value_of_owner = dic.get("owner")

    # Check login name of owner repo
    assert value_of_owner.get("login") == "yaaszp"

    # Check total_count by name of repo
    assert body["total_count"] == 1


@pytest.mark.api_additional
def test_get_emojis(github_api):
    body = github_api.get_emojis()

    # Check that json file with emojis is not empty
    assert len(body.items()) != 0


@pytest.mark.api_additional
def test_list_of_commits_not_found(github_api):
    body = github_api.get_commits("owner", "repo")

    # Check message Resource not found
    assert body["message"] == "Not Found"


@pytest.mark.api_additional
def test_list_of_commits_can_be_found_(github_api):
    body = github_api.get_commits("octocat", "Hello-World")

    # Check that the list from the body is not empty
    assert len(body) != 0


@pytest.mark.api_additional
def test_list_of_commits_can_be_found(github_api):
    body = github_api.get_commits("yaaszp", "YaroshenkoQaPython")

    # Check that the list from the body is not empty
    assert len(body) != 0


@pytest.mark.api_additional
def test_get_details_of_commit_(github_api):
    body = github_api.get_commits("yaaszp", "YaroshenkoQaPython")
    dic = body[-1]
    commit = dic["commit"]
    author = commit.get("author")

    assert dic["sha"] == "ee401468e6ace74a20549a9c12c08a0d8db947b0"
    assert commit.get("message") == "Frame structure"
    assert author.get("name") == "Oleksii Yaroshenko"


@pytest.mark.api_additional
def test_get_details_of_commit(github_api):
    body = github_api.get_commits("octocat", "Hello-World")
    dic = body[-1]
    commit = dic["commit"]
    author = commit.get("author")

    assert dic["sha"] == "553c2077f0edc3d5dc5d17262f6aa498e69d6f8e"
    assert commit.get("message") == "first commit"
    assert author.get("name") == "cameronmcefee"


@pytest.mark.api_additional
def test_get_commit_by_sha_(github_api):
    body = github_api.get_commits_by_sha(
        "yaaszp", "YaroshenkoQaPython", "ee401468e6ace74a20549a9c12c08a0d8db947b0"
    )
    assert body["sha"] == "ee401468e6ace74a20549a9c12c08a0d8db947b0"


@pytest.mark.api_additional
def test_get_commit_by_sha(github_api):
    body = github_api.get_commits_by_sha(
        "octocat", "Hello-World", "553c2077f0edc3d5dc5d17262f6aa498e69d6f8e"
    )
    assert body["sha"] == "553c2077f0edc3d5dc5d17262f6aa498e69d6f8e"


@pytest.mark.api_additional
def test_get_commit_by_sha_as_param(github_api):
    body = github_api.get_commits_by_sha(
        "octocat", "Hello-World", "553c2077f0edc3d5dc5d17262f6aa498e69d6f8e"
    )

    assert body.get("sha") == "553c2077f0edc3d5dc5d17262f6aa498e69d6f8e"


@pytest.mark.api_additional
def test_get_commit_by_author(github_api):
    body = github_api.get_commits_by_author("octocat", "Hello-World", "Cameron423698")
    dic = body[0]
    commit = dic.get("commit")
    author = commit.get("author")
    assert author.get("email") == "cameron@github.com"


@pytest.mark.api_additional
def test_get_commit_by_author_(github_api):
    body = github_api.get_commits_by_author(
        "yaaszp", "YaroshenkoQaPython", "a.s.yaroshenko.zp@gmail.com"
    )
    dic = body[0]
    commit = dic.get("commit")
    author = commit.get("author")
    assert author.get("email") == "a.s.yaroshenko.zp@gmail.com"


@pytest.mark.api_additional
def test_get_commit_by_committer(github_api):
    body = github_api.get_commits_by_committer("octocat", "Hello-World", "Spaceghost")
    dic = body[0]
    commit = dic.get("commit")
    committer = commit.get("committer")
    assert committer.get("email") == "Johnneylee.rollins@gmail.com"


@pytest.mark.api_additional
def test_get_commit_by_committer_(github_api):
    body = github_api.get_commits_by_committer(
        "yaaszp", "YaroshenkoQaPython", "a.s.yaroshenko.zp@gmail.com"
    )
    dic = body[0]
    commit = dic.get("commit")
    committer = commit.get("committer")
    assert committer.get("email") == "a.s.yaroshenko.zp@gmail.com"
