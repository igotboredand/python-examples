#!/usr/bin/python3

# Various stuff from the sys module.
import sys, os, glob

print("sys.argv:", sys.argv)
print()
print("\n-----------------------------------------------------------------")
print("os.environ:")
for v in sorted(os.environ.keys()):
    print("    %-15s => %s" % (v, os.environ[v]))
    print()
print("\n-----------------------------------------------------------------")
print("sys.platform:", sys.platform)
print()
print("\n-----------------------------------------------------------------")
print("os.getcwd:", os.getcwd())
print()
print("\n-----------------------------------------------------------------")
print("os.listdir('.'):", os.listdir('.'))
print()
print("\n-----------------------------------------------------------------")
print("glob.glob('*.py'):", glob.glob('*.py'))
print()
print("\n-----------------------------------------------------------------")
print("sys:", dir(sys))
print()
print("\n-----------------------------------------------------------------")
print("os:", dir(os))
print()
print("\n-----------------------------------------------------------------")
print()
os.system('ls -l')
print("\n-----------------------------------------------------------------")