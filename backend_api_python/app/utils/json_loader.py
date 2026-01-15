"""
json loader

load llm models api key from loacl json file
"""


import json
from typing import Dict, Any
import os

from app.utils.logger import get_logger

logger = get_logger(__name__)

def load_llm_api_key_config(path: str) -> Dict[str, Any]:
    """
    Load LLMs API Keys form local json file
    """
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load LLM API Key config: {e}")
        return {}

if __name__ == "__main__":
    result = load_llm_api_key_config("/home/jarvis/QuantDinger/backend_api_python/llm_models.json")
    print(result)
