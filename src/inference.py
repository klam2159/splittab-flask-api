import torch
import re
import base64

from PIL import Image
from io import BytesIO

def load_and_preprocess_image(image_base64: str, processor):
    image_data = base64.b64decode(image_base64)
    image = Image.open(BytesIO(image_data)).convert("RGB")
    pixel_values = processor(image, return_tensors="pt").pixel_values
    return pixel_values

def generate_text_from_image(pixel_values, model, processor, device):
    """
    Generate text from an image using the trained model.
    """
    # Load and preprocess the image
    pixel_values = pixel_values.to(device)

    # Generate output using model
    model.eval()
    with torch.no_grad():
        task_prompt = "<s_receipt>" # <s_cord-v2> for v1
        decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt").input_ids
        decoder_input_ids = decoder_input_ids.to(device)
        generated_outputs = model.generate(
            pixel_values,
            decoder_input_ids=decoder_input_ids,
            max_length=model.decoder.config.max_position_embeddings, 
            pad_token_id=processor.tokenizer.pad_token_id,
            eos_token_id=processor.tokenizer.eos_token_id,
            early_stopping=True,
            bad_words_ids=[[processor.tokenizer.unk_token_id]],
            return_dict_in_generate=True
        )

    # Decode generated output
    decoded_text = processor.batch_decode(generated_outputs.sequences)[0]
    decoded_text = decoded_text.replace(processor.tokenizer.eos_token, "").replace(processor.tokenizer.pad_token, "")
    decoded_text = re.sub(r"<.*?>", "", decoded_text, count=1).strip()  # remove first task start token
    decoded_text = processor.token2json(decoded_text)
    return decoded_text
