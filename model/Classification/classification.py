import numpy
from PIL import Image
from paddle import fluid


def resize_img(img):
    im = img.resize((32, 32), Image.ANTIALIAS)
    im = numpy.array(im).astype(numpy.float32)
    im = im.transpose((2, 0, 1))  # CHW
    im = im / 255.0
    im = numpy.expand_dims(im, axis=0)
    return im


class Classification:
    instance = None
    scope = fluid.Scope()

    def __init__(self):
        with fluid.scope_guard(self.scope):
            self.exe = fluid.Executor(fluid.CUDAPlace(0))
            [self.inference_program, self.feed_target_names, self.fetch_targets] = fluid.io.load_inference_model(
                'model/Classification/weight', self.exe)
            self.label_list = ["normal", "phone", "sleep", "stand"]

    def infer(self, image):
        with fluid.scope_guard(self.scope):
            img = resize_img(image)
            results = self.exe.run(self.inference_program, feed={self.feed_target_names[0]: img},
                                   fetch_list=self.fetch_targets)
            label_index = numpy.argmax(results[0])
            if results[0][0][label_index] < 0.5:
                return "normal"
            elif label_index == 3 and results[0][0][label_index] < 0.85:
                return "normal"
            else:
                return self.label_list[label_index]

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Classification()
        return cls.instance
