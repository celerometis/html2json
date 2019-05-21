data2 = '<html xmlns="http://www.w3.org/1999/xhtml" lang="en" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]--><!--[if IE 7]><html xmlns="http://www.w3.org/1999/xhtml" lang="en" class="no-js lt-ie9 lt-ie8"> <![endif]--><!--[if IE 8]><html xmlns="http://www.w3.org/1999/xhtml" lang="en" class="no-js lt-ie9"> <![endif]--><!--[if gt IE 8]><!--><html xmlns="http://www.w3.org/1999/xhtml" lang="en" class="no-js"> <!--<![endif]--><!--[if lt IE 9]><!--><script type="text/javascript" src="/static/nhsuk_shared/js/jquery-1.11.3.min.b091a47f6b91.js" charset="utf-8"></script><!--<![endif]--><head>    <!--[if IE 9]>    <meta http-equiv="X-UA-Compatible" content="IE=9">    <![endif]-->    <script>        (function (d) {            d.className = d.className.replace(/\bno-js\b/, "js-enabled")        })(document.documentElement)    </script>    <meta charset="utf-8"/>    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>    <meta name="DC.Author" content="NHS website"/>    <meta name="DC.Publisher" content="Department of Health"/>    <meta name="DC.Format" scheme="IMT" content="text/html"/>    <meta name="DC.Subject" scheme="eGMS.IPSV" content="National Health Service (NHS), "/>'
from bs4 import BeautifulSoup

dic = dict()
from lxml import etree

itt = 0


def list_tree_names(node):
    global itt
    for child in node.contents:
        try:
            dic.update({child.name + "/" + str(itt): child.attrs})
            itt += 1
            list_tree_names(node=child)
        except:
            dic.update({"text" + "/" + str(itt): child})
            itt += 1


soup = BeautifulSoup(data2, "html.parser")
list_tree_names(soup)
# for item in soup.contents:
#     a = item
#     dic.update({item.name + str(itt): item.attrs})
#     itt += 1

import json

with open('result.json', 'w') as fp:
    json.dump(dic, fp)
