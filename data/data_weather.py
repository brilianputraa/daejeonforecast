import meteostat
import matplotlib.pyplot as plt

from datetime import datetime

start_period = datetime(2014,1,1)
end_period = datetime.utcnow()

nonsan_point = meteostat.Point(36.1214, 127.05499, 16)
weather_data = meteostat.Daily(nonsan_point, start_period, end_period)
weather_data = weather_data.fetch()

weather_data.plot()
plt.show()
