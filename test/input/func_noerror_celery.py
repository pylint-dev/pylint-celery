"""
Checks that Pylint does not complain about certain aspects of the Celery library
"""
#  pylint: disable=C0111,R0903,W0232

from celery import task

@task(queue='celery')
def test_task(an_arg, another_arg):
    return an_arg + another_arg


TEST_TASK_NON_DECORATOR = task(ignore_results=True)(lambda: 0)
