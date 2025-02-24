
base_url = "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/tpci"

def get_image_url(set, number):
    url = f"{base_url}/{set}/{set}_{number}_R_EN.png"
    return url



