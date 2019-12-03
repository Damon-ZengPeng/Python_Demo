from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
import os
import time
import shutil

scripts_path=r'F:\python\test_fold\scripts'

def check_fold_exist_py_file():


def script_start(script_full_path: str):
    print(script_full_path)
    work_dir=os.path.join(os.getcwd(),'test')
    # if script_full_path.endswith('.py'):
    copy_to_path = work_dir + script_full_path.replace(scripts_path,'')
    if not os.path.isdir(script_full_path)
        
        if not os.path.exists(os.path.dirname(copy_to_path)):
            os.makedirs(os.path.dirname(copy_to_path))
        shutil.copy(script_full_path, copy_to_path)
        os.remove(script_full_path)
    else:
        
        shutil.copytree(script_full_path, copy_to_path)
        
        os.removedirs(script_full_path)



class ScriptHandler(FileSystemEventHandler):
    def on_created(self, event):
        script_start(event.src_path)


def test():
    
    print(os.path.abspath(scripts_path))
    print(os.path.exists(scripts_path))
    ob = Observer()
    script_handler=ScriptHandler()
    ob.schedule(script_handler, scripts_path, recursive=False)
    ob.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        ob.stop()
    ob.join()