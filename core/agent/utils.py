import json
import re
from typing import Any, Dict
import requests


def parse_llm_json_block(raw: str) -> Dict[str, Any]:
    """
    Parse JSON that may be:
    - A JSON-encoded string containing a Markdown code block
    - A raw Markdown code block containing JSON
    - A plain JSON object string

    Returns the decoded Python dict.
    """
    text = raw

    # 1) Try: it's already plain JSON
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass

    # 2) Try: it's a JSON string that needs unescaping once
    try:
        text = json.loads(text)
    except json.JSONDecodeError:
        # if this fails, we just keep `text` as-is
        pass

    # 3) Strip Markdown code fences like ```json ... ``` or ``` ... ```
    fence_match = re.search(
        r"```(?:json)?\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if fence_match:
        json_str = fence_match.group(1)
    else:
        # Fallback: assume the whole thing is JSON
        json_str = text.strip()

    # 4) Final JSON parse
    return json.loads(json_str)

def download_image_bytes(url: str) -> bytes:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.content