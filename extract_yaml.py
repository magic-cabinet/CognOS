#!/usr/bin/env python3
"""
extract_yaml.py

Extracts the contents of triple-backtick YAML code fences from a string.

Example fenced block formats handled (case-insensitive for 'yaml'):
    ```yaml
    key: value
    ```
    ``` yaml
    key: value
    ```

If multiple YAML fences are present, their contents are concatenated with a
single blank line between them. If none are found, an empty string is returned.
"""

from __future__ import annotations

import re
from typing import Final


# Match ```yaml ... ``` (with optional space before yaml, case-insensitive), non-greedy body.
_YAML_FENCE_RE: Final[re.Pattern[str]] = re.compile(
    r"```[ \t]*yaml[ \t]*\r?\n(.*?)\r?\n?```",
    re.IGNORECASE | re.DOTALL,
)


def extract_yaml(text: str) -> str:
    """
    Return the concatenated contents of all YAML code-fenced blocks in `text`,
    excluding the fence markers themselves.

    Parameters
    ----------
    text : str
        A string that may contain one or more triple-backtick YAML code blocks.

    Returns
    -------
    str
        The inner contents of all matched YAML fences, joined by a blank line.
        Returns an empty string if no YAML fences are found.
    """
    blocks = _YAML_FENCE_RE.findall(text)
    return "\n\n".join(b.strip("\r\n") for b in blocks)


__all__ = ["extract_yaml"]
