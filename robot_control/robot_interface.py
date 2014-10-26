#!/usr/bin/env python

# interface to the Parallax ActivityBot through the Propeller Loader's
# terminal interface

ROBOT_COMMAND = "propeller-loader -r -t blinkenlights.elf"

# XXX Testing
ROBOT_COMMAND = "python2.7 robot_sim.py"

import pexpect

cmds = ['l', 'r', 'l', 'l', 'r', 'r', 'q']

# load and start the control program to the ActivityBot.  Have the loader
# provide a terminal interace to the robot.
robot = pexpect.spawn(ROBOT_COMMAND)
robot.expect("Entering terminal mode.")

# Execute our commands:
for c in cmds:
  robot.expect("Cmd: ")
  print robot.before
  robot.sendline(c)

# Terminate the loader process
robot.close
