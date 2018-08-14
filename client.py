import zmq

c = zmq.Context()
s = c.socket(zmq.REQ)
s.connect('tcp://172.17.0.16:5000')
#s.connect('ipc:///tmp/zmq')
s.send_pyobj('hello')

msg = s.recv_pyobj()

print(msg)
