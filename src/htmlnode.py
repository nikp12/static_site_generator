def convert_to_html(value, tag):
    html_head = f"<{tag}> "
    html_tail = f" </{tag}>"
    return f"{html_head}{value}{html_tail}"

def convert_to_link(value, tag, props):
    props_str = ""
    for att in props:
        props_str += f"{att}=\"{props[att]}\" "
    props_str = props_str[0:-1]
    html_head = f"<{tag} {props_str}> "
    html_tail = f" </{tag}>"
    return f"{html_head}{value}{html_tail}"

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return f" {self.props}"
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("value is required")
        if self.tag == None:
            return self.value
        if self.props != None:
            return convert_to_link(self.value, self.tag, self.props)
        return convert_to_html(self.value, self.tag)
    
class ParentNode(HTMLNode):
    def __init__(tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        output_html = ""
        if self.tag == None:
            raise ValueError("node must have a tag")
        if self.children == None:
            raise ValueError("node must have a child")
        for child in self.children:
            print("DEBUG", child)
            return child.to_html()
        output_html += self.to_html
        return output_html

