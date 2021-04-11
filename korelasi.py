# Map View

import pandas as pd
import plotly.express as px

well_meta_df = pd.read_csv('wellbore_exploration_all.csv')
well_meta_df.rename(columns={'wlbWellboreName': 'WELL',
                             'wlbWell': 'WELL_HEAD',
                            'wlbNsDecDeg': 'lat',
                            'wlbEwDesDeg': 'lon',
                            'wlbDrillingOperator': 'Drilling Operator',
                            'wlbPurposePlanned': 'Purpose',
                            'wlbCompletionYear': 'Completion Year',
                            'wlbFormationAtTd': 'Formation'}, inplace=True)


well_locations_df = well_meta_df[['WELL_HEAD', 'lat', 'lon']].drop_duplicates(subset=['WELL_HEAD'])

well_names = ['17/11-1', '17/4-1']
well_meta_df = well_meta_df[['WELL','Drilling Operator', 'Purpose','Completion Year', 'Formation']]
well_names_df = pd.DataFrame({'WELL':well_names})

def base_well_name(row):
    
    well_name = row['WELL']
    
    return well_name.split()[0]


well_names_df['WELL_HEAD'] = well_names_df.apply(lambda row: base_well_name(row), axis=1)

locations_df = well_names_df.merge(well_locations_df, how='inner', on='WELL_HEAD')
locations_df = locations_df.merge(well_meta_df, how='left', on='WELL')

fig = px.scatter_mapbox(locations_df, lat="lat", lon="lon",
                        color='WELL', 
                        zoom=5, height=600,
                        )
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":200,"t":20,"l":200,"b":0})
fig.show()


# Marker

import matplotlib.pyplot as plt
import lasio

sumur_b = lasio.read('/content/drive/MyDrive/ta/las sumur/17_11-1.las', ignore_header_errors=True).df()
sumur_g = lasio.read('/content/drive/MyDrive/ta/las sumur/17_4-1.las', ignore_header_errors=True).df()

sumur_b_GR = sumur_b[['DEPTH_MD', 'GR']]
sumur_g_GR = sumur_g[['DEPTH_MD', 'GR']]

formasi = pd.read_excel('NPD_Lithostratigraphy_member_formations_all_wells.xlsx')
		.drop(['Surface', 'X', 'Y', 'Z', 'MD', 'Interpreter', 'Unnamed: 8'], axis=1)

marker_b = formasi[formasi['Well identifier']=='17/11-1'].drop(['Well identifier'], axis=1)
marker_g = formasi[formasi['Well identifier']=='17/4-1'].drop(['Well identifier'], axis=1)


plt.figure(figsize=(8,20))

plt.subplot(121)
plt.title('17/11-1')
plt.plot('GR', 'DEPTH_MD', data=sumur_b)
for i in marker_b.values:
    plt.hlines(i[1], 0, 1,'red',linestyles='dashed', alpha=0.5)
    plt.text(0, i[1],i[0])
plt.ylim(800,4000)
plt.gca().invert_yaxis()

plt.subplot(122)
plt.title('17/4-1')
plt.plot('GR', 'DEPTH_MD', data=sumur_g)
for i in marker_g.values:
    plt.hlines(i[1], 0, 1,'red',linestyles='dashed', alpha=0.5)
    plt.text(0, i[1],i[0])
plt.ylim(800,4000)
plt.gca().invert_yaxis()

plt.show()
plt.tight_layout()


# Korelasi

from correlation import Korelasi

depth_b = sumur_b['DEPTH_MD'].values
GR_b = sumur_b['GR'].values
Res_b = sumur_b['RDEP'].values
depth_g = sumur_g['DEPTH_MD'].values
GR_g = sumur_g['GR'].values
Res_g = sumur_g['RDEP'].values

df_marker_b = pd.read_csv('marker_b.csv').drop(['Unnamed: 0'], axis=1)
df_marker_g = pd.read_csv('marker_g.csv').drop(['Unnamed: 0'], axis=1)
df_mark_bg = pd.merge(df_marker_b, df_marker_g, how='inner', on=['HorizonName']).rename(columns={'ZABS_x': 'ZABS_b', 'ZABS_y': 'ZABS_g'})

MarkerName = df_marker_bg['HorizonName'].values
Marker_b = df_marker_bg['ZABS_b'].values
Marker_g = df_marker_bg['ZABS_g'].values

mindepth = 800
maxdepth = 3500
majortick = 50
minortick = 10
korelasi = Korelasi(30, 20,'Well Correlation', majortick, minortick)
korelasi.mainwell('well 17/11-1', mindepth, maxdepth, depth_b, GR_b, Res_b, MarkerName, Marker_b)
korelasi.secondwell('well 17/4-1', mindepth, maxdepth, depth_g, GR_g, Res_g, MarkerName, Marker_g)
korelasi.show_2wells_correlation(MarkerName, Marker_b, Marker_g)












































