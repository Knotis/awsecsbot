from distutils.core import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bootstrap/__init__.py').read(),
    re.M
).group(1)

with open("README.rst", "rb") as f:
    long_description = f.read().decode("utf-8")

setup(
    name='awsecsbot',
    version=version,
    description='Bot for managing Amazon Web Service Elastic Container Service deployments.',
    long_description=long_desctiption,
    author='Seth Denner',
    author_email='seth@knotis.com',
    url='https://github.com/Knotis/awsecsbot',
    packages=['awsecsbot'],
    entry_points = {
        'console_scripts': ['awsecsbot = awsecsbot.awsecsbot:run']
    }
)    
