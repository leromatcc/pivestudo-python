from typing import Any, Dict, List, Literal, Optional, Union, cast

from PIL import Image
from numpy import asarray

from landingai.postprocess import crop
from landingai.predict import Predictor
from landingai.predict import OcrPredictor
from landingai import visualize

from . import verificaRegex

# used for debug
import os
cwd = os.getcwd()
print(f"identificador.py path: {cwd}")

#path which stores the images to be analised
images_path_base = f"/home/userpivestudo-python/app/resources"
images_path_to_frames = f"{images_path_base}/frames"

#dev images
images_which_one = f"video_frame_8.jpg"
images_to_analyse = f"{images_path_to_frames}/{images_which_one}"


print(f"identificador.py images_path_base: {images_path_base}")
print(f"identificador.py images_path_to_frames: {images_path_to_frames}")
print(f"identificador.py images_which_one: {images_which_one}")
print(f"identificador.py images_to_analyse: {images_to_analyse}")


def detectImage(images_which_one):
    cwd = os.getcwd()
    print(f"detectImage path: ${cwd}")

    pathToImage = f"{images_path_to_frames}/{images_which_one}"

    image = Image.open(pathToImage)

    data = asarray(image)
    frameX = Image.fromarray(data)
    frames = [frameX]


    bounding_boxes = []
    overlayed_frames = []

    api_key = "landingai_sk_detection-token-key"
    model_endpoint = "e001c156-5de0-43f3-9991-f19699b31202"
    predictor = Predictor(model_endpoint, api_key=api_key)

    for frame in frames:
        prediction = predictor.predict(frame)
        # store predictions in a list
        overlay = visualize.overlay_predictions(prediction, frame)
        bounding_boxes.append(prediction)
        overlayed_frames.append(overlay)
    
    return frames, bounding_boxes, overlayed_frames


def recortar(frames, bounding_boxes):
# cropping the license plate
    cropped_imgs = []
    for frame, bboxes in zip(frames, bounding_boxes):
        cropped_imgs.append(crop(bboxes, frame))

    return cropped_imgs




def identificaLandingAi(cropped_imgs) -> List[OcrPredictor]:
    # NOTE: The API key below has a rate limit. Use an API key from your own LandingLens account for production use.
    API_KEY = "landingai_sk_OCR-token-key"
    ocr_predictor = OcrPredictor(api_key=API_KEY)

    ocr_preds = []
    overlayed_ocr = []
    print(cropped_imgs[0])
    for frame in cropped_imgs:
        for plate in frame:
            ocr_pred = ocr_predictor.predict(plate)
            ocr_preds.append(ocr_pred)
            overlay = visualize.overlay_predictions(ocr_pred, plate)
            overlayed_ocr.append(overlay)

    print(ocr_preds)

    print(f"identificaLandingAi path: ${cwd}")

    # ocr_preds = []
    for frame, ocr_pred in zip(overlayed_ocr, ocr_preds):
        if len(ocr_pred) == 0:
            continue

        nomeArquivo="arquivo1"
        nomeArquivoCompleto=f"{images_path_base}/prediction/{nomeArquivo}.jpg"
        print(f"identificaLandingAi nomeArquivoCompleto: ${nomeArquivoCompleto}")

        frame.save( nomeArquivoCompleto )
        
    return ocr_preds


def separaPlacas(predictsList: List[OcrPredictor]):

    texts = []
    for predicts in predictsList:
        for predict in predicts:
            if( float(predict.score) > 0.9):
                if(verificaRegex.contemPlacaBr(predict.text) or verificaRegex.contemPlacaUSA(predict.text)):
                    texts.append(predict)

    return texts


def todosPassos():
    frames, bounding_boxes, overlayed_frames = detectImage(images_which_one="video_frame_8.jpg")
    cropped_imgs = recortar( frames=frames, bounding_boxes=bounding_boxes)
    predicts = identificaLandingAi(cropped_imgs)

    print("predicts: " + str(predicts))
    
    textosUsa = separaPlacas(predicts)

    return textosUsa 
