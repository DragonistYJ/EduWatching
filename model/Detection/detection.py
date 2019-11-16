import os

import cv2
import numpy
from paddle import fluid


def img_reader(im_path):
    im = cv2.imread(im_path).astype('float32')
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    h, w, _ = im.shape
    im_scale_x = 608 / float(w)
    im_scale_y = 608 / float(h)
    out_img = cv2.resize(
        im,
        None,
        None,
        fx=im_scale_x,
        fy=im_scale_y,
        interpolation=cv2.INTER_CUBIC)
    mean = numpy.array([0.485, 0.456, 0.406]).reshape((1, 1, -1))
    std = numpy.array([0.229, 0.224, 0.225]).reshape((1, 1, -1))
    out_img = (out_img / 255.0 - mean) / std
    out_img = out_img.transpose((2, 0, 1))

    return out_img, (h, w)


def reader(img_path):
    im, im_shape = img_reader(img_path)
    batch_out = [(im, im_shape)]
    yield batch_out


class Detection:
    instance = None
    scope = fluid.Scope()

    def __init__(self):
        with fluid.scope_guard(self.scope):
            image = fluid.layers.data(name='image', shape=[3, 608, 608], dtype='float32')
            im_shape = fluid.layers.data(name="im_shape", shape=[2], dtype='int32')
            self.feeder = fluid.DataFeeder(place=fluid.CUDAPlace(0), feed_list=[image, im_shape])
            self.exe = fluid.Executor(fluid.CUDAPlace(0))
            [self.infer_program, self.feed_target_names, self.fetch_targets] = fluid.io.load_inference_model(
                'model/Detection/weight', self.exe)
            self.score_thresh = 0.2
            self.init_detection()

    # 非常神奇
    # 如果没有这张图片，信号量锁不住
    def init_detection(self):
        self.count_number('model/Detection/timg.jpg')

    def count_number(self, image_path):
        with fluid.scope_guard(self.scope):
            data = next(reader(image_path))
            outputs = self.exe.run(self.infer_program, feed=self.feeder.feed(data), fetch_list=self.fetch_targets,
                                   return_numpy=False)
            bboxes = numpy.array(outputs[0])
            scores = bboxes[:, 1].astype('float32')
            num = 0
            for x in scores:
                if x >= self.score_thresh: num += 1
            return num

    def get_boxes(self, image_path):
        with fluid.scope_guard(self.scope):
            data = next(reader(image_path))
            outputs = self.exe.run(self.infer_program, feed=self.feeder.feed(data), fetch_list=self.fetch_targets,
                                   return_numpy=False)
            bboxes = numpy.array(outputs[0])
            scores = bboxes[:, 1].astype('float32')
            boxes = bboxes[:, 2:].astype('float32')
            thresh_boxes = []
            for i in range(len(boxes)):
                if scores[i] >= self.score_thresh:
                    thresh_boxes.append(boxes[i])
            return thresh_boxes

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Detection()
        return cls.instance
