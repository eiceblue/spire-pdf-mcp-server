import logging
import re
import os
from pathlib import Path
from typing import Tuple, Optional, List,Any
import datetime

from spire_pdf_mcp.utils.exceptions import UtilsError
from spire.pdf import *

logger = logging.getLogger(__name__)

def validate_path_permission(path: str, mode: str = "read"):
    if mode == "read" and not os.access(path, os.R_OK):
        raise PermissionError(f"no read access: {path}")
    if mode == "write" and not os.access(os.path.dirname(path), os.W_OK):
        raise PermissionError(f"no write access: {os.path.dirname(path)}")


def AppendAllText(fileName: str, text: List[str]) -> None:
    try:
        parent_dir = Path(fileName).parent
        if not parent_dir.exists():
            parent_dir.mkdir(parents=True, exist_ok=True)
        
        with open(fileName, 'w', encoding='utf-8') as file:
            for line in text:
                file.write(f"{line}\n") 
    except Exception as e:
        logger.error(f"Text Write Failure: {e}")
        raise UtilsError(f"Text Write Failure: {e!s}")