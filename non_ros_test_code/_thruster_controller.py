import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel
import time

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class ThrusterController:
    THROTTLE_FORWARD_MAX    = 1.0 # Forward at 100% throttle
    THROTTLE_REVERSE_MAX    = -1.0 # Reverse at 100% throttle

    PWM_LOW_DURATION_MS     = 1.1 # milliseconds
    PWM_NEUTRAL_DURATION_MS = 1.5 # milliseconds
    PWM_HIGH_DURATION_MS    = 1.9 # milliseconds

    def __init__(self, pwm_freq):
        if pwm_freq < 1 or pwm_freq > 526:
            raise Exception('Frequency has to be constrained between 1 Hz and 526 Hz')

        # Setup PWM frequency for all channels
        navigator.set_pwm_freq_hz(pwm_freq)

        # Enables or disables the PWM chip
        navigator.set_pwm_enable(True)

        self.TOTAL_PERIOD_DURATION_MS = (1 / pwm_freq) * 1000

    
    def _calc_pwm_value_from_duration(self, on_duration_ms):
        pwm_value = int(4095 * (on_duration_ms / self.TOTAL_PERIOD_DURATION_MS))
        return pwm_value


    def set_pwm_thrusters(self, throttle_val, channels):
        duration_ms = map_range(
            throttle_val,
            self.THROTTLE_REVERSE_MAX, self.THROTTLE_FORWARD_MAX,
            self.PWM_LOW_DURATION_MS, self.PWM_HIGH_DURATION_MS,
        )

        pwm_value = self._calc_pwm_value_from_duration(duration_ms)
        navigator.set_pwm_channels_value(channels, pwm_value)


    def init_thrusters(self, channels, run_full_init_cycle = False):
        # Set PWM channels to neutral
        print('  Initializing ESCs: Setting PWM Channels to NEUTRAL...')
        self.set_pwm_thrusters(0.0, channels)
        # NOTE: We wait for 8 seconds since it seems to be required
        time.sleep(8.0)
    
        if run_full_init_cycle:
            # Set PWM channels to min range
            print('  Initializing ESCs: Setting PWM Channels to LOW...')
            self.set_pwm_thrusters(-1.0, channels)
            time.sleep(4.0)

            # Set PWM channels to high range
            print('  Initializing ESCs: Setting PWM Channels to HIGH...')
            self.set_pwm_thrusters(1.0, channels)
            time.sleep(4.0)
            
            # Set PWM channels to neutral
            print('  Initializing ESCs: Setting PWM Channels to NEUTRAL...')
            self.set_pwm_thrusters(0.0, channels)
            time.sleep(4.0)


if __name__ == '__main__':
    print("Initializing navigator module...")
    navigator.init()

    thruster_ctrl = ThrusterController(pwm_freq = 200)
    ACTIVE_PWM_CHANNELS = [
        PwmChannel.Ch1,
        # PwmChannel.Ch2,
    ]

    print("Initializing ROV thrusters...")
    thruster_ctrl.init_thrusters(
        channels=ACTIVE_PWM_CHANNELS,
        run_full_init_cycle=True
    )

    def go_up():
        thruster_ctrl.set_pwm_thrusters(0.5, ACTIVE_PWM_CHANNELS)


    def go_down():
        thruster_ctrl.set_pwm_thrusters(-0.5, ACTIVE_PWM_CHANNELS)

    def off():
        thruster_ctrl.set_pwm_thrusters(0.0, ACTIVE_PWM_CHANNELS)

    try:
        while True:
            print("forward")
            go_up()
            time.sleep(2)
            
            print("back")
            go_down()
            
            print("Done")
            time.sleep(5)
            off()
    except KeyboardInterrupt as ex:
        print('Exiting per user request...')
    finally:
        off()
