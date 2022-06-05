from flask import Blueprint

bp = Blueprint('index', __name__, url_prefix='/')
# rg = Blueprint('register', __name__, url_prefix='/register')

from .import index_view
# from .import  auth_routes, bs_mods_routes, routes