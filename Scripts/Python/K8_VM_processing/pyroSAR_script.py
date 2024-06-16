from pyroSAR import identify
from pyroSAR.snap.auxil import parse_recipe, parse_node
from pyroSAR.snap import geocode
from spatialist import Vector
from pyroSAR import Archive
import time

from IPython.display import clear_output

import pandas as pd
import logging
import os

# detailed debug & log info
logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

#workspace directory
workspace_directory = r'/home/ubuntu/Tryggvi/my-awesome-masters-project' #VM
os.chdir(workspace_directory)

#directory setup
path_to_granule_directory = '/home/ubuntu/Tryggvi/Data/asf_slc_granules_dl'

granule_list = r'Data/Vindefjallen_data/Vindefjallen_cleaning/Vindefjallen_Granule_processing/list_of_slc_granules_2023.csv'
#import csv
granules = pd.read_csv(granule_list)
#granule_id column to list
granule_id = granules['granule_ID'].tolist()

#create a dictonry
granule_directory = '/home/ubuntu/Tryggvi/Data/asf_slc_granules_dl'
output_directory = '/home/ubuntu/Tryggvi/Data/pyrosar_processed_granules'

path_to_granule = [granule_directory + '/' + i+'.zip' for i in granule_id ]
path_to_output_directory = [output_directory + '/' +str(i)+'_'+ granule_id[i][17:21] + '-' + granule_id[i][21:23] + '-' + granule_id[i][23:25] for i in range(len(granule_id))]
# date_of_granule =  [i[17:21] + '-' + i[21:23] + '-' + i[23:25] for i in granule_id]

#create dictionary with path_to_granule and path_to_output_directory as values and key is range of granules
granule_paths_dict = {}
for i in range(len(granule_id)):
    granule_paths_dict[i] = { 
        "path_to_granule": path_to_granule[i], 
        'path_to_output_directory': path_to_output_directory[i]
    }

#granule processing loop
for i in range(len(granule_paths_dict)):
    input_path = granule_paths_dict[i]['path_to_granule']
    output_path = granule_paths_dict[i]['path_to_output_directory']
    print("Processing granule number " , i)
    print(input_path)
    print(output_path)
    time.sleep(2)  # Sleep for 1 second

    geocode(
        infile = input_path,
        outdir = output_path,
        t_srs='EPSG:3006', #SWEREF
        polarizations = ['VV', 'VH'],
        scaling = 'linear',
        removeS1ThermalNoise = True,
        terrainFlattening = True,

        demName = 'Copernicus 30m Global DEM',
        export_extra =['localIncidenceAngle', 'layoverShadowMask'],
        alignToStandardGrid = True, #
        speckleFilter = 'Refined Lee',
        refarea = 'gamma0',
        rlks = 27,
        azlks = 7,
        spacing = 100,
        clean_edges = True,
        test = False
    )
    # clear_output(wait=True)
