# 0x01. Basic authentication

## Background Context
In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API.
In the industry, you should not implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-HTTPAuth](https://intranet.alxswe.com/rltoken/rpsPy0M3_FJuCLGNPUbmvg)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/5/6ccb363443a8f301bc2bc38d7a08e9650117de7c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231007%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231007T160136Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e90e318a90ba9e3a202ad2e4408fcb8d8da5aefb78853fc5ddbfee47ff74b216)


## Learning Objectives
### General

    What authentication means
    What Base64 is
    How to encode a string in Base64
    What Basic authentication means
    How to send the Authorization header

## Requirements
### Python Scripts

    All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/env python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle style (version 2.5)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
