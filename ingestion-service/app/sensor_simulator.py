import random
import time


while True:
    water_level = round(random.uniform(0.2, 2.0), 2)

    print(f"Water level: {water_level} m")

    time.sleep(5)
