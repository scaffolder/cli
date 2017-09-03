from setuptools import setup, find_packages

setup(
    name = "scaffolder",
    version = "0.1.2",
    author = "Goran Angelkovski",
    author_email = "goran@scaffolder.io",
    description = "High level project and application modeling tool based on the rules of Scaffolder DSL which utilizes Scaffolder aPaaS to generate all source code, configuration and testing files.",
    keywords = ['code generator', 'scaffolding', 'automatic coding'],
    license = "",
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