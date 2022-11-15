
<p align="center">
<img src="https://user-images.githubusercontent.com/70070951/201959147-de2f0b35-af44-4b29-b6bc-00765c5d37e2.png" width="400" height="200">
</p>
<p align="center">
📔<a href="https://github.com/Faris-abukhader/mawdoo3-scrapper/blob/master/README.md"> English </a>📔 
 </p>

## 🚩 قائمة المحتويات 


- [المقدمة](#--المقدمة)
- [تحميل المستودع](#--تحميل-المستودع)
- [تهيئة المشروع](#--تهيئة-المشروع)
- [المكتبات](#-المكتبات)
- [الرخصة](#-الرخصة)




## <img src="https://cdn-icons-png.flaticon.com/512/1436/1436664.png" width="25" height="25" style="padding-right:15px">  المقدمة 

<p>
تنويه : تم انشاء هذا المشروع لاسباب دراسية فقط ، يمنع منعاً باتاً اعادة نشر هذه المواضيع من دون اذن موقع موضوع .
</br>
هناك طريقتين للحصول على جميع المقالات المتوفرة : 
</br>
١- عن طريق وهي الطريقة المباشرة وتتم عن طريق استخدام الدالة save_all_articles_into_file 
</br>
٢- ينصح بهذا الطريقة اذا كان اتصالك للانترنت غير ثابت ؛ تنقسم هذه الطريقة إلى جزئين ، الأول هو حفظ عناوين المواضيع ، عن طريق استعمال الدالة save_all_articles_title_into_file ، بعد ذلك يمكنك استخدام هذه العناوين للحصول على المقالات واحده تلو الأخرى عن طريق استعمال الدالة get_target_article ولا تنسى حفظ المقالة عند الحصول عليها . 



</p>


## <img src="https://cdn-icons-png.flaticon.com/512/814/814848.png" width="25" height="25" style="padding-right:15px">  تحميل المستودع  


### 🔘 نسخ مستودع المشروع 
1. اذهب الى الصفحة الرئسية للمشروع .
2. في اعلى الصفحة انقر على الزر "code".
3. انسخ رابط المستودع .
4. افتح خط الاوامر terminal على الجهاز الخاص بك.
5. انتقل على المكان المراد تحميل المشروع اليه .
6. ادخل الامر التالي لنسخ مستودع المشروع لجهاز الحاسب الخاص بك:
```
git clone github.com/Faris-abukhader/mawdoo3-scrapper
```
انقر على الزر enter لاتمام العملية 
```
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `mawdoo3-scrapper`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
<br/>


## <img src="https://cdn-icons-png.flaticon.com/512/814/814848.png" width="25" height="25" style="padding-right:15px">  تهيئة المشروع 

لتهيئة المشروع لابد من تحميل Python  على جهاز الخاص ، اما اذا كنت تمتلكه بالفعل فتأكد تحميل اخر اصدار.
 ### 🔘 التأكد من اصدار Python للماك
```
python3 -V
```

 ### 🔘 التأكد من اصدار Python للوندوز
```
 python --version
```

### 🔘 تحميل Python

> لاجهزة وندوز
- يمكن تحميل نسخة ويندوز عبر الصفحة الرسمية ل Python ، يرجى التأكد من تحميل آخر اصدار متاح .
 [الصفحة الرسمية](python.org/downloads/)

<br/>

> لاجهزة الماك 
- يمكن تحميل Python عبر اوامر brew 
```
brew install node
```
- يمكنك تحميل نسخة الماك عن طريق  ل Python  [الصفحة الرسمية  ](python.org/downloads/)
<br/>
<hr/>


### 🔘 تحميل المكتبات اللازمة 

من خلال شريط الاوامر terminal انتقل الى مكان تواجد الملف requirements.txt ثم ادخل الامر التالي  :
```
pip install -r requirements.txt  
```

<br/>
<hr/>



## 📦 المكتبات


  | اسم المكتبة  | الوصف |
| --- | --- |
| [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | Beautiful Soup is a Python library for pulling data out of HTML and XML files. |
| [`pyarabic`](https://pypi.org/project/PyArabic/) | A specific Arabic language library for Python, provides basic functions to manipulate Arabic letters and text, like detecting Arabic letters, Arabic letters groups and characteristics, remove diacritics etc. |
| [`selenium`](https://pypi.org/project/selenium/) |The selenium package is used to automate web browser interaction from Python. |


## 📜 الرخصة

هذا المشروع تحت رخصة [MIT](https://github.com/Faris-abukhader/mawdoo3-scrapper/blob/main/license) © [FaRiS](https://github.com/Faris-abukhader).
