# What's Spire.PDF MCP Server ?

Spire.PDF MCP Server is a Model Context Protocol (MCP) server that allows you to create, [read](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Document-Operation/python-read-pdf.html), edit, and [convert PDF documents](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Images-JPG-PNG-BMP.html) directly through your AI agent — without relying on Adobe Acrobat or other PDF software.  

It provides a wide range of PDF manipulation capabilities, including [merging](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Document-Operation/Python-Merge-PDF-Documents.html), splitting, [text replacement](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Text/Python-Find-and-Replace-Text-in-PDF.html), [form operations](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Form-Field/Python-Create-or-Fill-in-a-Form-in-PDF.html), watermarking, and format conversion.

## Key Features

- [Create PDF documents from scratch](https://www.e-iceblue.com/en/pdf/python-create-pdf.html)
- Modify existing PDF files (replace text, add watermark, compress, etc.)
- Convert [PDF to Word](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Word-DOC-or-DOCX.html), [PDF to Excel](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Excel.html), [PDF to HTML](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-HTML.html), and more)
- [Merge](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Document-Operation/Python-Merge-PDF-Documents.html) and split PDF files
- [Encrypt and decrypt PDF documents](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Security/Python-Protect-or-Unprotect-PDF-Documents.html)
- [Flatten form fields](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Form-Field/Python-Flatten-Forms-in-PDF.html) and extract form values
- Delete or expand PDF bookmarks
- [Remove attachments from PDF files](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Attachment/Python-Remove-Attachments-from-a-PDF-Document.html)

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

### Document Operations (10 tools)

* **create_pdfducoment**: Create new PDF documents
* **convert_pdfdocument**: Convert PDF to other formats (Word, Excel, HTML, images, PDF/A, etc.)
* **extract_text**: Extract text from PDF pages
* **merge_pdfs**: Merge multiple PDFs into one
* **add_text_watermark**: Insert text watermarks into PDF
* **compress_document**: Reduce PDF file size
* **split_document**: Split a PDF into multiple files
* **encrypt_document**: Apply password protection to PDFs
* **decrypt_document**: Remove password protection
* **replace_all_text**: Replace all matching text in a PDF

### Bookmarks Operations (2 tools)

* **delete_all_bookmarks**: Remove all bookmarks from a PDF
* **expand_bookmarks**: Expand bookmark tree

### Forms Operations (2 tools)

* **flatten_formfield**: Flatten form fields in PDF
* **get_forms_values**: Extract values form PDF forms

### Attachments Operations (1 tool)

* **delete_all_attachments**: Remove all attachments from a PDF

## Supported Conversion Formats

* [**DOC/DOCX**](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Word-DOC-or-DOCX.html): Microsoft Word
* [**XLS/XLSX**](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Excel.html): Microsoft Excel
* **PPTX**: Microsoft PowerPoint
* [**HTML**](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-HTML.html): HyperText Markup Language
* **SVG**: Scalable Vector Graphics
* [**Image formats**](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Images-JPG-PNG-BMP.html): PNG, JPG, BMP, etc.
* [**PDF/A (1a, 1b, 2a, 2b, 3a, 3b)](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-PDF/A-and-Vice-Versa.html)**: Archival PDF
* **PDF/X-1a:2001**: Printing industry standard
* **XPS, PCL, Markdown, Gray PDF, Linearized PDF**

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

- **v1.0.0**: Initial stable release with tools
- Complete pdf document manipulation capabilities
- Comprehensive error handling
- Full format conversion support