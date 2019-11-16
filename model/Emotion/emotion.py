import io
import os

import jieba
from paddle import fluid
import numpy as np


# 0 消极
# 2 积极
# 1 中性
def get_predict_label(pos):
    neg = 1 - pos
    threshold = 0.55
    if neg > threshold:
        label = '消极'
    elif pos > threshold:
        label = '积极'
    else:
        label = '中性'
    return label


def load_vocab(file_path):
    vocab = {}
    with io.open(file_path, 'r', encoding='utf8') as f:
        wid = 0
        for line in f:
            if line.strip() not in vocab:
                vocab[line.strip()] = wid
                wid += 1
    vocab["<unk>"] = len(vocab)
    return vocab


def to_lodtensor(data):
    seq_lens = [len(seq) for seq in data]
    cur_len = 0
    lod = [cur_len]
    for l in seq_lens:
        cur_len += l
        lod.append(cur_len)
    flattened_data = np.concatenate(data, axis=0).astype("int64")
    flattened_data = flattened_data.reshape([len(flattened_data), 1])
    res = fluid.LoDTensor()
    res.set(flattened_data, fluid.CUDAPlace(0))
    res.set_lod([lod])
    return {"words": res}


class Emotion:
    instance = None
    scope = fluid.Scope()

    def __init__(self):
        with fluid.scope_guard(self.scope):
            self.exe = fluid.Executor(fluid.CUDAPlace(0))
            [self.inference_program, self.feed_target_names, self.fetch_targets] = fluid.io.load_inference_model(
                'model/Emotion/weight', self.exe)
            self.word_dict = load_vocab('model/Emotion/vocab.txt')

    def infer(self, word_list):
        with fluid.scope_guard(self.scope):
            data = next(self.data_reader(word_list))
            predict = self.exe.run(self.inference_program,
                                   feed=to_lodtensor([data[0]]),
                                   fetch_list=self.fetch_targets,
                                   return_numpy=True)
            return get_predict_label(predict[0][0, 1])
        # positive [0][0,1]
        # negative [0][0,0]

    def data_reader(self, word_list):
        all_data = []
        unk_id = len(self.word_dict)
        wids = [self.word_dict[x] if x in self.word_dict else unk_id for x in word_list]
        all_data.append((wids, 0))

        for doc, label in all_data:
            yield doc, label

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Emotion()
        return cls.instance
