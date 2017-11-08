import os
import sys


base_hwmon_dir = '/sys/class/hwmon/'


def get_hwmon_dir():
    """Parse the hwmon tree, looking for an 'amdgpu' device."""
    for sub_dir in os.listdir(base_hwmon_dir):
        name_file = os.path.join(base_hwmon_dir, sub_dir, 'name')
        with open(name_file) as f:
            if 'amdgpu' in f.read():
                return os.path.join(base_hwmon_dir, sub_dir)
    else:
        return None


hwmon_dir = get_hwmon_dir()

# bail out if no device is found:
if not hwmon_dir:
    print("No AMDGPU cards found under {}".format(base_hwmon_dir))
    sys.exit(1)


def get_fan_stats(directory):
    """Parse all files that start with 'fan'."""
    stats = []
    for file in os.listdir(directory):
        if file.startswith('fan'):
            name = file.split('_')[0]

            with open(os.path.join(directory, file)) as f:
                temp = int(f.read())

            stats.append((name, temp))

    return stats


print("Found a device at: {}".format(hwmon_dir))
print("Found these fans:")
for fan, temp in get_fan_stats(hwmon_dir):
    print("    Fan: {},  Temp: {}".format(fan, temp))




