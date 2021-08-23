
import rasterio
import rasterio.plot
import matplotlib.pyplot as plt
import logging
class Visualize:
    def plot(self, filename : str, title : str):
       
        try:
            tif = rasterio.open(filename)
        except FileNotFoundError:
            print(f'Error: file  not Found')
            logging.error(f'Error: file not Found')
        fig, axes = plt.subplots(figsize=(13,13))
        rasterio.plot.show(tif, title = title)
