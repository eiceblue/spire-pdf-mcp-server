import logging
from pathlib import Path
from typing import Any, Dict, Optional

from spire.pdf import *

from spire_pdf_mcp.utils.exceptions import SecurityError
from spire_pdf_mcp.utils.utils import *
logger = logging.getLogger(__name__)


    
def encryptdocument (filepath: str,userpsw: str,ownerpsw: str,options: Dict[str, Any] = None) -> Dict[str, Any]:
    """Encrypt the pdf"""
    try:

        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(filepath)
        base_name = save_path.stem
        encrypt_output_path = os.path.join(output_dir, f"{base_name}-encrypt.pdf")
        
        # Load a Pdf document from disk
        doc = PdfDocument()
        doc.LoadFromFile(filepath)

        # Create a security policy with user and owner passwords
        securityPolicy = PdfPasswordSecurityPolicy(userpsw, ownerpsw)

        # Set the encryption algorithm
        securityPolicy.EncryptionAlgorithm = PdfEncryptionAlgorithm.RC4_128

        # Define document privileges
        dp = PdfDocumentPrivilege.ForbidAll()
        dp.AllowPrint = True
        dp.AllowFillFormFields = True
        securityPolicy.DocumentPrivilege = dp

        # Encrypt the document with the security policy
        doc.Encrypt(securityPolicy)
        
        # Save the document
        doc.SaveToFile(encrypt_output_path)        
            
        return {
            "message": f"Encrypt the pdf to file: {encrypt_output_path}"
        }
    except Exception as e:
        logger.error(f"Failed to Encrypt the pdf: {e}")
        raise SecurityError(f"Failed to Encrypt the pdf: {e!s}")    
    
def decryptdocument (filepath: str,psw: str,options: Dict[str, Any] = None) -> Dict[str, Any]:
    """Decrypt the pdf"""
    try:

        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(filepath)
        base_name = save_path.stem
        decrypt_output_path = os.path.join(output_dir, f"{base_name}-decrypt.pdf")
        
        # Load a Pdf document from disk
        doc = PdfDocument()
        doc.LoadFromFile(filepath,psw)

        # Decrypt the document
        doc.Decrypt()
        
        # Save the document
        doc.SaveToFile(decrypt_output_path)        
            
        return {
            "message": f"Decrypt the pdf to file: {decrypt_output_path}"
        }
    except Exception as e:
        logger.error(f"Failed to Decrypt the pdf: {e}")
        raise SecurityError(f"Failed to Decrypt the pdf: {e!s}")             