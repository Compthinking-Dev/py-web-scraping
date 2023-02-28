from github import Github


API_KEY = "YOUR_API_KEY"
g = Github(API_KEY)


def org_profile(org_name):
    org = g.get_organization(org_name)
    repos = org.get_repos()
    print(f"{org_name} has {repos.totalCount} repos. First 3:")    
    for repo in repos[:3]:
        print(f"{repo.full_name} ({repo.stargazers_count} Stars) - {repo.description}")
        print(f"Languages: {repo.get_languages()}")


def user_profile(user_name):
    user = g.get_user(user_name)
    print(f"User {user_name} has {user.public_repos} public repos and {user.followers} followers")
    star = 0
    fork = 0
    for repo in user.get_repos():
        star += repo.stargazers_count
        fork += repo.forks_count
    print(f"His projects have {star} Stars and {fork} Forks in total")


if __name__ == '__main__':
    org_profile("mozilla")
    print("---")
    user_profile("torvalds")
