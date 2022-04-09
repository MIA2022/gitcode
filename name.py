class Name:
    def __init__(self, first_name, last_name, nick_name=''):
        if not isinstance(first_name, str):
            raise TypeError
        if not isinstance(last_name, str):
            raise TypeError
        if not isinstance(nick_name, str):
            raise TypeError
        if first_name == '':
            raise ValueError
        if last_name == '':
            raise ValueError
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name

    def get_first_name(self):
        output = self.first_name
        return output

    def get_last_name(self):
        output = self.last_name
        return output

    def get_full_name(self):
        output = self.first_name + ' ' + self.last_name
        return output

    def set_nick_name(self, nick_name):
        if nick_name == '':
            raise ValueError
        if not isinstance(nick_name, str):
            raise TypeError
        self.nick_name = nick_name

    def get_nick_name(self):
        output = self.nick_name
        return output

    def __str__(self):
        output = self.first_name + ' "' + \
                  self.nick_name + '" ' + self.last_name
        return output
