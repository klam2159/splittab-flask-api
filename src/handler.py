import runpod

# If your handler runs inference on a model, load the model here.
# You will want models to be loaded into memory before starting serverless.
import torch
from transformers import DonutProcessor, VisionEncoderDecoderModel
from inference import load_and_preprocess_image, generate_text_from_image


# the model parameters are stored in model/
processor = DonutProcessor.from_pretrained("model") #model
model = VisionEncoderDecoderModel.from_pretrained("model") #model
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
model.to(device)

def handler(job):
    """ Handler function that will be used to process jobs. """
    job_input = job['input']


    image_base64 = job_input.get('image_base64', '')
    pixel_values = load_and_preprocess_image(image_base64, processor)
    generated_text = generate_text_from_image(pixel_values, model, processor, device)
    return generated_text

runpod.serverless.start({"handler": handler})