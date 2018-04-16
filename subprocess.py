from subprocess import Popen, PIPE
from threading import Thread
from Queue import Queue, Empty

io_queue = Queue()

def stream_watcher(identifier, stream):

    for line in stream:
        io_queue.put((identifier, line))

    if not stream.closed:
        stream.close()

proc = Popen(***meterpreter cmd here***, stdout=PIPE, stderr=PIPE)

Thread(target=stream_watcher, name='stdout-watcher',
        args=('STDOUT', proc.stdout)).start()
Thread(target=stream_watcher, name='stderr-watcher',
        args=('STDERR', proc.stderr)).start()

def printer():
    while True:
        try:
            # Block for 1 second.
            item = io_queue.get(True, 1)
        except Empty:
            # No output in either streams for a second. Are we done?
            if proc.poll() is not None:
                break
        else:
            identifier, line = item
            #print identifier + ':', line

Thread(target=printer, name='printer').start()