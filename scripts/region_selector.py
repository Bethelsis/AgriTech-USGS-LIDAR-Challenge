import io

def SelectName(region:str):
    name_ls = []
    names_list =  io.open('../data/filename.txt', encoding='UTF-8').read().strip().split('\n')
    
    if region in names_list or region == 'IA_FullState':
        return region

    if region == 'all':
        return names_list

    else:
        for words in names_list:
            words_ls = words.split('_')
            if region in words_ls:
                name_ls.append(words)
            else: continue
        if name_ls == []:
            return None
        else: return name_ls

def dataset_path(region:str):
    name_list = SelectName(region)

    if type(name_list) == str:
        full_dataset_path = f'https://s3-us-west-2.amazonaws.com/usgs-lidar-public/{name_list}/ept.json'
        tif_path = name_list+'.tif'
        laz_path = name_list+'.laz'
        return full_dataset_path, tif_path, laz_path

    if type(name_list) == None:
        full_dataset_path = f'https://s3-us-west-2.amazonaws.com/usgs-lidar-public/{name_list}/ept.json'
        tif_path = f'{name_list}.tif'
        laz_path = f'{name_list}.laz'
        return full_dataset_path, tif_path, laz_path
    
    if type(name_list) == list:
        full_dataset_path_list = []
        tif_path_list = []
        laz_path_list = []
        for i in name_list:
            path = 'https://s3-us-west-2.amazonaws.com/usgs-lidar-public/'+i+'/ept.json'
            tif = i+'.tif'
            laz = i+'.laz'
            tif_path_list.append(tif)
            laz_path_list.append(laz)
            full_dataset_path_list.append(path)
        return full_dataset_path_list, tif_path_list, laz_path_list

