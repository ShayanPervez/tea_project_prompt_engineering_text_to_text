import subprocess
import sys

def generate_requirements_txt(output_file):
    try:
        output = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
        with open(output_file, "w") as f:
            f.write(output.decode("utf-8"))
        print(f"Successfully generated {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    output_file = "requirements.txt"
    generate_requirements_txt(output_file)
