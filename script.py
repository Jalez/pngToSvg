import cv2
import numpy as np
import svgwrite

def png_to_svg(input_path, output_path):
    # Read image
    img = cv2.imread(input_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply threshold to get binary image
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create SVG drawing
    dwg = svgwrite.Drawing(output_path, size=(img.shape[1], img.shape[0]))
    
    # Add contours to SVG
    for contour in contours:
        # Convert contour to path string
        path_data = "M"
        for point in contour:
            x, y = point[0]
            path_data += f" {x},{y}"
        path_data += "Z"
        
        # Add path to drawing
        path = dwg.path(d=path_data, fill='black')
        dwg.add(path)
    
    # Save SVG
    dwg.save()

if __name__ == "__main__":
    input_path = './image.png'
    output_path = './output.svg'
    png_to_svg(input_path, output_path)

