import os
import shutil
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV = ".env.prod"
ENV_PATH = os.path.join(BASE_DIR, ENV)
HEROKU = "heroku"
HEROKU_TOOLBELT = shutil.which(HEROKU)
GIT_REPO = os.path.join(BASE_DIR, ".git")


def config_set():
    if not HEROKU_TOOLBELT:
        raise FileNotFoundError(
            "Heroku toolbelt not found. Install it and try again."
        )
    if not os.path.isfile(ENV_PATH):
        raise FileNotFoundError(
            f"{ENV} does not exists. Create the file and try again"
        )
    if not os.path.exists(GIT_REPO):
        raise OSError(
            f"{GIT_REPO} is not a valid Git repo. Create a Git repo and try again"
        )
    with open(ENV_PATH, encoding="utf-8") as fp:
        for _, line in enumerate(fp):
            subprocess.run([HEROKU_TOOLBELT, "config:set", line.strip()])


if __name__ == "__main__":
    config_set()
