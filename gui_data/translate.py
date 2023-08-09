import os
# 全局变量
translate_text = ""
# cython: language_level=3
import Levenshtein
from Levenshtein import ratio
import pickle
from multiprocessing import Pool
import cython

# 设置语言环境变量
lang = 'zh_CN' 

# 读取翻译文件
dir_path = os.getcwd()
filename = f"{dir_path}\\gui_data\\locales\\LC_MESSAGES\\{lang}.tmp"

# 初始化翻译文本
with open(filename, 'r', encoding='utf-8') as f:
    translate_text = f.read()

# 提前编译成翻译字典    
translates = {}
for line in translate_text.split('\n'):
    if line.startswith('msgid'):
        original = line.split(' ', 1)[1]
    elif line.startswith('msgstr'):
        translation = line.split(' ', 1)[1]
        translates[original] = translation

# 加缓存        
cache = {}

# Cython编译       
@cython.ccall
def translate(text):
    #print (text)  
    if text in cache:
        return cache[text]
    
    if text in translates:
        translated = translates[text]
        cache[text] = translated
        return translated
    
    matches = []
    for original, translation in translates.items():
        ratio = Levenshtein.ratio(original, text)
        if ratio > 0.8:
            matches.append((ratio, translation))
            
    if matches:
        translated = max(matches)[1]
        cache[text] = translated
        return translated
      
    return text
    
# 多进程翻译
#def mp_translate(texts):
#    pool = Pool()
#    results = pool.map(translate, texts)
#    pool.close()
#    pool.join()
#    return results

