"""Routes for core Flask app."""
from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
from .scheduler import scheduled_task

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/')
def home():
    for i in range(1):
       app.apscheduler.add_job(func=scheduled_task, trigger='date', args=[i], id='j'+str(i))
    """Landing page."""
    return redirect(url_for('/dashapp/'))
    #return render_template('index.html',
    #                       title='Plotly Flask Tutorial for Yeoh',
    #                       template='home-template',
    #                       body="This is an example homepage served with Flask from Chun-Yeow Yeoh.")
