import time

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []

    def allow_request(self):
        current_time = time.time()
        # Remove outdated calls
        self.calls = [call for call in self.calls if call > current_time - self.period]
        if len(self.calls) < self.max_calls:
            self.calls.append(current_time)
            return True
        return False
