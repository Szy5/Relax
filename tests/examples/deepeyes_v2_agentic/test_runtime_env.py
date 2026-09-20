# Copyright (c) 2026 Relax Authors. All Rights Reserved.
"""Launch-script checks for DeepEyesV2 runtime env propagation."""

from __future__ import annotations

from pathlib import Path


EXAMPLE_DIR = Path(__file__).resolve().parents[3] / "examples" / "deepeyes_v2_agentic"

SEARCH_ENV_VARS = {
    "DEEPEYES_V2_SEARCH_CACHE_PATHS",
    "DEEPEYES_V2_SEARCH_BACKEND",
    "DEEPEYES_V2_SEARCH_RETRIEVER_URL",
    "DEEPEYES_V2_SEARCH_TOPK",
    "DEEPEYES_V2_SEARCH_BRAVE_API_KEY",
    "DEEPEYES_V2_SEARCH_BRAVE_ENDPOINT",
    "DEEPEYES_V2_SEARCH_TRUST_ENV",
    "DEEPEYES_V2_SEARCH_TIMEOUT",
    "DEEPEYES_V2_SEARCH_MAX_RETRIES",
    "DEEPEYES_V2_SEARCH_RETRY_BUDGET",
}


def test_training_scripts_forward_search_env_vars_to_ray_runtime_env():
    scripts = [
        EXAMPLE_DIR / "run_deepeyes_v2_agentic.sh",
        EXAMPLE_DIR / "run_deepeyes_v2_agentic_klx.sh",
    ]

    for script in scripts:
        text = script.read_text(encoding="utf-8")
        assert "env_vars" in text or "EXTRA_ENV_VARS_JSON" in text
        missing = [name for name in SEARCH_ENV_VARS if name not in text]
        assert not missing, f"{script.name} does not forward: {missing}"
