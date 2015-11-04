#! /usr/bin/env python3

""" For deployment on ix under CGI """

import site
site.addsitedir("/home/users/djg/public_html/proj2-flask/env/lib/python3.4/site-packages")

from wsgiref.handlers import CGIHandler
from syllabus import app

CGIHandler().run(app)
