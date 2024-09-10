from git import Repo
username = "OvAlexander"
project_name = "easy_readme"

user_socials = {
    "github": f"https://github.com/{username}",
    "website": "https://alexanderov.com",
    "linkedin": "https://www.linkedin.com/in/alexander-ov"
}

project_urls = {
    "contributors-url": f"https://github.com/{username}/{project_name}/graphs/contributors",
    "forks-url": f"https://github.com/{username}/{project_name}/forks",
    "stars-url": f"https://github.com/{username}/{project_name}/stargazers",
    "issues-url": f"https://github.com/{username}/{project_name}/issues",
    "license-url": f"https://github.com/{username}/{project_name}/blob/main/LICENSE",
    "contrib-rocks-url": f"https://contrib.rocks/image?repo={username}/{project_name}"
}

def create_shields(**kwargs)->str:
    options = { "contrib": "[![Contributors][contributors-shield]][contributors-url]", 
                "fork": "[![Forks][forks-shield]][forks-url]",
                "star": "[![Stargazers][stars-shield]][stars-url]", 
                "issues": "[![Issues][issues-shield]][issues-url]", 
                "license": "[![MIT License][license-shield]][license-url]", 
                "linkedin": "[![LinkedIn][linkedin-shield]][linkedin-url]"}
    shield_str = ""
    for key, value in kwargs.items():
        if key in options and value:
            shield_str += f"{options[key]}\n"
        elif key in options and not value:
            print(f"{key} exists but pass")
        else:
            print(f"{key} does not exist")
    return shield_str

def create_logo()->str:
    github_url = f"https://github.com/{username}/{project_name}"
    logo_file_path = "../images/logo.png"
    name = "easy_readme"
    logo_html = '''\
    <br />
    <div align="center">
    <a href="{github_url}">
        <img src="{logo_file_path}" alt="Logo" width="80" height="80">
    </a>
    <h3 align="center">{name}</h3>
    <p align="center">
        project_description
        <br />
        <a href="{github_url}"><strong>Explore the docs >></strong></a>
        <br />
        <br />
        <a href="{github_url}">View Demo</a>
        <a href="{github_url}/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
        <a href="{github_url}/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
    </p>
    </div>
    '''.format(**locals())
    return logo_html

def create_readme():
    file_path = "./output/README.md"
    file = open(file_path, "w")
    shields = create_shields(contrib = False, fork = True, star = False, issues = True, license = True, linkedin = True, test = True, test_false = False)
    logo = create_logo()
    file.write(f"{shields}{logo}")

def get_repo():
    repo_path = "./"
    repo = Repo(repo_path)
    repo_url = repo.remotes.origin.url
    repo_name = repo_url.split('.git')[0].split('/')[-1]
    return repo_name


if __name__ == "__main__":
    create_readme()
    # print(get_repo())