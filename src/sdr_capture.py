# Requires rtl-sdr tools: sudo apt install rtl-sdr
# Captures raw IQ samples and prints spectrum placeholder

import os

def capture_samples(output_file="capture.bin", freq=100e6, sample_rate=2e6, duration=5):
    print(f"[SDR] Capturing {duration}s at {freq/1e6} MHz...")
    cmd = f"rtl_sdr -f {int(freq)} -s {int(sample_rate)} -n {int(sample_rate*duration)} {output_file}"
    os.system(cmd)
    print(f"[SDR] Capture complete: {output_file}")

if __name__ == "__main__":
    capture_samples()
