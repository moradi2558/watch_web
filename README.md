# Ecommerce website with Django

Features:

1-پنل ادمین

2-صفحه محصولات 	

3-سرچ کردن بین محصولات بر اساس اسم و قیمت	 

4-فلینر محصولات (محدوده قیمت.برند.رنگ.دسته بندی,...)	

5-ترتیب بندی محصولات (تاریخ.قیمت.تخفیف.امتیاز.مقدار خریداری شده,...)	

6-سبد خرید و درگاه پرداخت 	

7-صفحه جزییات محصولات (تعداد ویو , امتیاز دهی .کامنت و ریپلای . محصولات مشابه . اضافه کردن به علاقه مندی ها . مقایسه با محصولی دیگر . گالری عکس .نمودار تغییر قیمت محصول )	

8-صقحه کاربری (پروفایل و تفییر رمز و تغییر اطالاعات کاربر , صفحه محصولات خریداری شده و صفحه اخرین محصولات دیده شده و صفحه محصولات علافه مندی ها )	

	
https://github.com/moradi2558/shop_web/assets/125353647/24dfc122-d87e-4247-bd62-db3b0bf779cb


Setup and Instructions
To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

pip install virtualenv

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

virtualenv env

That will create a new folder env in your project directory. Next activate it with this command on mac/linux:

source env/bin/active

Then install the project dependencies with

pip install -r requirements.txt

Now you can run the project with this command

python manage.py runserver

After django you should install yarn or npm and start the project in ecommerce/frontend folder and use:

npm start

Now you can use the project on http://localhost:3000/.

Enjoy :)
