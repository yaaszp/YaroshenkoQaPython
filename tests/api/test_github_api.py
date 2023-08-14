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

test_data_1 = [("yaaszp", "Oleksii Yaroshenko"), ("octocat", "The Octocat")]


@pytest.mark.api_additional
@pytest.mark.parametrize("login, expected_name", test_data_1)
def test_user_exists(login, expected_name, github_api):
    user = github_api.get_user(login)
    assert user["login"] == login
    assert user["name"] == expected_name


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


test_data_2 = [("octocat", "Hello-World"), ("yaaszp", "YaroshenkoQaPython")]


@pytest.mark.api_additional
@pytest.mark.parametrize("login, repo_name", test_data_2)
def test_list_of_commits_can_be_found_(login, repo_name, github_api):
    body = github_api.get_commits(login, repo_name)

    # Check that the list from the body is not empty
    assert len(body) != 0


test_data_3 = [
    (
        "yaaszp",
        "YaroshenkoQaPython",
        "ee401468e6ace74a20549a9c12c08a0d8db947b0",
        "Frame structure",
        "Oleksii Yaroshenko",
    ),
    (
        "octocat",
        "Hello-World",
        "553c2077f0edc3d5dc5d17262f6aa498e69d6f8e",
        "first commit",
        "cameronmcefee",
    ),
]


@pytest.mark.api_additional
@pytest.mark.parametrize(
    "login, repo_name, expected_sha, expected_message, expected_name", test_data_3
)
def test_get_details_of_commit_(
    login, repo_name, expected_sha, expected_message, expected_name, github_api
):
    body = github_api.get_commits(login, repo_name)
    dic = body[-1]
    commit = dic["commit"]
    author = commit.get("author")

    assert dic["sha"] == expected_sha
    assert commit.get("message") == expected_message
    assert author.get("name") == expected_name


test_data_4 = [
    ("yaaszp", "YaroshenkoQaPython", "ee401468e6ace74a20549a9c12c08a0d8db947b0"),
    ("octocat", "Hello-World", "553c2077f0edc3d5dc5d17262f6aa498e69d6f8e"),
]


@pytest.mark.api_additional
@pytest.mark.parametrize("login, repo_name, sha", test_data_4)
def test_get_commit_by_sha_(login, repo_name, sha, github_api):
    body = github_api.get_commits_by_sha(login, repo_name, sha)
    assert body["sha"] == sha


test_data_5 = [
    ("octocat", "Hello-World", "553c2077f0edc3d5dc5d17262f6aa498e69d6f8e"),
    ("yaaszp", "YaroshenkoQaPython", "ee401468e6ace74a20549a9c12c08a0d8db947b0"),
]


@pytest.mark.api_additional
@pytest.mark.parametrize("login, repo_name, sha", test_data_5)
def test_get_commit_by_sha_as_param(login, repo_name, sha, github_api):
    body = github_api.get_commits_by_sha(login, repo_name, sha)

    assert body.get("sha") == sha


test_data_6 = [
    ("octocat", "Hello-World", "Cameron423698", "cameron@github.com"),
    (
        "yaaszp",
        "YaroshenkoQaPython",
        "a.s.yaroshenko.zp@gmail.com",
        "a.s.yaroshenko.zp@gmail.com",
    ),
]


@pytest.mark.api_additional
@pytest.mark.parametrize("login, repo_name, author, expected_email", test_data_6)
def test_get_commit_by_author(login, repo_name, author, expected_email, github_api):
    body = github_api.get_commits_by_author(login, repo_name, author)
    dic = body[0]
    commit = dic.get("commit")
    author = commit.get("author")
    assert author.get("email") == expected_email


test_data_7 = [
    ("octocat", "Hello-World", "Spaceghost", "Johnneylee.rollins@gmail.com"),
    (
        "yaaszp",
        "YaroshenkoQaPython",
        "a.s.yaroshenko.zp@gmail.com",
        "a.s.yaroshenko.zp@gmail.com",
    ),
]


@pytest.mark.api_additional
@pytest.mark.parametrize(
    "login, repo_name, name_committer, expected_email", test_data_7
)
def test_get_commit_by_committer(
    login, repo_name, name_committer, expected_email, github_api
):
    body = github_api.get_commits_by_committer(login, repo_name, name_committer)
    dic = body[0]
    commit = dic.get("commit")
    committer = commit.get("committer")
    assert committer.get("email") == expected_email


@pytest.mark.api_additional
def test_update_comment_without_authorization(github_api):
    body, status_code = github_api.update_comment("octocat", "Hello-World", "1146825")

    # We used method Patch without authorization.
    # So, server returned 401 status code (Unauthorized. The requested page needs a username and a password)
    # This action requires authorization
    assert status_code == 401
    assert body["message"] == "Requires authentication"
