#!/usr/bin/env python3
"""
Test the zundoko logic without fastmcp dependency
"""

import random

def zundoko() -> str:
    """
    Returns either "Zun" or "Doko" randomly.
    """
    choices = ["Zun", "Doko"]
    return random.choice(choices)

if __name__ == "__main__":
    print("Testing zundoko function:")
    for i in range(10):
        result = zundoko()
        print(f"Call {i+1}: {result}")
        assert result in ["Zun", "Doko"], f"Unexpected result: {result}"
    
    print("\nAll tests passed! The zundoko function works correctly.")