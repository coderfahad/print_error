import os,sys
def print_error(func_name, error = ""):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    red =  '\033[93m'
    if exc_tb:
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(red," Error--> ",error," | Exception type: ", exc_type, " File Name: ",fname, " Function Name: ",func_name," Line No: ", exc_tb.tb_lineno)
    else:
        print(red," Function Name: ",func_name, " Error--> ",error)