from github import Github

# Replace with your GitHub personal access token
github_token = "your_personal_access_token"

def authenticate_github(token):
    """Authenticate to GitHub using a personal access token."""
    return Github(token)

def list_repositories(g):
    """List all repositories for the authenticated user."""
    user = g.get_user()
    repos = user.get_repos()
    for repo in repos:
        print(repo.name)

def create_repository(g, repo_name, description="", private=True):
    """Create a new repository on GitHub."""
    user = g.get_user()
    repo = user.create_repo(name=repo_name, description=description, private=private)
    print(f"Repository '{repo.name}' created successfully.")

if __name__ == "__main__":
    g = authenticate_github(github_token)
    print("Your repositories:")
    list_repositories(g)
    
    # Example: Create a new repository
    repo_name = "my-new-repo"
    description = "This is a test repository created using PyGithub."
    create_repository(g, repo_name, description)
