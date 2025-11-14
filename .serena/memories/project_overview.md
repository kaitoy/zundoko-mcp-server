# Zundoko MCP Server - Project Overview

## Purpose
A Model Context Protocol (MCP) server implementing the classic "Zundoko Kiyoshi" Japanese programming challenge using the fastmcp framework.

## Game Rules
1. Randomly output either "Zun" (heavy thumping sound) or "Doko" (light tapping sound)
2. Continue until the sequence "Zun Zun Zun Zun Doko" appears (4 Zuns + 1 Doko)
3. When pattern is found, elicit "Ki-yo-shi!" from user and end the game

## Architecture

### Core Files
- **server.py**: Main MCP server implementation with tools, resources, and prompts
- **client.py**: Example client using fastmcp.Client (stdio transport)
- **http_client.py**: Example client using HTTP transport with custom message handlers
- **test_logic.py**: Simple test script for the zundoko logic

### Dependencies
- fastmcp >= 2.12.4 (MCP framework)
- Python >= 3.8

### Server Components (server.py)

#### Global State
- `zundoko_history`: List storing all "Zun"/"Doko" calls
- `kiyoshi`: TextResource created when game is won (None otherwise)

#### Tools (3)
1. **get_zundoko()**: Returns random "Zun" or "Doko", adds to history, reports progress via Context methods
2. **check_kiyoshi()**: Checks for winning pattern, elicits response from user, validates answer
3. **reset_zundoko_kiyoshi()**: Clears history and resets game state

#### Resources (2)
1. **zundoko://history**: Returns complete history as JSON array
2. **zundoko://kiyoshi**: Returns completion message with timestamp (only after winning)

#### Resource Templates (1)
- **zundoko://history/{index}**: Returns specific item from history (1-based indexing)

#### Prompts (1)
- **explain_zundoko_kiyoshi()**: Returns game instructions

#### Helper Functions
- **_report_zundoko_progress()**: Reports progress tracking consecutive Zuns (0-5 scale)

### Client Examples

#### client.py
- Uses stdio transport via fastmcp.Client
- Demonstrates: listing capabilities, reading prompts, calling tools, reading resources

#### http_client.py  
- Uses HTTP transport with custom message handling
- Implements handlers for: sampling, elicitation, progress tracking, logging
- Demonstrates interactive gameplay with user input

## Key Features
- Uses MCP Context methods: info(), warning(), report_progress(), elicit(), sample()
- Sends resource_list_changed notifications when state changes
- Validates user responses and provides humorous feedback via LLM sampling
- Tracks progress toward winning pattern with detailed reporting
- Prevents further play after game is won ("The show is over")

## Testing
- `test_logic.py`: Basic non-MCP test of random selection logic
- No formal test framework detected

## Configuration
- Entry point: `zundoko-server` script defined in pyproject.toml
- Can run via: `python server.py` or `fastmcp run server.py --transport http`
