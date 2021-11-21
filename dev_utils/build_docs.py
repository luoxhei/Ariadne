import os
import shutil
import subprocess

os.chdir(os.path.join(__file__, "..", ".."))
subprocess.run(["black", "."])
subprocess.run(["isort", "."])
try:
    shutil.rmtree(os.path.abspath(os.path.join(".", "docs")))
except FileNotFoundError:
    pass
os.chdir(os.path.abspath(os.path.join(__file__, "..", "..", "src", "graia")))
subprocess.run(["pdoc", "--html", "ariadne", "-o", "./../.."])
opt = input("Confirm to publish?")
if not opt.lower().startswith("y"):
    exit(0)
os.chdir(os.path.abspath(os.path.join(__file__, "..", "..")))
os.rename("ariadne", "docs")
subprocess.run(["poetry", "publish", "--build"])
