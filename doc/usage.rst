

Usage
=====


How to clone the code
---------------------
The package is not available PyPi yet. You can download the github repository and use it.

$ git clone https://github.com/Bethelsis/AgriTech-USGS-LIDAR-Challenge.git



description
-----------
Class fetch_lidar_data:
This class retrieves lidar elevation data points from a publicly available data file. (https://s3-us-west-2.amazonaws.com/usgs-lidar-public/).
It leverages the pdal.io pipeline to fetch, translate, and alter cloud data points. A JSON pipeline description is required by the pdal.io pipeline. The pipeline is defined via a json file template (pipeline.json file).

  def get_elevation(self, array_data):
  This method takes a numpy array of cloud data points from the pdal pipeline and creates a geopandas data frame with an elevation column and a geometry column that   indicate point coordinates in a particular coordinate reference system.
        Args:
            array_data (Numpy): cloud data points in Numpy format
        Returns:
            geopandas.GeoDataFrame: a geopandas data frame having an elevation column and a geometry column.
  def get_polygon_boundaries(self, polygon: Polygon) :

  This method computes the rectangular limits of a specified polygon and returns a string representation of the bounds computed.

       Args:
           polygon (Polygon): a given shapely.geometry.Polygon object

       Returns:
           A two-element tuple consisting of a string representation of the calculated limits and a string format of the specified polygon in the format expected by            the pdal pipeline.

  def runPipeline(self):
  reads the point cloud data from the EPT resource on AWS.
     Returns:
     list of numpy array of cloud point data 






