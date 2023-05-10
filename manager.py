import os
import random
import subprocess
import time

objects = ["can", "cracker_box", "banana", "mug"]  # list of objects to select from

# start train_ppo.py
subprocess.Popen(["python", "tools/train_ppo.py", "task=FrankaPickObject"])
print(f"Started train.py with object {objects[0]}")

while True:  
    # check if model.lock exists
    if os.path.exists("logdir/model_lock.lock"):
        print("model.lock exists, killing train.py")
        os.system("pkill -f tools/train_ppo.py")  # kill train.py process
        
        # start a subprocess of train.py with a different object name
        subprocess.Popen(["python", "tools/train_ppo.py", "task=FrankaPickObject", "cptdir=logdir", "resume=1000"])
        print(f"Started train.py with object {objects[0]}")
        
        
        os.remove("logdir/model_lock.lock")
        print("Deleted new_model.lock")
        break
        
    time.sleep(5)  # wait for 5 seconds before select