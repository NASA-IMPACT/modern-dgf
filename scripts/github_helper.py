import subprocess

import typer
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


def authenticate_with_gh():
    """Invoke the GitHub CLI authentication process."""
    try:
        subprocess.run(["gh", "auth", "login"], check=True)
        print("Authentication successful!")
    except subprocess.CalledProcessError:
        print("Authentication failed. Please try again.")


def run_gh_command(command):
    """Execute a GitHub CLI command and return its output."""
    gh_command = " ".join(["gh", *command.split()])
    result = subprocess.run(gh_command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error executing command: {result.stderr}")
        return None

    return result.stdout


def create_issues(repo_name, title, body):
    """Create a new GitHub repository using the specified name."""
    command = f'issue create --repo {repo_name} --title "{title}" --body "{body}"'
    output = run_gh_command(command)
    if output:
        print(f"Successfully created issue: {output}")
    else:
        print("Failed to create issue.")


def prepare_github_cli():
    typer.echo(
        "In order to use this script, you must have the GitHub CLI installed. To install it, please visit https://cli.github.com/. \n Once installed, please run `gh auth login` to authenticate with GitHub."
    )
    typer.echo(
        "You will now be asked to log in to your GitHub account. Please note we do not store your login information. This will solely be used by the official github cli for authentication purposes in order to create issues on your repository. "
    )
    repo_org = input(
        "Enter the name of the organization where you forked the repository: "
    )

    repo_name = input("Enter the name of the new GitHub repository: ")

    authenticate_with_gh()
    return f"{repo_org}/{repo_name}"
