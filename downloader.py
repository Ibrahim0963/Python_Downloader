import urllib.request
from tqdm import tqdm
import getopt
import sys
import os


def usage():
    print("""
    downloader.py [options]
    #######################
    -u / --url               URL Data to download
    -o / --output            Destination to sava / [default] your current path
    -h / --help              for help
    
    examples:
    python3 downloader.py -u https://www.eccouncil.org/wp-content/uploads/2020/09/CEHv11-Brochure.pdf 
    python3 downloader.py --url https://www.eccouncil.org/wp-content/uploads/2020/09/CEHv11-Brochure.pdf
    python3 downloader.py -u Your_URL --output C:/Users/habibi/Destop/    
    """)

url = ""
dest = ""
openfile = ""
opt_s, arg_s = getopt.getopt(sys.argv[1:], "hu:o", ["--help", "--url", "--output"])
print(opt_s)
print(arg_s)
for o, a in opt_s:
    if o in ("-h", "--help"):
        print(usage())
    elif o in ("-u", "--url"):
        url = a
    elif o in ("-o", "--output"):
        dest = a
    else:
        raise ValueError("Unhandle Error !!!")


if str(url) != None:
    filename = url.split("/")[-1]

    if os.name == "nt":
        openfile = open(dest + "\\" + filename, "wb")
    elif os.name == "posix":
        openfile = open(dest + "/" + filename, "wb")
else:
    print("Your have to enter at least a url to download")

openurl = urllib.request.urlopen(url)
print(openurl.info())
block_size = 1024
file_size = int(openurl.header["Content-Length"])
for i in tqdm(range(file_size)):
    buffer = openurl.read(block_size)
    i += block_size
    openfile.write(buffer)
openfile.close()
