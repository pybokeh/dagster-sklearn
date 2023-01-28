from dagster import repository
from jobs.sklearn_job import sklearn_job
from schedules.sklearn_schedule import every_weekday_9am

# There are 2 forms of return value for the repository definition:
# 1) list or 
# 2) dict form (for "lazy" evaluation)
# Even though not needed in this example, I personally prefer the dict
# form for the explicitness it provides as the key value aids in describing that
# I am passing in a pipeline vs schedule vs sensor, etc
# Documentation reference:
# https://docs.dagster.io/_apidocs/repositories#dagster.RepositoryDefinition

@repository
def sklearn_repo():
    return {
        "jobs": {
            "sklearn_job": lambda: sklearn_job 
        },
        "schedules": {
            "every_weekday_9am": lambda: every_weekday_9am
        }
    }
