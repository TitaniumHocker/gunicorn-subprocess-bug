import subprocess


def on_exit(server):
    for _ in range(10):
        subprocess.run(["/bin/sh", "./justexit.sh", "3"], capture_output=True)

# Workaround
# def on_exit(server):
#     import threading
#     def run_commands():
#         for _ in range(10):
#             subprocess.run(["/bin/sh", "./justexit.sh", "3"], capture_output=True)
#     thread = threading.Thread(target=run_commands)
#     thread.start()
#     thread.join()
