import easyocr

reader = easyocr.Reader(['en'])

# The output is a list in format [([[176, 4], [348, 4], [348, 28], [176, 28]], 'Supported devices', 0.9999310169899559)]
# which means [[x1,y1],[x2,y2],[x3,y3],[x4,y4]], text, confidence
result = reader.readtext('devices_weekly_23122407.png')

# for better readability:
for row in result:
    print(row)
