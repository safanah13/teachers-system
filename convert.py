# -*- coding: utf-8 -*-
with open('مساءلة.html', 'r', encoding='windows-1256') as file:
    content = file.read()
with open('مساءلة.html', 'w', encoding='utf-8') as file:
    file.write(content)
