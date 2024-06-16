vindefjallen_corner_coords_processing_2023 - listi yfir gjörsamlega alla punkta og info með þeim - deleted
slc_granule_every_point_2023 er listi yfir alla punkta sem passa á SLC granules
vindefjallen_corner_coords_processing_2023_middletime_with_granule_paths. Það er búið að bæta við nöfnum á processed granule tif fælum. Búið til í values_from_raster.ipynb
Middle time er median á þeim tíma sem tók að mæla EINN triangle. Þannig að 3 mælingar í sama triangle hafa sama gildi. En þá geta margir triangles sem voru m´ldir á sama degi
haft mismuandi middletime values.
list_of_slc_granules_2023_ERA5.csv - nýtt. Búið til með því að nota ERA5 til að finna aðra daga og granules fyrir datasetið mitt. Búið til með Scripts\Python\ERA5\era5_weather.ipynb

list_of_slc_granules_2023_ERA5_MISTAKE_DELETE_LATER - óvart hef ég exportað dict sem er með allar stakar mælingar + granules, en ekki bara granules. Þetta gæti hafa leitt til vandamála.