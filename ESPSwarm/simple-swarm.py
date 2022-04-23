from swarm import TelloSwarm
import time

swarm = TelloSwarm.fromSerialSSID([
#    ["/dev/ttyUSB0", "TELLO-xxxxxx"],
#    ["/dev/ttyUSB1", "TELLO-yyyyyy"]
    ["/dev/cu.usbserial-0001", "TELLO-xxxxxx"],
    ["/dev/cu.usbserial-10", "TELLO-yyyyyy"]
])

swarm.connect()
swarm.get_battery()
swarm.takeoff()
swarm.rotate_clockwise(90)
time.sleep(1)
swarm.rotate_counter_clockwise(180)
time.sleep(1)
swarm.rotate_clockwise(90)
time.sleep(1)
#
## run in parallel on all tellos
#swarm.move_up(100)
#
## run by one tello after the other
#swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))
#
## making each tello do something unique in parallel
#swarm.parallel(lambda i, tello: tello.move_left(i * 100 + 20))
#
swarm.land()
