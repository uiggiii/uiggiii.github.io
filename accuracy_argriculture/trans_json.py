import json
import os

save_path = r"C:\Users\Lenovo\Desktop\data.json"

# 分度单位转换
def convert_coord(raw_val):
    val = float(raw_val)
    deg = int(val / 100)
    minute = val - (deg * 100)
    dec_val = deg + (minute / 60)
    return round(dec_val, 7)

def main():
    
    dir_name = os.path.dirname(os.path.abspath(save_path))
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        
    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
    else:
        data_dict = {}
        
    print("启动录入程序。在名称提示处输入“退出”即可结束并保存。")
    
    while True:
        pt_name = input("请输入测点名称 (例如：跑道1): ")
        if pt_name == '退出':
            break
            
        lat_input = input("请输入纬度 (例如：3018.48385): ")
        lon_input = input("请输入经度 (例如：12004.67241): ")
        
        try:
            lat_val = convert_coord(lat_input)
            lon_val = convert_coord(lon_input)
            
            data_dict[pt_name] = {
                "latitude": lat_val,
                "longitude": lon_val
            }
            print(f"[{pt_name}] 记录成功 -> 纬度: {lat_val}, 经度: {lon_val}\n")
            
        except ValueError:
            print("输入格式有误，请确保输入的是纯数字。\n")
            
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=4)
        
    print(f"数据已成功保存至绝对路径: {save_path}")

if __name__ == "__main__":
    main()