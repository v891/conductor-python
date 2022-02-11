from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.queue_admin_resource_api import QueueAdminResourceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestQueueAdminResourceApi(unittest.TestCase):
    """QueueAdminResourceApi unit test stubs"""

    def setUp(self):
        self.api = QueueAdminResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_names(self):
        """Test case for names

        Get Queue Names  # noqa: E501
        """
        pass

    def test_size1(self):
        """Test case for size1

        Get the queue length  # noqa: E501
        """
        pass

    def test_update1(self):
        """Test case for update1

        Publish a message in queue to mark a wait task as completed.  # noqa: E501
        """
        pass

    def test_update_by_task_id(self):
        """Test case for update_by_task_id

        Publish a message in queue to mark a wait task (by taskId) as completed.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
