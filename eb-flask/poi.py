import pandas as pd

# CSV data imports
df_rest = pd.read_csv('CSVs/Rest_Stop_API.csv')
df_walmart = pd.read_csv("CSVs/Walmart_API.csv")
df_weigh = pd.read_csv("CSVs/Weigh_Station_API.csv")
df_descents = pd.read_csv("CSVs/Road_Descents_API.csv")
df_tourist = pd.read_csv("CSVs/Tourist_Attractions_API.csv")
df_campsite = pd.read_csv("CSVs/Campsites_API.csv")
df_dump = pd.read_csv("CSVs/Dump_Stations_API.csv")

def location_finder(df, latitude, longitude, distance):
    """
    Returns places of interest within a designated area for a users specific geographic coordinates.
    
    Parameters:
        df (Pandas DataFrame): DataFrame containing places of interest and their corresponding lat/long coordinates
        latitude (Float value): Users designated latitude
        longitude (Float value): Users designated longitude
        distance (Int): Value that determines the search area size for designated place of interest
        
    Returns:
        df (Pandas DataFrame): DataFrame containing only the places of interest that are within the user's designated search area
    
    
    """
    
    # Each lat/long degree is ~69.2 miles
    geo_dist = distance / 69.2

    # Creates boundary limits on the latitude parallel
    lat_plus = latitude + geo_dist
    lat_minus = latitude - geo_dist

    # Creates boundary limits on the longitude parallel
    long_plus = longitude + geo_dist
    long_minus = longitude - geo_dist
    
    long_list = []
    lat_list = []

    # Append to list the longitude coordinates that fall within boundary limits
    for i in df['Longitude']:
        if i < long_plus:
            if i > long_minus:
                long_list.append(i)
    
    # Create new dataframe containing only rows containing longitude's within long_list
    df_long = df.loc[df['Longitude'].isin(long_list)]

    # Append to list the latitude coiordinates that fall within boundary limits
    for i in df_long['Latitude']:
        if i < lat_plus:
            if i > lat_minus:
                lat_list.append(i)
                
    # Create final dataframe containing only rows containing latitude's within lat_list 
    df_final = df_long.loc[df_long['Latitude'].isin(lat_list)]
    
    #df_final = df_final.drop('Unnamed: 0', axis=1)
    
    return df_final