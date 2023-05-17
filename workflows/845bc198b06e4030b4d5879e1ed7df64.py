from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2023-05-17', 'schedule_interval': None, 'catchup': False, 'dag_id': '845bc198b06e4030b4d5879e1ed7df64'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_1 = Task(
        dag, 
        task_id='task_1',
        workflow_shared_storage={'source': 'Local', 'base_folder': None, 'mode': None, 'provider_options': None, 'storage_repository_id': None},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SimpleLogPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces_tests:0.0.2-group0', 'repository_id': 100},
        piece_input_kwargs={'input_arg_1': 'default'}
    )()
    task_2 = Task(
        dag, 
        task_id='task_2',
        workflow_shared_storage={'source': 'Local', 'base_folder': None, 'mode': None, 'provider_options': None, 'storage_repository_id': None},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SimpleLogPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces_tests:0.0.2-group0', 'repository_id': 100},
        piece_input_kwargs={'input_arg_1': {'type': 'fromUpstream', 'upstream_task_id': 'task_1', 'output_arg': 'output_arg_1'}}
    )()

    task_2.set_upstream([globals()[t] for t in ['task_1']])
