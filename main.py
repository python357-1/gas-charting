DATA_URL = ""

import matplotlib.pyplot as plt
import pandas as pd

def normalize_price(x):
    if x != "- - -":
        if (x.startswith("$")):
            return float(x[1:])
        else:
            return float(x)

gas_stations = pd.read_json(DATA_URL)
nonzero_prices = gas_stations[gas_stations["price"] > 0.01]

murphy = nonzero_prices[nonzero_prices["station_name"].str.contains("Murphy USA")]
sams = nonzero_prices[nonzero_prices["station_name"].str.contains("Sam's Club")]
chevron = nonzero_prices[nonzero_prices["station_name"].str.contains("Chevron")]
kroger = nonzero_prices[nonzero_prices["station_name"].str.contains("Kroger")]
shell = nonzero_prices[nonzero_prices["station_name"].str.contains("Shell")]

plt.plot(sams["scraped_time"], sams['price'], label='sams')
plt.plot(murphy["scraped_time"], murphy['price'], label='murphy')
plt.plot(kroger["scraped_time"], kroger['price'], label='kroger')
plt.plot(shell["scraped_time"], shell['price'], label='shell')

plt.legend()

plt.show()
