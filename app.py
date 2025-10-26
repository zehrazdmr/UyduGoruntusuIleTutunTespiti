import ee
ee.Initialize(project='ee-fatmazehraozdemir21')

# Sentinel-2 veri kümesi
region = ee.Geometry.Point([38.23,38.03])

collection = ee.ImageCollection('COPERNICUS/S2') \
    .filterDate('2022-05-10', '2022-09-20') \
    .filterBounds(region) \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))

    # Özellik hesaplama fonksiyonu
def calculate_features(image):
    ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')  # NDVI
    ndwi = image.normalizedDifference(['B8', 'B11']).rename('NDWI')  # NDWI
    chlorophyll = image.select('B5').divide(image.select('B4')).rename('Chlorophyll')  # Klorofil yoğunluğu
    nir_absorption = image.select('B8').rename('NIR_Absorption')  # NIR absorpsiyonu
    return image.addBands([ndvi, ndwi, chlorophyll, nir_absorption])

# Koleksiyona özellikleri ekleme
features_collection = collection.map(calculate_features)
median_image = features_collection.median()

# Eğitim verisi (tütün alanları)
training_data = ee.FeatureCollection([
    ee.Feature(ee.Geometry.Point([38.2172, 38.0259]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2170, 38.0255]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2164, 38.0253]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2162, 38.0249]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2160, 38.0246]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2158, 38.0244]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2152, 38.0238]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2147, 38.0236]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2149, 38.0235]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2151, 38.0235]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2144, 38.0218]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2149, 38.0214]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2147, 38.0216]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2143, 38.0216]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2145, 38.0214]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2142, 38.0214]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2143, 38.0213]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2145, 38.0212]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2146, 38.0211]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2147, 38.0210]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2168, 37.9918]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2164, 37.9914]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2172, 38.0133]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2167, 37.9918]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2297, 37.9944]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.2191, 37.9935]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.1999, 38.0257]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.211657, 38.012259]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.200800, 37.997392]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.211346, 38.011978]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.198407, 38.022514]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.198362, 38.022741]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.198015, 38.022412]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.197901, 38.022757]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.197544, 38.022190]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.197458, 38.022638]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.196132, 38.024069]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.196592, 38.023870]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.199097, 38.025751]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.198647, 38.026560]), {'label': 1}),
    ee.Feature(ee.Geometry.Point([38.199610, 38.025487]), {'label': 1}),

    ee.Feature(ee.Geometry.Point([38.2344, 37.9997]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2358, 38.0012]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2360, 38.0012]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2362, 38.0013]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2364, 38.0014]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2390, 37.9961]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.1920, 38.0473]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2247, 38.0091]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2263, 38.0091]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2454, 38.0497]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2453, 38.0491]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2444, 38.0488]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2441, 38.0487]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2438, 38.0486]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2435, 38.0485]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2514, 38.0336]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2488, 38.0349]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2582, 38.0346]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2477, 38.0514]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2477, 38.0507]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2481, 38.0513]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2464, 38.0503]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2487, 38.0502]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2457, 38.0493]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2299, 37.9942]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2275, 37.9936]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2280, 37.9936]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2208, 37.9992]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2615, 37.9841]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2635, 37.9836]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2329, 38.0532]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2500, 38.0610]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.3000, 38.0727]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.3021, 38.1199]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2991, 38.1211]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2713, 38.4886]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2698, 38.4886]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2737, 38.4877]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2727, 38.4861]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2711, 38.4861]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2693, 38.4858]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2695, 38.4851]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2723, 38.4844]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2739, 38.4845]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2731, 38.4810]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2722, 38.4806]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2735, 38.4803]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2729, 38.4800]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2715, 38.4802]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2737, 38.4775]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2744, 38.4775]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2741, 38.4787]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.2736, 38.4775]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.273523, 38.475267]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.274443, 38.475295]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.273595, 38.474631]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.276187, 38.475726]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.276340, 38.475267]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.275345, 38.474897]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.274924, 38.474567]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.274388, 38.474268]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.273599, 38.473770]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.272968, 38.473742]), {'label': 0}),
    ee.Feature(ee.Geometry.Point([38.272580, 38.474024]), {'label': 0}),
])
# Eğitim verisi için özellikleri örnekleme
training_samples = median_image.sampleRegions(
    collection=training_data,
    properties=['label'],
    scale=10
)

# Random Forest sınıflandırıcıyı eğitme
classifier = ee.Classifier.smileRandomForest(200).train(
    features=training_samples,
    classProperty='label',
    inputProperties=['NDVI', 'NDWI', 'Chlorophyll', 'NIR_Absorption']
)

def test(lat,lng):
    test_point= ee.Geometry.Point([lng, lat])
   # Convert ee.Geometry to Feature
    feature = ee.Feature(test_point)
    # Sample the classified image using the feature
    result = classified_image.sample(test_point, scale=10).first().get('classification').getInfo()
    if (result==1):
        print("Bu alan tütün alanıdır.")
    elif(result==0):
        print("Bu alan tütün alanı değildir.")
    else:
        print("Bu alana dair bilgi bulunmadı.")
     

 