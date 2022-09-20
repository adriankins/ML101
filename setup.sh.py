# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:35:58 2022

@author: SYSTEMarket
"""

mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml