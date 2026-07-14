import platform
import os

print("=" * 50)

print("AI Investment Agent")

print("=" * 50)

print()

print("Python :", platform.python_version())

print("OS     :", platform.system())

print("Machine:", platform.machine())

print()

print("Current Folder")

print(os.getcwd())

print()

print("Project Files")

for item in sorted(os.listdir()):

    print(item)

print()

print("=" * 50)