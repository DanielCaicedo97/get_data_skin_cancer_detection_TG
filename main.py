import cv2
from segmentation.main import Segmentation
from pre_procesing.main import PreProcessing
from extract_features.texture_features import TextureFeatures


if __name__ == "__main__":

    #PreProcesssing
    img_path = 'data_example/raw/ISIC_1435135.JPG'  # Ruta de tu imagen
    img = cv2.imread(img_path)
    preprocessor = PreProcessing(img_path)
    processed_img = preprocessor.pipeline_preprocessing()

    # Mostrar la imagen procesada
    cv2.imshow('Imagen sin Procesar', img)
    cv2.imshow('Imagen Procesada', processed_img)

    #Segmentation
    
    segmentator = Segmentation(processed_img)

    # Segmentación usando método de Otsu
    otsu_segmented_img = segmentator.method_otsu()

    # Segmentación usando K-Means
    kmeans_segmented_img = segmentator.k_means_segmentation()

    # Mostrar las imágenes segmentadas
    cv2.imshow('Otsu Segmentation', otsu_segmented_img)
    cv2.imshow('K-Means Segmentation', kmeans_segmented_img)


    texture_features = TextureFeatures(kmeans_segmented_img).get_texture_features()

    print(texture_features)

    cv2.waitKey(0)
    cv2.destroyAllWindows()