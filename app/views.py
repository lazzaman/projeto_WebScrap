from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

sample_page = Blueprint('sample_page', 'sample_page', template_folder='templates')


@sample_page.route('/sample')
def get_sample():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@sample_page.route('/notas')
def get_notas():
    try:
        return render_template('notas.html')
    except TemplateNotFound:
        abort(404)
