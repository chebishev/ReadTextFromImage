# import easyocr
from ocr_result import devices_list

# reader = easyocr.Reader(['en'])
# result_weekly = reader.readtext('devices_weekly_23122407.png')
# result_stable = reader.readtext('devices_stable_v14_23111222.png')

devices = devices_list[6:]
weekly_devices = {
    "code_name": "",
    "market_name": "",
    "rom_name": "",
    "rom_options": "",
    "slug": ""
}
# for index in range(0, len(devices), 5):
#     data_index = 1
#     print(devices[index][data_index], devices[index+1][data_index], devices[index+2][data_index])
last_codename = ""
last_rom_name = ""
stop_words = ("Global", "China", "Hybrid", "Delayed")
