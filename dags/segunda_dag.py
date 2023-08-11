# Importação de bibliotecas
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Criação de Dag
dag = DAG('segunda_dag',
          description = 'Minha segunda DAG',
          schedule = None,
          start_date = datetime(2023, 10, 8),
          catchup = False)

# Criação de tasks
task1 = BashOperator(task_id = 'tsk1',
                     bash_command = 'sleep 5',
                     dag = dag)

task2 = BashOperator(task_id = 'tsk2',
                     bash_command = 'sleep 5',
                     dag = dag)

task3 = BashOperator(task_id = 'tsk3',
                     bash_command = 'sleep 5',
                     dag = dag)

# Cria ordem de precedência com paralelismo
task1 >> [task2, task3]