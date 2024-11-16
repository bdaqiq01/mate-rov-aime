import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel
import time

# NOTE: Useful for copy-pasting
ALL_PWM_CHANNELS = [
    None,
    PwmChannel.Ch1,
    PwmChannel.Ch2,
    PwmChannel.Ch3,
    PwmChannel.Ch4,
    PwmChannel.Ch5,
    PwmChannel.Ch6,
    PwmChannel.Ch7,
    PwmChannel.Ch8,
    PwmChannel.Ch9,
    PwmChannel.Ch10,
    PwmChannel.Ch11,
    PwmChannel.Ch12,
    PwmChannel.Ch13,
    PwmChannel.Ch14,
    PwmChannel.Ch15,
    PwmChannel.Ch16,
]

def init_rov_thrusters(pwm_freq, channels, run_full_init_cycle = False):
    '''
    Initializes the ROV's ESCs for the thrusters. This involves setting specified thrusters to the
    neutral PWM value (1.5 ms) for some chunk of time to ensure they all properly initialize.

    NOTE: This is assuming the navigator module has been properly initialized with 'navigator.init()'

    Rules to follow prior to initialization:
    - Frequency cannot be higher than 909 Hz, otherwise low PWM does not fit into signal.       (min = 1.1 ms)
    - Frequency cannot be higher than 666 Hz, otherwise neutral PWM does not fit into signal.   (neutral = 1.5 ms)
    - Frequency cannot be higher than 526 Hz, otherwise max PWM does not fit into signal.       (max = 1.9 ms)

    Arguments:
    - `pwm_freq` - The PWM Frequency for the servo rail
    - `channels` - An array of PWM Channels (via the bluerobotics_navigator.PwmChannel type) that are assigned to ROV thrusters
    - `run_full_init_cycle` - If true, this will set the PWM values to LOW, then HIGH, then NEUTRAL. Otherwise just set to NEUTRAL

    Example Usage:
    ```python
    import bluerobotics_navigator as navigator
    from bluerobotics_navigator import PwmChannel

    print("Initializing navigator module...")
    navigator.init()

    print("Initializing ROV thrusters...")
    init_rov_thrusters(
        pwm_freq=200,
        channels=[
            PwmChannel.Ch1,
            PwmChannel.Ch2,
            PwmChannel.Ch3,
            PwmChannel.Ch4,
            PwmChannel.Ch5,
            PwmChannel.Ch6,
        ],
        run_full_init_cycle=False
    )

    print("Done!")
    ```

    Formulas:
    - duration (ms) = (1 / frequency) * 1000
    - pwm_value     = 4095 * (neutral_pwm / duration)
    '''

    if pwm_freq < 1 or pwm_freq > 526:
        raise Exception('Frequency has to be constrained between 1 Hz and 526 Hz')

    # Setup PWM frequency for all channels
    navigator.set_pwm_freq_hz(pwm_freq)

    # Enables or disables the PWM chip
    navigator.set_pwm_enable(True)


    TOTAL_PERIOD_DURATION_MS = (1 / pwm_freq) * 1000
    calc_pwm_value = lambda duration_on_ms: int(4095 * (duration_on_ms / TOTAL_PERIOD_DURATION_MS))

    PWM_LOW_DURATION_MS     = 1.1 # milliseconds
    PWM_NEUTRAL_DURATION_MS = 1.5 # milliseconds
    PWM_HIGH_DURATION_MS    = 1.9 # milliseconds
    DELAY_EACH_STEP         = 4.0 # seconds
    # default 8.0 seconds

    # Set PWM channels to neutral
    print('  Initializing ESCs: Setting PWM Channels to NEUTRAL...')
    navigator.set_pwm_channels_value(channels, calc_pwm_value(PWM_NEUTRAL_DURATION_MS))
    time.sleep(DELAY_EACH_STEP) # NOTE: try setting it for 8.0
  
    if run_full_init_cycle:
        # Set PWM channels to min range
        print('  Initializing ESCs: Setting PWM Channels to HIGH...')
        navigator.set_pwm_channels_value(channels, calc_pwm_value(PWM_LOW_DURATION_MS))
        time.sleep(DELAY_EACH_STEP)

        # Set PWM channels to high range
        print('  Initializing ESCs: Setting PWM Channels to LOW...')
        navigator.set_pwm_channels_value(channels, calc_pwm_value(PWM_HIGH_DURATION_MS))
        time.sleep(DELAY_EACH_STEP)
        
        # Set PWM channels to neutral
        print('  Initializing ESCs: Setting PWM Channels to NEUTRAL...')
        navigator.set_pwm_channels_value(channels, calc_pwm_value(PWM_NEUTRAL_DURATION_MS))
        time.sleep(DELAY_EACH_STEP)


# calc_pwm_value = lambda duration_on_ms: int(4095 * (duration_on_ms / TOTAL_PERIOD_DURATION_MS))
def set_pwm_channels(val, channels):
    pwm_freq = 200
    TOTAL_PERIOD_DURATION_MS = (1 / pwm_freq) * 1000
    PWM_LOW_DURATION_MS     = 1.1 # milliseconds
    PWM_NEUTRAL_DURATION_MS = 1.5 # milliseconds
    PWM_HIGH_DURATION_MS    = 1.9 # milliseconds

    def map_range(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def calc_pwm_value(duration_on_ms):
        return int(4095 * (duration_on_ms / TOTAL_PERIOD_DURATION_MS))

    calculated_ms = map_range(val, -1.0, 1.0, PWM_LOW_DURATION_MS, PWM_HIGH_DURATION_MS)
    navigator.set_pwm_channels_value(channels, calc_pwm_value(calculated_ms))


if __name__ == '__main__':
    print("Initializing navigator module...")
    navigator.init()

    print("Initializing ROV thrusters...")
    init_rov_thrusters(
        pwm_freq=200,
        channels=[
            PwmChannel.Ch1,
            # PwmChannel.Ch2,
            # PwmChannel.Ch3,
            # PwmChannel.Ch4,
            # PwmChannel.Ch5,
            # PwmChannel.Ch6,
        ],
        run_full_init_cycle=False
    )

    print("Done!")
