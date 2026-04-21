import json
import math

a = 6378137.0
f = 1 / 298.257223563
b = a * (1 - f)
e2 = (a**2 - b**2) / a**2

# 转换空间直角坐标
def wgs84_to_ecef(lat, lon, h=0):
    phi = math.radians(lat)
    lam = math.radians(lon)
    n = a / math.sqrt(1 - e2 * math.sin(phi)**2)
    x = (n + h) * math.cos(phi) * math.cos(lam)
    y = (n + h) * math.cos(phi) * math.sin(lam)
    z = (n * (1 - e2) + h) * math.sin(phi)
    return x, y, z

# 转换平面坐标
def ecef_to_enu(x, y, z, lat0, lon0, x0, y0, z0):
    phi = math.radians(lat0)
    lam = math.radians(lon0)
    dx = x - x0
    dy = y - y0
    dz = z - z0
    east = -math.sin(lam) * dx + math.cos(lam) * dy
    north = -math.sin(phi) * math.cos(lam) * dx - math.sin(phi) * math.sin(lam) * dy + math.cos(phi) * dz
    return east, north

# 计算距离
def get_dist(p1, p2):
    lat1 = p1["latitude"]
    lon1 = p1["longitude"]
    lat2 = p2["latitude"]
    lon2 = p2["longitude"]
    x1, y1, z1 = wgs84_to_ecef(lat1, lon1)
    x2, y2, z2 = wgs84_to_ecef(lat2, lon2)
    east, north = ecef_to_enu(x2, y2, z2, lat1, lon1, x1, y1, z1)
    return math.sqrt(east**2 + north**2)

def run():
    with open("data.json", "r", encoding="utf-8") as file_obj:
        data_dict = json.load(file_obj)
        
    pairs = []
    for key in data_dict.keys():
        if key.endswith("1"):
            pair_key = key[:-1] + "2"
            if pair_key in data_dict:
                pairs.append((key, pair_key))
                
    for k1, k2 in pairs:
        dist = get_dist(data_dict[k1], data_dict[k2])
        print(f"{k1} 与 {k2} 之间的距离为: {dist:.3f} 米")

if __name__ == "__main__":
    run()