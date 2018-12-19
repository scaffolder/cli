from setuptools import setup, find_packages

setup(
    name = "scaffolder",
    version = "0.1.3",
    author = "Goran Angelkovski",
    author_email = "goran@scaffolder.io",
    description = "High level project and application modeling tool based on the rules of Scaffolder DSL which utilizes Scaffolder aPaaS to generate all source code, configuration and testing files.",
    long_description = "Interactive command line tool for rapid prototyping and automatic code generation used for creating full-stack web, mobile, TV and other apps. It can be used to create wire-frames as well by utilizing any existing front-end or back-end framework. It can generate boilerplate skeleton for your project according to strict rules and naming conventions for the files and folders been used. Trough a simple and easy command line oriented interface it creates multiple YAML files and based on it generates all the code and configuration files in a predefined directory tree.",
    keywords = ['code generator', 'scaffolding', 'automatic coding'],
    license = "MIT",
    url = "https://scaffoder.io",
    scripts = ['scaffolder'],
    packages = find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Topic :: Software Development :: Code Generators'
    ],
)
