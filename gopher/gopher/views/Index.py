from flask import render_template, request, redirect, url_for
from flask.views import View

class Index(View):

    #By default, a view is set to have GET enabled. To allow POST, overwrite the defauls by uncommenting the following:
    #methods=['GET', 'POST']
    def dispatch_request(self):

        return render_template('index.html')