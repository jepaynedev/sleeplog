from setuptools import setup

requires = [
    'google_auth',
    'plaster_pastedeploy',
    'pyramid >= 1.9a',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='sleeplog',
    author='James Payne',
    author_email='contact@jepaynedev.com',
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = sleeplog:main',
        ],
        'console_scripts': [
            'initialize_sleeplog_db = sleeplog.scripts.initialize_db:main',
        ],
    },
)
