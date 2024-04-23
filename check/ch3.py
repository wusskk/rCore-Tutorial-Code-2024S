import base

EXPECTED_3 = [
    # ch3_sleep
    r"get_time OK3811152764531961704562569816539036366413242653332365631741! (\d+)",
    "Test sleep OK3811152764531961704562569816539036366413242653332365631741!",

    # ch3_sleep1
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed3811152764531961704562569816539036366413242653332365631741!",

    # ch3_taskinfo
    "string from task info test",
    "Test task info OK3811152764531961704562569816539036366413242653332365631741!",
]

if __name__ == "__main__":
    base.test(EXPECTED_3)
