<p align="center">
<img src="https://user-images.githubusercontent.com/70070951/201959147-de2f0b35-af44-4b29-b6bc-00765c5d37e2.png" width="400" height="200">
</p>

<h1 align="center">Mawdoo3 scrapper</h1>
<p align="center">
📔<a href="https://github.com/Faris-abukhader/mawdoo3-scrapper/blob/master/README_ar.md">  بالعربي </a>📔 
 </p>


## 🚩 Table of Contents

- [Introduction](#--introduction)
- [Installation](#--installation)
- [Development setup](#--development-setup)
- [Packages](#-packages)
- [License](#-license)




## <img src="https://cdn-icons-png.flaticon.com/512/1436/1436664.png" width="25" height="25" style="padding-right:15px">  Introduction 

<p>
<b>Warning</b>: This project is only for study purpose , please don’t re-share these articles under your name , all these articles is only belongs to Mawdoo3 . 
</br>
<h3>You have two approaches to get your data : </h3>
- by calling save_all_articles_into_file functions and get all available articles into .txt file 
</br>
<br/>
- by cut down the process into two stages ( recommended if you have unstable internet connection) , first you call save_all_articles_title_into_file , then after you successfully got all titles saved to .txt file , you can read the file and pass each title into get_target_article function, and save each article once you get it into .txt file .

</p>


## <img src="https://cdn-icons-png.flaticon.com/512/814/814848.png" width="25" height="25" style="padding-right:15px">  Installation 


### 🔘 Cloning repository
1. On GitHub.com, navigate to the main page of the repository.
2. Above the list of files, click  Code.
3. Copy the URL for the repository.
4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier.
```
git clone github.com/Faris-abukhader/mawdoo3-scrapper
```
Press Enter to create your local clone
```
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `mawdoo3-scrapper`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
<br/>


## <img src="https://cdn-icons-png.flaticon.com/512/814/814848.png" width="25" height="25" style="padding-right:15px">  Development setup

To set up this project you need to download Python in your machine or if you have it make sure you have the latest version of it.

### 🔘 Checking up Python version in mac
```
python3 -V
```
### 🔘 Checking up Python version in windows
```
python --version
```
### 🔘 Downloading Python

> for Windows  


Download the windows installer from [Python offical website](https://www.python.org/downloads/) make sure you have download the latest version of Python.
<br/>


> for Mac
- You can download Python using brew CLI
```
brew install python
```
- You can download Python mac version through [the offical website](https://www.python.org/downloads/)
<br/>
<hr/>


### 🔘 Downloading the packages

Go to project direct where  requirements.txt is exist and type in terminal :
```
pip install -r requirements.txt 
```

<br/>
<hr/>

## 📦 Packages

| Name | Description |
| --- | --- |
| [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | Beautiful Soup is a Python library for pulling data out of HTML and XML files. |
| [`pyarabic`](https://pypi.org/project/PyArabic/) | A specific Arabic language library for Python, provides basic functions to manipulate Arabic letters and text, like detecting Arabic letters, Arabic letters groups and characteristics, remove diacritics etc. |
| [`selenium`](https://pypi.org/project/selenium/) |The selenium package is used to automate web browser interaction from Python. |



## 📜 License

This software is licensed under the [MIT](https://github.com/Faris-abukhader/mawdoo3-scrapper/blob/main/license) © [FaRiS](https://github.com/Faris-abukhader).
