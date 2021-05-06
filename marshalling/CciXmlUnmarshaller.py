from objects.cci.cci import Cci
from objects.cci.reference import Reference


def unmarshall_reference(reference_element):
    attribs = reference_element.attrib
    reference = Reference()
    reference.index = attribs['index']
    reference.creator = attribs['creator']
    reference.title = attribs['title']
    reference.version = attribs['version']
    reference.location = attribs['location']
    return reference


class CciXmlUnmarshaller:
    @staticmethod
    def unmarshall(cci_element):
        attribs = cci_element.attrib
        cci = Cci()
        cci.id = attribs['id']
        cci.status = attribs['status']
        cci.publishdate = attribs['publishdate']
        cci.contributor = attribs['contributor']
        cci.definition = attribs['definition']
        cci.type = attribs['type']
        cci.parameter = attribs['parameter']
        cci.note = attribs['note']
        cci.references = set()
        reference_items = cci_element.find('references')
        for reference in reference_items.getchildren():
            cci.references.add(unmarshall_reference(reference))
        return cci
