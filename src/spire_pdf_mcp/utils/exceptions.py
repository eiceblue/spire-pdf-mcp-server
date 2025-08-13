class PdfMCPError(Exception):
    """Base exception for Pdf MCP errors."""
    pass

class PdfDocumentError(PdfMCPError):
    """Raised when pdfdocument operations fail."""
    pass
    
class ConversionError(PdfMCPError):
    """Exception raised for errors during file conversion."""
    pass
class SecurityError(PdfMCPError):
    """Exception raised for errors during file operate security."""
    pass
class TextError(PdfMCPError):
    """Exception raised for errors during file operate text."""
    pass
class AttachmentsError(PdfMCPError):
    """Exception raised for errors during file operate attachments."""
    pass
class BookmarksError(PdfMCPError):
    """Exception raised for errors during file operate bookmarks."""
    pass
class FormsError(PdfMCPError):
    """Exception raised for errors during file operate forms."""
    pass

class UtilsError(PdfMCPError):
    """Exception raised for errors during Utils."""
    pass

