class Check:
    # This method returns True if string contains digits
    @staticmethod
    def check_string_on_digit(str):
        temp = False
        for i in str:
            if i.isdigit():
                temp = True
                break
        return temp

    # This method returns True if string contains special symbols
    @staticmethod
    def check_string_on_special_symbols(str):
        temp = False
        special_symbols = "~!@#$%^&*()}{:><?.,№/|"
        for i in str:
            for y in special_symbols:
                if i == y:
                    temp = True
                    break
        return temp
