class TestFunc:

    def func_for_test(self, file_path, n):
        try:
            with open(file_path) as file:
                text = ''
                if n == 0:
                    return ''
                else:
                    for line in (file.readlines()[-n:]):
                        text += line
                    return text
        except FileNotFoundError:
            return 'File not found'
        except UnicodeDecodeError:
            return 'Incorrect file format'
        except TypeError:
            return 'n should be integer'
