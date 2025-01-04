# **Rental Application with Python**

This is a Python-based rental application that allows users to manage their rental carts, checkout products, and handle payments. The application features a graphical user interface (GUI) built using **CustomTkinter**.

## **Features**
- User authentication (Sign Up, Sign In, and Logout).
- Display product list and add items to the cart.
- Update product quantity in the cart.
- Checkout items with payment processing.
- Save invoices in **JSON format**.
- View real-time cart total (total price and total quantity).

## **Tech Used**
- **Python**: Backend and application logic.
- **CustomTkinter**: GUI design.
- **CSV**: To manage user accounts, product data, and carts.
- **JSON**: To store invoices.



## **Installation**

### **1. Clone the repository**
```bash
git clone <repository-url>
cd <repository-folder>
```

Here’s the updated **README.md** section with virtual environment instructions and using `requirements.txt`:

---
### **2. Install dependencies**

Make sure you have Python installed on your system.

#### **Step 1: Create a virtual environment**
Create and activate a virtual environment to keep dependencies isolated:
```bash
python -m venv venv
venv\Scripts\activate
```

#### **Step 2: Install required packages**
Install all the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### **Step 3: Run the application**
Once the dependencies are installed, you can run the application:
```bash
python main.py
```


## **License**
This project is open-source and available under the [MIT License](LICENSE).
