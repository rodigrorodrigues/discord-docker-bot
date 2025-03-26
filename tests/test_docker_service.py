import unittest
from src.services.docker_service import DockerService

class TestDockerService(unittest.TestCase):

    def setUp(self):
        self.docker_service = DockerService()

    def test_start_container(self):
        result = self.docker_service.start_container('test_container')
        self.assertTrue(result)

    def test_stop_container(self):
        result = self.docker_service.stop_container('test_container')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()