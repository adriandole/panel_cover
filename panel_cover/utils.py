import time
from datetime import timedelta


class ProgressBar:
    def __init__(self, bar_length: int = 20):
        """
        Creates a progress bar and records the inital time

        :param bar_length: length of the bar (default 20)
        """
        time.perf_counter()
        self.bar_length = bar_length
        self.start_time = time.time()

    def update(self, progress: float):
        """
        Updates and displays the progress bar

        :param progress: The progress to display; [0,1]
        """
        elapsed = time.time() - self.start_time
        if isinstance(progress, int):
            progress = float(progress)
        if not isinstance(progress, float):
            progress = 0
        if progress < 0:
            progress = 0
        if progress >= 1:
            progress = 1
        block = int(round(self.bar_length * progress))
        eta_seconds = (elapsed / progress) * (1 - progress)
        eta = timedelta(seconds=eta_seconds)
        print("\rProgress: [{}] {:4.2f}% ETA: {:.7}"
              .format("#" * block + "-" * (self.bar_length - block),
                      progress * 100, str(eta)), end='', flush=True)