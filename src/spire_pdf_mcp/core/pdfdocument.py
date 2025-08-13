import logging
from pathlib import Path
from typing import Any, Dict, Optional

from spire.pdf import *

from spire_pdf_mcp.utils.exceptions import PdfDocumentError
from spire_pdf_mcp.utils.utils import *
logger = logging.getLogger(__name__)


def create_pdfdocument(filepath: str) -> Dict[str, Any]:
    """Create a new pdfdocument"""
    try:
        #Create a pdf document
        doc= PdfDocument()
        #Create one page
        page = doc.Pages.Add()

        save_path = Path(filepath)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        doc.SaveToFile(str(save_path))
        return {
            "message": f"Created pdfdocument: {filepath}",
            "pdfdocument": doc
        }
    except Exception as e:
        logger.error(f"Failed to create pdfdocument: {e}")
        raise PdfDocumentError(f"Failed to create pdfdocument: {e!s}")

def get_or_create_pdfdocument(filepath: str) -> PdfDocument:
    """Get existing PdfDocument or create new one if it doesn't exist"""
    try:
        doc= PdfDocument()
        if Path(filepath).exists():
            doc.LoadFromFile(filepath)
        else:
            doc = create_pdfdocument(filepath)["pdfdocument"]
        return doc
    except Exception as e:
        logger.error(f"Failed to get or create pdfdocument: {e}")
        raise PdfDocumentError(f"Failed to get or create pdfdocument: {e!s}")
    
def extract_text (filepath: str,options: Dict[str, Any] = None) -> Dict[str, Any]:
    """Extract the text from the pdf"""
    try:
        doc= PdfDocument()
        if Path(filepath).exists():
            doc.LoadFromFile(filepath)
        else:
            doc = create_pdfdocument(filepath)["pdfdocument"]

        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(filepath)
        base_name = save_path.stem
        text_output_path = os.path.join(output_dir, f"{base_name}.txt")
        
        # Create a buffer to store the extracted text
        sbuffer = []

        # Iterate through each page in the document
        for i in range(doc.Pages.Count):
            page = doc.Pages.get_Item(i)

            # Create a PdfTextExtractor object for the page
            pdfTextExtractor = PdfTextExtractor(page)

            # Create PdfTextExtractOptions object
            pdfTextExtractOptions = PdfTextExtractOptions()

            # Extract the text from the page
            sbuffer.append(pdfTextExtractor.ExtractText(pdfTextExtractOptions))
        
        AppendAllText(text_output_path, sbuffer)    
            
        return {
            "message": f"Text extraction to file: {text_output_path}"
        }
    except Exception as e:
        logger.error(f"Failed to text extraction: {e}")
        raise PdfDocumentError(f"Failed to text extraction: {e!s}")    
    
def merge_pdfs(filepaths: List[str], output_path: str, options: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Merge multiple PDF files into one using pdfmerger library.
    
    Args:
        filepaths: List of PDF file paths to be merged
        output_path: Path where the merged PDF will be saved
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        # Check if output directory exists, create if not
        output_dir = os.path.dirname(filepaths[0])
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        merge_pdfs_output_path = os.path.join(output_dir, output_path)            
        
        # Iterate through all PDF files to be merged
        for filepath in filepaths:
            if not Path(filepath).exists():
                logger.warning(f"PDF file not found: {filepath}")
                continue
                
        # Add PDF file using mergebyfile method
        mergeOp = MergerOptions()
        # Create a PDF merger 
        PdfMerger.MergeByFile(filepaths,merge_pdfs_output_path,mergeOp)
        
        return {
            "message": f"PDFs merged successfully and saved to: {merge_pdfs_output_path}",
            "output_path": merge_pdfs_output_path
        }
        
    except Exception as e:
        logger.error(f"Failed to merge PDFs: {e}")
        raise PdfDocumentError(f"Failed to merge PDFs: {e!s}")     
    
def add_text_watermark(input_path: str, output_path: str, watermark_text: str, 
                       options: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Add text watermark to an existing PDF file.
    
    Args:
        input_path: Path to the original PDF file
        output_path: Path to save the PDF with watermark
        watermark_text: Text content of the watermark
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        # Check if input file exists
        if not Path(input_path).exists():
            raise FileNotFoundError(f"Input PDF file not found: {input_path}")
            
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(input_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        add_text_watermark_output_path = os.path.join(output_dir, output_path)                
            
        # Load the PDF document
        document = PdfDocument()
        document.LoadFromFile(input_path)
        
        #default options
        #font_size: Font size of the watermark (default: 24)
        #opacity: Opacity of the watermark (0.0-1.0, default: 0.3)
        #rotation: Rotation angle of the watermark in degrees (default: 45)
        font_size = 24.0
        opacity = 0.3
        opacity1 = 1.0
        rotation = 45.0
        
        # Loop through each page
        for i in range(document.Pages.Count):
            page = document.Pages.get_Item(i)
            
            #Draw text watermark
            brush = PdfTilingBrush(SizeF(page.Canvas.ClientSize.Width / float(2), page.Canvas.ClientSize.Height / float(3)))
            brush.Graphics.SetTransparency(opacity)
            brush.Graphics.Save()
            brush.Graphics.TranslateTransform(brush.Size.Width / float(2), brush.Size.Height / float(2))
            brush.Graphics.RotateTransform(-rotation)
            brush.Graphics.DrawString(watermark_text, PdfFont(PdfFontFamily.Helvetica, font_size), PdfBrushes.get_Violet(), 0.0, 0.0, PdfStringFormat(PdfTextAlignment.Center))
            brush.Graphics.Restore()
            brush.Graphics.SetTransparency(opacity1)
            page.Canvas.DrawRectangle(brush, RectangleF(PointF(0.0, 0.0), page.Canvas.ClientSize))
        
        # Save the document with watermark
        document.SaveToFile(add_text_watermark_output_path)
        document.Close()
        
        return {
            "message": f"Text watermark added successfully and saved to: {add_text_watermark_output_path}",
            "output_path": add_text_watermark_output_path
        }
        
    except Exception as e:
        logger.error(f"Failed to add text watermark: {e}")
        raise PdfDocumentError(f"Failed to add text watermark: {e!s}")    
    
def compressdocument(input_path: str, output_path: str,
                       options: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Compress the content in an existing PDF file.
    
    Args:
        input_path: Path to the original PDF file
        output_path: Path to save the PDF 
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        # Check if input file exists
        if not Path(input_path).exists():
            raise FileNotFoundError(f"Input PDF file not found: {input_path}")
            
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(input_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        compressdocument_output_path = os.path.join(output_dir, output_path)                
            
        # Load the PDF document
        pdfcompressor = PdfCompressor(input_path)
        cpoptions = OptimizationOptions()
        cpoptions.SetImageQuality(ImageQuality.Low)
        cpoptions.SetIsCompressFonts(False)
        cpoptions.SetIsCompressImage(True)
        cpoptions.SetIsCompressContents(False)
        cpoptions.SetResizeImages(True)
        pdfcompressor.OptimizationOptions = cpoptions
        pdfcompressor.CompressToFile(compressdocument_output_path)
        
        return {
            "message": f"Compress document successfully and saved to: {compressdocument_output_path}",
            "output_path": compressdocument_output_path
        }
        
    except Exception as e:
        logger.error(f"Failed to compress document: {e}")
        raise PdfDocumentError(f"Failed to compress document: {e!s}")       
    
def splitdocument(input_path: str, 
                       options: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Split the content in an existing PDF file.
    
    Args:
        input_path: Path to the original PDF file
        output_path: Path to save the PDF 
    
    Returns:
        Dictionary containing the operation result
    """
    try:
        # Check if input file exists
        if not Path(input_path).exists():
            raise FileNotFoundError(f"Input PDF file not found: {input_path}")
            
        output_dir = os.path.dirname(input_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(input_path)
        base_name = save_path.stem
        splitdocument_output_path = os.path.join(output_dir, f"{base_name}-{0}.pdf")           
            
        # Load the PDF document
        doc = PdfDocument()
        doc.LoadFromFile(input_path)
        #Split document
        doc.Split(splitdocument_output_path)
        
        return {
            "message": f"Split document successfully and saved to: {output_dir}",
            "output_path": output_dir
        }
        
    except Exception as e:
        logger.error(f"Failed to split document: {e}")
        raise PdfDocumentError(f"Failed to split document: {e!s}")             