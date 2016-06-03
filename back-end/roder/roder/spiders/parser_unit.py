'''
Test module to make sure that spider output is getting parsed correctly
'''
import re
k =['Technology', '2G bands', '3G Network', '4G Network', 'Speed', 'GPRS', 'EDGE', 'Announced', 'Status', 'Dimensions', 'Weight', 'SIM', 'Type', 'Size', 'Resolution', 'Multitouch', 'Protection', 'OS', 'Chipset', 'CPU', 'GPU', 'Card slot', 'Internal', 'Primary', 'Features', 'Video', 'Secondary', 'Alert types', 'Loudspeaker', '3.5mm jack', 'WLAN', 'Bluetooth', 'GPS', 'Infrared port', 'Radio', 'USB', 'Sensors', 'Messaging', 'Browser', 'Java', 'Stand-by', 'Talk time', 'Colors']
r1 = [['\r\n', 'Network', '\r\n', 'Technology', '\r\n', 'GSM / HSPA / LTE', '\r\n', '  \r\n', '  \r\n'], ['\r\n', '2G bands', '\r\n', 'GSM 850 / 900 / 1800 / 1900 ', '\r\n', '  \r\n', '  \r\n\r\n'], ['\r\n', u'\xa0', '\r\n', 'GSM 850 / 1900 - XT1644 (USA)', '\r\n', '  \r\n', '  \r\n'], ['\r\n', '3G Network', '\r\n', 'HSDPA 850 / 900 / 1700(AWS) / 1900 / 2100 - XT1644, XT1644 (USA), XT1644 (India)', '\r\n', '\r\n', '\r\n'], ['\r\n', '4G Network', '\r\n', 'LTE band 1(2100), 3(1800), 7(2600), 8(900), 20(800) - XT1644', '\r\n', '\r\n', '\r\n'], ['\r\n', u'\xa0', '\r\n', 'LTE band 1(2100), 2(1900), 3(1800), 4(1700/2100), 5(850), 7(2600), 8(900), 12(700), 13(700), 25(1900), 26(850), 41(2500) - XT1644 (USA)', '\r\n', '\r\n', '\r\n'], ['\r\n', u'\xa0', '\r\n', 'LTE band 1(2100), 3(1800), 5(850), 8(900), 40(2300) - XT1644 (India)', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Speed', '\r\n', 'HSPA 42.2/5.76 Mbps, LTE Cat4 150/50 Mbps', '\r\n', '\r\n', '\r\n'], ['\r\n', 'GPRS', '\r\n', 'Yes', '\r\n', '\r\n', '\r\n'], ['\r\n', 'EDGE', '\r\n', 'Yes', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Launch', '\r\n', 'Announced', '\r\n', '2016, May', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Status', '\r\n', 'Available. Released 2016, May', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Body', '\r\n', 'Dimensions', '\r\n', '153 x 76.6 x 9.8 mm (6.02 x 3.02 x 0.39 in)', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Weight', '\r\n', '155 g (5.47 oz)', '\r\n', '\r\n', '\r\n'], ['\r\n', 'SIM', '\r\n', 'Micro-SIM', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Display', '\r\n', 'Type', '\r\n', 'IPS LCD capacitive touchscreen, 16M colors', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Size', '\r\n', '5.5 inches (~71.2% screen-to-body ratio)', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Resolution', '\r\n', '1080 x 1920 pixels (~401 ppi pixel density)', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Multitouch', ' ', '\r\n', 'Yes', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Protection', ' ', '\r\n', 'Corning Gorilla Glass 3', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Platform', '\r\n', 'OS', '\r\n', 'Android OS, v6.0.1 (Marshmallow)', '\r\n', '\r\n', '\r\n'], ['Chipset', '\r\n', 'Qualcomm MSM8952 Snapdragon 617', '\r\n', '\r\n', '\r\n'], ['CPU', '\r\n', 'Quad-core 1.5 GHz Cortex-A53 & quad-core 1.2 GHz Cortex-A53', '\r\n', '\r\n', '\r\n'], ['GPU', '\r\n', 'Adreno 405', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Memory', '\r\n', 'Card slot', '\r\n', 'microSD, up to 128 GB (dedicated slot)', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Internal', '\r\n', '16 GB, 2 GB RAM or 32 GB, 3 GB RAM or 64 GB, 4 GB RAM', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Camera', '\r\n', 'Primary', '\r\n', '16 MP, f/2.0, phase detection & laser autofocus, dual-LED (dual tone) flash', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Features', '\r\n', 'Geo-tagging, touch focus, face detection, panorama, auto-HDR', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Video', '\r\n', '1080p@30fps, HDR', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Secondary', '\r\n', '5 MP, f/2.2, auto-HDR', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Sound', '\r\n', 'Alert types', '\r\n', 'Vibration; MP3, WAV ringtones', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Loudspeaker', ' ', '\r\n', 'Yes', '\r\n', '\r\n', '\r\n'], ['\r\n', '3.5mm jack', ' ', '\r\n', 'Yes', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Comms', '\r\n\r\n', 'WLAN', '\r\n', 'Wi-Fi 802.11 a/b/g/n, Wi-Fi Direct, hotspot', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Bluetooth', '\r\n', 'v4.1, A2DP, LE', '\r\n', '\r\n', '\r\n'], ['\r\n', 'GPS', '\r\n', 'Yes, with A-GPS, GLONASS, BDS', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Infrared port', '\r\n', 'No', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Radio', '\r\n', 'FM radio', '\r\n', '\r\n', '\r\n'], ['\r\n', 'USB', '\r\n', 'microUSB v2.0, USB Host', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Features', '\r\n\r\n', 'Sensors', '\r\n', 'Fingerprint, accelerometer, gyro, proximity', '\r\n', '\r\n', '\r\n'], ['\r\n\t\r\n', 'Messaging', '\r\n', 'SMS(threaded view), MMS, Email, Push Email, IM', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Browser', '\r\n', 'HTML5', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Java', '\r\n', 'No', '\r\n', '\r\n', '\r\n'], [u'\xa0', '- Fast battery charging', '\r\n- Active noise cancellation with dedicated mic', '\r\n- MP3/AAC+/WAV/Flac player', '\r\n- MP4/H.264 player', '\r\n- Photo/video editor', '\r\n- Document viewer', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Battery', '\r\n', u'\xa0', '\r\n', 'Non-removable Li-Ion 3000 mAh battery', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Stand-by', '\r\n', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Talk time', '\r\n', '\r\n', '\r\n', '\r\n'], ['\r\n', 'Misc', '\r\n'], ['\r\n', 'Colors', '\r\n', 'Black, White', '\r\n', '\r\n', '\r\n']]
# KEY ===>  ['Technology', '2G bands', '3G bands', '4G bands', 'Speed', 'GPRS', 'EDGE', 'Announced', 'Status', 'Dimensions', 'Weight', 'Build', 'SIM', 'Type', 'Size', 'Resolution', 'Multitouch', 'Protection', 'OS', 'Chipset', 'CPU', 'GPU', 'Card slot', 'Internal', 'Primary', 'Features', 'Video', 'Secondary', 'Alert types', 'Loudspeaker', '3.5mm jack', 'WLAN', 'Bluetooth', 'GPS', 'NFC', 'Infrared port', 'Radio', 'USB', 'Sensors', 'Messaging', 'Browser', 'Java', 'Colors', 'Price group', 'Performance', 'Display', 'Camera', 'Loudspeaker', 'Audio quality', 'Battery life']
r2 =[['\r\n', 'Network', '\r\n', 'Technology', '\r\n', 'GSM / CDMA / HSPA / EVDO / LTE', '\r\n'], ['\r\n', '2G bands', '\r\n', 'GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2', '\r\n'], ['\r\n', u'\xa0', '\r\n', 'CDMA 800 / 1900 ', '\r\n'], ['\r\n', '3G bands', '\r\n', 'HSDPA 850 / 900 / 1900 / 2100 ', '\r\n'], ['\r\n', u'\xa0', '\r\n', 'CDMA2000 1xEV-DO ', '\r\n'], ['\r\n', u'\xa0', '\r\n', ' TD-SCDMA', '\r\n'], ['\r\n', '4G bands', '\r\n', 'LTE band 1(2100), 3(1800), 7(2600), 38(2600), 39(1900), 40(2300), 41(2500)', '\r\n'], ['\r\n', 'Speed', '\r\n', 'HSPA 42.2/5.76 Mbps, LTE Cat12 600/150 Mbps', '\r\n'], ['\r\n', 'GPRS', '\r\n', 'Yes', '\r\n'], ['\r\n', 'EDGE', '\r\n', 'Yes', '\r\n'], ['\r\n', 'Launch', '\r\n', 'Announced', '\r\n', '2016, February', '\r\n'], ['\r\n', 'Status', '\r\n', 'Available. Released 2016, April', '\r\n'], ['\r\n', 'Body', '\r\n', 'Dimensions', '\r\n', '144.6 x 69.2 x 7.3 mm (5.69 x 2.72 x 0.29 in)', '\r\n'], ['\r\n', 'Weight', '\r\n', '129 g / 139 g (4.90 oz)', '\r\n'], ['\r\n', 'Build', '\r\n', 'Corning Gorilla Glass 4 back panel', '\r\n'], ['\r\n', 'SIM', '\r\n', 'Dual SIM (Nano-SIM, dual stand-by)', '\r\n'], ['\r\n', 'Display', '\r\n', 'Type', '\r\n', 'IPS LCD capacitive touchscreen, 16M colors', '\r\n'], ['\r\n', 'Size', '\r\n', '5.15 inches (~73.1% screen-to-body ratio)', '\r\n'], ['\r\n', 'Resolution', '\r\n', '1080 x 1920 pixels (~428 ppi pixel density)', '\r\n'], ['\r\n', 'Multitouch', '\r\n', 'Yes', '\r\n'], ['\r\n', 'Protection', '\r\n', 'Corning Gorilla Glass 4', '\r\n'], [u'\xa0', '- MIUI 7.0'], ['\r\n', 'Platform', '\r\n', 'OS', '\r\n', 'Android OS, v6.0 (Marshmallow)', '\r\n'], ['Chipset', '\r\n', 'Qualcomm MSM8996 Snapdragon 820', '\r\n'], ['CPU', '\r\n', 'Dual-core 1.8 GHz Kryo & dual-core 1.36 GHz Kryo - Standard edition', 'Dual-core 2.15 GHz Kryo & dual-core 1.6 GHz Kryo - other editions', '\r\n'], ['GPU', '\r\n', 'Adreno 530', '\r\n'], ['\r\n', 'Memory', '\r\n', 'Card slot', '\r\n\r\n\r\n', 'No'], ['\r\n', 'Internal', '\r\n', '128 GB, 4 GB RAM - Pro edition', '32/64 GB, 3 GB RAM - other editions', '\r\n'], ['\r\n', 'Camera', '\r\n', 'Primary', '\r\n', '16 MP, f/2.0, phase detection autofocus, OIS (4-axis), dual-LED (dual tone) flash, ', 'check quality', '\r\n'], ['\r\n', 'Features', '\r\n', u'1/2.8" sensor size, 1.12 \xb5m pixel size, geo-tagging, touch focus, face/smile detection, panorama, HDR', '\r\n'], ['\r\n', 'Video', '\r\n', '2160p@30fps, 1080p@30fps, 720p@120fps, ', 'check quality', '\r\n'], ['\r\n', 'Secondary', '\r\n', u'4 MP, f/2.0, 1/3" sensor size, 2\xb5m pixel size, 1080p@30fps', '\r\n'], ['\r\n', 'Sound', '\r\n', 'Alert types', '\r\n', 'Vibration; MP3, WAV ringtones', '\r\n\t'], ['\r\n', 'Loudspeaker', ' ', '\r\n', 'Yes', '\r\n'], ['\r\n', '3.5mm jack', ' ', '\r\n', 'Yes', '\r\n'], ['\r\n', 'Comms', '\r\n', 'WLAN', '\r\n', 'Wi-Fi 802.11 a/b/g/n/ac, dual-band, Wi-Fi Direct, DLNA, hotspot', '\r\n'], ['\r\n', 'Bluetooth', '\r\n', 'v4.2, A2DP, LE', '\r\n'], ['\r\n', 'GPS', '\r\n', 'Yes, with A-GPS, GLONASS, BDS', '\r\n'], ['\r\n', 'NFC', '\r\n', 'Yes', '\r\n'], ['\r\n', 'Infrared port', '\r\n', 'Yes', '\r\n'], ['\r\n', 'Radio', '\r\n', 'No', '\r\n'], ['\r\n', 'USB', '\r\n', 'Type-C 1.0 reversible connector', '\r\n'], ['\r\n', 'Features', '\r\n', 'Sensors', '\r\n', 'Fingerprint, accelerometer, gyro, proximity, compass, barometer', '\r\n'], ['\r\n', 'Messaging', '\r\n', 'SMS(threaded view), MMS, Email, Push Mail, IM', '\r\n'], ['\r\n', 'Browser', '\r\n', 'HTML5', '\r\n'], ['\r\n', 'Java', '\r\n', 'No', '\r\n'], [u'\xa0', '- Fast battery charging: 83% in 30 min (Quick Charge 3.0)', '\r\n- Active noise cancellation with dedicated mic', '\r\n- MP4/DivX/XviD/WMV/H.265 player', '\r\n- MP3/WAV/eAAC+/FLAC player', '\r\n- Photo/video editor', '\r\n- Document viewer'], ['\r\n', 'Battery', '\r\n', u'\xa0', '\r\n', 'Non-removable Li-Po 3000 mAh battery', '\r\n'], ['\r\n', 'Misc', '\r\n', 'Colors', '\r\n', 'Black, White, Gold, Ceramic', '\r\n'], ['\r\n', 'Price group', '\r\n', '7/10', ' ', '(About 380 EUR)', '\r\n'], ['\r\n', 'Tests', '\r\n', 'Performance', '\r\n', '\r\n', 'Basemark OS II: 2444 / Basemark OS II 2.0: 2180', 'Basemark X: 33110', '\r\n'], ['\r\n\r\n', 'Display', '\r\n', '\r\n', 'Contrast ratio: 1227:1 (nominal), 3.240 (sunlight)', '\r\n'], ['\r\n\r\n', 'Camera', '\r\n', '\r\n', 'Photo', ' / ', 'Video', '\r\n'], ['\r\n\r\n', 'Loudspeaker', '\r\n', '\r\n', 'Voice 67dB / Noise 67dB / Ring 74dB', '\r\n\r\n', '\r\n'], ['\r\n\r\n', 'Audio quality', '\r\n', '\r\n', 'Noise -95.3dB / Crosstalk -95.4dB', '\r\n'], ['\r\n\r\n\r\n', 'Battery life', '\r\n', '\r\n', '\r\n', 'Endurance rating 92h', '\r\n', '\r\n', '\r\n'], ['\r\n\r\n']]
r3 =[['\r\n', 'Network', '\r\n', 'Technology', '\r\n', 'GSM / HSPA / LTE', '\r\n'], ['\r\n', '2G bands', '\r\n', 'GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM model only)', '\r\n'], ['\r\n', '3G bands', '\r\n', ' HSDPA', '\r\n'], ['\r\n', '4G bands', '\r\n', ' LTE', '\r\n'], ['\r\n', 'Speed', '\r\n', 'HSPA, LTE', '\r\n'], ['\r\n', 'GPRS', '\r\n', 'Yes', '\r\n'], ['\r\n', 'EDGE', '\r\n', 'Yes', '\r\n'], ['\r\n', 'Launch', '\r\n', 'Announced', '\r\n', '2016, April', '\r\n'], ['\r\n', 'Status', '\r\n', 'Coming soon. Exp. release 2016, June', '\r\n'], ['\r\n', 'Body', '\r\n', 'Dimensions', '\r\n', '-', '\r\n'], ['\r\n', 'Weight', '\r\n', '-', '\r\n'], ['\r\n', 'SIM', '\r\n', 'Single SIM (Micro-SIM) or Dual SIM (Micro-SIM, dual stand-by)', '\r\n'], ['\r\n', 'Display', '\r\n', 'Type', '\r\n', 'IPS LCD capacitive touchscreen, 16M colors', '\r\n'], ['\r\n', 'Size', '\r\n', '5.5 inches', '\r\n'], ['\r\n', 'Resolution', '\r\n', '720 x 1280 pixels (~267 ppi pixel density)', '\r\n'], ['\r\n', 'Multitouch', '\r\n', 'Yes', '\r\n'], ['\r\n', 'Platform', '\r\n', 'OS', '\r\n', 'Android OS, v6.0 (Marshmallow)', '\r\n'], ['Chipset', '\r\n', 'Mediatek MT6735', '\r\n'], ['CPU', '\r\n', 'Quad-core 1.3 GHz Cortex-A53', '\r\n'], ['GPU', '\r\n', 'Mali-T720MP2', '\r\n'], ['\r\n', 'Memory', '\r\n', 'Card slot', '\r\n\r\n\r\n', 'microSD (dedicated slot)'], ['\r\n', 'Internal', '\r\n', '16 GB, 2 GB RAM', '\r\n'], ['\r\n', 'Camera', '\r\n', 'Primary', '\r\n', '13 MP, phase detection/laser autofocus, LED flash', '\r\n'], ['\r\n', 'Features', '\r\n', 'Geo-tagging, touch focus, face detection, HDR, panorama', '\r\n'], ['\r\n', 'Video', '\r\n', '1080p@30fps', '\r\n'], ['\r\n', 'Secondary', '\r\n', '5 MP', '\r\n'], ['\r\n', 'Sound', '\r\n', 'Alert types', '\r\n', 'Vibration; MP3, WAV ringtones', '\r\n\t'], ['\r\n', 'Loudspeaker', ' ', '\r\n', 'Yes', '\r\n'], ['\r\n', '3.5mm jack', ' ', '\r\n', 'Yes', '\r\n'], [u'\xa0', '- DTS HD sound'], ['\r\n', 'Comms', '\r\n', 'WLAN', '\r\n', 'Yes', '\r\n'], ['\r\n', 'Bluetooth', '\r\n', 'Yes', '\r\n'], ['\r\n', 'GPS', '\r\n', 'Yes, with A-GPS', '\r\n'], ['\r\n', 'Radio', '\r\n', 'To be confirmed', '\r\n'], ['\r\n', 'USB', '\r\n', 'microUSB v2.0', '\r\n'], ['\r\n', 'Features', '\r\n', 'Sensors', '\r\n', 'Accelerometer, proximity, compass', '\r\n'], ['\r\n', 'Messaging', '\r\n', 'SMS(threaded view), MMS, Email, Push Mail, IM', '\r\n'], ['\r\n', 'Browser', '\r\n', 'HTML5', '\r\n'], ['\r\n', 'Java', '\r\n', 'No', '\r\n'], [u'\xa0', '- Fast battery charging', '\r\n- Active noise cancellation with dedicated mic', '\r\n- MP3/WAV/AAC/Flac player', '\r\n- MP4/H.264 player', '\r\n- Photo/video editor', '\r\n- Document viewer'], ['\r\n', 'Battery', '\r\n', u'\xa0', '\r\n', 'Non-removable Li-Ion 5000 mAh battery', '\r\n'], ['\r\n', 'Misc', '\r\n', 'Colors', '\r\n', 'Blue, White', '\r\n'], ['\r\n', 'Price group', '\r\n', '6/10', ' ', '(About 270 EUR)', '\r\n']]

p = re.compile(ur'\s*\r\n|\r|\n')
storage_and_ram_regex = re.compile(ur'\s(\d{1,3})\sgb,\s(\d{1})\sgb')
camera_regex = re.compile(ur'\d+\smp')
battery_regex = re.compile(ur'\d+\smah')


def parse_feature(body):
    specs = ['batter', 'camera', 'ram', 'storage']
    mobile_data = {}
    for i in range(len(body)):
        clear_val = map(lambda x: re.sub(p, "", x), body[i])
        # clear_val = map((lambda x: x.replace('\r\n', "")), r[i])
        clear_val = [j.lower() for j in clear_val if j is not ""]
        clear_val = " ".join(clear_val)
        clear_val = " ".join(clear_val.split())
        if any(x in clear_val for x in specs):
            print clear_val
            print ""
            if 'battery' in clear_val:
                # print clear_val
                search = re.search(battery_regex, clear_val)
                if search:
                    # print "battery => ",search.group(0)
                    mobile_data['battery'] = search.group(0)

            if 'camera' in clear_val:
                # UPDATE HERE WITH BATTERY LOGIC
                # print clear_val
                search = re.search(camera_regex, clear_val)
                if search:
                    mobile_data['camera'] = search.group(0)
                # print "camera => ",re.search(camera_regex,clear_val).group(0)

            if 'ram' in clear_val:
                print clear_val
                search = re.findall(storage_and_ram_regex, clear_val)
                if search:
                    temp_ram = []
                    temp_storeage = []
                    for i in search:
                        temp_ram.append(i[1])
                        temp_storeage.append(i[0])
                    mobile_data['ram'] = temp_ram
                    mobile_data['storage'] = temp_storeage
    return mobile_data


def split_product(mobile_data):
    mobile_list = []
    if len(mobile_data.get('ram', 0)) and len(mobile_data['storage']):
        for m in range(len(mobile_data['ram'])):
            temp_mobile_data = {}
            temp_mobile_data = mobile_data.copy()
            temp_mobile_data['ram'] = mobile_data['ram'][m]
            temp_mobile_data['storage'] = mobile_data['storage'][m]
            mobile_list.append(temp_mobile_data)
        print mobile_list

mdata = parse_feature(r3)
print mdata
split_product(mdata)
