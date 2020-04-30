**Overview**

This project deals with monitoring a free lancer by recording their activity in respective system.
The monitoring is done by recording the processes opened in the system and identification of windows/tabs present(if any) in a screenshot captured at a random instant of time

***background process.py*** is used to find all the running processes in the system.

***template_matching.py*** identifies the tab/windows present in the given screenshot.

***text detection.py*** determines the active tab in the browser if the screenshot includes any.

***template_test.py*** is a test program before saving the favicon in **test images/favicon** folder to test whether the favicon can be used for identification and make necessary changes if required.

**Requirments**
   *  Python 3.4 +
   *  Tesseract OCR

**Modules Required**
   *  psutil == 5.6.3
   *  opencv-python == 4.1.0.25
   *  numpy == 1.16.4
   *  pytesseract == 0.2.6
   *  os

**Installation**

   The required modules can be installed in windows using **pip install module_name** in command prompt. The [Python Package Index (PyPI)](https://pypi.org/) is a repository of software for the Python programming language. For more details reach out there to solve any issues.
   
   Tesseract is an optical character recognition engine for various operating systems. It is free software, released under the Apache License, Version 2.0, and development has been sponsored by Google since 2006.
