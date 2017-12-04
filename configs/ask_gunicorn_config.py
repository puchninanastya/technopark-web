# Gunicorn configuration file.

# Server socket
#
#   bind - The socket to bind.
bind = '127.0.0.1:8081'

# Worker processes
#
#   workers - The number of worker processes that this server
#       should keep alive for handling requests.
workers = 4
#   worker_class - The type of workers to use. The default
#       sync class should handle most 'normal' types of work
#       loads.
worker_class = 'sync'
#   worker_connections - For the eventlet and gevent worker classes
#       this limits the maximum number of simultaneous clients that
#       a single process can handle.
worker_connections = 1000
#   timeout - If a worker does not notify the master process in this
#       number of seconds it is killed and a new worker is spawned
#       to replace it.
timeout = 30
#   keepalive - The number of seconds to wait for the next request
#       on a Keep-Alive HTTP connection.
keepalive = 2

# Process naming
#
#   proc_name - A base to use with setproctitle to change the way
#       that Gunicorn processes are reported in the system process
#       table. This affects things like 'ps' and 'top'.
proc_name = 'askpuchnina_gunicorn'
