import json
   
def open_json(path):
    with open(path, 'r')as json_file:
        dict_ob = json.load(json_file)
    return dict_ob

def edit_pipeline(full_dataset_path, laz_path, tif_path, output_epsg, bound, polygon_input):
    fetch_json = open_json("./pipeline.json")
    fetch_json['pipeline'][0]['filename'] = full_dataset_path
    fetch_json['pipeline'][0]['bounds'] = bound
    fetch_json['pipeline'][1]['polygon'] = polygon_input
    fetch_json['pipeline'][3]['out_srs'] = f'EPSG:{output_epsg}'
    fetch_json['pipeline'][4]['filename'] = "../data/"+laz_path
    fetch_json['pipeline'][5]['filename'] = "../data/"+tif_path


    return fetch_json
