import os

from flask import send_from_directory

from app.routes import bp


@bp.route('/icon/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, '..', 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@bp.route('/icon/favicon-16x16.png')
def favicon_16_png():
    return send_from_directory(os.path.join(bp.root_path, '..', 'static'),
                               'favicon-16x16.png', mimetype='image/png')


@bp.route('/icon/favicon-32x32.png')
def favicon_32_png():
    return send_from_directory(os.path.join(bp.root_path, '..', 'static'),
                               'favicon-32x32.png', mimetype='image/png')


@bp.route('/icon/apple-touch-icon.png')
def apple_png():
    return send_from_directory(os.path.join(bp.root_path, '..', 'static'),
                               'apple-touch-icon.png', mimetype='image/png')


@bp.route('/icon/android-chrome-192x192.png')
def android_chrome_192_png():
    return send_from_directory(os.path.join(bp.root_path, '..', 'static'),
                               'android-chrome-192x192.png', mimetype='image/png')


@bp.route('/icon/android-chrome-512x512.png')
def android_chrome_512_png():
    return send_from_directory(os.path.join(bp.root_path, '..', 'static'),
                               'android-chrome-512x512.png', mimetype='image/png')


@bp.route('/css/style.css')
def style_css():
    return send_from_directory(os.path.join(bp.root_path, '..', 'static'),
                               'style.css', mimetype='text/css')
