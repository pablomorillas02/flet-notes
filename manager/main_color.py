file = "./storage/ui_settings.txt"

def get_color(file):
    with open(file) as f:
        line = f.readline()

    return line

# Color principal de la aplicación
color = get_color(file)