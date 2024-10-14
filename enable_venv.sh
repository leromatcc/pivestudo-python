
## criar estruturas do venv
# python3 -m venv .venv

#enable
source .venv/bin/activate


# disable
# deactivate

which python

pip install uv
cd example/
uv add ruff
uv run ruff check
uv tool install ruff
uv tool update-shell
ruff --version