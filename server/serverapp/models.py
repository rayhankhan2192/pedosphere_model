# from django.db import models
# import pickle
# import json
# import numpy as np
# import os

# __model = None
# __data_columns = None

# def get_predicted_plant_type(soil_temp, soil_ph):
#     if soil_temp < 0 or soil_temp > 50:
#         return 'Invalid soil temperature value'
#     if soil_ph < 0 or soil_ph > 14:
#         return 'Invalid soil pH value'

#     # Prepare the input for the model
#     x = np.array([soil_temp, soil_ph]).reshape(1, -1)
#     return __model.predict(x)[0]  # Fixed to predict properly

# def load_saved_artifacts():
#     global __data_columns, __model
#     print("Loading saved artifacts... start")

#     # Get the full paths to the artifact files
#     base_dir = os.path.dirname(os.path.realpath(__file__))
#     columns_path = os.path.join(base_dir, 'artifacts', 'columns.json')
#     model_path = os.path.join(base_dir, 'artifacts', 'pedosphere_model.pickle')

#     with open(columns_path, 'r') as f:
#         __data_columns = json.load(f)['data_columns']

#     if __model is None:
#         with open(model_path, 'rb') as f:
#             __model = pickle.load(f)
    
#     print("Loading saved artifacts... done")

# def get_data_columns():
#     return __data_columns



# import pickle
# import json
# import numpy as np
# import os

# __model = None
# __data_columns = None

# def get_predicted_plant_type(soil_temp, soil_ph):
#     if soil_temp < 0 or soil_temp > 50:
#         return 'Invalid soil temperature value'
#     if soil_ph < 0 or soil_ph > 14:
#         return 'Invalid soil pH value'

#     # Prepare the input for the model
#     x = np.array([soil_temp, soil_ph]).reshape(1, -1)
#     return __model.predict(x)[0]  # Return prediction

# def load_saved_artifacts():
#     print("Loading saved artifacts... start")
#     global __data_columns
#     global __model

#     # Get the directory where the artifacts are located
#     artifacts_path = os.path.join(os.path.dirname(__file__), 'artifacts')

#     # Load columns.json
#     with open(os.path.join(artifacts_path, 'columns.json'), 'r') as f:
#         __data_columns = json.load(f)['data_columns']

#     # Load atmosphere_model.pickle
#     if __model is None:
#         with open(os.path.join(artifacts_path, 'pedosphere_model.pickle'), 'rb') as f:
#             __model = pickle.load(f)

#     print("Loading saved artifacts... done")

# def get_data_columns():
#     return __data_columns


import pickle
import json
import numpy as np
import os

__model = None
__data_columns = None

def get_predicted_plant_type(soil_temp, soil_ph):
    # Validate inputs
    if not isinstance(soil_temp, (int, float)) or not isinstance(soil_ph, (int, float)):
        return 'Invalid input type. Expected numerical values for soil temperature and pH.'
    
    if soil_temp < 0 or soil_temp > 50:
        return 'Invalid soil temperature value. It should be between 0 and 50.'
    
    if soil_ph < 0 or soil_ph > 14:
        return 'Invalid soil pH value. It should be between 0 and 14.'

    # Prepare the input for the model
    x = np.array([soil_temp, soil_ph]).reshape(1, -1)
    
    # Return prediction
    return __model.predict(x)[0]

def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns
    global __model

    # Get the directory where the artifacts are located
    artifacts_path = os.path.join(os.path.dirname(__file__), 'artifacts')

    try:
        # Load columns.json
        with open(os.path.join(artifacts_path, 'columns.json'), 'r') as f:
            __data_columns = json.load(f).get('data_columns', [])

        # Load the model
        if __model is None:
            with open(os.path.join(artifacts_path, 'pedosphere_model.pickle'), 'rb') as f:
                __model = pickle.load(f)

        print("Loading saved artifacts... done")
    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the artifacts are in the correct directory.")
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from columns.json.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_data_columns():
    return __data_columns
