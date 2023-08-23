## **_Capstone Ishita Sharma_**
Harvard's CS50 Web Programming with Python and Javascript 2020<br>
Brian Yu
brian@cs.harvard.edu<br>
David J. Malan
malan@harvard.edu

---
Project Name: Capstone [ Charil ]<br>
Email: ishita8851581104@gmail.com 

### **About:**

The project I chose for the capstone project is a business website that allows users to log in and know about the business and buy the products availabe. This Website is dedicated to my Father's Business and it is made to expand the business globally.This website ensures a smooth and convenient experience for customers looking to buy bath fittings. This project aims to make the process convenient and hassle-free, allowing customers to enjoy the benefits of online shopping from the comfort of their homes.This project will also allows the business to reach a wider customer base beyond their physical location.

#### Features

1. Create Product.
2. Add or remove the product from project.
3. Add the Product to the cart.
4. Know about the Company.
5. Login and Buy the product.
6. Company's profile.
7. Login using email.

#### Files & Directories

- `Main Directory`

  - `product` - Main application directory.

      - `models.py` - ORM auth model. Contains an Code class which has user and hashed reset password code.
      - `urls.py` - Contains all url paths for the authentication of the website such as login, Register, Active, etc.
      - `views.py` - Contains all view functions for the authentication of the website such as login, Register, Active, etc. Contains all view functions for Project and Product (mentioned in `urls.py`).
    - `static` - Holds all static files.
      - `css` - Contain all css files for styling the website.
      - `js` - Contains all JavaScript files for manipulating the DOM with ajax functionalities.
      - `img` - Holds all static images and icons  but they are not in a folder but in jpg format.
    - `Templates` - Holds all html files.


### **Project distinctiveness and complexities:**

The project is distinct in many aspects. Developing an efficient and user-friendly website for selling bath fittings requires expertise in web development, design, and integration of secure payment gateways. It involves managing a vast product catalog, implementing search and filtering options, and ensuring a smooth user experience throughout the purchasing process.

  - More models with complex relation between them.
  - Designed in a user friendly and professional way.
  - Set password and username to login.
  - Saves product in django framework using different categories.
  - Uses index.js for more interactive features.
  - Completely Mobile responsive.
**Bootstrap** CSS library was also integrated to assist with styling. 

CS50's projects were challenging to say the least. My prior experiences with other web development courses were elementery compare to the challenges set forth by the instructors of this course. I truly appreciate the spirit of pushing the students to solve the problems themselves. This course has helped me as a developer and made me understand programming at a fundamental level. It was important for the capstone project to embody that same spirit, so I decided to work on the biggest project of my life which was to expand my father's business. I had no exposure to Python when I began the course, let alone the Django framework. In essense, the reason for this project selection was to grow as a student.

### **Project future scope**

Coordinating the logistics and shipping of bath fittings purchased online can be challenging. My Next step for this project will be  Efficiently managing order fulfillment, tracking shipments, and ensuring timely delivery requires integration with shipping providers and careful coordination between the online store and logistics teams.

### **How to run website:**

1. Navigate to the project folder and create a virtual enviornment and activate it.

```
virtualenv venv
source venv/Scripts/activate
```

2. Install all required packages.

```
pip install -r requirements.txt
```

3. Initialize the database with makemigrations, migrate, then create superuser.

```
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
```

4. Launch the Django server. If set up correctly, server will launch on http://127.0.0.1:8000/.

```
py manange.py runserver
```

#### Preview

![Preview](preview.gif)
