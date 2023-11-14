from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

from django.conf import settings

from django.core.management.base import BaseCommand

from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler.util import close_old_connections

import logging

from pools.jobs import refresh_data_of_bordeaux

logger = logging.getLogger(__name__)

after_10s = datetime.now() + timedelta(seconds=10)


@close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # Enables the app to fetch data just after being launched
        scheduler.add_job(
            refresh_data_of_bordeaux,
            trigger=DateTrigger(after_10s),
            id="instantaneous_refresh_data_of_bordeaux",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added instantaneous job: 'refresh_data_of_bordeaux'.")

        scheduler.add_job(
            refresh_data_of_bordeaux,
            trigger=CronTrigger(hour="8-22", minute="*/15"),
            id="periodically_refresh_data_of_bordeaux",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added periodically job: 'refresh_data_of_bordeaux'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(day_of_week="mon", hour="00", minute="00"),
            id="weekly_delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
