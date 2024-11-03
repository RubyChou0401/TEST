from PIL import Image

def resize_image_half(input_path, output_path):
    # 開啟圖片
    with Image.open(input_path) as img:
        # 計算新的大小，寬度和高度各縮小一半
        new_size = (img.width // 2, img.height // 2)
        
        # 調整圖片大小
        resized_img = img.resize(new_size, Image.ANTIALIAS)
        
        # 儲存調整後的圖片
        resized_img.save(output_path)
        print(f"圖片已儲存為 {output_path}，新尺寸：{resized_img.size}")

# 使用範例
input_path = "input_image.jpg"  # 原始圖片路徑
output_path = "output_image_half.jpg"  # 儲存縮小後的圖片路徑
resize_image_half(input_path, output_path)
