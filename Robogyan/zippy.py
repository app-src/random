from zippyshare_downloader import extract_info, extract_info_coro

# by default, parameter download is True
file = extract_info('https://www.zippyshare.com/v/2PtTbchb/file.html', download=True)

print(file)

# Output: <Zippyshare File name="..." size="...">

# async version
async def get_info():
    file = await extract_info_coro('https://www.zippyshare.com/v/2PtTbchb/file.html', download=True)
    print(file)