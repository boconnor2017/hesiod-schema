from markitdown import MarkItDown
import markdown_to_json

def convert_o365_2_md(o365_docname):
    markitdown = MarkItDown()
    result = markitdown.convert(o365_docname)
    return(result.text_content)

def convert_md_2_json(markdown_content):
    #Parse the mardown file into a variable and pass into this function as a string object: markdown_content
    md_json_str = markdown_to_json.jsonify(markdown_content)
    #Returns a json formatted string: md_json_str 
    #Use the Hesiod json library to convert this string as needed
    return md_json_str