# app.py
# author: sunny patel (100867748)
# course: csci 4230 advanced web development
# activity 8: devops — minimal flask api with tests and ci

from __future__ import annotations  # future annotations for 3.10+  # inline: keeps typing clean
from flask import Flask, jsonify, request, abort  # inline: flask core imports
from typing import Dict  # inline: explicit type for in-memory store


def create_app() -> Flask:
    """build and return a flask app instance."""
    app = Flask(__name__)  # inline: create app

    # simple in-memory kv store for demo endpoints (resets each run)
    store: Dict[str, str] = {}  # inline: ephemeral data for put/delete tests

    @app.route("/hello", methods=["GET"])
    def hello() -> tuple:
        """health/greeting endpoint used by unit tests."""
        return jsonify(message="Hello, World!"), 200  # inline: json response + 200

    @app.route("/echo", methods=["POST"])
    def echo() -> tuple:
        """echo back received json, status 201 (create semantics for the lab)."""
        data = request.get_json(force=True, silent=True)  # inline: parse json safely
        if data is None:  # inline: guard bad payloads
            abort(400, description="invalid json")
        return jsonify(data), 201  # inline: mirror payload

    @app.route("/items/<key>", methods=["PUT"])
    def put_item(key: str) -> tuple:
        """store a value under key in the in-memory store."""
        payload = request.get_json(force=True, silent=True)  # inline: parse json
        if not isinstance(payload, dict) or "value" not in payload:  # inline: validate shape
            abort(400, description="expected {'value': ...}")
        store[key] = str(payload["value"])  # inline: coerce to str for predictability
        return jsonify(key=key, value=store[key]), 200  # inline: echo saved pair

    @app.route("/items/<key>", methods=["DELETE"])
    def delete_item(key: str) -> tuple:
        """delete key from the store if present."""
        if key not in store:  # inline: 404 when absent
            abort(404, description="key not found")
        del store[key]  # inline: remove
        return jsonify(deleted=key), 200  # inline: confirm deletion

    return app  # inline: return configured app


# expose `app` for `pytest` and `flask run`
app = create_app()  # inline: default app

if __name__ == "__main__":
    # inline: debug server for local dev only (not used in ci)
    app.run(host="127.0.0.1", port=5000, debug=True)
