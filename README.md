# Zundoko MCP Server

A sample Model Context Protocol (MCP) server using [fastmcp](https://github.com/jlowin/fastmcp) that provides a tool to randomly return "Zun" or "Doko" text.

## Features

- **get_zundoko()** tool: Returns either "Zun" or "Doko" randomly

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

The server exposes one tool:

- `get_zundoko()`: Returns either "Zun" or "Doko" randomly

## What is "Zundoko"?

"Zun" (ズン) and "Doko" (ドコ) are Japanese onomatopoeia representing different types of percussion sounds:
- **Zun**: A heavy, thumping sound
- **Doko**: A lighter, tapping sound

This is often referenced in Japanese programming tutorials and examples, similar to "Hello World" in Western programming culture.

## License

MIT License - see [LICENSE](LICENSE) file for details.