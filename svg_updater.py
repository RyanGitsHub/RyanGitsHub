import xml.etree.ElementTree as ET
from datetime import date

today = date.today()

# Create root SVG element
root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width="600", height="550")

# Base layers
border = ET.SubElement(root, "rect", x="0", y="0", width="600", height="550", fill="#DBD7BC", rx="10")
bezel = ET.SubElement(root, "rect", x="40", y="40", width="520", height="470", fill="#928E75", rx="6")
screen = ET.SubElement(root, "rect", x="50", y="50", width="500", height="450", fill="#2C2C28", rx="2")

# Add text elements
title = ET.SubElement(root, "text", {"x": "60", "y": "85", "text-anchor": "left", "font-size": "40", "fill": "#4ABDBD", "font-family": "Courier New", "font-weight": "bold"})
title.text = "Hello World!"

welcomeText = ET.SubElement(root, "text", {"x": "60", "y": "120", "text-anchor": "left", "font-size": "24", "fill": "#4ABDBD", "font-family": "Courier New", "font-weight": "bold"})
welcomeText.text = "Welcome to Ryan's Profile!"

welcomeText = ET.SubElement(root, "text", {"x": "60", "y": "150", "text-anchor": "left", "font-size": "22", "fill": "#4ABDBD", "font-family": "Courier New", "font-weight": "bold"})
welcomeText.text = "A little about me:"

dateText = ET.SubElement(root, "text", {"x": "360", "y": "480", "text-anchor": "left", "font-size": "18", "fill": "#4ABDBD", "font-family": "Courier New", "font-weight": "bold"})
dateText.text = f"Date: {today}"

infoText1 = ET.SubElement(root, "text", {"x": "60", "y": "180", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText1.text = "I am an aspiring software engineer and"
infoText2 = ET.SubElement(root, "text", {"x": "60", "y": "200", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText2.text = "data analyst that is passionate about"
infoText3 = ET.SubElement(root, "text", {"x": "60", "y": "220", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText3.text = "all things tech and design. I am a "
infoText4 = ET.SubElement(root, "text", {"x": "60", "y": "240", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText4.text = "retro tech enthusiast and I love coding"
infoText5 = ET.SubElement(root, "text", {"x": "60", "y": "260", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText5.text = "new projects on my IBM model M. Lately I"
infoText6 = ET.SubElement(root, "text", {"x": "60", "y": "280", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText6.text = "have been spending my time studying "
infoText7 = ET.SubElement(root, "text", {"x": "60", "y": "300", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText7.text = "but I plan to get back to some passion"
infoText8 = ET.SubElement(root, "text", {"x": "60", "y": "320", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText8.text = "projects shortly. I am currently on the"
infoText9 = ET.SubElement(root, "text", {"x": "60", "y": "340", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText9.text = "lookout for some work opportunities in"
infoText10 = ET.SubElement(root, "text", {"x": "60", "y": "360", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText10.text = "data analysis and software engineering."
infoText11 = ET.SubElement(root, "text", {"x": "60", "y": "380", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText11.text = "I am often starting new passion projects"
infoText12 = ET.SubElement(root, "text", {"x": "60", "y": "400", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText12.text = "(and sometimes finishing them) so check "
infoText13 = ET.SubElement(root, "text", {"x": "60", "y": "420", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText13.text = "out my other projects if you like retro "
infoText14 = ET.SubElement(root, "text", {"x": "60", "y": "440", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText14.text = "vibes and whimsical improvements to your "
infoText15 = ET.SubElement(root, "text", {"x": "60", "y": "460", "text-anchor": "left", "font-size": "20", "fill": "#4ABDBD", "font-family": "Courier New"})
infoText15.text = "daily life! "


# Build tree and write to file
tree = ET.ElementTree(root)
ET.indent(tree, space="  ")  # Pretty print formatting
tree.write("images/80Screen.svg", encoding="utf-8", xml_declaration=True)
