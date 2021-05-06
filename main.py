from lxml import etree
import requests


from marshalling.CciJsonMarshaller import CciJsonMarshaller
from marshalling.CciXmlUnmarshaller import CciXmlUnmarshaller

xml_filepath = "U_CCI_List.xml"
xslt_filepath = "xslt_translators/cci_translator.xsl"


if __name__ == '__main__':
    dom = etree.parse(xml_filepath)
    xslt = etree.parse(xslt_filepath)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    for child in newdom.getroot().getchildren():
        cci = CciXmlUnmarshaller.unmarshall(child)
        cci_json = CciJsonMarshaller.marshal(cci)
        headers = {"Content-Type": "application/json"}
        url = "http://localhost:8080/cci/{}".format(cci.id)
        print(url)
        r = requests.put(url, data=cci_json, headers=headers)


