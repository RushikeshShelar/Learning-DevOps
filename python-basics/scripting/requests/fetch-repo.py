import argparse
import requests

parser = argparse.ArgumentParser(description='Fetch repository details from GitHub')

parser.add_argument('-u', '--username', type=str, required=True, help='GitHub username')
parser.add_argument('-r', '--repo', type=str, help='Repository name')

args = parser.parse_args()

def fetch_repo_details(username, repo=None):
    url = f"https://api.github.com/users/{username}/repos"

    if repo:
        url = f"https://api.github.com/repos/{username}/{repo}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")        
    

if __name__ == "__main__":
    if args.repo:
        repo_details = fetch_repo_details(args.username, args.repo)
        if repo_details:
            print(f"Repository Name: {repo_details['name']}")
            print(f"Description: {repo_details.get('description', 'No description available')}")
            print(f"URL: {repo_details['html_url']}")
            print(f"Stars: {repo_details['stargazers_count']}")
            print(f"Forks: {repo_details['forks_count']}")
            print(f"Language: {repo_details['language']}")
            print(f"Created At: {repo_details['created_at']}")
            print(f"Updated At: {repo_details['updated_at']}")
            print(f"Owner: {repo_details['owner']['login']}")
        else:
            print(f"Repository '{args.repo}' not found for user '{args.username}'.")
    else:
        repos = fetch_repo_details(args.username)
        if repos:
            for repo in repos:
                print(f"Repository Name: {repo['name']}, URL: {repo['html_url']}")

