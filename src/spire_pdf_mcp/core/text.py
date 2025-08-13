import logging
from pathlib import Path
from typing import Any, Dict, Optional

from spire.pdf import *

from spire_pdf_mcp.utils.exceptions import TextError
from spire_pdf_mcp.utils.utils import *
logger = logging.getLogger(__name__)


    
def replacealltext (filepath: str,oldtext: str,newtext: str,options: Dict[str, Any] = None) -> Dict[str, Any]:
    """Replace text in PDF document"""
    try:

        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(filepath)
        base_name = save_path.stem
        replacetext_output_path = os.path.join(output_dir, f"{base_name}-replacetext.pdf")
        
        # Load a Pdf document from disk
        doc = PdfDocument()
        doc.LoadFromFile(filepath)

        for i in range(doc.Pages.Count):
            page = doc.Pages[i]
            replacer = PdfTextReplacer(page)
            rpoptions = PdfTextReplaceOptions()
            rpoptions.ReplaceType = ReplaceActionType.WholeWord
            replacer.Options = rpoptions
            replacer.ReplaceAllText(oldtext,newtext)
        
        # Save the document
        doc.SaveToFile(replacetext_output_path)        
            
        return {
            "message": f"Document after text replacement to file: {replacetext_output_path}"
        }
    except Exception as e:
        logger.error(f"Failed to Replace text in PDF document: {e}")
        raise TextError(f"Failed to Replace text in PDF document: {e!s}")    
         