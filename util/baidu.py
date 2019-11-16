from aip import AipSpeech


class DuAPI:
    APP_ID = '17674810'
    API_KEY = 'fVP9VGjFeUMNEf8dhyLyuiN7'
    SECRET_KEY = 'BG349KHUIt7Ddu1cNKGuY3B32p07OKaC'
    instance = None

    def __init__(self):
        self.aipClient = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def asr(self, wav_path):
        def get_file_content(path):
            with open(path, 'rb') as fp:
                return fp.read()

        ans = self.aipClient.asr(get_file_content(wav_path), 'wav', 16000, {'dev_pid': 1936})
        if ans['err_msg'] == 'success.':
            return ans['result'][0]
        else:
            return ''

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = DuAPI()
        return cls.instance
