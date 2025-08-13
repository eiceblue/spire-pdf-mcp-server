# What's Spire.PDF MCP Server ?

Spire.PDF MCP Server is a Model Context Protocol (MCP) server that allows you to create, read, edit, and convert PDF documents directly through your AI agent—without relying on Adobe Acrobat or other PDF software.  
It provides a wide range of PDF manipulation capabilities, including merging, splitting, text replacement, form operations, encryption, watermarking, and format conversion.

## Key Features

- Create PDF documents from scratch
- Modify existing PDF files (replace text, add watermark, compress, etc.)
- Merge and split PDFs
- Delete or expand bookmarks
- Remove attachments from PDF files
- Flatten form fields and extract form values
- Encrypt and decrypt documents
- Convert PDF to multiple formats (Word, Excel, HTML, images, PDF/A, PDF/X, and more)

## Quick Start

### Prerequisites

- Python 3.10 or higher

### Installation

1. Clone the repository:

```bash
git clone https://github.com/eiceblue/spire-pdf-mcp-server.git
cd spire-pdf-mcp-server
````

2. Install using uv:

```bash
uv pip install -e .
```

### Running the Server

Start the server (default port 8000):

```bash
uv run spire-pdf-mcp-server
```

Custom port (e.g., 8080):

```bash
# Bash/Linux/macOS
export FASTMCP_PORT=8080 && uv run spire-pdf-mcp-server

# Windows PowerShell
$env:FASTMCP_PORT = "8080"; uv run spire-pdf-mcp-server
```

## Integration with AI Tools

### Cursor IDE

1. Add this configuration to Cursor:

```json
{
  "mcpServers": {
    "pdf": {
      "url": "http://localhost:8000/sse",
      "env": {
        "PDF_FILES_PATH": "/path/to/pdf/files"
      }
    }
  }
}
```

2. The PDF tools will be available through your AI assistant.

### Remote Hosting & Protocols

This server uses **Server-Sent Events (SSE)** transport protocol.
For other environments:

* **Claude Desktop (requires stdio)**: Use [Supergateway](https://github.com/supercorp-ai/supergateway) to convert SSE to stdio.
* **Remote hosting**: Follow the [Remote MCP Server Guide](https://developers.cloudflare.com/agents/guides/remote-mcp-server/).

## Environment Variables

| Variable         | Description             | Default       |
| ---------------- | ----------------------- | ------------- |
| `FASTMCP_PORT`   | Server port             | `8000`        |
| `PDF_FILES_PATH` | Directory for PDF files | `./pdf_files` |

## Available Tools

The server provides **15+ tools** organized into 5 categories:

### Document Operations

* **create\_pdfdocument**: Create new PDF documents
* **convert\_pdfdocument**: Convert PDF to other formats (Word, Excel, HTML, images, PDF/A, PDF/X, etc.)
* **extract\_text**: Extract text from PDF pages
* **merge\_pdfs**: Merge multiple PDFs into one
* **add\_text\_watermark**: Insert text watermarks
* **compress\_document**: Reduce PDF file size
* **split\_document**: Split a PDF into multiple files
* **encrypt\_document**: Apply password protection
* **decrypt\_document**: Remove password protection
* **replace\_all\_text**: Replace all matching text in a PDF

### Bookmarks Operations

* **delete\_all\_bookmarks**: Remove all bookmarks from a PDF
* **expand\_bookmarks**: Expand bookmark tree

### Forms Operations

* **flatten\_formfield**: Flatten form fields
* **get\_forms\_values**: Extract form data

### Attachments Operations

* **delete\_all\_attachments**: Remove all attachments from a PDF

## Supported Conversion Formats

* **DOC/DOCX**: Microsoft Word
* **XLSX**: Microsoft Excel
* **PPTX**: Microsoft PowerPoint
* **HTML**: HyperText Markup Language
* **SVG**: Scalable Vector Graphics
* **Image formats**: PNG, JPG, BMP, etc.
* **PDF/A (1a, 1b, 2a, 2b, 3a, 3b)**: Archival PDF
* **PDF/X-1a:2001**: Printing industry standard
* **OFD**: Open Fixed-layout Document
* **XPS, PCL, PostScript, Gray PDF, Linearized PDF**

## Development

### Project Structure

```
spire-pdf-mcp-server/
├── src/spire_pdf_mcp/
│   ├── api/                 # API layer (tools)
│   │   ├── document_tools.py
│   │   ├── bookmarks_tools.py
│   │   ├── forms_tools.py
│   │   ├── attachments_tools.py
│   ├── core/                # Core business logic
│   │   ├── document.py
│   │   ├── bookmarks.py
│   │   ├── forms.py
│   │   ├── attachments.py
│   │   └── base.py
│   ├── utils/               # Utilities and constants
│   │   ├── exceptions.py
│   │   └── constants.py
│   ├── server.py            # MCP server implementation
│   └── __main__.py          # Entry point
├── pyproject.toml           # Project configuration
├── README.md                # This file
└── TOOLS.md                 # Detailed tool documentation
```

### Running Tests

```bash
uv run pytest
```

### Code Quality

* Fully typed with Python type hints
* Comprehensive error handling
* Modular architecture
* Consistent code formatting
* Detailed inline documentation

## Documentation

* **[TOOLS.md](TOOLS.md)**: Complete tool documentation with usage examples
* **Error Handling**: Common errors and troubleshooting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Add tests where applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Version History

* **v1.0.0**: Initial stable release with complete PDF manipulation capabilities
* Full conversion support to multiple formats
* Comprehensive error handling