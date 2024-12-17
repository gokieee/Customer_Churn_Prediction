import sys

def error_message_detaile(error, error_detaile:sys):
    _,_,exc_tb=error_detaile.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detaile(error_message,error_details)

    def str(self):
        return self.error_message