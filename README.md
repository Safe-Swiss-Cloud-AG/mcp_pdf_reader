# MCP Enabled PDF Reader
Model Context Protocol (MCP) server exposes a tool called read_pdf to read a single pdf document. This has been tested on Claude Desktop and LibreChat with Ollama. There is no maximum size to the pdf file that can be read in; the number of tokens will be the limiting factor. 

## Installation

### Prerequisites

#### Windows
1. Install Claude Desktop (or another MCP-enabled AI tool)
   - Download [Claude for Desktop](https://claude.ai/download) 
   - Follow the current installation instructions: [Installing Claude Desktop](https://support.anthropic.com/en/articles/10065433-installing-claude-for-desktop)
     
2. Install Python 3.10 or higher:
   - Download the latest Python installer from [python.org](https://python.org)
   - Run the installer, checking "Add Python to PATH"
   - Open Command Prompt and verify installation with `python --version`

3. Install uv:
   - Open Command Prompt as Administrator
   - Run `pip install --user uv`
   - Verify installation with `uv --version`

#### macOS
1. Install Claude Desktop (or another MCP-enabled AI tool)
   - Download [Claude for Desktop](https://claude.ai/download) 
   - Follow the current installation instructions: [Installing Claude Desktop](https://support.anthropic.com/en/articles/10065433-installing-claude-for-desktop)
     
2. Install Python 3.10 or higher:
   - Using Homebrew: `brew install python`
   - Verify installation with `python3 --version`

3. Install uv:
   - Using Homebrew: `brew install uv`
   - Alternatively: `pip3 install --user uv`
   - Verify installation with `uv --version`

## Configuration

Add the following to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "mcp-pdf-reader": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/karateboss/mcp_pdf_reader@main",
                "mcp_pdf_reader"
            ]
        }
    }
}
```
## Attribution

This software package implements the ability to read a pdf file into a MCP enabled framework and is developed by [Safe Swiss Cloud](https://safeswisscloud.com). 


## Contributing

We welcome contributions to improve these tools. Please submit issues and pull requests through our repository.

## Support

For questions and support:
1. Check our documentation
2. Submit an issue in our repository
