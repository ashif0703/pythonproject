from github import Github

# Authenticate using a personal access token (replace with your token)
ACCESS_TOKEN = "your_personal_access_token"
g = Github(ACCESS_TOKEN)

# Function to fetch repository details
def get_repo_details(repo_name):
    try:
        repo = g.get_repo(repo_name)
        print(f"Repository: {repo.full_name}")
        print(f"Description: {repo.description}")
        print(f"Stars: {repo.stargazers_count}")
        print(f"Forks: {repo.forks_count}")
    except Exception as e:
        print(f"Error fetching repository: {e}")

# Function to create a new repository
def create_repo(repo_name, description="", private=True):
    try:
        user = g.get_user()
        repo = user.create_repo(name=repo_name, description=description, private=private)
        print(f"Repository '{repo.name}' created successfully!")
    except Exception as e:
        print(f"Error creating repository: {e}")

# Function to list issues of a repository
def list_issues(repo_name):
    try:
        repo = g.get_repo(repo_name)
        issues = repo.get_issues(state='open')
        for issue in issues:
            print(f"#{issue.number} - {issue.title}")
    except Exception as e:
        print(f"Error fetching issues: {e}")

# Example Usage
if __name__ == "__main__":
    repo_name = "octocat/Hello-World"  # Example public repo
    get_repo_details(repo_name)
    # create_repo("my-new-repo", "This is a test repo", private=False)
    # list_issues(repo_name)
