from lxml import etree

# Read HTML content from file
with open("/home/santhosh/EDUCATION CONTENTS/1.Programing/Pythons/map_project/short address/HTML_page.txt", 'r') as response:
    html_content = response.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Find the element using the provided XPath
target_elements = tree.xpath('//div[@class="bfdHYd Ppzolf OFBs3e  "]//div[@class="UaQhfb fontBodyMedium"]/div[4]')

# Extract and print the text content of each matching element
dl = []
for element in target_elements:
    # Use the initial XPath to get the desired attribute directly
    try:
        dl.append(element.xpath('./div[2]/span/span/span[1]')[0].text)
    except IndexError:
        dl.append('fu')

print(dl)
