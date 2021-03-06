import signal


# https://stackoverflow.com/a/31464349
class GracefulKiller:
    kill_now = False
    shutdown_withhold = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True
        if not self.shutdown_withhold:
            exit()
