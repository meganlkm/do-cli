import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def getReqs(reqfile='requirements.txt'):
    reqs = []
    with open(os.path.join(os.path.dirname(__file__), reqfile)) as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.strip()
            if len(line) and line[0] != "#":
                reqs.append(line)
    return reqs


REQUIREMENTS = getReqs()


setup(
    name='do_cli',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    description='manage digitalocean stuff',
    long_description='manage digitalocean stuff',
    url='https://github.com/meganlkm/do-cli',
    author='DevStuff.IO',
    author_email='megan@devstuff.io',
    install_requires=REQUIREMENTS,
    entry_points="""
        [console_scripts]
        do-cli=do_cli.cli:cli
    """
)
