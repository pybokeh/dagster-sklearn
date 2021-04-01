from dagster import repository
from pipelines.sklearn_pipeline import sklearn_pipeline
from schedules.sklearn_schedule import every_weekday_9am


@repository
def sklearn_repo():
    return {
        "pipelines": {
            "sklearn_pipeline": lambda: sklearn_pipeline 
        },
        "schedules": {
            "every_weekday_9am": lambda: every_weekday_9am
        }
    }
