# Pdf MCP Server Tools

This document provides detailed information about all available tools in the Pdf MCP server.

## pdfdocument Operations

### create_pdfducoment

Creates a new Pdf document.

```python
create_pdfducoment(filepath: str) -> str:
```

- `filepath`: Path where the new document will be saved
- Returns: Success message with the created document path

### convert_pdfdocument

Converts Pdf file to different formats.

```python
convert_pdfdocument(
        filepath: str,
        output_filepath: str,
        format_type: str,  
        options: Dict[str, Any] = None
) -> str:
```

- `filepath`: Path to the Pdf file
- `format_type`: Target format type (pdf,xps,doc,docx,html,svg,pcl,xlsx,postscript,ofd,pptx,image,linearizedpdf,graypdf,pdfa1a,pdfa1b,pdfa2a,pdfa2b,pdfa3a,pdfa3b,pdfx1a2001)
- `output_filepath`: Path for the output file
- `options`: Format-specific options
- Returns: Success message or error description

### extract_text

Extract the text from the page

```python
extract_text(filepath: str,options: Dict[str, Any] = None) -> str:
```

- `filepath`: Path to the Pdf file
- `options`: extract_text options
- Returns: Success message or error description

### merge_pdfs

Merge multiple PDF files.

```python
merge_pdfs(filepaths: List[str], output_path: str, options: Dict[str, Any] = None) -> str:
```

- `filepaths`: List of PDF file paths to be merged
- `output_path`: Path where the merged PDF will be saved
- `options`: merge_pdfs options
- Returns: message or error description

### add_text_watermark

Add text watermark to an existing PDF file.

```python 
add_text_watermark(input_path: str, output_path: str, watermark_text: str, 
                       options: Dict[str, Any] = None) -> str:
```                   

- `input_path`: Path to the Pdf file
- `output_path`: Path to save the PDF with watermark
- `watermark_text`: Text content of the watermark
- `options`: add_text_watermark options
- Returns: Success message or error description


### compress_document

Compress the content in an existing PDF file.

```python 
compress_document(input_path: str, output_path: str,
                       options: Dict[str, Any] = None) -> str:
```                          
- `input_path`: Path to the original PDF file
- `output_path`: Path to save the PDF 
- Returns: Success message or error description

### split_document

Split the content in an existing PDF file.

```python 
split_document(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
```                         

- `input_path`: Path to the original PDF file
- Returns: Dictionary containing the operation result

### encrypt_document

Encrypt the document with the security policy

```python 
encrypt_document(input_path: str, userpsw: str,ownerpsw: str,
                       options: Dict[str, Any] = None) -> str:
```                           
- `input_path`: Path to the original PDF file
- `userpsw`: the user password to the pdf file 
- `ownerpsw`: the owner password to the pdf file
- Returns: Dictionary containing the operation result

### decrypt_document

Decrypt the document with the password

```python
decrypt_document(input_path: str, password: str,
                       options: Dict[str, Any] = None) -> str:
```                       
- `input_path`: Path to the original PDF file
- `password`: the password to the pdf file 
- Returns: Dictionary containing the operation result

### replace_all_text

Replace text in PDF document

```python
replace_all_text(input_path: str, oldtext: str,newtext: str,
                       options: Dict[str, Any] = None) -> str:
```                        

- `input_path`: Path to the original PDF file
- `oldtext`: Text to be replaced
- `newtext`: Replaced text
- Returns: Dictionary containing the operation result


## Bookmarks Operations

### delete_all_bookmarks

Delete bookmarks in PDF

```python
delete_all_bookmarks(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
```                        

- `input_path`: Path to the original PDF file
- Returns: Dictionary containing the operation result

### expand_bookmarks

Expand bookmarks in PDF

```python
expand_bookmarks(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
```                        

- `input_path`: Path to the original PDF file
- Returns: Dictionary containing the operation result


## Forms Operations

### flatten_formfield

Flatten Form Field in PDF document

```python
flatten_formfield(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
```                        

- `input_path`: Path to the original PDF file
- Returns: Dictionary containing the operation result

### get_forms_values

Get forms values from the pdf

```python
get_forms_values(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
```                        

- `input_path`: Path to the original PDF file
- Returns: Dictionary containing the operation result

## Attachments Operations

### delete_all_attachments

Delete all attachments in PDF document

```python
delete_all_attachments(input_path: str, 
                       options: Dict[str, Any] = None) -> str:
```                       

- `input_path`: Path to the original PDF file
- Returns: Dictionary containing the operation result




