import requests
import csv
import os

# Set your GitHub token here
token = "use your token here"
headers = {"Authorization": f"Bearer {token}"}

# Function to fetch all users in Barcelona with over 100 followers
def fetch_users():
    url = "token value :>100"
    response = requests.get(url, headers=headers)
    users = response.json().get("items", [])
    user_data = []
    
    for user in users:
        user_info = requests.get(user["url"], headers=headers).json()
        user_data.append({
            "login": user_info["login"],
            "name": user_info["name"] or "",
            "company": (user_info["company"] or "").strip().lstrip('@').upper(),
            "location": user_info["location"] or "",
            "email": user_info["email"] or "",
            "hireable": user_info["hireable"],
            "bio": user_info["bio"] or "",
            "public_repos": user_info["public_repos"],
            "followers": user_info["followers"],
            "following": user_info["following"],
            "created_at": user_info["created_at"]
        })
    
    return user_data

# Function to fetch repositories for each user in users.csv
def fetch_repositories(login):
    url = f"https://api.github.com/users/{login}/repos?per_page=500&sort=pushed"
    response = requests.get(url, headers=headers)
    repos = response.json()
    repo_data = []
    
    for repo in repos:
        repo_data.append({
            "login": login,
            "full_name": repo["full_name"],
            "created_at": repo["created_at"],
            "stargazers_count": repo["stargazers_count"],
            "watchers_count": repo["watchers_count"],
            "language": repo["language"] or "",
            "has_projects": repo["has_projects"],
            "has_wiki": repo["has_wiki"],
            "license_name": repo["license"]["key"] if repo["license"] else ""
        })
    
    return repo_data

# Function to write users.csv file
def write_users_to_csv(users):
    with open("users.csv", mode="w", newline='', encoding='utf-8') as file:
        fieldnames = ["login", "name", "company", "location", "email", "hireable", "bio", "public_repos", "followers", "following", "created_at"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

# Function to write repositories.csv file
def write_repositories_to_csv(repositories):
    with open("repositories.csv", mode="w", newline='', encoding='utf-8') as file:
        fieldnames = ["login", "full_name", "created_at", "stargazers_count", "watchers_count", "language", "has_projects", "has_wiki", "license_name"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(repositories)

# Main function to orchestrate data fetching and saving
def main():
    print("Fetching users...")
    users = fetch_users()
    write_users_to_csv(users)
    
    repositories = []
    for user in users:
        print(f"Fetching repositories for {user['login']}...")
        repositories.extend(fetch_repositories(user["login"]))
    
    write_repositories_to_csv(repositories)
    print("Data fetching complete! Check users.csv and repositories.csv.")

if __name__ == "__main__":
    main()
