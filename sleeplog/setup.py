from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

setup(
    name='sleeplog',
    install_requires=requires,
    entry_points="""
    [paste.app_factory]
    main = sleeplog:main
    """,
)
