import sys
import torch
import transformers
import platform
import subprocess

def get_cuda_version():
    try:
        output = subprocess.check_output(['nvcc', '--version']).decode('utf-8')
        cuda_version = output.split("release ")[-1].split(",")[0]
        return cuda_version
    except:
        return "Not found"

def get_environment_info():
    info = {
        "OS": f"{platform.system()} {platform.release()}",
        "Python": platform.python_version(),
        "Transformers": transformers.__version__,
        "PyTorch": torch.__version__,
        "CUDA": get_cuda_version(),
        "GPU": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "Not available",
        "CPU": platform.processor()
    }
    return info

def get_model_config(model):
    return model.config

# Print environment info
env_info = get_environment_info()
print("运行环境 | Environment:")
for key, value in env_info.items():
    print(f"* **{key}**: {value}")

# Print model config
print("\nModel Configuration:")
print("```python")
print(get_model_config(model))
print("```")

# Print any other relevant information
print("\nAdditional Information:")
print("* **Image Size**: ", image.size)
print("* **CUDA_VISIBLE_DEVICES**: ", os.environ.get('CUDA_VISIBLE_DEVICES', 'Not set'))

print("\nError Message:")
print("```")
# Print the full error message and stack trace here
print("```")
