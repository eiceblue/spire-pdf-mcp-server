import logging
import sys
import os
from typing import Any, List, Dict, Optional

from mcp.server.fastmcp import FastMCP

# Import exceptions
from spire_pdf_mcp.utils.exceptions import (
    PdfDocumentError,
    ConversionError,
    SecurityError,
    TextError,
    BookmarksError,
    FormsError
)

from spire_pdf_mcp.core.conversion import convert_pdfdocument as convert_pdfdocument_impl

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("spire-pdf-mcp.log")
    ],
    force=True
)

logger = logging.getLogger("spire-pdf-mcp")

# Get Pdf files path from environment or use default
PDF_FILES_PATH = os.environ.get("PDF_FILES_PATH", "./pdf_files")

def get_pdf_path(filename: str) -> str:
    """Get full path to Pdf file.
    
    Args:
        filename: Name of Pdf file
        
    Returns:
        Full path to Pdf file
    """
    # If filename is already an absolute path, return it
    if os.path.isabs(filename):
        return filename

    # Use the configured Pdf files path
    return os.path.join(PDF_FILES_PATH, filename)

# Initialize FastMCP server
mcp = FastMCP(
    "spire-pdf-mcp",
    version="0.1.1",
    description="Pdf MCP Server for manipulating Pdf files",
    dependencies=["Spire.Pdf.Free>=10.12.0"],
    env_vars={
        "PDF_FILES_PATH": {
            "description": "Path to Pdf files directory",
            "required": False,
            "default": PDF_FILES_PATH
        }
    }
)


@mcp.tool()
def create_pdfdocument(filepath: str) -> str:
    """
    Creates a new Pdf document.

    Args:
        filepath (str): Path where the new document will be saved

    Returns:
        str: Success message with the created document path
    """
    try:
        full_path = get_pdf_path(filepath)
        from spire_pdf_mcp.core.pdfdocument import create_pdfdocument as create_pdfdocument_impl
        result = create_pdfdocument_impl(full_path)
        return f"Created pdfdocument at {full_path}"
    except PdfDocumentError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Error creating pdfdocument: {e}")
        raise

@mcp.tool()
def convert_pdfdocument(
        filepath: str,
        output_filepath: str,
        format_type: str,  
        options: Dict[str, Any] = None
) -> str:
    """
    Converts Pdf file to different formats.

    Supported formats:
    - pdf: Convert to PDF document
    - xps: Convert to XPS file
    - doc: Convert to DOC document
    - docx: Convert to DOCX document
    - html: Convert to HTML document
    - svg: Convert to SVG file
    - pcl: Convert to PCL file
    - xlsx: Convert to XLSX file
    - postscript: Convert to POSTSCRIPT file
    - ofd: Convert to OFD document
    - pptx: Convert to pptx file
    - graypdf: Convert to graypdf document   
    - linearizedpdf: Convert to linearizedpdf document   
    - image: Convert to image file(png)
    - pdfa: Convert to pdfa document(pdfa1a,pdfa1b,pdfa2a,pdfa2b,pdfa3a,pdfa3b,pdfx1a2001)   

    Args:
        filepath (str): Path to the Pdf file
        format_type (str): Target format type (pdf,xps,doc,docx,html,svg,pcl,xlsx,postscript,ofd,pptx,image,linearizedpdf,graypdf,pdfa1a,pdfa1b,pdfa2a,pdfa2b,pdfa3a,pdfa3b,pdfx1a2001)
        output_filepath (str): Path for the output file
        options (dict, optional): Format-specific options

    Returns:
        str: Success message or error description
    """
    try:
        full_path = get_pdf_path(filepath)
        output_path = get_pdf_path(output_filepath)
        
        result = convert_pdfdocument_impl(
            filepath=full_path,
            output_filepath=output_path,
            format_type=format_type,
            options=options
        )
        
        return result["message"]
    except ConversionError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Error converting file: {e}")
        raise ConversionError(f"Failed to convert Pdf file: {str(e)}")

@mcp.tool()
def extract_text(filepath: str,options: Dict[str, Any] = None) -> str:
    """
    Extract the text from the page

    Args:
        filepath (str): Path to the Pdf file
        options (dict, optional): extract_text options

    Returns:
        str: Success message or error description
    """
    try:
        full_path = get_pdf_path(filepath)
        from spire_pdf_mcp.core.pdfdocument import extract_text as extract_text_impl
        result = extract_text_impl(full_path,options)
        return result["message"]
    except PdfDocumentError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Error extract_text :{e}")
        raise
    
@mcp.tool()
def merge_pdfs(filepaths: List[str], output_path: str, options: Dict[str, Any] = None) -> str:
    """
    Merge multiple PDF files.
    
    Args:
        filepaths: List of PDF file paths to be merged
        output_path: Path where the merged PDF will be saved
        options (dict, optional): merge_pdfs options
    
    Returns:
        Success message or error description
    """
    try:
        full_path_list = []  
    
        for item in filepaths:
            full_path = get_pdf_path(item)
            full_path_list.append(full_path)  
            
        from spire_pdf_mcp.core.pdfdocument import merge_pdfs as merge_pdfs_impl
        result = merge_pdfs_impl(full_path_list,output_path,options)
        return result["message"]
    except PdfDocumentError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Error merge_pdfs :{e}")
        raise 
    
@mcp.tool()
def add_text_watermark(input_path: str, output_path: str, watermark_text: str, 
                       options: Dict[str, Any] = None) -> str:
    """
    Add text watermark to an existing PDF file.

    Args:
        input_path (str): Path to the Pdf file
        output_path: Path to save the PDF with watermark
        watermark_text: Text content of the watermark
        options (dict, optional): add_text_watermark options

    Returns:
        str: Success message or error description
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.pdfdocument import add_text_watermark as add_text_watermark_impl
        result = add_text_watermark_impl(full_path,output_path,watermark_text,options)
        return result["message"]
    except PdfDocumentError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Error add_text_watermark :{e}")
        raise   
    
@mcp.tool()
def compress_document(input_path: str, output_path: str,
                       options: Dict[str, Any] = None) -> str:
    """
    Compress the content in an existing PDF file.
    
    Args:
        input_path: Path to the original PDF file
        output_path: Path to save the PDF 
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.pdfdocument import compressdocument as compressdocument_impl
        result = compressdocument_impl(full_path,output_path,options)
        return result["message"]
    except PdfDocumentError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Error compress_document :{e}")
        raise       
    
@mcp.tool()
def split_document(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
    """
    Split the content in an existing PDF file.
    
    Args:
        input_path: Path to the original PDF file
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.pdfdocument import splitdocument as splitdocument_impl
        result = splitdocument_impl(full_path,options)
        return result["message"]
    except PdfDocumentError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Error split_document :{e}")
        raise   
    
@mcp.tool()
def encrypt_document(input_path: str, userpsw: str,ownerpsw: str,
                       options: Dict[str, Any] = None) -> str:
    """
    Encrypt the document with the security policy
    
    Args:
        input_path: Path to the original PDF file
        userpsw: the user password to the pdf file 
        ownerpsw: the owner password to the pdf file
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.security import encryptdocument as encryptdocument_impl
        result = encryptdocument_impl(full_path,userpsw,ownerpsw,options)
        return result["message"]
    except SecurityError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Error encrypt_document :{e}")
        raise     
    
@mcp.tool()
def decrypt_document(input_path: str, password: str,
                       options: Dict[str, Any] = None) -> str:
    """
    Decrypt the document with the password
    
    Args:
        input_path: Path to the original PDF file
        password: the password to the pdf file 
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.security import decryptdocument as decryptdocument_impl
        result = decryptdocument_impl(full_path,password,options)
        return result["message"]
    except SecurityError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Decrypt document :{e}")
        raise 
    
@mcp.tool()
def replace_all_text(input_path: str, oldtext: str,newtext: str,
                       options: Dict[str, Any] = None) -> str:
    """
    Replace text in PDF document
    
    Args:
        input_path: Path to the original PDF file
        oldtext: Text to be replaced
        newtext: Replaced text
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.text import replacealltext as replacealltext_impl
        result = replacealltext_impl(full_path,oldtext,newtext,options)
        return result["message"]
    except TextError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Decrypt document :{e}")
        raise     
    
@mcp.tool()
def delete_all_bookmarks(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
    """
    Delete bookmarks in PDF
    
    Args:
        input_path: Path to the original PDF file
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.bookmarks import deleteallbookmarks as deleteallbookmarks_impl
        result = deleteallbookmarks_impl(full_path,options)
        return result["message"]
    except BookmarksError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Delete bookmarks :{e}")
        raise    
    
@mcp.tool()
def expand_bookmarks(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
    """
    Expand bookmarks in PDF
    
    Args:
        input_path: Path to the original PDF file
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.bookmarks import expandbookmarks as expandbookmarks_impl
        result = expandbookmarks_impl(full_path,options)
        return result["message"]
    except BookmarksError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Expand bookmarks :{e}")
        raise     
    
@mcp.tool()
def flatten_formfield(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
    """
    Flatten formfield in PDF
    
    Args:
        input_path: Path to the original PDF file
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.forms import flattenformfield as flattenformfield_impl
        result = flattenformfield_impl(full_path,options)
        return result["message"]
    except FormsError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Flatten formfield :{e}")
        raise       
    
@mcp.tool()
def get_forms_values(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
    """
    Get forms values from the pdf
    
    Args:
        input_path: Path to the original PDF file
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.forms import getformsvalues as getformsvalues_impl
        result = getformsvalues_impl(full_path,options)
        return result["message"]
    except FormsError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Get forms values :{e}")
        raise             

@mcp.tool()
def delete_all_attachments(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
    """
    Delete all attachments in PDF document
    
    Args:
        input_path: Path to the original PDF file
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        full_path = get_pdf_path(input_path)
        from spire_pdf_mcp.core.attachments import deleteallattachments as deleteallattachments_impl
        result = deleteallattachments_impl(full_path,options)
        return result["message"]
    except FormsError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Delete all attachments :{e}")
        raise    

async def run_server():
    """Run the Pdf MCP server."""
    try:
        logger.info(f"Starting Pdf MCP server (files directory: {PDF_FILES_PATH})")
        await mcp.run_sse_async()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        await mcp.shutdown()
    except Exception as e:
        logger.error(f"Server failed: {e}")
        raise
    finally:
        logger.info("Server shutdown complete")
