import logging
from pathlib import Path
from typing import Any, Dict, Optional

from spire.pdf import *

from spire_pdf_mcp.utils.exceptions import BookmarksError
from spire_pdf_mcp.utils.utils import *
logger = logging.getLogger(__name__)

    
def deleteallbookmarks (filepath: str,options: Dict[str, Any] = None) -> Dict[str, Any]:
    """Delete bookmarks in PDF"""
    try:

        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(filepath)
        base_name = save_path.stem
        deleteallbookmarks_output_path = os.path.join(output_dir, f"{base_name}-deleteallbookmarks.pdf")
        
        #Create a new Pdf document.
        document = PdfDocument()
        #Load the file from disk.
        document.LoadFromFile(filepath)
        #Remove all bookmarks.
        document.Bookmarks.Clear()
        #Save the document
        document.SaveToFile(deleteallbookmarks_output_path)
        document.Close()      
            
        return {
            "message": f"Delete bookmarks to file: {deleteallbookmarks_output_path}"
        }
    except Exception as e:
        logger.error(f"Failed to Delete bookmarks in PDF: {e}")
        raise BookmarksError(f"Failed to Delete bookmarks in PDF: {e!s}")    
    
def expandbookmarks (filepath: str,options: Dict[str, Any] = None) -> Dict[str, Any]:
    """Expand bookmarks in PDF"""
    try:

        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(filepath)
        base_name = save_path.stem
        expandbookmarks_output_path = os.path.join(output_dir, f"{base_name}-expandbookmarks.pdf")
        
        #Create a new PDF document.
        doc = PdfDocument()
        #Load the file from disk.
        doc.LoadFromFile(filepath)
        #Set BookMarkExpandOrCollapse as true to expand the bookmarks.
        doc.ViewerPreferences.BookMarkExpandOrCollapse = True
        #Save the document
        doc.SaveToFile(expandbookmarks_output_path)
        doc.Close()    
            
        return {
            "message": f"Expand bookmarks to file: {expandbookmarks_output_path}"
        }
    except Exception as e:
        logger.error(f"Failed to Expand bookmarks in PDF: {e}")
        raise BookmarksError(f"Failed to Expand bookmarks in PDF: {e!s}")     
         