from blinker import Namespace
hipflask_signals = Namespace()

# Signals
post_added = hipflask_signals.signal('post-added')


# Signal Handlers
@post_added.connect
def log_post(post):
    print 'Received post', post
