import subprocess
result = subprocess.run(['./hello_contrib'], capture_output=True, text=True)
print(result.stdout)
