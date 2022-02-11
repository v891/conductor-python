from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.admin_resource_api import AdminResourceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAdminResourceApi(unittest.TestCase):
    """AdminResourceApi unit test stubs"""

    def setUp(self):
        self.api = AdminResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_config(self):
        """Test case for get_all_config

        Get all the configuration parameters  # noqa: E501
        """
        pass

    def test_get_event_queues(self):
        """Test case for get_event_queues

        Get registered queues  # noqa: E501
        """
        pass

    def test_requeue_sweep(self):
        """Test case for requeue_sweep

        Queue up all the running workflows for sweep  # noqa: E501
        """
        pass

    def test_verify_and_repair_workflow_consistency(self):
        """Test case for verify_and_repair_workflow_consistency

        Verify and repair workflow consistency  # noqa: E501
        """
        pass

    def test_view(self):
        """Test case for view

        Get the list of pending tasks for a given task type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
