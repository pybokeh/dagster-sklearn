from dagster import repository
from pipelines.sklearn_pipeline import sklearn_pipeline


@repository
def sklearn_repo():
    return {
        "pipelines": {
            "sklearn_pipeline": lambda: sklearn_pipeline 
        },
    }
