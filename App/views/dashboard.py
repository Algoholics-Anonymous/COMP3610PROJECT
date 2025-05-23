from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize

dashboard_views = Blueprint('dashboard_views', __name__, template_folder='../templates')

@dashboard_views.route('/', methods=['GET'])
def index_page():
    return render_template('dashboard.html')

@dashboard_views.route('/dashboard', methods=['GET'])
def dashboard_page():
    return render_template('dashboard.html')

# @dashboard_views.route('/init', methods=['GET'])
# def init():
#     initialize()
#     return jsonify(message='db initialized!')

@dashboard_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
