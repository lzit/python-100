'''判断给定字符串是否包含重复字符'''

class UniqueChars(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)
