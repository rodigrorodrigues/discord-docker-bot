import docker

class DockerService:
    def __init__(self):
        self.client = docker.from_env()

    def start_container(self, image_name: str, container_name: str) -> bool:
        try:
            container = self.client.containers.get(container_name)
            if container.status != 'running':
                container.start()
            return True
        except docker.errors.NotFound:
            try:
                self.client.containers.run(
                    image_name,
                    name=container_name,
                    detach=True
                )
                return True
            except Exception as e:
                print(f"Error starting container: {e}")
                return False

    def stop_container(self, container_name: str) -> bool:
        try:
            container = self.client.containers.get(container_name)
            if container.status == 'running':
                container.stop()
            return True
        except Exception as e:
            print(f"Error stopping container: {e}")
            return False