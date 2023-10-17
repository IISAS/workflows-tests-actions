from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2023-10-17', 'schedule_interval': None, 'catchup': False, 'dag_id': '954869efd43842e1a9fb5ce1a2ab293a'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    SimpleLogP_0298c1669d404e08b631ebe1490e1c45 = Task(
        dag, 
        task_id='SimpleLogP_0298c1669d404e08b631ebe1490e1c45',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'base_folder': None, 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SimpleLogPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces_tests:0.0.2-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.0.2'},
        piece_input_kwargs={'input_str': 'default value', 'input_int': 10, 'input_float': 10.5, 'input_bool': False, 'input_enum': 'option1', 'input_date': '2023-01-01', 'input_time': '16:20:00', 'input_datetime': '2023-01-01T16:20:00', 'input_array': ['default_1', 'default_2', 'default_3'], 'input_code': "print('Hello world!')"}
    )()

