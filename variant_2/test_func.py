class TestFunc:

    def func_for_test(self, file_path, n):
        try:
            with open(file_path) as file:
                text = ''
                if n == 0:
                    print('')
                else:
                    for line in (file.readlines()[-n:]):
                        text += line
                    print(text)
        except FileNotFoundError:
            print('File not found')
        except UnicodeDecodeError:
            print('Incorrect file format')
        except TypeError:
            print('n should be integer')
