# Task U1: Lab 3.5.7 - The Script to Test
from typing import Any, Optional

def json_search(key: str, input_object: Any) -> Optional[Any]:
    """
    Search for a key in a nested JSON object/list and return its value.
    Returns the first match found.
    """
    ret_val = None
    
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                return v
            else:
                ret_val = json_search(key, v)
                if ret_val is not None:
                    return ret_val
                    
    elif isinstance(input_object, list):
        for item in input_object:
            ret_val = json_search(key, item)
            if ret_val is not None:
                return ret_val
                
    return ret_val