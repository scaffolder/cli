from setuptools import setup, find_packages

setup(
    name = "scaffolder",
    version = "0.1",
    author = "Goran Angelkovski",
    author_email = "goran@scaffolder.io",
    description = "This is an interactive command line tool for rapid prototyping and automatic code generation used for creating full-stack web, mobile, TV and other apps. It can be used to create wire-frames as well by utilizing any existing front-end or back-end framework.",
    keywords = ['code generator', 'scaffolding', 'automatic coding'],
    license = "",
    url = "https://scaffoder.io",
    scripts = ['scaffolder'],
    packages = find_packages()
)