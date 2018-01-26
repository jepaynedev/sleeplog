from setuptools import setup

requires = [
    'pyramid',
    'waitress',
    'sqlalchemy',
    'pyramid_tm',
    'zope.sqlalchemy',
    'pyramid_jinja2',
]

setup(
    name='sleeplog',
    install_requires=requires,
    entry_points="""
    [paste.app_factory]
    main = sleeplog:main
    [console_scripts]
    initialize_sleeplog_db = sleeplog.initialize_db:main
    """,
)
