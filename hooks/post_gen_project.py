#!/usr/bin/env python
import pathlib


PROJECT_DIRECTORY = pathlib.Path.cwd()


if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file }}" != "y":
        pathlib.Path(PROJECT_DIRECTORY / "AUTHORS.rst").unlink()
        pathlib.Path(PROJECT_DIRECTORY / "docs/authors.rst").unlink()

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = pathlib.Path(PROJECT_DIRECTORY / "{{ cookiecutter.project_slug }}" / "cli.py")
        cli_file.unlink()

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        pathlib.Path(PROJECT_DIRECTORY / "LICENSE").unlink()

    issue_template_path = {
        "GitHub": ".github/",
        "GitLab": ".gitlab/issue_templates/",
        "Codeberg": ".gitea/",
        "Default": ".github/",
    }
    rename = issue_template_path.get("{{ cookiecutter.vcs }}", issue_template_path["Default"])
    pathlib.Path(rename).mkdir(parents=True, exist_ok=True)
    pathlib.Path(PROJECT_DIRECTORY / "ISSUE_TEMPLATE.md").rename(PROJECT_DIRECTORY / rename / "ISSUE_TEMPLATE.md")
