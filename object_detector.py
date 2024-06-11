import torch
import numpy as np
import models
from PIL import Image
from torchvision.transforms import functional as F
from torchvision import transforms
from models import Darknet
import yaml

def load_model(model_path, config_path):
    with open(config_path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    model = Darknet(data['model']['cfg'])
    model.load_state_dict(torch.load(model_path, map_location='cpu')['model'])
    return model, data['names']

def preprocess_image(image):
    image = F.to_tensor(image)
    image, _ = F.resize(image, (416, 416))
    return image.unsqueeze(0)

def detect_objects(image_path, model, names):
    image = Image.open(image_path).convert('RGB')
    image_tensor = preprocess_image(image)
    with torch.no_grad():
        output = model(image_tensor)
    # Process output here
    return output


