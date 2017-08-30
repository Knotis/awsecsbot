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
    description='Bot for managing and deploying docker containers to various sevice providers.',
    long_description=long_desctiption,
    author='Seth Denner',
    author_email='seth@knotis.com',
    url='https://github.com/Knotis/containerbot',
    packages=['containerbot'],
    entry_points = {
        'console_scripts': ['containerbot = containerbot.containerbot:run']
    },
    install_requires=[
        'Click'
    ]
)    
