import os
import sys
from datetime import datetime


from airflow.decorators import dag, task
from airflow import DAG
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner': 'MQ',
    'start_date': datetime(2025, 11, 4)
}

file_postfix = datetime.now().strftime("%Y%m%d")


@dag(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# extraction from reddit
def etl_reddit_pipeline():

    @task(task_id='reddit_extraction')
    def extract_task():
        file_path = reddit_pipeline(
            file_name= f'reddit_{file_postfix}',
            subreddit= 'dataengineering',
            time_filter= 'day',
            limit= 100
            )
        return file_path
    
    # upload to s3
    @task(task_id='s3_upload')
    def upload_s3_task(ti = None):
        upload_s3_pipeline(ti)
        
    extract_task() >> upload_s3_task()

dag = etl_reddit_pipeline()