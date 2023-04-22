Sleep Log
=========

History
-------
This project was started to explore developing a website using the Pyramid web framework. The concept was to be a site that allows users to track sleep habits and quality over time.

In the interest of not managing my own authentication for users, this project quickly became a learning experience for using Google OAuth, and the site itself was never completed beyond the initial scaffolding.

Setup
-----
As this project is never intented to be finished or shared, setup instructions are very high level.

#. Clone repository
#. Install locally with ``pip install -e .[dev]``
#. Create a .env file to set keys for the sleeplog/models/config.py environment variables
    * AUTHTKT_SECRET and SESSION_SECRET can be any unique strings
    * Google OAuth 2.0 variables should be created using Google API Console obtained OAuth 2.0 credentials (further information is beyond the scope of this setup instructions and more information can be found at `https://developers.google.com/identity/protocols/oauth2`)
#. Run initialize_sleeplog_db development.ini to create local sqlite database file
#. Run ``pserve development.ini``
#. Open ``http://localhost:8080/``
