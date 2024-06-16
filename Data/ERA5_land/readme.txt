fixing my mistake. this is era5 14.5.2024
  
adaptor.mars.internal-1715687018.5196297-2796-7-bccc8a41-f2ec-4a0b-806c-a6ce5f2094fc.nc

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-land',
    {
                "area": [
            66.25,
            15.25,
            65.75,
            16.75,
        ],
        'variable': [
            'snow_density', 
            'snow_depth', 
            'snow_depth_water_equivalent',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': '12:00',
        "month": ["01","02","03","04","05"],
        "year": ["2017","2018","2019","2020","2021","2022",
            "2023"],
        'format': 'netcdf',
    },
    'download.nc')
	
	
adaptor.mars.internal-1715696417.7502532-29298-8-26517478-0dc3-4ccd-9076-d779e94b04ca.nc

reanalysis-era5-landRequest body:{
  "area": [
    66.25,
    15.25,
    65.75,
    16.75
  ],
  "day": [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31"
  ],
  "format": "netcdf",
  "month": [
    "01",
    "02",
    "03",
    "04",
    "05"
  ],
  "time": "12:00",
  "variable": [
    "skin_temperature"
  ],
  "year": [
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023"
  ]
}

#bara snow depth
adaptor.mars.internal-1715766930.6635869-31765-6-a200f460-334d-4af3-99a7-32b83d4debbe.nc


reanalysis-era5-landRequest body:{
  "area": [
    67,
    14.5,
    65,
    17
  ],
  "day": [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31"
  ],
  "format": "netcdf",
  "month": [
    "01",
    "02",
    "03",
    "04",
    "05"
  ],
  "time": "12:00",
  "variable": "snow_depth",
  "year": [
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023"
  ]
}

25.5.24

eanalysis-era5-landRequest body:{
  "area": [
    67,
    14.5,
    65,
    17
  ],
  "day": [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "21",
    "22",
    "23",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31"
  ],
  "format": "netcdf",
  "month": [
    "01",
    "02",
    "03",
    "04",
    "05"
  ],
  "time": "13:00",
  "variable": [
    "leaf_area_index_high_vegetation",
    "leaf_area_index_low_vegetation",
    "skin_temperature",
    "snow_density",
    "snow_depth",
    "snow_depth_water_equivalent",
    "temperature_of_snow_layer",
    "total_precipitation"
  ],
  "year": [
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023"
  ]
}