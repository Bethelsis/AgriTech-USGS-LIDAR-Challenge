from fetch_data import FetchData
from shapely.geometry import Polygon, Point

MINX, MINY, MAXX, MAXY = [-93.756155, 41.918015, -93.756055, 41.918115]
polygon = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))
bound = '([-10425171.940, -10423171.940], [5164494.710, 5166494.710])'
region = 'IA_FullState'
fetch_data = FetchData(bound, region)
fetch_data.run_pipeline()
