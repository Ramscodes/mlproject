import os
import sys


class HousingException(Exception):
    
    #error_message is the object of the exception occurred while the project is running.
    #error_detail is the sys object which contains current execution information is stored 
        #from which file and from which line the exception is occurred.
    def __init__(self, error_message:Exception,error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_detail_message = HousingException.get_detailed_error_message(error_message=error_message,
                                                                                error_detail=error_detail) 
    
    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        """
        This function takes the error_message and error_details and 
        returns them as a string which contain file name,line number and the error got occurred.
        """
        _,_,exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_detail_message  = f"""Error occurred in the script:->[{file_name}] at line number [{line_number}] 
                                          and the error message :->[{error_message}]
        """
        return error_detail_message

    def __str__(self) -> str:
        return self.error_detail_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()
    
    




        

