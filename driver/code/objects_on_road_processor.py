import cv2
import logging
import datetime
import time
#import edgetpu.detection.engine
from PIL import Image
from traffic_objects import *

_SHOW_IMAGE = False


class ObjectsOnRoadProcessor(object):
    """
    This class 1) detects what objects (namely traffic signs and people) are on the road
    and 2) controls the car navigation (speed/steering) accordingly
    """

    def __init__(self,
                 car=None,
                 speed_limit=30,
                 model=r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/model/object_detection/data/model_result/road_signs_quantized_edgetpu.tflite',
                 label=r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/model/object_detection/data/model_result/road_sign_labels.txt',
                 width=640,
                 height=480):
        # model: This MUST be a tflite model that was specifically compiled for Edge TPU.
        # https://coral.withgoogle.com/web-compiler/
        logging.info('Creating a ObjectsOnRoadProcessor...')
        self.width = width
        self.height = height

        # initialize car
        self.car = car
        self.speed_limit = speed_limit
        self.speed = speed_limit

        # initialize TensorFlow models
        with open(label, 'r') as f:
            pairs = (l.strip().split(maxsplit=1) for l in f.readlines())
            self.labels = dict((int(k), v) for k, v in pairs)

        # initial edge TPU engine
        logging.info('Initialize Edge TPU with model %s...' % model)
        #self.engine = edgetpu.detection.engine.DetectionEngine(model)
        self.min_confidence = 0.30
        self.num_of_objects = 3
        logging.info('Initialize Edge TPU with model done.')

        # initialize open cv for drawing boxes
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.bottomLeftCornerOfText = (10, height - 10)
        self.fontScale = 1
        self.fontColor = (255, 255, 255)  # white
        self.boxColor = (0, 0, 255)  # RED
        self.boxLineWidth = 1
        self.lineType = 2
        self.annotate_text = ""
        self.annotate_text_time = time.time()
        self.time_to_show_prediction = 1.0  # ms

        self.traffic_objects = {0: RedTrafficLight(),
                                1: YellowTrafficLight(),
                                2: GreenTrafficLight(),
                                3: Pedestrian(),
                                4: yeild(),
                                5: StopSign(),
                                6: SpeedLimit(15),
                                7: SpeedLimit(30)}

    def process_objects_on_road(self, frame):
        # Main entry point of the Road Object Handler
        logging.debug('Processing objects.................................')
        final_frame = self.detect_objects(frame)
        #objects, final_frame = self.detect_objects(frame)
        #self.control_car(objects)
        logging.debug('Processing objects END..............................')
        #retutn objects, final_frame
        return final_frame

    def control_car(self, objects):
        logging.debug('Control car...')
        car_state = {"speed": self.speed_limit, "speed_limit": self.speed_limit}

        if len(objects) == 0:
            logging.debug('No objects detected, drive at speed limit of %s.' % self.speed_limit)

        contain_stop_sign = False
        for obj in objects:
            obj_label = self.labels[obj.label_id]
            processor = self.traffic_objects[obj.label_id]
            if processor.is_close_by(obj, self.height):
                processor.set_car_state(car_state)
            else:
                logging.debug("[%s] object detected, but it is too far, ignoring. " % obj_label)
            if obj_label == 'Stop':
                contain_stop_sign = True

        if not contain_stop_sign:
            self.traffic_objects[5].clear()

        self.resume_driving(car_state)

    def resume_driving(self, car_state):
        old_speed = self.speed
        self.speed_limit = car_state['speed_limit']
        self.speed = car_state['speed']

        if self.speed == 0:
            self.set_speed(0)
        else:
            self.set_speed(self.speed_limit)
        logging.debug('Current Speed = %d, New Speed = %d' % (old_speed, self.speed))

        if self.speed == 0:
            logging.debug('full stop for 1 seconds')
            time.sleep(1)

    def set_speed(self, speed):
        # Use this setter, so we can test this class without a car attached
        self.speed = speed
        if self.car is not None:
            logging.debug("Actually setting car speed to %d" % speed)
            self.car.back_wheels.speed = speed



    ############################
    # Frame processing steps
    ############################
    def detect_objects(self, frame):
        logging.debug('Detecting objects...')
        car_xml = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/xml_file/haarcascade_car.xml'
        cars_cascade = cv2.CascadeClassifier(car_xml)
        # call tpu for inference
        start_ms = time.time()
        #frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cars = cars_cascade.detectMultiScale(gray, 1.1, 1)
        img_pil = Image.fromarray(cars)
        #img_pil = Image.fromarray(frame_RGB)
        
        #objects = self.engine.DetectWithImage(img_pil, threshold=self.min_confidence, keep_aspect_ratio=True,
        #                                 relative_coord=False, top_k=self.num_of_objects)       
        '''
        if objects:
            for obj in objects:
                height = obj.bounding_box[1][1]-obj.bounding_box[0][1]
                width = obj.bounding_box[1][0]-obj.bounding_box[0][0]
                logging.debug("%s, %.0f%% w=%.0f h=%.0f" % (self.labels[obj.label_id], obj.score * 100, width, height))
                box = obj.bounding_box
                coord_top_left = (int(box[0][0]), int(box[0][1]))
                coord_bottom_right = (int(box[1][0]), int(box[1][1]))
                cv2.rectangle(frame, coord_top_left, coord_bottom_right, self.boxColor, self.boxLineWidth)
                annotate_text = "%s %.0f%%" % (self.labels[obj.label_id], obj.score * 100)
                coord_top_left = (coord_top_left[0], coord_top_left[1] + 15)
                cv2.putText(frame, annotate_text, coord_top_left, self.font, self.fontScale, self.boxColor, self.lineType)
        else:
            logging.debug('No object detected')
        '''
        elapsed_ms = time.time() - start_ms

        annotate_summary = "%.1f FPS" % (1.0/elapsed_ms)
        logging.debug(annotate_summary)
        cv2.putText(frame, annotate_summary, self.bottomLeftCornerOfText, self.font, self.fontScale, self.fontColor, self.lineType)
        cv2.imshow('Detected Objects', frame)

        #return objects, frame
        return frame

############################
# Utility Functions
############################
def show_image(title, frame, show=_SHOW_IMAGE):
    if show:
        cv2.imshow(title, frame)


############################
# Test Functions
############################
def test_photo(file):
    object_processor = ObjectsOnRoadProcessor()
    frame = cv2.imread(file)
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Detected Objects', combo_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test_stop_sign():
    stop_sign = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/stop_sign.jpg'
    green_light = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/green_light.jpg'
    # this simulates a car at stop sign
    object_processor = ObjectsOnRoadProcessor()
    frame = cv2.imread(stop_sign)
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Stop 1', combo_image)
    time.sleep(1)
    frame = cv2.imread(stop_sign)
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Stop 2', combo_image)
    time.sleep(2)
    frame = cv2.imread(stop_sign)
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Stop 3', combo_image)
    time.sleep(1)
    frame = cv2.imread(green_light)
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Stop 4', combo_image)
    
    

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test_video(video_file):
    object_processor = ObjectsOnRoadProcessor()
    cap = cv2.VideoCapture(video_file + '.avi')

    # skip first second of video.
    for i in range(3):
        _, frame = cap.read()

    #video_type = cv2.VideoWriter_fourcc(*'mp4')
    video_type = cv2.VideoWriter_fourcc(*'XVID')
    date_str = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    video_overlay = cv2.VideoWriter("%s_overlay_%s.avi" % (video_file, date_str), video_type, 20.0, (320, 240))
    try:
        i = 0
        while cap.isOpened():
            _, frame = cap.read()
            cv2.imwrite("%s_%03d.png" % (video_file, i), frame)

            combo_image = object_processor.process_objects_on_road(frame)
            cv2.imwrite("%s_overlay_%03d.png" % (video_file, i), combo_image)
            video_overlay.write(combo_image)

            cv2.imshow("Detected Objects", combo_image)

            i += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        video_overlay.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-5s:%(asctime)s: %(message)s')

    # These processors contains no state
    red = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/red_light.jpg'
    yellow = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/yellow_light.jpg'
    green = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/green_light.jpg'
    pedistrian = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/person.jpg'
    speed15 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/15_mph.jpg'
    yeilding = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/yield.jpg'
    speed30 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/30_mph.jpg'
    stopSign = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/driver/data/objects/stop_sign.jpg'
    test_photo(red)
    test_photo(yellow)
    test_photo(green)
    test_photo(pedistrian)
    test_photo(yeilding)
    test_photo(stopSign)
    test_photo(speed15)
    test_photo(speed30)


    # test stop sign, which carries state
    test_stop_sign()