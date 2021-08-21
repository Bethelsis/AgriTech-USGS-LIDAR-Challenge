import pdal
import json
import geopandas as gpd
from shapely.geometry import box, Point, Polygon
class Fetch_data:
    def __init__(self,bound,region:str) -> None:
        self.bound = bound
        self.region = region
    def read_Json(self) -> dict:
        try:
            with open("fetch_data.json", 'r') as json_file:
                dict_obj = json.load(json_file)
            return dict_obj
        except FileNotFoundError as e:
            print('FILE NOT FOUND')
    def polygon_boundaries(self, polygon: Polygon):
        polygon_df = gpd.GeoDataFrame([polygon], columns=['geometry'])

        polygon_df.set_crs(26915, inplace=True)
        polygon_df['geometry'] = polygon_df['geometry'].to_crs(3857)
        minx, miny, maxx, maxy = polygon_df['geometry'][0].bounds
        polygon_input = 'POLYGON(('
        xcord, ycord = polygon_df['geometry'][0].exterior.coords.xy
        for x, y in zip(list(xcord), list(ycord)):
            polygon_input += f'{x} {y}, '
        polygon_input = polygon_input[:-2]
        polygon_input += '))'
        return polygon_input

    def getPipeline(self, polygon: Polygon):
        fetch_json = self.read_Json()
        polygon_input = self.polygon_boundaries(polygon)
        full_dataset_path = f"https://s3-us-west-2.amazonaws.com/usgs-lidar-public/{region}/ept.json"
        #print(full_dataset_path)
        fetch_json['pipeline'][0]['filename'] = full_dataset_path
        fetch_json['pipeline'][0]['bounds'] = bound
        fetch_json['pipeline'][1]['polygon'] = polygon_input
        fetch_json['pipeline'][5]['filename']=f"data/{region}.laz"
        fetch_json['pipeline'][6]['filename']=f"data/{region}.tif"
        pipeline = pdal.Pipeline(json.dumps(fetch_json))
        return pipeline

    def runPipeline(self, polygon: Polygon):
        pipeline = self.getPipeline(polygon)
        try:
            pipeline.execute()
            metadata = pipeline.metadata
            log = pipeline.log
            return pipeline.arrays
        except RuntimeError as e:
            print(e)
    def get_elevation(self, array_data):
        if array_data:

            for i in array_data:
                geometry_points = [Point(x, y) for x, y in zip(i["X"], i["Y"])]
                elevations = i["Z"]
                df = gpd.GeoDataFrame(columns=["elevation", "geometry"])
                df['elevation'] = elevations
                df['geometry'] = geometry_points
                df = df.set_geometry("geometry")
                df.set_crs(epsg=26915, inplace=True)

            return df
    def visualize (self, df: gpd.GeoDataFrame, cmap="terrain") -> None:

        fig, ax = plt.subplots(1, 1, figsize=(12, 10))

        df.plot(column='elevation', ax=ax, legend=True, cmap=cmap)
        plt.show()
if __name__ == "__main__":

    MINX, MINY, MAXX, MAXY = [-93.756155, 41.918015, -93.747334, 41.921429]

    polygon = Polygon(((MINX, MINY), (MINX, MAXY),
                       (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))
    bound="([-10425171.940, -10423171.940], [5164494.710, 5166494.710])"
    region="IA_FullState"
    fetcher = Fetch_data(bound,region)
    data=fetcher.runPipeline(polygon)
#     df = fetcher.get_elevation(data)
#     print(df.info())
#     print(df)
