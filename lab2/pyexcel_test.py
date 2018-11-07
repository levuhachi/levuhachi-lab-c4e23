import pyexcel
from collections import OrderedDict

# Prepar Data
list_dicts = [
    OrderedDict({ 
        "name":"Chi",
        "age":"20",
        "job":"Student"
    }),
    OrderedDict({
        "name":"Linh",
        "age":"27",
        "job":"Copywriter"
    }),
    OrderedDict({
        "name":"Minh",
        "age":"30",
        "job":"Business Analyst"
    })
]
#List comprehension

#3. save file using save_as()
pyexcel.save_as(records=list_dicts,dest_file_name="test.xlsx")