#!/usr/bin/env python3

'''
This script gets the total number of stars a
GitHub user received.
Take the name of the user as an argument.
'''


import sys
import requests
from pygal import Bar

def get_api_url(user):
    '''Return the GitHub API URL.'''
    return 'https://api.github.com/users/' + user + '/repos'


def get_repos(user):
    '''Return the list of repositories.'''
    repos = []
    url = get_api_url(user)
    while True:
        response = requests.get(url)
        repos.extend(response.json())
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            break
    return repos


def get_stars_count(repos):
    '''Return the total number of stars.'''
    stars_count = 0
    for repo in repos:
        stars_count += repo['stargazers_count']
    return stars_count



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <user>'.format(sys.argv[0]))
        sys.exit(1)
    user = sys.argv[1]
    repos = get_repos(user)
    stars_count = get_stars_count(repos)
    print("{} has a total of {} stars.".format(user, stars_count))

