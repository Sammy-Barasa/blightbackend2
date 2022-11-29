from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def index(request):
    prediction_classes = ["blight infected 5-7","blight infected day 1-3","blight infected day 3-5","blight infected day 7 onwards","healthy leaves"]
    if request.method == "GET":
        print(request.data)
        

        # assume data contains your decoded image
        return Response({"Messege":"PredictionAPIEndpoint GET"})
    
    
    import base64
    import tensorflow as tf
    import numpy as np
    
    # print(request.body)
    decoded_data=base64.b64decode((request.body))
    #write the decoded data back to original format in  file
    # DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
    img_name = f"../request_mages/image{3}.jpeg"
    img_file = open(img_name, 'wb')
    img_file.write(decoded_data)
    img_file.close()
    
    
    loaded_model = tf.keras.models.load_model("../saved_models/tomato_blight_model_version_1.h5")
    #  target_size = (674,450,3)
    img = tf.keras.preprocessing.image.load_img(img_name, target_size = (450,674,3))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    res = loaded_model.predict(images)
    
    print(res)
    pred_class = list(res[0]).index(max(list(res[0])))
    print(pred_class)
    perc_val = list(res[0])[pred_class]

    return Response({"data":{"class":prediction_classes[pred_class],"percent":perc_val}})