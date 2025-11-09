# Zundoko MCP Server

A sample Model Context Protocol (MCP) server using [fastmcp](https://github.com/jlowin/fastmcp) that implements the classic "Zundoko Kiyoshi" programming challenge.

## Features

The server provides tools, resources, resource templates, and prompts to play the Zundoko Kiyoshi game.

### Tools

- **get_zundoko()**: Returns either "Zun" or "Doko" randomly and adds it to the history. Reports progress toward the winning pattern.
- **check_kiyoshi()**: Checks if the history matches the winning pattern (Zun Zun Zun Zun Doko) and elicits "Ki-yo-shi!" from the user if it does.
- **reset_zundoko_kiyoshi()**: Resets the zundoko history and removes the kiyoshi resource.

### Resources

- **zundoko://history**: Returns the complete history of all zundoko calls as a JSON array.
- **zundoko://kiyoshi**: Returns the kiyoshi message with timestamp (only available after successfully completing the game).

### Resource Templates

- **zundoko://history/{index}**: Returns a specific zundoko from history by index (1-based).

### Prompts

- **explain_zundoko_kiyoshi()**: Provides instructions on how to play the Zundoko Kiyoshi game.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python server.py
   ```

   Or run with HTTP transport:
   ```bash
   fastmcp run server.py --transport http --port 8080 --host 127.0.0.1
   ```

## Usage

The server exposes three tools to play the game:

1. **get_zundoko()**: Call repeatedly to generate random "Zun" or "Doko" values
2. **check_kiyoshi()**: Check if you've achieved the winning pattern and say "Ki-yo-shi!"
3. **reset_zundoko_kiyoshi()**: Start over with a fresh game

## What is "Zundoko"?

"Zun" (ズン) and "Doko" (ドコ) are Japanese onomatopoeia representing different types of percussion sounds:
- **Zun**: A heavy, thumping sound
- **Doko**: A lighter, tapping sound

This is often referenced in Japanese programming tutorials and examples, similar to "Hello World" in Western programming culture.

## License

MIT License - see [LICENSE](LICENSE) file for details.