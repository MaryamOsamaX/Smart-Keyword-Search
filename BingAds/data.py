from BingAds.auth_helper import *
# from output_helper import *
# from adinsight_example_helper import *
from operator import itemgetter


def getKeywordsByURL(url, nKeywords=10):
    authorization_data, adinsight_service = auth()
    # You must specify the attributes that you want in each returned KeywordIdea.
    ideas_attributes = adinsight_service.factory.create('ArrayOfKeywordIdeaAttribute')
    ideas_attributes.KeywordIdeaAttribute.append([
        # 'AdGroupId',
        # 'AdGroupName',
        # 'AdImpressionShare',
        'Keyword',
        'Competition',
        'MonthlySearchCounts',
        'Relevance',
        'Source',
        'SuggestedBid'
    ])

    # Only one of each SearchParameter type can be specified per call.
    search_parameters = adinsight_service.factory.create('ArrayOfSearchParameter')
    url_search_parameter = adinsight_service.factory.create('UrlSearchParameter')
    url_search_parameter.Url = url

    competition_search_parameter = adinsight_service.factory.create('CompetitionSearchParameter')
    competition_levels = adinsight_service.factory.create('ArrayOfCompetitionLevel')
    competition_levels.CompetitionLevel.append([
        'High',
        'Medium',
        'Low'])
    competition_search_parameter.CompetitionLevels = competition_levels

    exclude_account_keyword_search_parameter = adinsight_service.factory.create(
        'ExcludeAccountKeywordsSearchParameter')
    exclude_account_keyword_search_parameter.ExcludeAccountKeywords = False

    # Equivalent of '0 <= value <= 50'
    impression_share_search_parameter = adinsight_service.factory.create('ImpressionShareSearchParameter')
    impression_share_search_parameter.Maximum = None
    impression_share_search_parameter.Minimum = '0'

    # Equivalent of 'value >= 50'
    search_volume_search_parameter = adinsight_service.factory.create('SearchVolumeSearchParameter')
    search_volume_search_parameter.Maximum = None
    search_volume_search_parameter.Minimum = '0'

    # Equivalent of both 'value <= 50' and '0 <= value <= 50'
    suggested_bid_search_parameter = adinsight_service.factory.create('SuggestedBidSearchParameter')
    suggested_bid_search_parameter.Maximum = None
    suggested_bid_search_parameter.Minimum = None

    device_search_parameter = adinsight_service.factory.create('DeviceSearchParameter')
    device = adinsight_service.factory.create('DeviceCriterion')
    # Possible values are All, Computers, Tablets, Smartphones
    device.DeviceName = 'All'
    device_search_parameter.Device = device

    language_search_parameter = adinsight_service.factory.create('LanguageSearchParameter')
    languages = adinsight_service.factory.create('ArrayOfLanguageCriterion')
    language = adinsight_service.factory.create('LanguageCriterion')
    # You must specify exactly one language
    language.Language = 'English'
    languages.LanguageCriterion.append([language])
    language_search_parameter.Languages = languages

    location_search_parameter = adinsight_service.factory.create('LocationSearchParameter')
    locations = adinsight_service.factory.create('ArrayOfLocationCriterion')
    # You must specify between 1 and 100 locations

    # Currentlythisfeature is available in the United States, United
    # Kingdom, Canada, Australia, France, and Germany
    ls = []
    los = ['190', '188', '32', '9', '66', '72']
    for l in los:
        location = adinsight_service.factory.create('LocationCriterion')
        location.LocationId = l
        ls.append(location)
    # for i in range(179, len(df)):
    #     if df['Location Type'][i] == 'Country':
    #         location = adinsight_service.factory.create('LocationCriterion')
    #         # United States
    #         location.LocationId = df['Location Id'][i]
    #         ls.append(location)
    #         print(df['Bing Display Name'][i], ' - ', df['Location Id'][i])
    locations.LocationCriterion.append(ls)
    location_search_parameter.Locations = locations

    network_search_parameter = adinsight_service.factory.create('NetworkSearchParameter')
    network = adinsight_service.factory.create('NetworkCriterion')
    network.Network = 'OwnedAndOperatedAndSyndicatedSearch'
    network_search_parameter.Network = network

    # Populate ArrayOfSearchParameter
    search_parameters.SearchParameter.append([
        url_search_parameter,
        competition_search_parameter,
        exclude_account_keyword_search_parameter,
        impression_share_search_parameter,
        search_volume_search_parameter,
        suggested_bid_search_parameter,
        device_search_parameter,
        language_search_parameter,
        location_search_parameter,
        network_search_parameter
    ])
    get_keyword_ideas_response = adinsight_service.GetKeywordIdeas(
        IdeaAttributes=ideas_attributes,
        SearchParameters=search_parameters,
        ExpandIdeas=True
    )
    keyword_ideas = get_keyword_ideas_response
    # print(keyword_ideas['KeywordIdea'][0:nKeywords])
    keywords = []
    for i in keyword_ideas['KeywordIdea'][0:nKeywords]:
        # print(i.Keyword)
        keywords.append(str(i.Keyword))
    # print(type(str(keywords[0])))
    return keywords


def exist(obj, data):
    if obj is None:
        return -1
    else:
        return data


def getKeywordData(keywords, url):
    authorization_data, adinsight_service = auth()

    # You must specify the attributes that you want in each returned KeywordIdea.
    ideas_attributes = adinsight_service.factory.create('ArrayOfKeywordIdeaAttribute')
    ideas_attributes.KeywordIdeaAttribute.append([
        # 'AdGroupId',
        # 'AdGroupName',
        # 'AdImpressionShare',
        'Keyword',
        'Competition',
        'MonthlySearchCounts',
        'Relevance',
        'Source',
        'SuggestedBid'
    ])

    # Only one of each SearchParameter type can be specified per call.
    search_parameters = adinsight_service.factory.create('ArrayOfSearchParameter')

    query_search_parameter = adinsight_service.factory.create('QuerySearchParameter')
    queries = adinsight_service.factory.create('ns1:ArrayOfstring')
    queries.string.append(keywords)  ###
    query_search_parameter.Queries = queries

    url_search_parameter = adinsight_service.factory.create('UrlSearchParameter')
    url_search_parameter.Url = url

    competition_search_parameter = adinsight_service.factory.create('CompetitionSearchParameter')
    competition_levels = adinsight_service.factory.create('ArrayOfCompetitionLevel')
    competition_levels.CompetitionLevel.append([
        'High',
        'Medium',
        'Low'])
    competition_search_parameter.CompetitionLevels = competition_levels

    exclude_account_keyword_search_parameter = adinsight_service.factory.create(
        'ExcludeAccountKeywordsSearchParameter')
    exclude_account_keyword_search_parameter.ExcludeAccountKeywords = False

    # Equivalent of '0 <= value <= 50'
    impression_share_search_parameter = adinsight_service.factory.create('ImpressionShareSearchParameter')
    impression_share_search_parameter.Maximum = None
    impression_share_search_parameter.Minimum = '0'

    # Equivalent of 'value >= 50'
    search_volume_search_parameter = adinsight_service.factory.create('SearchVolumeSearchParameter')
    search_volume_search_parameter.Maximum = None
    search_volume_search_parameter.Minimum = '0'

    # Equivalent of both 'value <= 50' and '0 <= value <= 50'
    suggested_bid_search_parameter = adinsight_service.factory.create('SuggestedBidSearchParameter')
    suggested_bid_search_parameter.Maximum = None
    suggested_bid_search_parameter.Minimum = None

    device_search_parameter = adinsight_service.factory.create('DeviceSearchParameter')
    device = adinsight_service.factory.create('DeviceCriterion')
    # Possible values are All, Computers, Tablets, Smartphones
    device.DeviceName = 'All'
    device_search_parameter.Device = device

    language_search_parameter = adinsight_service.factory.create('LanguageSearchParameter')
    languages = adinsight_service.factory.create('ArrayOfLanguageCriterion')
    language = adinsight_service.factory.create('LanguageCriterion')
    # You must specify exactly one language
    language.Language = 'English'
    languages.LanguageCriterion.append([language])
    language_search_parameter.Languages = languages

    location_search_parameter = adinsight_service.factory.create('LocationSearchParameter')
    locations = adinsight_service.factory.create('ArrayOfLocationCriterion')
    # You must specify between 1 and 100 locations

    # Currentlythisfeature is available in the United States, United
    # Kingdom, Canada, Australia, France, and Germany
    ls = []
    los = ['190', '188', '32', '9', '66', '72']
    for l in los:
        location = adinsight_service.factory.create('LocationCriterion')
        location.LocationId = l
        ls.append(location)
    # for i in range(179, len(df)):
    #     if df['Location Type'][i] == 'Country':
    #         location = adinsight_service.factory.create('LocationCriterion')
    #         # United States
    #         location.LocationId = df['Location Id'][i]
    #         ls.append(location)
    #         print(df['Bing Display Name'][i], ' - ', df['Location Id'][i])
    locations.LocationCriterion.append(ls)
    location_search_parameter.Locations = locations

    network_search_parameter = adinsight_service.factory.create('NetworkSearchParameter')
    network = adinsight_service.factory.create('NetworkCriterion')
    network.Network = 'OwnedAndOperatedAndSyndicatedSearch'
    network_search_parameter.Network = network

    # Populate ArrayOfSearchParameter
    search_parameters.SearchParameter.append([
        query_search_parameter,
        url_search_parameter,
        competition_search_parameter,
        exclude_account_keyword_search_parameter,
        impression_share_search_parameter,
        search_volume_search_parameter,
        suggested_bid_search_parameter,
        device_search_parameter,
        language_search_parameter,
        location_search_parameter,
        network_search_parameter
    ])
    get_keyword_ideas_response = adinsight_service.GetKeywordIdeas(
        IdeaAttributes=ideas_attributes,
        SearchParameters=search_parameters,
        ExpandIdeas=False
    )
    keyword_ideas = get_keyword_ideas_response
    #print(keyword_ideas['KeywordIdea'])
    keywords_data = []
    ad_group_ids = []
    for keyword_idea in keyword_ideas['KeywordIdea']:
        ad_group_ids.append(keyword_idea.AdGroupId)
    distinct_ad_group_ids = list(set(ad_group_ids))
    ad_group_estimator_count = len(distinct_ad_group_ids)
    seed_offset = 0 if distinct_ad_group_ids.__contains__(None) else 1

    ad_group_estimators = adinsight_service.factory.create('ArrayOfAdGroupEstimator')

    for index in range(0, ad_group_estimator_count):
        ad_group_estimator = adinsight_service.factory.create('AdGroupEstimator')
        # The AdGroupId is reserved for future use.
        # The traffic estimates are not based on any specific ad group.
        ad_group_estimator.AdGroupId = None
        # Optionally you can set an ad group level max CPC (maximum search bid)
        ad_group_estimator.MaxCpc = '1000.00'
        # We will add new keyword estimators while iterating the keyword ideas below.
        ad_group_estimator.KeywordEstimators = adinsight_service.factory.create('ArrayOfKeywordEstimator')
        ad_group_estimators.AdGroupEstimator.append(ad_group_estimator)

    for keyword_idea in keyword_ideas['KeywordIdea']:
        keyword_estimator = adinsight_service.factory.create('KeywordEstimator')
        keyword = adinsight_service.factory.create('Keyword')
        # The keyword Id is reserved for future use.
        # The returned estimates are not based on any specific keyword.
        keyword.Id = None
        # The match type is required. Exact, Broad, and Phrase are supported.
        # Aggregate:
        # Aggregates the data across all match types.
        # Broad:
        # A broad match results when words in the keyword are present in the user's search query; however, the word order can vary.
        # Exact:
        # An exact match results when all of the words in the keyword exactly match the user's search query.
        # Phrase:
        # A phrase match results when all of the words in the keyword are present in the user's search query and are in the same order.

        keyword.MatchType = 'Broad'  # change it from exact to Broad as Aggregate is not supported in the right time
        # Use the suggested keyword.
        keyword.Text = keyword_idea.Keyword
        keyword_estimator.Keyword = keyword
        keyword_estimator.MaxCpc = None
        k = {}
        k['text'] = keyword_idea.Keyword
        k['competition'] = exist(keyword_idea.Competition, keyword_idea.Competition)
        m = [1, 2]
        if keyword_idea.MonthlySearchCounts is not None:
            m = keyword_idea.MonthlySearchCounts.long
        k['volume'] = exist(keyword_idea.MonthlySearchCounts, m[-1])
        k['avgVolume'] = exist(keyword_idea.MonthlySearchCounts, round(sum(m) / len(m)))

        # print('avg_volume = ', k['avg_volume'], '  -> ', type(k['avg_volume']))
        k['relevance'] = 0.0
        k['suggestedBid'] = exist(keyword_idea.SuggestedBid, keyword_idea.SuggestedBid)
        k['avgCpc'] = 0.0
        k['avgPosition'] = 0.0
        k['clicks'] = 0.0
        k['ctr'] = 0.0
        k['impressions'] = 0.0
        k['totalCost'] = 0.0
        k['rate'] = 0.0
        k['source'] = ''
        keywords_data.append(k)
        index = (keyword_idea.AdGroupId * -1) - seed_offset if keyword_idea.AdGroupId is not None else 0
        ad_group_estimators['AdGroupEstimator'][index].KeywordEstimators.KeywordEstimator.append(keyword_estimator)

    # Currently you can include only one CampaignEstimator per service call.
    campaign_estimators = adinsight_service.factory.create('ArrayOfCampaignEstimator')
    campaign_estimator = adinsight_service.factory.create('CampaignEstimator')

    # Let's use the ad group and keyword estimators that were sourced from keyword ideas above.
    campaign_estimator.AdGroupEstimators = ad_group_estimators

    # The CampaignId is reserved for future use.
    # The returned estimates are not based on any specific campaign.
    campaign_estimator.CampaignId = None

    # campaign_estimator.DailyBudget = 50.00

    # The location, language, and network criterions are required for traffic estimates.
    traffic_criteria = adinsight_service.factory.create('ArrayOfCriterion')

    # # You must specify between 1 and 100 locations
    # traffic_location = adinsight_service.factory.create('LocationCriterion')
    # # United States
    # traffic_location.LocationId = '190'

    # You must specify exactly one language criterion
    traffic_language = adinsight_service.factory.create('LanguageCriterion')
    traffic_language.Language = 'English'

    # You must specify exactly one network criterion
    traffic_network = adinsight_service.factory.create('NetworkCriterion')
    traffic_network.Network = 'OwnedAndOperatedAndSyndicatedSearch'

    # Optionally you can specify exactly one device.
    # If you do not specify a device, the returned traffic estimates
    # are aggregated for all devices.
    # The "All" device name is equivalent to omitting the DeviceCriterion.
    traffic_device = adinsight_service.factory.create('DeviceCriterion')
    traffic_device.DeviceName = 'All'

    traffic_criteria.Criterion.append([
        ls,
        traffic_language,
        traffic_network,
        traffic_device
    ])
    campaign_estimator.Criteria = traffic_criteria
    campaign_estimators.CampaignEstimator.append(campaign_estimator)

    # output_status_message("-----\nGetKeywordTrafficEstimates:")
    get_keyword_traffic_estimates_response = adinsight_service.GetKeywordTrafficEstimates(
        CampaignEstimators=campaign_estimators)

    e = get_keyword_traffic_estimates_response.CampaignEstimate[0].AdGroupEstimates.AdGroupEstimate[
        0]  # .KeywordEstimates.KeywordEstimate
    estimates = e['KeywordEstimates']['KeywordEstimate']

    for i in range(len(estimates)):
        keywords_data[i]['avgCpc'] = round((exist(estimates[i].Maximum.AverageCpc, estimates[i].Maximum.AverageCpc)
                                            + exist(estimates[i].Minimum.AverageCpc, estimates[i].Minimum.AverageCpc)) / 2,
                                           2)
        keywords_data[i]['avgPosition'] = round(
            (exist(estimates[i].Maximum.AveragePosition, estimates[i].Maximum.AveragePosition)
             + exist(estimates[i].Minimum.AveragePosition, estimates[i].Minimum.AveragePosition)) / 2, 2)
        keywords_data[i]['clicks'] = round((exist(estimates[i].Maximum.Clicks, estimates[i].Maximum.Clicks)
                                            + exist(estimates[i].Minimum.Clicks, estimates[i].Minimum.Clicks)) / 2, 2)
        keywords_data[i]['ctr'] = round((exist(estimates[i].Maximum.Ctr, estimates[i].Maximum.Ctr)
                                         + exist(estimates[i].Minimum.Ctr, estimates[i].Minimum.Ctr)) / 2, 2)
        keywords_data[i]['impressions'] = round(
            (exist(estimates[i].Maximum.Impressions, estimates[i].Maximum.Impressions)
             + exist(estimates[i].Minimum.Impressions, estimates[i].Minimum.Impressions)) / 2, 2)
        keywords_data[i]['totalCost'] = round((exist(estimates[i].Maximum.TotalCost, estimates[i].Maximum.TotalCost)
                                               + exist(estimates[i].Minimum.TotalCost, estimates[i].Minimum.TotalCost)) / 2,
                                              2)
    return keywords_data


def auth():
    authorization_data = AuthorizationData(
        account_id=None,
        customer_id=None,
        # client_secret=CLIENT_SECRET,
        developer_token=DEVELOPER_TOKEN,
        authentication=None,
    )

    adinsight_service = ServiceClient(
        service='AdInsightService',
        authorization_data=authorization_data,
        environment=ENVIRONMENT,
        version=13
    )
    authenticate(authorization_data)
    return authorization_data, adinsight_service


if __name__ == '__main__':
    # authorization_data = AuthorizationData(
    #     account_id=None,
    #     customer_id=None,
    #     # client_secret=CLIENT_SECRET,
    #     developer_token=DEVELOPER_TOKEN,
    #     authentication=None,
    # )
    #
    # adinsight_service = ServiceClient(
    #     service='AdInsightService',
    #     authorization_data=authorization_data,
    #     environment=ENVIRONMENT,
    #     version=13
    # )
    #
    # authenticate(authorization_data)
    import time

    start_time = time.time()
    keywords = ['page rank', 'keyword extraction', 'rake', 'keyword extraction algorithms']
    url = 'https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0'
    print('KeywordData: ')
    print(getKeywordData(keywords, url))
    print('suggested keywords from url: ')
    print(getKeywordsByURL(url, 10))
    print("--- %s seconds ---" % (time.time() - start_time))
