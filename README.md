# Activity 8 – DevOps: Advanced GitHub Actions for a Flask App
Sunny Patel (100867748) • CSCI 4230 Advanced Web Development

## What’s included
- Minimal Flask API: `/hello`, `/echo`, `/items/<key>` with PUT/DELETE
- Unit tests with pytest + coverage
- GitHub Actions:
  - CI matrix (3.10, 3.11, 3.12) running tests + coverage
  - Flake8 lint workflow
  - CodeQL static analysis
  - Codecov upload
- Dependabot weekly updates

## Run locally (Windows PowerShell)
CODE BLOCK GOES HERE (powershell)
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python .\app.py
CODE BLOCK ENDS

Open http://127.0.0.1:5000/hello

## Run tests locally
CODE BLOCK GOES HERE (powershell)
pytest -q
pytest -q --cov=app --cov-report=term --cov-report=xml
CODE BLOCK ENDS

## Push to GitHub
CODE BLOCK GOES HERE (bash)
git init
git add .
git commit -m "activity 8 initial"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
CODE BLOCK ENDS

## Codecov setup
- Public repo: no token needed.
- Private repo: create token in Codecov and add as GitHub secret `CODECOV_TOKEN`.
- Workflow already uploads `coverage.xml`.

## Files
- `app.py` — Flask app
- `test_app.py` — pytest tests
- `.github/workflows/test.yml` — matrix + coverage + Codecov
- `.github/workflows/lint.yml` — flake8
- `.github/workflows/codeql.yml` — CodeQL security
- `.github/dependabot.yml` — weekly pip updates
- `.flake8`, `requirements.txt`, `.gitignore`

## Endpoints
- `GET /hello` → `{"message":"Hello, World!"}`
- `POST /echo` → mirrors request JSON with 201
- `PUT /items/<key>` body: `{"value": "..."}`
- `DELETE /items/<key>` → `{"deleted": "<key>"}`

## What to submit
- ZIP of the repo
- Screenshots of passing GitHub Actions runs:
  - CI matrix (tests + coverage)
  - Lint (flake8)
  - CodeQL analysis
- Short note: everything passed on push; no issues beyond typical `flake8` line-length (handled via `.flake8`).

## Troubleshooting
- **pytest not found**: ensure `pytest` and `pytest-cov` exist in `requirements.txt` and re-install.
- **Codecov fails**: verify `coverage.xml` is produced; add `CODECOV_TOKEN` for private repos.
- **Flake8 errors**: follow output or adjust `.flake8` rules where justified.
- **Matrix failures**: confirm Python compatibility or narrow versions in `test.yml`.
