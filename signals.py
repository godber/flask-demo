from blinker import Namespace
hipflask_signals = Namespace()

# Signals
post_added = hipflask_signals.signal('post-added')


# Signal Handlers
def log_post(post):
    print 'Received post', post


# Connect to Signals
post_added.connect(log_post)
