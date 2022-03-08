"""This test the homepage"""


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"introduction" in response.data

# def test_request_about(client):
#     """This makes the index page"""
#     response = client.get("/about")
#     assert response.status_code == 200
#     assert b"About Page" in response.data

def test_request_git(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b" GIT" in response.data

def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_python(client):
    """This makes the index page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Python & Flask" in response.data

def test_request_githubactions(client):
    """This makes the index page"""
    response = client.get("/githubactions")
    assert response.status_code == 200
    assert b"GitHub Actions" in response.data

# def test_request_page2(client):
#     """This makes the index page"""
#     response = client.get("/page2")
#     assert response.status_code == 200
#     assert b"Page 2" in response.data
