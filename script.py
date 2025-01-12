from PIL import Image
import subprocess
import sys
import os

def png_to_svg(input_path, output_path):
    try:
        # Convert PNG to PBM first
        temp_pbm = 'temp_output.pbm'
        with Image.open(input_path) as img:
            # Convert to grayscale and then to binary
            img = img.convert('L')
            # Convert to binary using threshold
            img = img.point(lambda x: 0 if x < 128 else 255, '1')
            img.save(temp_pbm)

        try:
            # Convert PBM to SVG using potrace
            result = subprocess.run([
                'potrace',
                '-s',  # SVG output
                '-o', output_path,
                '--tight',  # Remove whitespace
                temp_pbm
            ], check=True, capture_output=True, text=True)
            
            if result.stderr:
                print("Warning from potrace:", result.stderr)
                
        finally:
            # Clean up temporary file
            if os.path.exists(temp_pbm):
                os.remove(temp_pbm)
            
    except subprocess.CalledProcessError as e:
        print("Error running potrace:", e)
        print("Command output:", e.output)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: potrace command not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_path = './image.png'
    output_path = './output.svg'
    png_to_svg(input_path, output_path)

