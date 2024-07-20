import os
from transformers import DonutProcessor, VisionEncoderDecoderModel
from dotenv import load_dotenv

load_dotenv()

# Define the model name
model_name = 'AdamCodd/donut-receipts-extract'

# Download and save the model and processor
model = VisionEncoderDecoderModel.from_pretrained(model_name)
processor = DonutProcessor.from_pretrained(model_name)

# Define the local directory to save the model and processor
local_model_dir = os.getenv('LOCAL_MODEL_DIR')

# Save the model and processor locally
model.save_pretrained(local_model_dir)
processor.save_pretrained(local_model_dir)
