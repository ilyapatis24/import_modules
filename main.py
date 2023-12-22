from datetime import datetime
from application.db.people import get_employees as ge
from application.salary import calculate_salary as cs

import numpy # нашел интересный модуль для себя!!!

avg_li = [1,2,3,4]
new_li_avg = numpy.average(avg_li)
if __name__=="__main__":
    ge()
    cs()
    print(datetime.now())
    print(new_li_avg)