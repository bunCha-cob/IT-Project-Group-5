import time, random
import numpy as np
from absl import app, flags, logging
from absl.flags import FLAGS
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny
)
from yolov3_tf2.dataset import transform_images
from yolov3_tf2.utils import draw_outputs, convert_boxes

from deep_sort import preprocessing
from deep_sort import nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker
from tools import generate_detections as gdet
from PIL import Image
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm

import mysql.connector as mariadb
import sys

flags.DEFINE_string('classes', './data/labels/coco.names', 'path to classes file')
flags.DEFINE_string('weights', './weights/yolov3.tf',
                    'path to weights file')
flags.DEFINE_boolean('tiny', False, 'yolov3 or yolov3-tiny')
flags.DEFINE_integer('size', 416, 'resize images to')
flags.DEFINE_string('video', './data/video/test.mp4',
                    'path to video file or number for webcam)')
flags.DEFINE_string('output', None, 'path to output video')
flags.DEFINE_string('output_format', 'XVID', 'codec used in VideoWriter when saving video to file')
flags.DEFINE_integer('num_classes', 80, 'number of classes in the model')


def main(_argv):
    # Definition of the parameters
    max_cosine_distance = 0.5
    nn_budget = None
    nms_max_overlap = 1.0
    
    #initialize deep sort
    model_filename = 'model_data/mars-small128.pb'
    encoder = gdet.create_box_encoder(model_filename, batch_size=1)

    """
    A nearest neighbor distance metric that, for each target, returns
    the closest distance to any sample that has been observed so far.
    """
    metric = nn_matching.NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)

    # multi target tracker
    tracker = Tracker(metric)

    # Return a list of physical devices visible to the host runtime
    physical_devices = tf.config.experimental.list_physical_devices('GPU')

    if len(physical_devices) > 0:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        # enable memory growth for physical devices

    # identify type of YoloV3 used
    if FLAGS.tiny:
        yolo = YoloV3Tiny(classes=FLAGS.num_classes)
    else:
        yolo = YoloV3(classes=FLAGS.num_classes)

    # load pre-trained weights
    yolo.load_weights(FLAGS.weights)
    logging.info('weights loaded')

    # array contains name of classes
    class_names = [c.strip() for c in open(FLAGS.classes).readlines()]
    logging.info('classes loaded')

    # capture a video from the camera or a video file
    try:
        vid = cv2.VideoCapture(int(FLAGS.video))
    except:
        vid = cv2.VideoCapture(FLAGS.video)

    # output video is empty
    out = None

    if FLAGS.output:
        # by default VideoCapture returns float instead of int
        width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(vid.get(cv2.CAP_PROP_FPS))
        codec = cv2.VideoWriter_fourcc(*FLAGS.output_format)
        out = cv2.VideoWriter(FLAGS.output, codec, fps, (width, height))
        list_file = open('detection.txt', 'w')
        frame_index = -1 
    
    _, img = vid.read()
    h, w, c = img.shape
    h_numStep = 12; # number of boxes in a column
    w_numStep = 20; # number of boxes in a row

    M = [[ 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5], 
     [ 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5],
     [ 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 8, 8],
     [ 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 8, 8, 8, 8], 
     [ 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8],
     [ 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 7, 7],
     [ 2, 2, 2, 2, 2, 2, 2, 2, 4, 6, 6, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7],
     [ 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 7, 7, 7, 7],
     [ 2, 2, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 7, 7, 7, 7, 7],
     [ 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 7, 7, 7, 7, 7],
     [ 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7],
     [ 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7]]

    # store the total time that customers stay in box[i][j] 
    total_time_engage = [[0 for i in range(w_numStep+1)] for j in range(h_numStep+1)]

    # store the time that customer k is stationary in box[i][j]
    stationary_time = [[[0 for i in range(w_numStep+1)] for j in range(h_numStep+1)] for k in range(100000)]

    # store the positions of single customer 
    x_single_tracking = []
    y_single_tracking = []
    # single customer's trackingID
    single_trackingID = 34

    fps = 0.0
    count = 0 
    while True:

        _, img = vid.read()

        if img is None:
            logging.warning("Empty Frame")
            time.sleep(0.1)
            count+=1
            if count < 3:
                continue
            else: 
                break

        # convert an image from one color space to another  
        img_in = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # return a tensor with a length 1 axis inserted at index 0
        img_in = tf.expand_dims(img_in, 0)

        # resize the image to 416x416
        # tensorflow.image.resize: resize image to size
        img_in = transform_images(img_in, FLAGS.size)

        # return the number of seconds passed since epoch
        t1 = time.time()
        time_finish_last_tracking = t1;

        boxes, scores, classes, nums = yolo.predict(img_in)
        classes = classes[0]
        names = []
        for i in range(len(classes)):
            names.append(class_names[int(classes[i])])
        names = np.array(names)
        converted_boxes = convert_boxes(img, boxes[0])
        features = encoder(img, converted_boxes)    

        detections = [Detection(bbox, score, class_name, feature) for bbox, score, class_name, feature in zip(converted_boxes, scores[0], names, features)]
        
        #initialize color map
        cmap = plt.get_cmap('tab20b')
        colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]

        # run non-maxima suppresion
        boxs = np.array([d.tlwh for d in detections])
        scores = np.array([d.confidence for d in detections])
        classes = np.array([d.class_name for d in detections])
        indices = preprocessing.non_max_suppression(boxs, classes, nms_max_overlap, scores)
        detections = [detections[i] for i in indices]        

        # Pass detections to the deepsort object and obtain the track information
        tracker.predict()
        tracker.update(detections)

        # draw horizontal boxes
        y_step = int(h/h_numStep);
        y_start = 0;
        while True:
            y_end = y_start + y_step 
            cv2.rectangle(img, (0, y_start), (int(w), y_end)  , (0,0,0), 1)
            y_start = y_end
            if y_start >= int(h):
                break # finish drawing here
        
        # draw vertical boxes
        x_step = int(w/w_numStep);
        x_start = 0;
        while True:
            x_end = x_start + x_step 
            cv2.rectangle(img, (x_start, 0), (x_end, int(h))  , (0,0,0), 1)
            x_start = x_end
            if x_start >= int(w):
                break # finish drawing here

        time_step = time.time() - time_finish_last_tracking
        for track in tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue 
            bbox = track.to_tlbr() # get the corrected/predicted bounding box
            class_name = track.get_class() # get the class name of particular object
            color = colors[int(track.track_id) % len(colors)] 
            color = [i * 255 for i in color] 

            # identify center of a boundary box
            x_cent = int(bbox[0] + (bbox[2]-bbox[0])/2)
            y_cent = int(bbox[1] + (bbox[3]-bbox[1])/2)

            # draw detection on frame
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), color, 2) # draw rectangle 
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1]-30)), (int(bbox[0])+(len(class_name)+len(str(track.track_id)))*17, int(bbox[1])), color, -1)
            cv2.putText(img, class_name + "-" + str(track.track_id),(int(bbox[0]), int(bbox[1]-10)),0, 0.75, (255,255,255),2) # insert objectName and objectID

            # update the stationary_time and total_time_engage array
            if class_name == "person":
                x_pos = int(x_cent/x_step)
                y_pos = int(y_cent/y_step)
                stationary_time[track.track_id][y_pos][x_pos] += time_step 
                total_time_engage[y_pos][x_pos] += time_step
            
            # track a single person
            if class_name == "person" and track.track_id == single_trackingID:
                x_single_tracking.append(x_pos)
                y_single_tracking.append(y_pos)
                
        ### UNCOMMENT BELOW IF YOU WANT CONSTANTLY CHANGING YOLO DETECTIONS TO BE SHOWN ON SCREEN
        #for det in detections:
        #    bbox = det.to_tlbr() 
        #    cv2.rectangle(img,(int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])),(255,0,0), 2)
        time_finish_last_tracking = time.time()

        # print fps on screen 
        fps  = ( fps + (1./(time.time()-t1)) ) / 2
        cv2.putText(img, "FPS: {:.2f}".format(fps), (0, 30),
                          cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
        cv2.imshow('output', img)
        if FLAGS.output:
            out.write(img)
            frame_index = frame_index + 1
            list_file.write(str(frame_index)+' ')
            if len(converted_boxes) != 0:
                for i in range(0,len(converted_boxes)):
                    list_file.write(str(converted_boxes[i][0]) + ' '+str(converted_boxes[i][1]) + ' '+str(converted_boxes[i][2]) + ' '+str(converted_boxes[i][3]) + ' ')
            list_file.write('\n')

        # press q to quit
        if cv2.waitKey(1) == ord('q'):
            break

    # insert data into the database

    # initialise track arrays
    track_time = [0] * 10000000
    track_customerID = [0] * 10000000
    track_area = ["" for x in range(10000000)]
    x_single = [0] * 10000000
    y_single = [0] * 10000000

    # organise data to be inserted
    track_index = -1
    for k in range(1000):
        for h in range(h_numStep):
            for w in range(w_numStep):
                if stationary_time[k][h][w] != 0:
                    track_index += 1 
                    track_time[track_index] = stationary_time[k][h][w]
                    track_customerID[track_index] = k
                    track_area[track_index] = str(h) + ', ' + str(w)
    x_tmp = -1
    y_tmp = -1        
    single_track_index = -1;
    for k in range(len(x_single_tracking)):
        if x_single_tracking[k] != x_tmp and y_single_tracking[k] != y_tmp:
            single_track_index += 1
            x_single[single_track_index] = x_single_tracking[k]
            y_single[single_track_index] = y_single_tracking[k]
            x_tmp = x_single[single_track_index] 
            y_tmp = y_single[single_track_index] 
    single_tracking_areas = ""
    for k in range(single_track_index):
        single_tracking_areas += '[' + str(x_single[k]) + ',' + str(y_single[k]) + '] , ' 

    # connect and insert the appropriate data in primary_table
    for k in range(track_index+1):
        try:
            conn = mariadb.connect( user="root",
                                    password="root",
                                    host="localhost",
                                    database="trackingDB")
        
            cur = conn.cursor()
            mySql_insert_query = """INSERT INTO primary_table(trackID, customerID, area) 
                                    VALUES (%s, %s, %s) """

            recordTuple = (k, track_customerID[k], track_area[k])
            cur.execute(mySql_insert_query, recordTuple)
            conn.commit()

        except mariadb.Error as error:
            print ("Failed to insert record into the primary_table {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()

    # connect and insert the appropriate data in "engaged" table 
    for k in range(track_index+1):
        try:
            conn = mariadb.connect( user="root",
                                    password="root",
                                    host="localhost",
                                    database="trackingDB")
        
            cur = conn.cursor()
            mySql_insert_query = """INSERT INTO engaged(trackID, engagement_time) 
                                    VALUES (%s, %s) """

            recordTuple = (k, track_time[k])
            cur.execute(mySql_insert_query, recordTuple)
            conn.commit()

        except mariadb.Error as error:
            print ("Failed to insert record into the engaged table {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()

    # connect and insert the appropriate data in "total_areas" table 
    try:
        conn = mariadb.connect( user="root",
                                password="root",
                                host="localhost",
                                database="trackingDB")
        
        cur = conn.cursor()
        mySql_insert_query = """INSERT INTO total_areas(customerID, all_areas_visited) 
                                    VALUES (%s, %s) """

        recordTuple = (single_trackingID, single_tracking_areas)
        cur.execute(mySql_insert_query, recordTuple)
        conn.commit()

    except mariadb.Error as error:
        print ("Failed to insert record into the total_areas table {}".format(error))
    finally:
        if (conn.is_connected()):
            cur.close()
            conn.close()

    # plot the graph 
    fig = plt.figure(1)
    fig.suptitle('Engagement time on different areas', fontsize=20)
    ax = plt.axes(projection='3d')
    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    x = np.arange(w_numStep-1, -1, -1)
    y = np.linspace(0, h_numStep-1, h_numStep)
    X, Y = np.meshgrid(x, y)
    Z = [[0 for j in range(w_numStep)] for i in range(h_numStep)]
    for i in range(h_numStep):
        for j in range(w_numStep):
            Z[i][j] = total_time_engage[i][j]
    Z = np.array(Z)

    # Plot the surface.
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_xlabel('width')
    ax.set_ylabel('height')
    ax.set_zlabel('time')

    ax.view_init(35, 80)

    frame = plt.gca()

    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])

    fig2 = plt.figure(2)
    fig2_title = 'Walking pattern of a single customer( trackingID = ' + str(single_trackingID) + ')'
    fig2.suptitle(fig2_title, fontsize=15)
    plt.plot(x_single_tracking,y_single_tracking, 'ro')
    plt.axis([0,w_numStep,h_numStep,0])

    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])

    fig.savefig('engage_level.jpg')
    fig2.savefig('single_tracking.jpg')
    plt.show()

    vid.release()
    if FLAGS.ouput:
        out.release()
        list_file.close()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
