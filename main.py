import os
import sqlite3
from sqlite3 import Connection
from typing import Any, Callable

import flask
from flask import Flask, g

from potyk_mu_back.albums.infra import AlbumRepo
from potyk_mu_back.genres.infra import GenreRepo


def create_app():
    app, get_db = _setup_app_and_db()

    @app.route("/")
    def index():
        cur = get_db().cursor()
        album_repo = AlbumRepo(cur)
        albums = album_repo.list_albums()

        genres_repo = GenreRepo(cur)
        genres = genres_repo.list_genres()

        return flask.render_template(
            "index.html",
            albums=albums,
            genres=genres,
        )

    return app


def _setup_app_and_db() -> tuple[Flask, Callable[[], Connection]]:
    app = Flask(__name__)
    app.secret_key = os.environ["FLASK_SECRET"]

    DATABASE = "main.db"

    def get_db() -> Connection | Any:
        db = getattr(g, "_database", None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
            db.row_factory = sqlite3.Row
        return db

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, "_database", None)
        if db is not None:
            db.close()

    return app, get_db
