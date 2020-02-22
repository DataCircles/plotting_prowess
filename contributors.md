# Contributors Guide

Welcome to the team! Here are the steps to make contributions to this repo:

1. Make yourself a branch:
A:  ![alt text](images/contrib2.png "Logo Title Text 1")
B: ![alt text](images/contrib1.png "Logo Title Text 1")

2. Clone the repo to your local machine:  
```git clone https://github.com/DataCircles/plotting_prowess.git```

3. Move to your branch:
```git checkout <your branch>```

4. Make a new notebook: 
```code <your filename>.ipynb```

5. Run jupyter notebook & plot away! 
Don't forget the Data Circles colors. You can import color options from colors.py. To use the ready-made cmap, code:
```python
from colors import Color_Coded
cc = Color_Coded()
cmap = cc.color_map()
```