import torch

# Comprobar que PyTorch se instaló correctamente
print("PyTorch version:", torch.__version__)

# Verificar si CUDA está disponible
print("CUDA available:", torch.cuda.is_available())

# Si CUDA está disponible, obtener el nombre de la GPU
if torch.cuda.is_available():
    print("CUDA device name:", torch.cuda.get_device_name(0))
    print("CUDA version:", torch.version.cuda)
