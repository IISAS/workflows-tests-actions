from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2024-05-13T14:04:00', 'schedule': None, 'catchup': False, 'dag_id': 'e71ce1e50de54ab89a63a12f2382e8c2'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    SimpleLogP_0298c1669d404e08b631ebe1490e1c45 = Task(
        dag,
        task_id='SimpleLogP_0298c1669d404e08b631ebe1490e1c45',
        workspace_id=2,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SimpleLogPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces_tests:0.0.4-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces_tests', 'repository_version': '0.0.4'},
        piece_input_kwargs={'input_str': 'default value', 'input_int': 10, 'input_float': 10.5, 'input_bool': False, 'input_enum': 'option1', 'input_date': '2023-01-01', 'input_time': '16:20:00', 'input_datetime': '2023-01-01T16:20:00', 'input_array': ['default_1', 'default_2', 'default_3'], 'input_code': "print('Hello world!')"}
    )()

