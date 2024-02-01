import requests
import yaml

def get_stars(repo_user, repo_name, token=None):
    # Build URL API de GitHub to obtain information of the stars
    url = f'https://api.github.com/repos/{repo_user}/{repo_name}/stargazers'
    
    # Build tokens (if any)
    headers = {}
    if token:
        headers['Authorization'] = f'Token {token}'
    
    # Make the GET
    response = requests.get(url, headers=headers)
    
    # Check if 200 is successful 
    if response.status_code == 200:
        # get the response
        stars = response.json()
        # Print informaion 
#        print(f'Stars Repo: {repo_user}/{repo_name}:')
        count = 0
        for estrella in stars:
#            print(f'- {estrella["login"]}')
            count += 1
#        print(stars)
        with open('fullyaml.yaml', 'w') as archivo:
            yaml.dump(stars, archivo, default_flow_style=False)
        format_url = [url,count]
        number_stars = yaml.dump(format_url,default_flow_style=False)
        print(number_stars)
    else:
        # Print a message if the response was not correct (not 200)
        print(f'Error to obtain star from {repo_user}/{repo_name}. status {response.status_code}')

####################################################################################################
github_user = 'normansaez'
repos_name = 'asyncio'

github_user = 'beekeeper-studio'
repos_name = 'beekeeper-studio'

get_stars(github_user,repos_name)
print('new test')
