# Importação de bibliotecas
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Criação DAG
dag = DAG('primeira_dag', # Nome da Dag
          description = 'Minha primeira DAG', # Descrição da Dag
          schedule = None, # Intervalo de agendamento que a Dag vai rodar
          start_date = datetime(2023, 10, 8), # Data de início
          catchup = False # Executa intervalos passados, pegando pelo start_date
          )

# Criação de tasks
task1 = BashOperator(task_id = 'tsk1', # Nome da task
                     bash_command = "sleep 5", # Comando de execução
                     dag = dag) # Informa de qual dag essa task pertence

task2 = BashOperator(task_id = 'tsk2', # Nome da task
                     bash_command = 'sleep 5', # Comando de execução
                     dag = dag) # Informa de qual dag essa task pertence

task3 = BashOperator(task_id = 'tsk3', # Nome da task
                     bash_command = 'sleep 5', # Comando de execução
                     dag = dag) # Informa de qual dag essa task pertence

# Cria ordem de precedência sequencial
task1 >> task2 >> task3