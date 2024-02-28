from lxml import etree

with open("/home/santhosh/EDUCATION CONTENTS/1.Programing/Pythons/map_project/short address/HTML_page.txt", 'r') as response:
    html_content = response.read()
tree = etree.HTML(html_content)
NAME=tree.xpath('//a[@class="hfpxzc"]')
TYPE=tree.xpath('//div[@class="bfdHYd Ppzolf OFBs3e  "]/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/span[1]/span')
RATTING=tree.xpath('//div[@class="bfdHYd Ppzolf OFBs3e  "]//span[@class="e4rVHe fontBodyMedium"]')
STATUS=tree.xpath('//div[@class="bfdHYd Ppzolf OFBs3e  "]//div[@class="UaQhfb fontBodyMedium"]/div[4]')
PHN_NO=tree.xpath('//div[@class="bfdHYd Ppzolf OFBs3e  "]//div[@class="UaQhfb fontBodyMedium"]/div[4]')

full_list=[]
for name,typ,rats,stats in zip(NAME,TYPE,RATTING,STATUS,PHN_NO):
    try:
        rat=rats.xpath('.//span[@class="ZkP5Je"]')[0].get('aria-label')
    except IndexError:
        rat=rats.text
    try:#status
        status=stats.xpath('./div[2]/span/span/span[1]')[0].text.strip().split()[0]
        if status == "Open" or status=="Closed" or status=="Closes":
            Status="Functioning"
        else:
            Status=stats.xpath('./div[2]/span/span/span[1]')[0].text
    except IndexError:
        Status="Not Specified"
    try:
        
    full_list.append([name.get('aria-label'),typ.text,rat,Status])
print(full_list)

