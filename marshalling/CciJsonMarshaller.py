import json


def reference_to_dict(reference):
    ref_dict = dict()
    ref_dict['index'] = reference.index
    ref_dict['creator'] = reference.creator
    ref_dict['title'] = reference.title
    ref_dict['version'] = reference.version
    ref_dict['location'] = reference.location
    return ref_dict


class CciJsonMarshaller:
    @staticmethod
    def marshal(cci):
        cci_dict = dict()
        cci_dict['cciId'] = cci.id
        cci_dict['status'] = cci.status
        cci_dict['publishDate'] = cci.publishdate
        cci_dict['contributor'] = cci.contributor
        cci_dict['definition'] = cci.definition
        cci_dict['type'] = cci.type
        cci_dict['parameter'] = cci.parameter
        cci_dict['note'] = cci.note
        cci_dict['references'] = []
        for reference in cci.references:
            ref_dict = reference_to_dict(reference)
            cci_dict['references'].append(ref_dict)
        return json.dumps(cci_dict)
