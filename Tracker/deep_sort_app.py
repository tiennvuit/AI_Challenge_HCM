# vim: expandtab:ts=4:sw=4
##############################################
"""
 python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_02 \
    --detection_file=output_generate/cam_02.npy \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
"""
###############################################


from __future__ import division, print_function, absolute_import

import argparse
import os

import cv2
import numpy as np

from application_util import preprocessing
from application_util import visualization
from deep_sort import nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker


def gather_sequence_info(sequence_dir, detection_file):
    """Gather sequence information, such as image filenames, detections,
    groundtruth (if available).

    Parameters
    ----------
    sequence_dir : str
        Path to the MOTChallenge sequence directory.
    detection_file : str
        Path to the detection file.

    Returns
    -------
    Dict
        A dictionary of the following sequence information:

        * sequence_name: Name of the sequence
        * image_filenames: A dictionary that maps frame indices to image
          filenames.
        * detections: A numpy array of detections in MOTChallenge format.
        * groundtruth: A numpy array of ground truth in MOTChallenge format.
        * image_size: Image size (height, width).
        * min_frame_idx: Index of the first frame.
        * max_frame_idx: Index of the last frame.

    """
    image_dir = os.path.join(sequence_dir, "img1")
    
    #print(image_dir)
    #for file in os.listdir(image_dir):
    #    print(os.path.join(image_dir, file))

    #input()
    image_filenames = {
        int(f.split("_")[-1].split(".")[0]): os.path.join(image_dir, f)
        for f in os.listdir(image_dir)}

    groundtruth_file = os.path.join(sequence_dir, "gt/gt.txt")

    detections = None
    if detection_file is not None:
        detections = np.load(detection_file)
    #print('detection',detections)
    groundtruth = None
    if os.path.exists(groundtruth_file):
        groundtruth = np.loadtxt(groundtruth_file, delimiter=',')
   
      

    if len(image_filenames) > 0:
        image = cv2.imread(next(iter(image_filenames.values())),
                           cv2.IMREAD_GRAYSCALE)
        image_size = image.shape
    else:
        image_size = None

    if len(image_filenames) > 0:
        min_frame_idx = min(image_filenames.keys())
        max_frame_idx = max(image_filenames.keys())
    else:
        min_frame_idx = int(detections[:, 0].min())
        max_frame_idx = int(detections[:, 0].max())

    info_filename = os.path.join(sequence_dir, "seqinfo.ini")
    if os.path.exists(info_filename):
        with open(info_filename, "r") as f:
            line_splits = [l.split('=') for l in f.read().splitlines()[1:]]
            info_dict = dict(
                s for s in line_splits if isinstance(s, list) and len(s) == 2)
        #print('dict',info_dict) 
        print('Frame rate',info_dict['frameRate'])
        update_ms = 1000 / int(info_dict["frameRate"])
    else:
        update_ms = None

    feature_dim = detections.shape[1] - 10 if detections is not None else 0
   # print('ground truth',groundtruth)
    seq_info = {
        "sequence_name": os.path.basename(sequence_dir),
        "image_filenames": image_filenames,
        "detections": detections,
        "groundtruth": groundtruth,
        "image_size": image_size,
        "min_frame_idx": min_frame_idx,
        "max_frame_idx": max_frame_idx,
        "feature_dim": feature_dim,
        "update_ms": update_ms
    }
    return seq_info


def create_detections(detection_mat, frame_idx, min_height=0):
    """Create detections for given frame index from the raw detection matrix.

    Parameters
    ----------
    detection_mat : ndarray
        Matrix of detections. The first 10 columns of the detection matrix are
        in the standard MOTChallenge detection format. In the remaining columns
        store the feature vector associated with each detection.
    frame_idx : int
        The frame index.
    min_height : Optional[int]
        A minimum detection bounding box height. Detections that are smaller
        than this value are disregarded.

    Returns
    -------
    List[tracker.Detection]
        Returns detection responses at given frame index.

    """
    frame_indices = detection_mat[:, 0].astype(np.int)
    mask = frame_indices == frame_idx

    detection_list = []
    #temp = []
    
    for row in detection_mat[mask]:
        #print('row',row)
        bbox, confidence, feature = row[2:6], row[6], row[10:]
        #print('Row 7', row[7])
        #tri.append(row[7])
        # if frame_idx == 50:
        #   print('Row 7',row[7])
        if bbox[3] < min_height:
            continue
        detection_list.append(Detection(bbox, confidence, feature,row[7]))
    
    return detection_list


def run(sequence_dir, detection_file, output_file, min_confidence,
        nms_max_overlap, min_detection_height, max_cosine_distance,
        nn_budget, display):
    """Run multi-target tracker on a particular sequence.

    Parameters
    ----------
    sequence_dir : str
        Path to the MOTChallenge sequence directory.
    detection_file : str
        Path to the detections file.
    output_file : str
        Path to the tracking output file. This file will contain the tracking
        results on completion.
    min_confidence : float
        Detection confidence threshold. Disregard all detections that have
        a confidence lower than this value.
    nms_max_overlap: float
        Maximum detection overlap (non-maxima suppression threshold).
    min_detection_height : int
        Detection height threshold. Disregard all detections that have
        a height lower than this value.
    max_cosine_distance : float
        Gating threshold for cosine distance metric (object appearance).
    nn_budget : Optional[int]
        Maximum size of the appearance descriptor gallery. If None, no budget
        is enforced.
    display : bool
        If True, show visualization of intermediate tracking results.

    """
    seq_info = gather_sequence_info(sequence_dir, detection_file)
    metric = nn_matching.NearestNeighborDistanceMetric(
        "cosine", max_cosine_distance, nn_budget)
    tracker = Tracker(metric)
    results = []
    
    # Create label
    # classs = []
    # 
    # for i in range(len(tri)):
    #   classs.append(label[tri[i]])
    # print(classs)
    #

    def frame_callback(vis, frame_idx):
        print("Processing frame %05d" % frame_idx)

        #input()

        # Load image and generate detections.
        detections = create_detections(
            seq_info["detections"], frame_idx, min_detection_height)
        detections = [d for d in detections if d.confidence >= min_confidence]

        # print("Detections: ", detections)
        # input()

        # Run non-maxima suppression.
        boxes = np.array([d.tlwh for d in detections])
        scores = np.array([d.confidence for d in detections])
        label =  np.array([d.label for d in detections])
        #print('boxes',boxes)
        #print('scores',scores)
        indices = preprocessing.non_max_suppression(
            boxes, nms_max_overlap, scores)
        detections = [detections[i] for i in indices]

        # build label
        label_name = ['Di bo','Xe dap','Xe may',
                'Xe hang rong','Xe ba gac','Xe tac xi',
                'Xe hoi','Xe ban tai','Xe cuu thuong',
                'Xe khach','Xe buyt',
                'Xe tai','Container','Xe cuu hoa']
                
        label_actual = []
        for i in label:
            i = int(i)
            #print('i',i)
            label_actual.append(label_name[i])
            
        # Update tracker.
        tracker.predict()
        tracker.update(detections)

        # Update visualization.
        if display:
            image = cv2.imread(
                seq_info["image_filenames"][frame_idx], cv2.IMREAD_COLOR)
            vis.set_image(image.copy())
            #print(boxes)
            
            # vis.draw_detections(detections,label_actual)
            vis.draw_trackers(tracker.tracks)

        # Store results.
        for track in tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue

            bbox = track.to_tlwh()
            #print('label',track.label)
            results.append([
                frame_idx, track.track_id, bbox[0], bbox[1], bbox[2], bbox[3],track.label])
        #print('Doneee')

    # Run tracker.
    if display:
        print('seq_info',seq_info)
        visualizer = visualization.Visualization(seq_info, update_ms=5)
    else:
        visualizer = visualization.NoVisualization(seq_info)
    
    cam = sequence_dir.split("/")[-1]

    output_path_frames = os.path.join("saved_frames", cam)
  

    visualizer.run(frame_callback, output_path_frames)


    print("Sequence dir: ", sequence_dir)
    print("Cam: ", cam)
    print(output_path_frames) 
    # Store results.
   
    # for k,row in enumerate(results):
    #    print('%d,%d,%.2f,%.2f,%.2f,%.2f,1,-1,-1,-1'.format(
    #             row[0], row[1], row[2], row[3], row[4], row[5]))
    
    print("Ahihi")

    f = open(output_file, 'w')
    #print("The abs path: ", os.path.join(os.path.abspath(output_file), cam + ".txt"))
    for k,row in enumerate(results):
        print('%d,%d,%.2f,%.2f,%.2f,%.2f,1,%d,-1,-1' % (
            row[0], row[1], row[2], row[3], row[4], row[5],row[6]),file=f)

    

    print("hiaa")

def bool_string(input_string):
    if input_string not in {"True","False"}:
        raise ValueError("Please Enter a valid Ture/False choice")
    else:
        return (input_string == "True")

def parse_args():
    """ Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="Deep SORT")
    parser.add_argument(
        "--sequence_dir", help="Path to MOTChallenge sequence directory",
        default=None, required=True)
    parser.add_argument(
        "--detection_file", help="Path to custom detections.", default=None,
        required=True)
    parser.add_argument(
        "--output_file", help="Path to the tracking output file. This file will"
        " contain the tracking results on completion.",
        default="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/")
    parser.add_argument(
        "--min_confidence", help="Detection confidence threshold. Disregard "
        "all detections that have a confidence lower than this value.",
        default=0.8, type=float)
    parser.add_argument(
        "--min_detection_height", help="Threshold on the detection bounding "
        "box height. Detections with height smaller than this value are "
        "disregarded", default=0, type=int)
    parser.add_argument(
        "--nms_max_overlap",  help="Non-maxima suppression threshold: Maximum "
        "detection overlap.", default=1.0, type=float)
    parser.add_argument(
        "--max_cosine_distance", help="Gating threshold for cosine distance "
        "metric (object appearance).", type=float, default=0.2)
    parser.add_argument(
        "--nn_budget", help="Maximum size of the appearance descriptors "
        "gallery. If None, no budget is enforced.", type=int, default=None)
    parser.add_argument(
        "--display", help="Show intermediate tracking results",
         default=True, type=bool_string)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run(
        args.sequence_dir, args.detection_file, args.output_file,
        args.min_confidence, args.nms_max_overlap, args.min_detection_height,
        args.max_cosine_distance, args.nn_budget, args.display)
