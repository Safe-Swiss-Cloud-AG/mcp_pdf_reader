[project]
name = "mcp_pdf_reader"
version = "0.1.0"
description = "An MCP enabled PDF reader"
authors = [
  { name = "David Poole", email = "david.poole@safeswisscloud.ch" }
]
readme = "README.md"
requires-python = ">=3.8"
dependencies = ["pymupdf", "mcp"]

[project.scripts]
mcp_pdf_reader = "mcp_pdf_reader:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
include = ["mcp_pdf_reader.py"]
