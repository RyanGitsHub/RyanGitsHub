import xml.etree.ElementTree as ET


# Create root SVG element
root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width="200", height="200")

# Add a blue rectangle
rect = ET.SubElement(root, "rect", x="20", y="20", width="160", height="160", fill="teal", rx="15")

# Build tree and write to file
tree = ET.ElementTree(root)
ET.indent(tree, space="  ")  # Pretty print formatting
tree.write("80Screen.svg", encoding="utf-8", xml_declaration=True)
