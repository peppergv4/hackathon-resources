import requests
import datetime as dt
import json
import sys
import os
from requests.auth import HTTPBasicAuth


def getMayhemHeroesProjects(api, headers, auth, page=1):
    projects = []
    endpoint = api + '/orgs/mayhemheroes/repos?q=type=forks&per_page=100&page=' + str(page)
    try:
        response = requests.get(endpoint, headers=headers, auth=auth)
        results = response.json()
        for project in results:
            projects.append(project['name'].lower())
        if len(results) == 100:
            projects = projects + getMayhemHeroesProjects(api, headers, auth, (page + 1))
    except BaseException as e:
        print('Error getting heroes repos.')
        print(e)
        sys.exit(1)
    return projects

def getOSSFuzz(api, headers, auth):
    endpoint = api + '/repos/google/oss-fuzz/contents/projects'
    try:
        response = requests.get(endpoint, headers=headers, auth=auth)
        results = response.json()
    except BaseException as e:
        print('Error getting OSS Fuzz Projects.')
        print(e)
        sys.exit(1)
    projects = []
    for v in results:
        projects.append(v['name'].lower())
    return projects

def getRepos(api, headers, auth, range=0, page=1):
    repos = []
    date_end = (dt.datetime.now() - dt.timedelta(days=range)).strftime('%Y-%m-%d')
    date_start = (dt.datetime.now() - dt.timedelta(days=range+1)).strftime('%Y-%m-%d')
    date_range = date_start + '..' + date_end
    query = 'pushed:' + date_range + '+fork:not+stars:>100+language:C+language:"C++"+language:Python+language:Rust+language:Go+language:Fortran+language:Ada+language:Java'
    #Note: this is incredibly slow but necessary - Github limits the per_page results to 100, and the total results to 1000. Splitting it up by date gets us some results (but not all). 
    endpoint = api + '/search/repositories?q=' + query + '&per_page=100&page=' + str(page)
    try:
        #print(endpoint)
        response = requests.get(endpoint, headers=headers, auth=auth)
        results = response.json()
        for repo in results['items']:
            repos.append(repo['html_url'])
        #if len(results['items']) == 100 and page < 10:
        #    repos = repos + getRepos(api, headers, auth, range, (page + 1))
        if range + 1 < 180:
            repos = repos + getRepos(api, headers, auth, (range+1), page)
    except BaseException as e:
        print('Error getting repos.')
        print(e)
        sys.exit(1)
    return repos

if __name__ == '__main__':

    if(sys.version_info.major < 3):
        print('Please use Python 3.x or higher')
        sys.exit(1)

    gh_api = 'https://api.github.com'
    gh_headers = {
        'Content-Type': 'application/vnd.github.v3+json'
    }

    try:
        gh_token = os.environ['GITHUB_TOKEN']
        gh_user = os.environ['GITHUB_USER']
    except KeyError as e:
        print('Error: please set the GITHUB_TOKEN and GITHUB_USER variables.')
        sys.exit(1)

    gh_auth = HTTPBasicAuth(gh_user, gh_token)

    repos = getRepos(gh_api, gh_headers, gh_auth)
    oss = getOSSFuzz(gh_api, gh_headers, gh_auth)
    heroes = getMayhemHeroesProjects(gh_api, gh_headers, gh_auth)
    print(len(repos))
    print(len(oss))
    print(len(heroes))
    for r in repos:
        rname = r.split('/')[4].lower()
        if rname in oss:
            continue
        elif rname in heroes:
            continue
        else:
            print(r)
