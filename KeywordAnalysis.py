import _locale
_locale._getdefaultlocale = (lambda *args: ['en_US', 'UTF-8'])

#keywords ia a list of keywords that we want to analyze and get their data
def analyze(client,keywords):
    PAGE_SIZE = 500
    targeting_idea_service = client.GetService('TargetingIdeaService', version='v201809')
    selector = {
        'ideaType': 'KEYWORD',
        'requestType': 'STATS'
    }
    selector['requestedAttributeTypes'] = [
        'KEYWORD_TEXT', 'SEARCH_VOLUME', 'AVERAGE_CPC', 'COMPETITION']

    selector['searchParameters'] = [{
        'xsi_type': 'RelatedToQuerySearchParameter',
        'queries': keywords
    }]

    offset = 0
    selector['paging'] = {
        'startIndex': str(offset),
        'numberResults': str(PAGE_SIZE)
    }

    results = []

    # more_pages = True
    # while more_pages:
    page = targeting_idea_service.get(selector)
    if 'entries' in page:
        for result in page['entries']:
            attributes = {}
            for attribute in result['data']:
                # Parse the appropriate value out of each row of data
                attributeValue = getattr(attribute['value'], 'value', '0')
                if getattr(attribute.value, 'Attribute.Type') == 'MoneyAttribute':
                    attributes[attribute['key']] = getattr(attributeValue, 'microAmount', 0) / 1000000.
                else:
                    attributes[attribute['key']] = attributeValue

            results.append(attributes)
    return results
