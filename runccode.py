result = subprocess.run(['./hello_contrib.py'], capture_output=True, text=True)
print(result.stdout)
