import os,glob
import gnupg
import binascii
import magic
from time import sleep
from getpass import getpass
from colorama import Fore
from colorama import Style
gpg = gnupg.GPG(gnupghome='/home/'+os.getlogin()+'/.gnupg')
gpg.encoding = 'utf-8'
appPath = os.getcwd()

clean = lambda: os.system('tput reset')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ext:
    data = {
    "123": {
        "signs": [
            "0,00001A00051004"
        ],
        "mime": "application/vnd.lotus-1-2-3"
    },
    "cpl": {
        "signs": [
            "0,4D5A",
            "0,DCDC"
        ],
        "mime": "application/cpl+xml"
    },
    "epub": {
        "signs": [
            "0,504B03040A000200"
        ],
        "mime": "application/epub+zip"
    },
    "ttf": {
        "signs": [
            "0,0001000000"
        ],
        "mime": "application/font-sfnt"
    },
    "gz": {
        "signs": [
            "0,1F8B08"
        ],
        "mime": "application/gzip"
    },
    "tgz": {
        "signs": [
            "0,1F8B08"
        ],
        "mime": "application/gzip"
    },
    "hqx": {
        "signs": [
            "0,28546869732066696C65206D75737420626520636F6E76657274656420776974682042696E48657820"
        ],
        "mime": "application/mac-binhex40"
    },
    "doc": {
        "signs": [
            "0,0D444F43",
            "0,CF11E0A1B11AE100",
            "0,D0CF11E0A1B11AE1",
            "0,DBA52D00",
            "512,ECA5C100"
        ],
        "mime": "application/msword"
    },
    "mxf": {
        "signs": [
            "0,060E2B34020501010D0102010102",
            "0,3C435472616E7354696D656C696E653E"
        ],
        "mime": "application/mxf"
    },
    "lha": {
        "signs": [
            "2,2D6C68"
        ],
        "mime": "application/octet-stream"
    },
    "lzh": {
        "signs": [
            "2,2D6C68"
        ],
        "mime": "application/octet-stream"
    },
    "exe": {
        "signs": [
            "0,4D5A"
        ],
        "mime": "application/octet-stream"
    },
    "class": {
        "signs": [
            "0,CAFEBABE"
        ],
        "mime": "application/octet-stream"
    },
    "dll": {
        "signs": [
            "0,4D5A"
        ],
        "mime": "application/octet-stream"
    },
    "img": {
        "signs": [
            "0,000100005374616E64617264204A6574204442",
            "0,504943540008",
            "0,514649FB",
            "0,53434D49",
            "0,7E742C015070024D52010000000800000001000031000000310000004301FF0001000800010000007e742c01",
            "0,EB3C902A"
        ],
        "mime": "application/octet-stream"
    },
    "iso": {
        "signs": [
            "32769,4344303031",
            "34817,4344303031",
            "36865,4344303031"
        ],
        "mime": "application/octet-stream"
    },
    "ogx": {
        "signs": [
            "0,4F67675300020000000000000000"
        ],
        "mime": "application/ogg"
    },
    "oxps": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/oxps"
    },
    "pdf": {
        "signs": [
            "0,25504446"
        ],
        "mime": "application/pdf"
    },
    "p10": {
        "signs": [
            "0,64000000"
        ],
        "mime": "application/pkcs10"
    },
    "pls": {
        "signs": [
            "0,5B706C61796C6973745D"
        ],
        "mime": "application/pls+xml"
    },
    "eps": {
        "signs": [
            "0,252150532D41646F62652D332E3020455053462D332030",
            "0,C5D0D3C6"
        ],
        "mime": "application/postscript"
    },
    "ai": {
        "signs": [
            "0,25504446"
        ],
        "mime": "application/postscript"
    },
    "rtf": {
        "signs": [
            "0,7B5C72746631"
        ],
        "mime": "application/rtf"
    },
    "tsa": {
        "signs": [
            "0,47"
        ],
        "mime": "application/tamp-sequence-adjust"
    },
    "msf": {
        "signs": [
            "0,2F2F203C212D2D203C6D64623A6D6F726B3A7A"
        ],
        "mime": "application/vnd.epson.msf"
    },
    "fdf": {
        "signs": [
            "0,25504446"
        ],
        "mime": "application/vnd.fdf"
    },
    "fm": {
        "signs": [
            "0,3C4D616B657246696C6520"
        ],
        "mime": "application/vnd.framemaker"
    },
    "kmz": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/vnd.google-earth.kmz"
    },
    "tpl": {
        "signs": [
            "0,0020AF30",
            "0,6D7346696C7465724C697374"
        ],
        "mime": "application/vnd.groove-tool-template"
    },
    "kwd": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/vnd.kde.kword"
    },
    "wk4": {
        "signs": [
            "0,00001A000210040000000000"
        ],
        "mime": "application/vnd.lotus-1-2-3"
    },
    "wk3": {
        "signs": [
            "0,00001A000010040000000000"
        ],
        "mime": "application/vnd.lotus-1-2-3"
    },
    "wk1": {
        "signs": [
            "0,0000020006040600080000000000"
        ],
        "mime": "application/vnd.lotus-1-2-3"
    },
    "apr": {
        "signs": [
            "0,D0CF11E0A1B11AE1"
        ],
        "mime": "application/vnd.lotus-approach"
    },
    "nsf": {
        "signs": [
            "0,1A0000040000",
            "0,4E45534D1A01"
        ],
        "mime": "application/vnd.lotus-notes"
    },
    "ntf": {
        "signs": [
            "0,1A0000",
            "0,30314F52444E414E43452053555256455920202020202020",
            "0,4E49544630"
        ],
        "mime": "application/vnd.lotus-notes"
    },
    "org": {
        "signs": [
            "0,414F4C564D313030"
        ],
        "mime": "application/vnd.lotus-organizer"
    },
    "lwp": {
        "signs": [
            "0,576F726450726F"
        ],
        "mime": "application/vnd.lotus-wordpro"
    },
    "sam": {
        "signs": [
            "0,5B50686F6E655D"
        ],
        "mime": "application/vnd.lotus-wordpro"
    },
    "mif": {
        "signs": [
            "0,3C4D616B657246696C6520",
            "0,56657273696F6E20"
        ],
        "mime": "application/vnd.mif"
    },
    "xul": {
        "signs": [
            "0,3C3F786D6C2076657273696F6E3D22312E30223F3E"
        ],
        "mime": "application/vnd.mozilla.xul+xml"
    },
    "asf": {
        "signs": [
            "0,3026B2758E66CF11A6D900AA0062CE6C"
        ],
        "mime": "application/vnd.ms-asf"
    },
    "cab": {
        "signs": [
            "0,49536328",
            "0,4D534346"
        ],
        "mime": "application/vnd.ms-cab-compressed"
    },
    "xls": {
        "signs": [
            "512,0908100000060500",
            "0,D0CF11E0A1B11AE1",
            "512,FDFFFFFF04",
            "512,FDFFFFFF20000000"
        ],
        "mime": "application/vnd.ms-excel"
    },
    "xla": {
        "signs": [
            "0,D0CF11E0A1B11AE1"
        ],
        "mime": "application/vnd.ms-excel"
    },
    "chm": {
        "signs": [
            "0,49545346"
        ],
        "mime": "application/vnd.ms-htmlhelp"
    },
    "ppt": {
        "signs": [
            "512,006E1EF0",
            "512,0F00E803",
            "512,A0461DF0",
            "0,D0CF11E0A1B11AE1",
            "512,FDFFFFFF04"
        ],
        "mime": "application/vnd.ms-powerpoint"
    },
    "pps": {
        "signs": [
            "0,D0CF11E0A1B11AE1"
        ],
        "mime": "application/vnd.ms-powerpoint"
    },
    "wks": {
        "signs": [
            "0,0E574B53",
            "0,FF000200040405540200"
        ],
        "mime": "application/vnd.ms-works"
    },
    "wpl": {
        "signs": [
            "84,4D6963726F736F66742057696E646F7773204D6564696120506C61796572202D2D20"
        ],
        "mime": "application/vnd.ms-wpl"
    },
    "xps": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/vnd.ms-xpsdocument"
    },
    "cif": {
        "signs": [
            "2,5B56657273696F6E"
        ],
        "mime": "application/vnd.multiad.creator.cif"
    },
    "odp": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/vnd.oasis.opendocument.presentation"
    },
    "odt": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/vnd.oasis.opendocument.text"
    },
    "ott": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/vnd.oasis.opendocument.text-template"
    },
    "pptx": {
        "signs": [
            "0,504B030414000600"
        ],
        "mime": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    },
    "xlsx": {
        "signs": [
            "0,504B030414000600"
        ],
        "mime": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    },
    "docx": {
        "signs": [
            "0,504B030414000600"
        ],
        "mime": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    },
    "prc": {
        "signs": [
            "0,424F4F4B4D4F4249",
            "60,74424D504B6E5772"
        ],
        "mime": "application/vnd.palm"
    },
    "pdb": {
        "signs": [
            "11,000000000000000000000000000000000000000000000000",
            "0,4D2D5720506F636B6574204469637469",
            "0,4D6963726F736F667420432F432B2B20",
            "0,736D5F",
            "0,737A657A",
            "0,ACED0005737200126267626C69747A2E"
        ],
        "mime": "application/vnd.palm"
    },
    "qxd": {
        "signs": [
            "0,00004D4D585052"
        ],
        "mime": "application/vnd.Quark.QuarkXPress"
    },
    "rar": {
        "signs": [
            "0,526172211A0700",
            "0,526172211A070100"
        ],
        "mime": "application/vnd.rar"
    },
    "mmf": {
        "signs": [
            "0,4D4D4D440000"
        ],
        "mime": "application/vnd.smaf"
    },
    "cap": {
        "signs": [
            "0,52545353",
            "0,58435000"
        ],
        "mime": "application/vnd.tcpdump.pcap"
    },
    "dmp": {
        "signs": [
            "0,4D444D5093A7",
            "0,5041474544553634",
            "0,5041474544554D50"
        ],
        "mime": "application/vnd.tcpdump.pcap"
    },
    "wpd": {
        "signs": [
            "0,FF575043"
        ],
        "mime": "application/vnd.wordperfect"
    },
    "xar": {
        "signs": [
            "0,78617221"
        ],
        "mime": "application/vnd.xara"
    },
    "spf": {
        "signs": [
            "0,5350464900"
        ],
        "mime": "application/vnd.yamaha.smaf-phrase"
    },
    "dtd": {
        "signs": [
            "0,0764743264647464"
        ],
        "mime": "application/xml-dtd"
    },
    "zip": {
        "signs": [
            "0,504B0304",
            "0,504B0304",
            "0,504B030414000100630000000000",
            "0,504B0708",
            "30,504B4C495445",
            "526,504B537058",
            "29152,57696E5A6970"
        ],
        "mime": "application/zip"
    },
    "amr": {
        "signs": [
            "0,2321414D52"
        ],
        "mime": "audio/AMR"
    },
    "au": {
        "signs": [
            "0,2E736E64",
            "0,646E732E"
        ],
        "mime": "audio/basic"
    },
    "m4a": {
        "signs": [
            "0,00000020667479704D344120",
            "4,667479704D344120"
        ],
        "mime": "audio/mp4"
    },
    "mp3": {
        "signs": [
            "0,494433",
            "0,FFFB"
        ],
        "mime": "audio/mpeg"
    },
    "oga": {
        "signs": [
            "0,4F67675300020000000000000000"
        ],
        "mime": "audio/ogg"
    },
    "ogg": {
        "signs": [
            "0,4F67675300020000000000000000"
        ],
        "mime": "audio/ogg"
    },
    "qcp": {
        "signs": [
            "0,52494646"
        ],
        "mime": "audio/qcelp"
    },
    "koz": {
        "signs": [
            "0,49443303000000"
        ],
        "mime": "audio/vnd.audikoz"
    },
    "bmp": {
        "signs": [
            "0,424D"
        ],
        "mime": "image/bmp"
    },
    "dib": {
        "signs": [
            "0,424D"
        ],
        "mime": "image/bmp"
    },
    "emf": {
        "signs": [
            "0,01000000"
        ],
        "mime": "image/emf"
    },
    "fits": {
        "signs": [
            "0,53494D504C4520203D202020202020202020202020202020202020202054"
        ],
        "mime": "image/fits"
    },
    "gif": {
        "signs": [
            "0,474946383961"
        ],
        "mime": "image/gif"
    },
    "jp2": {
        "signs": [
            "0,0000000C6A5020200D0A"
        ],
        "mime": "image/jp2"
    },
    "jpg": {
        "signs": [
            "0,FFD8",
            "0,FFD8",
            "0,FFD8",
            "0,FFD8"
        ],
        "mime": "image/jpeg"
    },
    "jpeg": {
        "signs": [
            "0,FFD8",
            "0,FFD8"
        ],
        "mime": "image/jpeg"
    },
    "jpe": {
        "signs": [
            "0,FFD8",
            "0,FFD8"
        ],
        "mime": "image/jpeg"
    },
    "jfif": {
        "signs": [
            "0,FFD8"
        ],
        "mime": "image/jpeg"
    },
    "png": {
        "signs": [
            "0,89504E470D0A1A0A"
        ],
        "mime": "image/png"
    },
    "tiff": {
        "signs": [
            "0,492049",
            "0,49492A00",
            "0,4D4D002A",
            "0,4D4D002B"
        ],
        "mime": "image/tiff"
    },
    "tif": {
        "signs": [
            "0,492049",
            "0,49492A00",
            "0,4D4D002A",
            "0,4D4D002B"
        ],
        "mime": "image/tiff"
    },
    "psd": {
        "signs": [
            "0,38425053"
        ],
        "mime": "image/vnd.adobe.photoshop"
    },
    "dwg": {
        "signs": [
            "0,41433130"
        ],
        "mime": "image/vnd.dwg"
    },
    "ico": {
        "signs": [
            "0,00000100"
        ],
        "mime": "image/vnd.microsoft.icon"
    },
    "mdi": {
        "signs": [
            "0,4550"
        ],
        "mime": "image/vnd.ms-modi"
    },
    "hdr": {
        "signs": [
            "0,233F52414449414E43450A",
            "0,49536328"
        ],
        "mime": "image/vnd.radiance"
    },
    "pcx": {
        "signs": [
            "512,0908100000060500"
        ],
        "mime": "image/vnd.zbrush.pcx"
    },
    "wmf": {
        "signs": [
            "0,010009000003",
            "0,D7CDC69A"
        ],
        "mime": "image/wmf"
    },
    "eml": {
        "signs": [
            "0,46726F6D3A20",
            "0,52657475726E2D506174683A20",
            "0,582D"
        ],
        "mime": "message/rfc822"
    },
    "art": {
        "signs": [
            "0,4A47040E"
        ],
        "mime": "message/rfc822"
    },
    "manifest": {
        "signs": [
            "0,3C3F786D6C2076657273696F6E3D"
        ],
        "mime": "text/cache-manifest"
    },
    "log": {
        "signs": [
            "0,2A2A2A2020496E7374616C6C6174696F6E205374617274656420"
        ],
        "mime": "text/plain"
    },
    "tsv": {
        "signs": [
            "0,47"
        ],
        "mime": "text/tab-separated-values"
    },
    "vcf": {
        "signs": [
            "0,424547494E3A56434152440D0A"
        ],
        "mime": "text/vcard"
    },
    "dms": {
        "signs": [
            "0,444D5321"
        ],
        "mime": "text/vnd.DMClientScript"
    },
    "dot": {
        "signs": [
            "0,D0CF11E0A1B11AE1"
        ],
        "mime": "text/vnd.graphviz"
    },
    "ts": {
        "signs": [
            "0,47"
        ],
        "mime": "text/vnd.trolltech.linguist"
    },
    "3gp": {
        "signs": [
            "0,0000001466747970336770",
            "0,0000002066747970336770"
        ],
        "mime": "video/3gpp"
    },
    "3g2": {
        "signs": [
            "0,0000001466747970336770",
            "0,0000002066747970336770"
        ],
        "mime": "video/3gpp2"
    },
    "mp4": {
        "signs": [
            "0,000000146674797069736F6D",
            "0,000000186674797033677035",
            "0,0000001C667479704D534E56012900464D534E566D703432",
            "4,6674797033677035",
            "4,667479704D534E56",
            "4,6674797069736F6D"
        ],
        "mime": "video/mp4"
    },
    "m4v": {
        "signs": [
            "0,00000018667479706D703432",
            "0,00000020667479704D345620",
            "4,667479706D703432"
        ],
        "mime": "video/mp4"
    },
    "mpeg": {
        "signs": [
            "0,00000100",
            "0,FFD8"
        ],
        "mime": "video/mpeg"
    },
    "mpg": {
        "signs": [
            "0,00000100",
            "0,000001BA",
            "0,FFD8"
        ],
        "mime": "video/mpeg"
    },
    "ogv": {
        "signs": [
            "0,4F67675300020000000000000000"
        ],
        "mime": "video/ogg"
    },
    "mov": {
        "signs": [
            "0,00",
            "0,000000146674797071742020",
            "4,6674797071742020",
            "4,6D6F6F76"
        ],
        "mime": "video/quicktime"
    },
    "cpt": {
        "signs": [
            "0,4350543746494C45",
            "0,43505446494C45"
        ],
        "mime": "application/mac-compactpro"
    },
    "sxc": {
        "signs": [
            "0,504B0304",
            "0,504B0304"
        ],
        "mime": "application/vnd.sun.xml.calc"
    },
    "sxd": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/vnd.sun.xml.draw"
    },
    "sxi": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/vnd.sun.xml.impress"
    },
    "sxw": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/vnd.sun.xml.writer"
    },
    "bz2": {
        "signs": [
            "0,425A68"
        ],
        "mime": "application/x-bzip2"
    },
    "vcd": {
        "signs": [
            "0,454E5452595643440200000102001858"
        ],
        "mime": "application/x-cdlink"
    },
    "csh": {
        "signs": [
            "0,6375736800000002000000"
        ],
        "mime": "application/x-csh"
    },
    "spl": {
        "signs": [
            "0,00000100"
        ],
        "mime": "application/x-futuresplash"
    },
    "jar": {
        "signs": [
            "0,4A4152435300",
            "0,504B0304",
            "0,504B0304140008000800",
            "0,5F27A889"
        ],
        "mime": "application/x-java-archive"
    },
    "rpm": {
        "signs": [
            "0,EDABEEDB"
        ],
        "mime": "application/x-rpm"
    },
    "swf": {
        "signs": [
            "0,435753",
            "0,465753",
            "0,5A5753"
        ],
        "mime": "application/x-shockwave-flash"
    },
    "sit": {
        "signs": [
            "0,5349542100",
            "0,5374756666497420286329313939372D"
        ],
        "mime": "application/x-stuffit"
    },
    "tar": {
        "signs": [
            "257,7573746172"
        ],
        "mime": "application/x-tar"
    },
    "xpi": {
        "signs": [
            "0,504B0304"
        ],
        "mime": "application/x-xpinstall"
    },
    "xz": {
        "signs": [
            "0,FD377A585A00"
        ],
        "mime": "application/x-xz"
    },
    "mid": {
        "signs": [
            "0,4D546864"
        ],
        "mime": "audio/midi"
    },
    "midi": {
        "signs": [
            "0,4D546864"
        ],
        "mime": "audio/midi"
    },
    "aiff": {
        "signs": [
            "0,464F524D00"
        ],
        "mime": "audio/x-aiff"
    },
    "flac": {
        "signs": [
            "0,664C614300000022"
        ],
        "mime": "audio/x-flac"
    },
    "wma": {
        "signs": [
            "0,3026B2758E66CF11A6D900AA0062CE6C"
        ],
        "mime": "audio/x-ms-wma"
    },
    "ram": {
        "signs": [
            "0,727473703A2F2F"
        ],
        "mime": "audio/x-pn-realaudio"
    },
    "rm": {
        "signs": [
            "0,2E524D46"
        ],
        "mime": "audio/x-pn-realaudio"
    },
    "ra": {
        "signs": [
            "0,2E524D460000001200",
            "0,2E7261FD00"
        ],
        "mime": "audio/x-realaudio"
    },
    "wav": {
        "signs": [
            "0,52494646"
        ],
        "mime": "audio/x-wav"
    },
    "webp": {
        "signs": [
            "0,52494646"
        ],
        "mime": "image/webp"
    },
    "pgm": {
        "signs": [
            "0,50350A"
        ],
        "mime": "image/x-portable-graymap"
    },
    "rgb": {
        "signs": [
            "0,01DA01010003"
        ],
        "mime": "image/x-rgb"
    },
    "webm": {
        "signs": [
            "0,1A45DFA3"
        ],
        "mime": "video/webm"
    },
    "flv": {
        "signs": [
            "0,00000020667479704D345620",
            "0,464C5601"
        ],
        "mime": "video/x-flv"
    },
    "mkv": {
        "signs": [
            "0,1A45DFA3"
        ],
        "mime": "video/x-matroska"
    },
    "asx": {
        "signs": [
            "0,3C"
        ],
        "mime": "video/x-ms-asf"
    },
    "wmv": {
        "signs": [
            "0,3026B2758E66CF11A6D900AA0062CE6C"
        ],
        "mime": "video/x-ms-wmv"
    },
    "avi": {
        "signs": [
            "0,52494646"
        ],
        "mime": "video/x-msvideo"
    }
}
class Program:
    __key = '';
    __version = "1.0.1"
    __author = "Mehdi ghazanfari"
    __information = {'email' : '','passphrase' : '','length' : 1024, 'key_type' : 'RSA','real_name' :'Autogenerated Key'}
    #fixed
    def returnKey(self):
        return (self.__key)
    #fixed 0.0.1
    def showItems(self):
        clean()
        print(f"{Fore.RED}[1]{Fore.GREEN} generate a new key\n" )
        print(f"{Fore.RED}[2]{Fore.GREEN} remove a key (need fingerprint)\n" )
        print(f"{Fore.RED}[3]{Fore.GREEN} show key's information\n")
        print(f"{Fore.RED}[4]{Fore.GREEN} start encrypting\n")
        print(f"{Fore.RED}[5]{Fore.GREEN} start decrypting\n")
        print(f"{Fore.RED}[6]{Fore.GREEN} import key\n")
        print(f"{Fore.RED}[7]{Fore.GREEN} about us\n")
        print(f"{Fore.RED}[8]{Fore.GREEN} exit the program\n{Fore.RESET}")
    #fixed 0.0.1
    def getOption(self):
        option = int(input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW}enter your option ... {Fore.RESET}"))
        if option == 1:#generate a new key
            self.getData()
            self.generate_key()
            self.__re()
        elif option == 2:#remove a key (need fingerprint)
            self.removeKey()
        elif option == 3:#showing key's information
            self.keysInformations()
            self.__re()
        elif option == 4:#start encrypting
            if self.__information == {'email' : '','passphrase' : '','length' : 1024, 'key_type' : 'RSA','real_name' :'Autogenerated Key'}:
                self.getData()
            self.startEncrypting()
            self.__re()
        elif option == 5:#start decrypting
            if self.__information == []:
                self.getData()
            self.startDecrtpting()
            self.__re()
        elif option == 6:#imorting key
            if self.__key == '':
                anwser = input(f'{Fore.MAGENTA}[- output]{Fore.YELLOW} you\'ve initialized a key already.do you wanna change it?type \'yes\' ... {Fore.RESET}')
                if anwser == 'yes':
                    key =input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW}enter your key {Fore.RESET}")
                    self.importKey(key)
                else:
                    self.__re()    
        elif option == 7:#about us
            self.aboutUs()
            self.__re()
        elif option == 8:#to exit
            print(f"{Fore.YELLOW}the program will terminate in 5 seconds{Fore.RESET}")
            sleep(5)
            os._exit(0)
    #fixed 0.0.1
    def getData(self):
        email = input("enter your email address : ")
        passphrase = getpass("enter your passphrase : ")
        length = input("enter key's length(default 1024) : ")
        key_type = input("enter key's type(RSA is default.check websites for other types) : ")
        real_name = input("enter your real name : ")
        self.__information = [email, passphrase, length, key_type,real_name]
    #fixed 0.0.1
    def generate_key(self):
        inputData = gpg.gen_key_input(
        name_email = self.__information[0],
        passphrase = self.__information[1],
        key_type= self.__information[3],
        key_length = self.__information[2],
        name_real = self.__information[4]
        )

        self.__key = gpg.gen_key(inputData)
    #fixed
    def removeKey(self):
        try:
            if(self.__key == ''):
                raise Exception(f"{Fore.RED}[- output]{Fore.YELLOW}you did not entered any key to the program or it's not valid.at first please specify a key.{Fore.RESET}")
            else:
                passcode = input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW}enter your passphrase {Fore.RESET}")
                result = gpg.delete_keys(self.__key,secret=True,passphrase=passcode)
                if result.status == 'No such key':
                    raise Exception(f"{Fore.RED}[- output]{Fore.YELLOW}your key is not valid.try again{Fore.RESET}")
                else:
                    gpg.delete_keys(self.__key,passphrase=passcode)
                    print(f"{Fore.RED}[- output]{Fore.YELLOW}the key deleted successfully{Fore.RESET}")
            
        except Exception as error:
            print(error)
            self.__key = input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW}enter your key fingerprint{Fore.RESET}")
            self.removeKey()
            self.__re()
    #fixed
    def aboutUs(self):
        clean()
        print(f"{Fore.RED}[author]{Fore.GREEN} " + self.__author + f'\n{Fore.RESET}' )
        print(f"{Fore.RED}[discord]{Fore.GREEN} ItsOverflow#2755\n" )
        print(f"{Fore.RED}[email]{Fore.GREEN} m.ghazanfari1384@gmail.com\n")
        print(f"{Fore.RED}[currect version]{Fore.GREEN} " + self.__version + f'\n{Fore.RESET}')
    #fixed
    def __re(self):
        try:
            result = int(input(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET}to return to menu press {Fore.RED}-1{Fore.RESET} and for exit press {Fore.RED}0{Fore.RESET}...\n"))
            if result == -1:
                self.showItems()
                self.getOption()
            elif result == 0:
                return os._exit(0)
            else:
                raise Exception(f"{Fore.RED}[- output]{Fore.YELLOW}entered value is not valid.try again{Fore.RESET}")
        except Exception as error:
            print(error)
            self.__re()
    #fixed 0.0.1
    def importKey(self,key):
        self.__key = key
    #fixed 0.0.1
    def keysInformations(self):
        print(f"{Fore.MAGENTA}[- output]{Fore.YELLOW}public keys are these :{Fore.RED}\n")
        print(gpg.list_keys(False))

        print(f"{Fore.MAGENTA}\n[- output]{Fore.YELLOW}private keys are these :{Fore.RED}\n")
        print(gpg.list_keys(True))    
    #need to be fixed
    def exportKeys(self):
        pass
    #fixed 0.0.1
    def startEncrypting(self):

        print(f"{Fore.MAGENTA}[- output]{Fore.YELLOW}choose one of these to encrypt\n{Fore.RESET}")

        for this in os.listdir(appPath):
            print(f"{Fore.RED}[+] {Fore.RESET}"+this + '\n')
        selectedFile =input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW} which one?type full name of it\n{Fore.RESET}")    

        with open(os.path.abspath(selectedFile), 'rb') as file:
            status = gpg.encrypt_file(file,recipients= [self.__information[0]],output= os.path.splitext(os.path.abspath(selectedFile))[0] + '.safe' )

        print(f"{Fore.RED}"+status.stderr) 
        print(f"{Fore.RED}"+status.status+ f"{Fore.RESET}")
    #fixed 0.0.2 
    def startDecrtpting(self):
        fileExtension = '' #to store file's extension
              
        print(f"{Fore.MAGENTA}[- output]{Fore.YELLOW}we found this/these files that have crypted\n{Fore.RESET}")
    
        for file in glob.glob("*.safe"):
            print(f"{Fore.RED}"+file)

        #to get selected file by user
        selectedFile = input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW} which one?type full name of it\n{Fore.RESET}")

        #opening ecrypted file to decrypt it
        with open(os.path.abspath(selectedFile), 'rb') as file:
            status = gpg.decrypt_file(file,passphrase = self.__information[1],output= os.path.splitext(os.path.abspath(selectedFile))[0])
        #new file has selected to rename it(final task)
  
        selectedFilePath = os.path.abspath(selectedFile).split('.safe')[0]
        #
        #rename it to the original file
        with open(selectedFilePath, 'rb') as file:
            tmpExtFile = magic.from_file(selectedFilePath, mime = True)
            for i in ext.data.keys():
                if ext.data[i]['mime'] == tmpExtFile:
                    print(f"{Fore.MAGENTA}[- output]{Fore.YELLOW}the extension of the file has founded!\n{Fore.RESET}")  
                    fileExtension = i
                    break
            os.rename(selectedFilePath,selectedFilePath + '.'+ fileExtension)

        print(f"{Fore.RED}"+status.stderr) 
        print(f"{Fore.RED}"+status.status+ f"{Fore.RESET}")

app = Program()

app.showItems()
app.getOption()
