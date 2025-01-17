#!/usr/bin/env python
import pathlib
import shutil

PROJECT_DIRECTORY = pathlib.Path.cwd()


if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file }}" != "y":
        pathlib.Path(PROJECT_DIRECTORY / "AUTHORS.rst").unlink()
        pathlib.Path(PROJECT_DIRECTORY / "docs/authors.rst").unlink()

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = pathlib.Path(
            PROJECT_DIRECTORY / "{{ cookiecutter.project_slug }}" / "cli.py"
        )
        cli_file.unlink()

    if "Proprietary" == "{{ cookiecutter.project_license }}":
        pathlib.Path(PROJECT_DIRECTORY / "LICENSE").unlink()

    issue_template_path = {
        "GitHub": ".github/",
        "GitLab": ".gitlab/issue_templates/",
        "Codeberg": ".gitea/",
        "Default": ".github/",
    }
    rename = issue_template_path.get(
        "{{ cookiecutter.vcs }}", issue_template_path["Default"]
    )
    pathlib.Path(rename).mkdir(parents=True, exist_ok=True)
    pathlib.Path(PROJECT_DIRECTORY / "ISSUE_TEMPLATE.md").rename(
        PROJECT_DIRECTORY / rename / "ISSUE_TEMPLATE.md"
    )

    if "y" == "{{cookiecutter.use_poetry}}":
        pathlib.Path(PROJECT_DIRECTORY / "requirements_dev.txt").unlink()
        pathlib.Path(PROJECT_DIRECTORY / "setup.py").unlink()
        pathlib.Path(PROJECT_DIRECTORY / "MANIFEST.in").unlink()

    if "y" == "{{cookiecutter.use_vscode}}":
        shutil.rmtree(pathlib.Path(PROJECT_DIRECTORY / ".vscode"), ignore_errors=True)
        pathlib.Path(PROJECT_DIRECTORY / "vscode").rename(PROJECT_DIRECTORY / ".vscode")
    else:
        pathlib.Path(PROJECT_DIRECTORY / "vscode").unlink()
