ACTIVITY_EVENT_ATTEND = 'Attended an Event'
ACTIVITY_EVENT_CREATE = 'Organized an Event'
ACTIVITY_CAMPAIGN = 'Participated in a campaign'
ACTIVITY_MONTH_PLANNING = 'Month planning'
ACTIVITY_MONTH_RECAP = 'Month recap'
ACTIVITY_POST_EVENT_METRICS = 'Completed post-event metrics'
ACTIVITY_RECRUITMENT_EFFORT = 'Recruitment effort'
RECRUIT_MOZILLIAN = 'Recruited a Mozillian'
ACTIVITY_ROTM_NOMINATED = 'Nominated Rep of the Month'

READONLY_ACTIVITIES = [ACTIVITY_CAMPAIGN, ACTIVITY_EVENT_ATTEND,
                       ACTIVITY_EVENT_CREATE, RECRUIT_MOZILLIAN,
                       ACTIVITY_POST_EVENT_METRICS, ACTIVITY_ROTM_NOMINATED]
VERIFIABLE_ACTIVITIES = [RECRUIT_MOZILLIAN]
UNLISTED_ACTIVITIES = [ACTIVITY_EVENT_ATTEND, ACTIVITY_EVENT_CREATE,
                       ACTIVITY_MONTH_PLANNING, ACTIVITY_MONTH_RECAP,
                       ACTIVITY_RECRUITMENT_EFFORT,
                       ACTIVITY_POST_EVENT_METRICS]


default_app_config = 'remo.reports.apps.ReportsConfig'
