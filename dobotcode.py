
from DobotEDU import *

# Block 1: pick at (320, 20, -15)
m_lite.set_ptpcmd(ptp_mode=0, x=320, y=20, z=-15, r=0)
m_lite.wait(delay=0.5)
m_lite.set_endeffector_gripper(enable=True, on=True)
m_lite.wait(delay=0.5)

# Block 1: place at the stack position (320, 100), lowest level
m_lite.set_ptpcmd(ptp_mode=0, x=320, y=100, z=-15, r=0)
m_lite.set_endeffector_gripper(enable=True, on=False)
m_lite.wait(delay=0.5)

# Block 2: pick at (320, -20, -15)
m_lite.set_ptpcmd(ptp_mode=0, x=320, y=-20, z=-15, r=0)
m_lite.wait(delay=0.5)
m_lite.set_endeffector_gripper(enable=True, on=True)
m_lite.wait(delay=0.5)

# Block 2: place on top of block 1 (z raised to -10)
m_lite.set_ptpcmd(ptp_mode=0, x=320, y=100, z=-10, r=0)
m_lite.set_endeffector_gripper(enable=True, on=False)
m_lite.wait(delay=0.5)

# Block 3: pick at (300, -100, -15)
m_lite.set_ptpcmd(ptp_mode=0, x=300, y=-100, z=-15, r=0)
m_lite.wait(delay=0.5)
m_lite.set_endeffector_gripper(enable=True, on=True)
m_lite.wait(delay=0.5)

# Block 3: place on top of the stack (z raised to 0)
m_lite.set_ptpcmd(ptp_mode=0, x=320, y=100, z=0, r=0)
m_lite.set_endeffector_gripper(enable=True, on=False)
m_lite.wait(delay=0.5)

# Move away from the stack
m_lite.set_ptpcmd(ptp_mode=0, x=200, y=0, z=0, r=-5)