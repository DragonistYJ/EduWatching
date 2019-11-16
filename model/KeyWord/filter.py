class DFAFilter:
    instance = None

    def __init__(self):
        self.keyword_chains = {}
        self.delimit = '\x00'
        self.parse("model/KeyWord/keywords")

    def add(self, keyword):
        keyword = keyword.lower()
        chars = keyword.strip()
        if not chars:
            return
        level = self.keyword_chains
        for i in range(len(chars)):
            if chars[i] in level:
                level = level[chars[i]]
            else:
                if not isinstance(level, dict):
                    break
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit: 0}
                break
        if i == len(chars) - 1:
            level[self.delimit] = 0

    def parse(self, path):
        with open(path, encoding='UTF-8') as f:
            for keyword in f:
                self.add(keyword.strip())

    def filter(self, message):
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        if step_ins == 1:
                            ret.append(message[start:start + step_ins])
                        else:
                            ret.append('<span>{0}</span>'.format(message[start:start + step_ins]))
                        start += step_ins - 1
                        break
                else:
                    ret.append(message[start])
                    break
            else:
                ret.append(message[start])
            start += 1

        return ''.join(ret)

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = DFAFilter()
        return cls.instance
