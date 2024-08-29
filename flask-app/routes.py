from flask import Blueprint, render_template, Response
from .camera import Camera

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/video_feed')
def video_feed():
    return Response(Camera().video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
