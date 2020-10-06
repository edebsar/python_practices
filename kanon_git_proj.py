import git
import os
import subprocess

class Repo_push_pull:
    """
    the gitpython module needs to be installed by pip3 for running this 
    object.
    """

    def __init__(self):
        self.repo_path = "/root/eureka-server-2"
        self.git_path = "https://github.com/a2z-ice/eureka-server"
        self.repo = git.Repo(repo_path)
        if os.getcwd() != self.repo_path:
            os.chdir(self.repo_path)

    def run(self):
        self.isCloned()
        self.build_java()
        self.docker_image_build()
        self.docker_image_push()
        self.docker_build()

    def isCloned(self):
        if self.repo.bare:
            git.Git(self.repo_path).clone(self.git_path)
        else:
            self.repo.remotes.origin.pull()
    
    def build_java(self):
        mvn_result = subprocess.run(["mvn", "package", "-Dspring.profiles.active=docker"])
        if mvn_result.returncode == 0:
            print("build successful!")
        else:
            print(f"build unsuccessful with exit code {mvn_result.returncode}!")

    def docker_image_build(self):
        d_image_result = subprocess.run(["docker", "build", "-f" "Dockerfile" "-t" "edebsar/eureka-server2:1.0" "."])
        if d_image_result.returncode == 0:
            print("docker image build successful!")
        else:
            print(f"docker image build unsuccessful with exit code {d_image_result.returncode}!")

    def docker_image_push(self):
        """
        docker login should be done if not done before running pull/push docker request.
        """
        push_image_result = subprocess.run(["docker", "push", "edebsar/eureka-server2:1.0"])
        if push_image_result.returncode == 0:
            print("docker image push successful!")
        else:
            print(f"docker image push unsuccessful with exit code {push_image_result.returncode}!")
        image_delete_result = subprocess.run(["docker", "rmi", "edebsar/eureka-server2:1.0"])
        if image_delete_result.returncode == 0:
            print("docker image delete successful!")
        else:
            print(f"docker image delete unsuccessful with exit code {image_delete_result.returncode}!")

    def docker_build(self):
        """
        docker login should be done if not done before running pull/push docker request.
        """
        pull_image_result = subprocess.run(["docker", "pull", "edebsar/eureka-server2:1.0"])
        if pull_image_result.returncode == 0:
            print("docker image push successful!")
        else:
            print(f"docker image push unsuccessful with exit code {pull_image_result.returncode}!")
        docker_run_result = subprocess.run(["docker", "run", "--network", "devops-net", "--name", "eureka-server", \
        "-p", "8761:8761", "-d", "edebsar/eureka-server2:1.0"])
        if docker_run_result.returncode == 0:
            print("docker image delete successful!")
        else:
            print(f"docker image delete unsuccessful with exit code {docker_run_result.returncode}!")


if __name__ == "__main__":
    Repo_push_pull().run()




