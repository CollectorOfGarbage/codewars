def bouncing_ball(h, bounce, window):
    if (h > 0 and bounce > 0 and bounce < 1 and window < h):
        times = 0
        while h > window:
            times += 1
            h *= bounce
            if h > window:
                times += 1
        return times
    else:
        return -1

import pytest

assert bouncing_ball(2, 0.5, 1) == 1
assert bouncing_ball(3, 0.66, 1.5) == 3
assert bouncing_ball(30, 0.66, 1.5) == 15
assert bouncing_ball(30, 0.75, 1.5) == 21
