from app import get_stars
def test_zero_stars():
    github_user = 'normansaez'
    repos_name = 'asyncio'
    number = get_stars(github_user,repos_name)
    assert 0 == number

def test_more_stars():
    github_user = 'beekeeper-studio'
    repos_name = 'beekeeper-studio'
    number = get_stars(github_user,repos_name)
    assert number >= 0

