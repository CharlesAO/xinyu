#!/usr/bin/env python2
# encoding: utf-8

import os
import argparse
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import pandas as pd
import matplotlib.pylab as plt
import re
import rosbag

os.system("python2 bag_to_pose_vrpn_angle.py husky_nav_exp_2018-12-18-15-18-02.bag /vrpn_client_node/husky/pose")
os.system("python2 change_to_ang.py")
os.system("python2 date_caculate.py")
os.system("python2 get_error.py")
os.system("python2 get_picture.py")


print('>_<  !!!  >_<')