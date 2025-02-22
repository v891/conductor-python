from conductor.client.automator.task_handler import TaskHandler
from conductor.client.automator.task_runner import TaskRunner
from conductor.client.configuration.configuration import Configuration
from tests.unit.resources.workers import ClassWorker
from unittest.mock import Mock
from unittest.mock import patch
import multiprocessing
import unittest


class PickableMock(Mock):
    def __reduce__(self):
        return (Mock, ())


class TestTaskHandler(unittest.TestCase):
    def test_initialization_with_invalid_workers(self):
        expected_exception = Exception('Invalid worker list')
        with self.assertRaises(Exception) as context:
            TaskHandler(
                configuration=Configuration(),
                workers=ClassWorker()
            )
            self.assertEqual(expected_exception, context.exception)

    def test_start_processes(self):
        with patch.object(TaskRunner, 'run', PickableMock(return_value=None)):
            with _get_valid_task_handler() as task_handler:
                task_handler.start_processes()
                self.assertEqual(len(task_handler.task_runner_processes), 1)
                for process in task_handler.task_runner_processes:
                    self.assertTrue(
                        isinstance(process, multiprocessing.Process)
                    )


def _get_valid_task_handler():
    return TaskHandler(
        configuration=Configuration(),
        workers=[
            ClassWorker('task')
        ]
    )
