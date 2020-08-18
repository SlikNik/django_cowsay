# from subprocess import run, PIPE

# list_files = subprocess.run(["cowsay", "trying......"])
# list_files = subprocess.run(["cowsay"], stdout=subprocess.PIPE, text=True,
# input="Hello from the other side")
# print(list_files.stdout)

# output = run(["cowsay", "Hello from the other side"],  stdout=PIPE, 
# stderr=PIPE, universal_newlines=True)
# print(output.stdout)
# {{ form.get_cowsay([form.clean_data['text']) }}