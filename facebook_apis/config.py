from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.ad import Ad

access_token = 'EAAnZAGuJRerQBAOT2x1Fb0A85t7AClVsD8Ji3jvWoIty7mYfAwES86lM0AMj0QOGnr0m4USmMhpCOisBoCyVlOZBQaSwHzTLnrT261GIKBsZCsmdpYnPrHTp72ZCsCDkZCjAZAvx1FnCvG0vfDpQenUFUCM85EagzXP0sckcQl2WMZC7CZCZCel0uGrnSErTQpmwZD'
app_secret = '5d26f5ad5d6087afe35c244faf035791'
ad_account_id = 'act_1333379653842209'
schedule_interval = 'DAILY'
entity_type = 'AD'
notification_user_id = '115431851044753'
filter_field = 'impressions'
filter_value = '1'
filter_operator = 'GREATER_THAN'
app_id = '2771984279763636'
FacebookAdsApi.init(access_token=access_token)
admin_access = "EAAnZAGuJRerQBALxkuw9rRYQDrkWTD5mT1bJv0riuGEDqxaLV9Dt6ZBQmzm4DzlQWSHbNQElO4KlQzeXKZB52GtILY6emnvfjUfSIwI3vhDqUZCydrZBmB29mCvf5fDMWhZBlivxaHIsMst4E60i9J3DTAPXrzX5Wu5eud1BCMVbkMSZBgZBPtsKyHQNnSfo2tkZD"
fields = [
]
params = {
    'name': 'Sample SDK Rule',
    'schedule_spec': {'schedule_type': schedule_interval},
    'evaluation_spec': {'evaluation_type': 'SCHEDULE',
                        'filters': [{'field': filter_field, 'value': filter_value, 'operator': filter_operator},
                                    {'field': 'entity_type', 'value': entity_type, 'operator': 'EQUAL'},
                                    {'field': 'time_preset', 'value': 'LIFETIME', 'operator': 'EQUAL'}]},
    'execution_spec': {'execution_type': 'NOTIFICATION', 'execution_options': [
        {'field': 'user_ids', 'value': [notification_user_id], 'operator': 'EQUAL'}]},
}
print(AdAccount(ad_account_id).create_ad_rules_library(
    fields=fields,
    params=params,
))
