from dagster import schedule


# https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules
@schedule(
    cron_schedule="0 9 * * 1-5",
    job_name='sklearn_job',
    execution_timezone='US/Eastern'
)
def every_weekday_9am():
    return {}