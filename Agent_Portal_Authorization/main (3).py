# import pandas as pd
# import geopandas as gpd
# import folium
# import numpy as np
# from branca.colormap import linear
#
# # Создаем данные о доходах от агентов  для каждого региона
# np.random.seed(0)
# income_data = pd.DataFrame({
#     'Region': ['Abruzzo', 'Basilicata', 'Calabria', 'Campania', 'Emilia-Romagna',
#                'Friuli-Venezia Giulia', 'Lazio', 'Liguria', 'Lombardia', 'Marche',
#                'Molise', 'Piemonte', 'Puglia', 'Sardegna', 'Sicilia', 'Toscana',
#                'Trentino-Alto Adige/Südtirol', 'Umbria', "Valle d'Aosta/Vallée d'Aoste", 'Veneto'],
#     'Agent': ['Ricci Girolamo', 'Carmela Alaia', 'Rosa Tropea', 'Carmela Alaia', 'Marinelli Davide',
#                'Massimo Zambon', 'Giovanni Pontone', 'Valter', 'Alberto Davi', 'Andrea Biaggi',
#                'Ricci Girolamo', 'Valter', 'Vito Trillo', 'Stefano Cuccu', 'Rosa Tropea', 'Andrea Biaggi',
#                'Sandor Jaro', 'Andrea Biaggi', "Valter", 'Massimo Zambon'],
#     'Income': np.random.randint(10000, 50000, 20),
# })
#
# # Геоданные геометрии регионов
# italy_geo = gpd.read_file('https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson')
#
# # Объединяем данные о доходах и геометрию каждого региона
# italy_geo = italy_geo.merge(income_data, left_on='reg_name', right_on='Region')
#
# # Создаем объект карты через Folium
# m = folium.Map(location=[42, 12], zoom_start=5)
#
# # Создаем цветовую карту поверх обычной
# colormap = linear.YlOrRd_09.scale(
#     italy_geo['Income'].min(),
#     italy_geo['Income'].max())
#
# # Геоданные в виде геообъектов и  стиль отображения
# folium.GeoJson(
#     italy_geo,
#     name='Income',
#     tooltip=folium.features.GeoJsonTooltip(fields=['reg_name', 'Agent', 'Income'],
#                                             aliases=['Region:', 'Agent:', 'Income:'],
#                                             labels=True,
#                                             sticky=False,
#                                             style='font-size: 12px;'),
#     style_function=lambda x: {
#         'fillColor': colormap(x['properties']['Income']),
#         'color': 'black',
#         'weight': 1,
#         'fillOpacity': 0.7 if x['properties']['Income'] is not None else 0
#     },
#     highlight_function=lambda x: {'weight': 3, 'color': 'black'},
# ).add_to(m)
#
# # Легенда к карте
# colormap.add_to(m)
# folium.LayerControl().add_to(m)
#
# # Сохраняем карту в HTML
# m.save('map.html')
#
# str = '123456789'
# print(str[-4:])