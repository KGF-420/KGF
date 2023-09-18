import os, sys, platform,time
bit = platform.architecture()[0]
if bit == '32bit':
    os.system('git pull')
    import kgf
