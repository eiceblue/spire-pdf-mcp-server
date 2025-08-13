import logging
from pathlib import Path
from typing import Any, Dict, Optional

from spire.pdf import *

from spire_pdf_mcp.utils.exceptions import FormsError
from spire_pdf_mcp.utils.utils import *
logger = logging.getLogger(__name__)


    
def flattenformfield (filepath: str,options: Dict[str, Any] = None) -> Dict[str, Any]:
    """Flatten Form Field in PDF document"""
    try:

        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(filepath)
        base_name = save_path.stem
        flattenformfield_output_path = os.path.join(output_dir, f"{base_name}-flattenformfield.pdf")
        
        #Open pdf document
        doc = PdfDocument()
        doc.LoadFromFile(filepath)
        #Flatten form fields
        doc.Form.IsFlatten = True
        #Save pdf document
        doc.SaveToFile(flattenformfield_output_path)
        doc.Close()      
            
        return {
            "message": f"Flatten Form Field to file: {flattenformfield_output_path}"
        }
    except Exception as e:
        logger.error(f"Failed to Flatten Form Field in PDF document: {e}")
        raise FormsError(f"Failed to Flatten Form Field in PDF document: {e!s}")    
    
def getformsvalues (filepath: str,options: Dict[str, Any] = None) -> Dict[str, Any]:
    """Get forms values from the pdf"""
    try:
        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        save_path = Path(filepath)
        base_name = save_path.stem
        getformsvalues_output_path = os.path.join(output_dir, f"{base_name}-getformsvalues.txt")
        
        #Load a pdf document
        doc = PdfDocument()
        doc.LoadFromFile(filepath)
        #Get pdf forms
        pdfform = doc.Form
        formWidget = PdfFormWidget(pdfform)
        sb = []
        #Traverse all the forms
        if formWidget.FieldsWidget.Count > 0:
            for i in range(formWidget.FieldsWidget.Count):
                field = formWidget.FieldsWidget.get_Item(i)
                if isinstance(field, PdfTextBoxFieldWidget):
                    textBoxField = field if isinstance(field, PdfTextBoxFieldWidget) else None
                    #Get text of textbox
                    text = textBoxField.Text
                    sb.append("The text in textbox is " + text + "\r\n")
                if isinstance(field, PdfListBoxWidgetFieldWidget):
                    listBoxField = field if isinstance(field, PdfListBoxWidgetFieldWidget) else None
                    sb.append("Listbox items are \r\n")
                    #Get values of listbox
                    items = listBoxField.Values
                    for i in range(items.Count):
                        item = items.get_Item(i)
                        sb.append(item.Value + "\r\n")
                    #Get selected value
                    selectedValue = listBoxField.SelectedValue
                    sb.append("The selected value in the listbox is " + selectedValue + "\r\n")
                if isinstance(field, PdfComboBoxWidgetFieldWidget):
                    comBoxField = field if isinstance(field, PdfComboBoxWidgetFieldWidget) else None
                    sb.append("comBoxField items are \r\n")
                    #Get values of comboBox
                    items = comBoxField.Values
                    for i in range(items.Count):
                        item = items.get_Item(i)
                        sb.append(item.Value + "\r\n")
                    #Get selected value
                    selectedValue = comBoxField.SelectedValue
                    sb.append("The selected value in the comBoxField is " + selectedValue + "\r\n")
                if isinstance(field, PdfRadioButtonListFieldWidget):
                    radioBtnField = field if isinstance(field, PdfRadioButtonListFieldWidget) else None
                    #Get value of radio button
                    value = radioBtnField.Value
                    sb.append("The text in radioButtonField is " + value + "\r\n")
                if isinstance(field, PdfCheckBoxWidgetFieldWidget):
                    checkBoxField = field if isinstance(field, PdfCheckBoxWidgetFieldWidget) else None
                    #Get the checked state of the checkbox
                    state = checkBoxField.Checked
                    stateValue = "True" if state else "False"
                    sb.append("If the checkBox is checked: " + stateValue + "\r\n")
        
        AppendAllText(getformsvalues_output_path, sb)    
            
        return {
            "message": f"Get forms values to file: {getformsvalues_output_path}"
        }
    except Exception as e:
        logger.error(f"Failed to get forms values: {e}")
        raise FormsError(f"Failed to get forms values: {e!s}")     
         