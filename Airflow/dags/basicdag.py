from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime as dt

def greet():
    print("Writing in file:")
    with open ('/home/derek/greet.txt', 'a+') as f:
        now =dt.now()
        t = now.strftime("%Y-%m-%d %H:%M")
        f.write(str(t)+'\n')
    return 'Greeted'


greet()


def respond():
    return 'Greet Responded Again'


default_args = {
    'owner': 'airflow',
    'start_date': dt(2020, 5, 3, 4, 00, 00),
    'concurrency': 1,
    'retries': 0
}

with DAG('simple_dag', default_args=default_args, schedule_interval='*/10 * * * *')  as dag:
    hitask = BashOperator(task_id="Hi", bash_command='echo Hi')
    writefile = PythonOperator(task_id='Greet', python_callable=greet)

hitask>>writefile
