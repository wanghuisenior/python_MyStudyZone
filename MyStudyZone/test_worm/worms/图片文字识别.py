#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/10/19 8:20
"""

import pytesseract
from PIL import Image

image = Image.open('test.png')
code = pytesseract.image_to_string(image)
print(code)