import subprocess
result = subprocess.run(['./dist/hello_contrib'], capture_output=True, text=True)
print(result.stdout)
