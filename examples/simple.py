import sdbg

sdbg.dprint("prints in debug mode.")

import time
def expensive() -> str:
    time.sleep(2)
    return "result of computation was 42."
    

sdbg.dprint_thunk(lambda: expensive())

print("Python print.")