def get_stream_type(type: str) -> str:
    if type == '00':
        return 'DATA'
    if type == '01':
        return 'HEADERS'
    if type == '02':
        return 'PRIORITY'
    if type == '03':
        return 'RST_STREAM'
    if type == '04':
        return 'SETTINGS'
    if type == '05':
        return 'PUSH_PROMISE'
    if type == '06':
        return 'PING'
    if type == '07':
        return 'GOAWAY'
    if type == '08':
        return 'WINDOW_UPDATE'
    if type == '09':
        return 'CONTINUATION'
    return ''


def get_settings_identifier(identifier: int) -> str:
    if identifier == 1:
        return 'SETTINGS_HEADER_TABLE_SIZE'
    if identifier == 2:
        return 'SETTINGS_ENABLE_PUSH'
    if identifier == 3:
        return 'SETTINGS_MAX_CONCURRENT_STREAMS'
    if identifier == 4:
        return 'SETTINGS_INITIAL_WINDOW_SIZE'
    if identifier == 5:
        return 'SETTINGS_MAX_FRAME_SIZE'
    if identifier == 6:
        return 'SETTINGS_MAX_HEADER_LIST_SIZE'
    return ''


f = open('./header.txt', 'r', encoding='utf-8')
http2 = ''
str_list = []
while True:
    http2 = f.readline()
    if not http2:
        break
    http2 = http2[http2.rfind('   '):len(http2)]
    str_list += http2.strip().split(' ')
# 首先读取前9个byte 读取length type flags r streamIdentifier
print(str_list)
cnt = len(str_list)
length = int(str_list[0] + str_list[1] + str_list[2], 16)
stream_type = get_stream_type(str_list[3])
flags = str_list[4]
settings_map = dict()
if stream_type == 'SETTINGS':
    # todo 处理settings帧
    start = 9
    for i in range(start, cnt, 6):
        identifier = get_settings_identifier(int(str_list[i] + str_list[i + 1], 16))
        settings_map[identifier] = int(str_list[i + 2] + str_list[i + 3] + str_list[i + 4] + str_list[i + 5], 16)
    print(settings_map)
    pass
elif stream_type == 'HEADERS':
    # todo 处理headers帧
    is_padding = int(flags, 16) & (1 << 3)
    end_headers = int(flags, 16) & (1 << 2)
    print(is_padding)
    print(end_headers)
    pass
