#!/usr/bin/env bash
set -euo pipefail

echo "Install backend deps"
pip install -r backend/requirements.txt 2>/dev/null || true

echo "Install frontend deps"
(cd frontend && npm install) 2>/dev/null || true

