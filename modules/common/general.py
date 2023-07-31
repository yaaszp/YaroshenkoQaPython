class General:
    # This method returns True if string contains digits
    def check_string_on_digit(self, str):
        temp = False
        for i in str:
            if i.isdigit():
                temp = True
                break
        return temp

    # This method returns True if string contains special symbols
    def check_string_on_special_symbols(self, str):
        temp = False
        special_symbols = "~!@#$%^&*()}{:><?.,№/|"
        for i in str:
            for y in special_symbols:
                if i == y:
                    temp = True
                    break
        return temp