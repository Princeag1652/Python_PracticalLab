import os
import numpy as np
from PIL import Image

def load_image(image_path):
    """Loads a JPEG/PNG image and converts it into a raw NumPy RGB pixel grid."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at: {image_path}")
    
    img = Image.open(image_path).convert("RGB")
    print(f"[INFO] Successfully loaded image: '{image_path}' (Dimensions: {img.size[0]}x{img.size[1]} pixels)")
    return np.array(img, dtype=np.float32)

def save_image(pixel_array, output_path):
    """Clips and saves a NumPy pixel array back into an image file."""
    clipped_array = np.clip(pixel_array, 0, 255).astype(np.uint8)
    img = Image.fromarray(clipped_array)
    img.save(output_path)
    print(f"[INFO] Processed image saved successfully -> '{output_path}'")

def convert_to_grayscale(pixel_array):
    """Converts the RGB pixel grid to grayscale using standard human perception luminance weights."""
    print("[PROCESSING] Applying Grayscale Conversion (Channel Transformation)...")
    r = pixel_array[:, :, 0]
    g = pixel_array[:, :, 1]
    b = pixel_array[:, :, 2]
    
    # Standard luminosity formula: 0.2989*R + 0.5870*G + 0.1140*B
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    
    # Stack back into 3 channels for standard image saving
    return np.stack([gray, gray, gray], axis=-1)

def apply_thresholding(pixel_array, threshold_value=127):
    """Generates a high-contrast Black and White image using pixel thresholding."""
    print(f"[PROCESSING] Applying Image Thresholding (Threshold = {threshold_value})...")
    r = pixel_array[:, :, 0]
    g = pixel_array[:, :, 1]
    b = pixel_array[:, :, 2]
    
    # Convert to grayscale first
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    
    # Apply binary thresholding (White if > threshold, else Black)
    binary = np.where(gray > threshold_value, 255.0, 0.0)
    return np.stack([binary, binary, binary], axis=-1)

def apply_spatial_blur(pixel_array):
    """Applies a custom 3x3 spatial box blur filter directly across raw pixel neighborhoods."""
    print("[PROCESSING] Applying Spatial Box Blur Filter (Neighborhood Grid Smoothing)...")
    h, w, c = pixel_array.shape
    
    # Pad borders to handle edge pixels safely
    padded = np.pad(pixel_array, ((1, 1), (1, 1), (0, 0)), mode='edge')
    blurred = np.zeros_like(pixel_array)
    
    # Iterate through each pixel's 3x3 neighborhood
    for i in range(h):
        for j in range(w):
            neighborhood = padded[i:i+3, j:j+3, :]
            blurred[i, j, :] = np.mean(neighborhood, axis=(0, 1))
            
    return blurred

if __name__ == "__main__":
    # Target image file (placed in the same folder or use full path)
    input_image_name = "sample.jpg"
    
    # Automatically generate a dummy sample image if none exists, for testing convenience
    if not os.path.exists(input_image_name):
        print(f"[SETUP] '{input_image_name}' not found. Creating a temporary test image...")
        dummy_img = Image.new("RGB", (300, 300), color=(60, 120, 180))
        dummy_img.save(input_image_name)

    try:
        print("--- DIGITAL IMAGE FILTER & COLOR CONVERTER UTILITY ---")
        
        # 1. Load raw pixel grid
        raw_pixels = load_image(input_image_name)
        
        # 2. Execute Grayscale Transformation
        gray_pixels = convert_to_grayscale(raw_pixels)
        save_image(gray_pixels, "output_grayscale.jpg")
        
        # 3. Execute Thresholding (Black & White)
        thresh_pixels = apply_thresholding(raw_pixels, threshold_value=120)
        save_image(thresh_pixels, "output_threshold.jpg")
        
        # 4. Execute Spatial Blur Filter
        blur_pixels = apply_spatial_blur(raw_pixels)
        save_image(blur_pixels, "output_blur.jpg")
        
        print("\n[SUCCESS] All image filters and color conversions applied successfully!")
        
    except Exception as error:
        print(f"[ERROR] An error occurred during processing: {error}")