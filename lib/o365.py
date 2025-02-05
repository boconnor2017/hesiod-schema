from markitdown import MarkItDown

def convert_o365_2_md(o365_docname):
    markitdown = MarkItDown()
    result = markitdown.convert(o365_docname)
    return(result.text_content)

