# html2json
html2json python
this is recursive function to extract html node and child , and add to dictionary
you can get html text to data and return dictionary

example:
```html

data2 = '<html xmlns="http://www.w3.org/1999/xhtml" lang="en" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]--><!--[if IE 7]><html xmlns="http://www.w3.org/1999/xhtml" lang="en" class="no-js lt-ie9 lt-ie8"> <![endif]--><!--[if IE 8]><html xmlns="http://www.w3.org/1999/xhtml" lang="en" class="no-js lt-ie9"> <![endif]--><!--[if gt IE 8]><!--><html xmlns="http://www.w3.org/1999/xhtml" lang="en" class="no-js"> <!--<![endif]--><!--[if lt IE 9]><!--><script type="text/javascript" src="/static/nhsuk_shared/js/jquery-1.11.3.min.b091a47f6b91.js" charset="utf-8"></script><!--<![endif]--><head>    <!--[if IE 9]>    <meta http-equiv="X-UA-Compatible" content="IE=9">    <![endif]-->    <script>        (function (d) {            d.className = d.className.replace(/\bno-js\b/, "js-enabled")        })(document.documentElement)    </script>    <meta charset="utf-8"/>    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>    <meta name="DC.Author" content="NHS website"/>    <meta name="DC.Publisher" content="Department of Health"/>    <meta name="DC.Format" scheme="IMT" content="text/html"/>    <meta name="DC.Subject" scheme="eGMS.IPSV" content="National Health Service (NHS), "/>'
```

and output of
```python
print(dic)
```
is

```json
{
  "html/0": {
    "xmlns": "http://www.w3.org/1999/xhtml",
    "lang": "en",
    "class": [
      "no-js",
      "lt-ie9",
      "lt-ie8",
      "lt-ie7"
    ]
  },
  "text/1": " ",
  "text/2": "endif]--><!--[if IE 7",
  "html/3": {
    "xmlns": "http://www.w3.org/1999/xhtml",
    "lang": "en",
    "class": [
      "no-js",
      "lt-ie9",
      "lt-ie8"
    ]
  },
  "text/4": " ",
  "text/5": "endif]--><!--[if IE 8",
  "html/6": {
    "xmlns": "http://www.w3.org/1999/xhtml",
    "lang": "en",
    "class": [
      "no-js",
      "lt-ie9"
    ]
  },
  "text/7": " ",
  "text/8": "endif]--><!--[if gt IE 8",
  "text/9": "><html xmlns=\"http://www.w3.org/1999/xhtml\" lang=\"en\" class=\"no-js\"> <!--<![endif]",
  "text/10": "[if lt IE 9]><!",
  "script/11": {
    "type": "text/javascript",
    "src": "/static/nhsuk_shared/js/jquery-1.11.3.min.b091a47f6b91.js",
    "charset": "utf-8"
  },
  "text/12": "<![endif]",
  "head/13": {},
  "text/14": " ",
  "text/15": "[if IE 9]>    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=9\">    <![endif]",
  "text/16": " ",
  "script/17": {},
  "text/18": "        (function (d) {            d.className = d.className.replace(/\bno-js\b/, \"js-enabled\")        })(document.documentElement)    ",
  "text/19": " ",
  "meta/20": {
    "charset": "utf-8"
  },
  "text/21": " ",
  "meta/22": {
    "http-equiv": "X-UA-Compatible",
    "content": "IE=edge"
  },
  "text/23": " ",
  "meta/24": {
    "name": "DC.Author",
    "content": "NHS website"
  },
  "text/25": " ",
  "meta/26": {
    "name": "DC.Publisher",
    "content": "Department of Health"
  },
  "text/27": " ",
  "meta/28": {
    "name": "DC.Format",
    "scheme": "IMT",
    "content": "text/html"
  },
  "text/29": " ",
  "meta/30": {
    "name": "DC.Subject",
    "scheme": "eGMS.IPSV",
    "content": "National Health Service (NHS), "
  }
}
```
