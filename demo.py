#!/usr/bin/env python

# ---------------------------------------------------------
# IOU Tracker
# Copyright (c) 2017 TU Berlin, Communication Systems Group
# Licensed under The MIT License [see LICENSE for details]
# Written by Erik Bochinski
# ---------------------------------------------------------

from time import time
import argparse

from iou_tracker import track_iou
from util import load_mot, save_to_csv


def main(detection_path, output_path, sigma_l, sigma_h, sigma_iou, t_min):
    detections = load_mot(detection_path)

    start = time()
    tracks = track_iou(detections, sigma_l, sigma_h, sigma_iou, t_min)
    end = time()

    num_frames = len(detections)
    print("finished at " + str(int(num_frames / (end - start))) + " fps!")

    save_to_csv(output_path, tracks)


if __name__ == '__main__':

    main("./MOT17-04-SDP/det/det.txt", "./MOT17-04-SDP.txt", 0, 0.5, 0.5, 2)