#!/usr/bin/env python
import pathlib


PROJECT_DIRECTORY = Path.cwd()


if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file }}" != "y":
        pathlib.Path(PROJECT_DIRECTORY / "AUTHORS.rst").unlink()
        pathlib.Path(PROJECT_DIRECTORY / "docs/authors.rst").unlink()

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = Path(PROJECT_DIRECTORY / "{{ cookiecutter.project_slug }}" / "cli.py")
        cli_file.unlink()

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        pathlib.Path(PROJECT_DIRECTORY / "LICENSE").unlink()

    issue_template_path = {
        "GitHub": ".github/ISSUE_TEMPLATE.md",
        "GitLab": ".gitlab/issue_templates/ISSUE_TEMPLATE.md",
        "Codeberg": ".gitea/ISSUE_TEMPLATE.md",
        "Default": ".github/ISSUE_TEMPLATE.md",
    }
    rename = issue_template_path.get("{{ cookiecutter.vcs }}", issue_template_path["Default"])
    pathlib.Path(PROJECT_DIRECTORY / "ISSUE_TEMPLATE.md").rename(PROJECT_DIRECTORY / rename)
