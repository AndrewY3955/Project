#!/usr/bin/env sh
set -eu

PROJECT_ROOT=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
cd "$PROJECT_ROOT"

if [ -n "${PYTHON:-}" ]; then
    BASE_PYTHON=$PYTHON
elif command -v python3 >/dev/null 2>&1; then
    BASE_PYTHON=$(command -v python3)
elif command -v python >/dev/null 2>&1; then
    BASE_PYTHON=$(command -v python)
else
    printf '%s\n' "Python 3.10 or newer is required. Install Python, then rerun ./run.sh." >&2
    exit 1
fi

if ! "$BASE_PYTHON" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)'; then
    printf 'Python 3.10 or newer is required; selected interpreter is: ' >&2
    "$BASE_PYTHON" --version >&2
    exit 1
fi

VENV_PYTHON="$PROJECT_ROOT/.venv/bin/python"
if [ ! -x "$VENV_PYTHON" ]; then
    printf 'Creating .venv with %s...\n' "$BASE_PYTHON"
    "$BASE_PYTHON" -m venv "$PROJECT_ROOT/.venv"
fi

if ! "$VENV_PYTHON" -c 'import importlib.util; raise SystemExit(0 if importlib.util.find_spec("pandas") else 1)'; then
    printf '%s\n' "Installing project dependencies from requirements.txt..."
    "$VENV_PYTHON" -m pip install -r "$PROJECT_ROOT/requirements.txt"
fi

exec "$VENV_PYTHON" -m climate_dashboard.launcher "$@"
