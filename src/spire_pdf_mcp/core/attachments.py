import logging
from pathlib import Path
from typing import Any, Dict, Optional

from spire.pdf import *

from spire_pdf_mcp.utils.exceptions import AttachmentsError
from spire_pdf_mcp.utils.utils import *
logger = logging.getLogger(__name__)


    
def deleteallattachments (filepath: str,options: Dict[str, Any] = None) -> Dict[str, Any]:
    """Delete all attachments in PDF document"""
    try:

        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(filepath)
        base_name = save_path.stem
        deleteallattachments_output_path = os.path.join(output_dir, f"{base_name}-deleteallattachments.pdf")
        
        #Open pdf document
        doc = PdfDocument()
        doc.LoadFromFile(filepath)
        #Get all attachments
        attachments = doc.Attachments
        #Delete all attachments
        attachments.Clear()
        #Save pdf document
        doc.SaveToFile(deleteallattachments_output_path)
        doc.Close()    
            
        return {
            "message": f"Delete all attachments to file: {deleteallattachments_output_path}"
        }
    except Exception as e:
        logger.error(f"Failed to Delete all attachments in PDF document: {e}")
        raise AttachmentsError(f"Failed to Delete all attachments in PDF document: {e!s}")    
    
 