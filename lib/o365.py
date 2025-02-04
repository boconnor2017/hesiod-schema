from markitdown import MarkItDown

def test(docname):
    markitdown = MarkItDown()
    result = markitdown.convert(docname)
    return(result.text_content)