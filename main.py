from git import Repo
username = "OvAlexander"
project_name = "easy_readme"

user_socials = {
    "github": f"https://github.com/{username}",
    "website": "https://alexanderov.com",
    "linkedin": "https://www.linkedin.com/in/alexander-ov"
}

def create_links(**kwargs)->str:
    url_str = ""
    base_gh_url = f"https://github.com/{username}/{project_name}/"
    options = {
        "contrib": f"[contributors-url]: {base_gh_url}graphs/contributors",
        "fork": f"[forks-url]: {base_gh_url}forks",
        "star": f"[stars-url]: {base_gh_url}stargazers",
        "issues": f"[issues-url]: {base_gh_url}issues",
        "license": f"[license-url]: {base_gh_url}blob/main/LICENSE",
        "contrib" : f"[contrib-rocks-url]: https://contrib.rocks/image?repo={username}/{project_name}",
        "linkedin": "[linkedin-url]: https://linkedin.com/in/alexander-ov"
    }
    for key, value in kwargs.items():
        if key in options and value: url_str += f"{options[key]}\n"
    return url_str

def create_imgs(**kwargs)->str:
    img_str = ""
    base_shield_url = "https://img.shields.io/github/"
    end_shield_url = f"/{username}/{project_name}.svg?style=for-the-badge"
    options = {
        "contrib": f"[contributors-shield]: {base_shield_url}contributers{end_shield_url}",
        "fork": f"[forks-shield]: {base_shield_url}forks{end_shield_url}",
        "star": f"[stars-shield]: {base_shield_url}stars{end_shield_url}",
        "issues": f"[issues-shield]: {base_shield_url}issues{end_shield_url}",
        "license": f"[license-shield]: {base_shield_url}license{end_shield_url}",
        "linkedin": "[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555"
    }
    for key, value in kwargs.items():
        if key in options and value: img_str += f"{options[key]}\n"
    return img_str


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

def create_readme(**kwargs):
    file_path = "./output/README.md"
    file = open(file_path, "w")
    shields = create_shields(**kwargs)
    logo = create_logo()
    links = create_links(**kwargs)
    imgs = create_imgs(**kwargs)
    file.write(f"{shields}{logo}\n{links}\n{imgs}")

def get_repo():
    repo_path = "./"
    repo = Repo(repo_path)
    repo_url = repo.remotes.origin.url
    repo_name = repo_url.split('.git')[0].split('/')[-1]
    return repo_name


if __name__ == "__main__":
    create_readme(contrib = False, fork = True, star = False, issues = True, license = True, linkedin = True, test = True, test_false = False)
    # print(get_repo())