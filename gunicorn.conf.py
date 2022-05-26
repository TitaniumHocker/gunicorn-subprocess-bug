import subprocess


def on_exit(server):
    for _ in range(10):
        subprocess.run(["/bin/sh", "./justexit.sh", "3"], capture_output=True)
