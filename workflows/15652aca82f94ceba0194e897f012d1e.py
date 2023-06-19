from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2023-06-19', 'schedule_interval': None, 'catchup': False, 'dag_id': '15652aca82f94ceba0194e897f012d1e'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_SleepPiece_0 = Task(
        dag, 
        task_id='task_SleepPiece_0',
        workflow_shared_storage={'source': 'None', 'base_folder': None, 'mode': 'Read/Write', 'provider_options': {'bucket': ''}, 'storage_repository_id': None},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SleepPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.3.9-group0', 'repository_id': 21},
        piece_input_kwargs={'sleep_time': 1}
    )()
    task_SimpleLogPiece_0 = Task(
        dag, 
        task_id='task_SimpleLogPiece_0',
        workflow_shared_storage={'source': 'None', 'base_folder': None, 'mode': 'Read/Write', 'provider_options': {'bucket': ''}, 'storage_repository_id': None},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SimpleLogPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.3.9-group0', 'repository_id': 21},
        piece_input_kwargs={'input_str': 'default value', 'input_int': 10, 'input_float': 10.5, 'input_bool': False, 'input_enum': 'option1', 'input_date': '2023-01-01', 'input_time': '16:20', 'input_datetime': '2023-01-01T16:20', 'input_array': [{'input_array': {'fromUpstream': False, 'upstreamId': None, 'upstreamArgument': None, 'value': 'default_1'}}, {'input_array': {'fromUpstream': False, 'upstreamId': None, 'upstreamArgument': None, 'value': 'default_2'}}, {'input_array': {'fromUpstream': False, 'upstreamId': None, 'upstreamArgument': None, 'value': 'default_3'}}], 'input_code': "print('Hello world!')", 'containerResources': {'cpu': {'min': 100, 'max': 100}, 'memory': {'min': 128, 'max': 128}, 'useGpu': False}}
    )()

    task_SimpleLogPiece_0.set_upstream([globals()[t] for t in ['task_SleepPiece_0']])
