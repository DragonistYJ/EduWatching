from model.KeyWord.filter import DFAFilter


def test():
    print(DFAFilter().get_instance().filter('的口味'))