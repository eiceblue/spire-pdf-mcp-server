import logging
from typing import Any, Dict, Optional

from spire.pdf import *

from spire_pdf_mcp.utils.exceptions import ConversionError

logger = logging.getLogger(__name__)


def convert_pdfdocument(
        filepath: str,
        output_filepath: str,
        format_type: str,
        options: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Convert PdfDocument to different formats.
    
    Args:
        filepath: Source Pdf file path
        output_filepath: Target output file path
        format_type: Target format (pdf,xps,doc,docx,html,svg,pcl,xlsx,postscript,ofd,pptx,image,linearizedpdf,graypdf,pdfa1a,pdfa1b,pdfa2a,pdfa2b,pdfa3a,pdfa3b,pdfx1a2001, etc.)
        options (dict, optional): Format-specific options
        
    Returns:
        Dictionary with operation status
    """
    try:
        # Load the pdfdocument
        doc = PdfDocument()
        doc.LoadFromFile(filepath)

        # Ensure output directory exists
        output_dir = os.path.dirname(output_filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # Handle format-specific conversion
        format_type = format_type.lower()

        # Process different format types
        if format_type == 'linearizedpdf':
            # Convert to linearizedpdf
            converter = PdfToLinearizedPdfConverter(filepath)
            converter.ToLinearizedPdf(output_filepath)

        elif format_type == 'image':
            # Convert to image(*.png)
            for i in range(doc.Pages.Count):
                with doc.SaveAsImage(i) as image:
                    image_output_path = os.path.join(output_dir, f"page_{i+1}.png")
                    image.Save(image_output_path)

        elif format_type == 'graypdf':
            converter = PdfGrayConverter(filepath)
            converter.ToGrayPdf(output_filepath)
        elif format_type == 'pdfa1a':
            converter = PdfStandardsConverter(filepath)
            converter.ToPdfA1A(output_filepath)      
        elif format_type == 'pdfa1b':
            converter = PdfStandardsConverter(filepath)
            converter.ToPdfA1B(output_filepath)  
        elif format_type == 'pdfa2a':
            converter = PdfStandardsConverter(filepath)
            converter.ToPdfA2A(output_filepath)      
        elif format_type == 'pdfa2b':
            converter = PdfStandardsConverter(filepath)
            converter.ToPdfA2B(output_filepath)   
        elif format_type == 'pdfa3a':
            converter = PdfStandardsConverter(filepath)
            converter.ToPdfA3A(output_filepath)          
        elif format_type == 'pdfa3b':
            converter = PdfStandardsConverter(filepath)
            converter.ToPdfA3B(output_filepath)     
        elif format_type == 'pdfx1a2001':
            converter = PdfStandardsConverter(filepath)
            converter.ToPdfX1A2001(output_filepath)                                                                              
                    
        elif format_type in ['pdf','xps','doc','docx','html','svg','pcl','xlsx','postscript','ofd','pptx']:
            # Map format type to file format
            format_map = {
                'pdf': FileFormat.PDF,
                'xps': FileFormat.XPS,
                'doc': FileFormat.DOC,
                'docx': FileFormat.DOCX,
                'html': FileFormat.HTML,
                'svg': FileFormat.SVG,
                'pcl': FileFormat.PCL,
                'xlsx': FileFormat.XLSX,
                'postscript': FileFormat.POSTSCRIPT,
                'ofd': FileFormat.OFD,
                'pptx': FileFormat.PPTX
            }

            if format_type not in format_map:
                raise ConversionError(f"Unsupported format_type: {format_type}")

            # Convert to the specified format
            doc.SaveToFile(output_filepath, format_map[format_type])

        else:
            raise ConversionError(f"Unsupported format type: {format_type}")

        return {
            "message": f"Pdf file successfully converted to {format_type.upper()}: {output_filepath}",
            "source_file": filepath,
            "output_file": output_filepath,
            "format": format_type
        }

    except ConversionError as e:
        logger.error(str(e))
        raise
    except Exception as e:
        logger.error(f"Failed to convert Pdf file: {e}")
        raise ConversionError(f"Failed to convert Pdf file: {str(e)}")
