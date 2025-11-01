import setuptools

# Read the contents of your README file / it is optional
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0" # project version

REPO_NAME = "End-to-end-ML-project-"
AUTHOR_USER_NAME = "Kartik-137"
SRC_REPO = "red_wine_quality_prediction"
AUTHOR_EMAIL = "kartikdahake11@gmail.com"

# setup the folder as a local package
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)