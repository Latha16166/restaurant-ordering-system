# Restaurant Ordering System 🍔🍕🥗

## Description
This is a simple **Restaurant Ordering System** built using **HTML, CSS and Javascript**.  
Users can **click on food images** to add items to the cart and see the **total bill update dynamically**.  
The project is designed to be **colorful and student-friendly**.

---

## Features
- Click on **food images** to add to cart ✅
- Shows **cart contents** and **total bill** ✅
- **Scroll menu** for multiple items ✅
- **Colorful UI** for easy interaction ✅
- Works in any **modern web browser** ✅

---

## Folder Structure
RestaurantOrderingSystem/ │ ├── index.html           # Main HTML file ├── style.css            # CSS for styling (optional) ├── script.js            # JavaScript file (optional) └── assets/ ├── veg_biryani.png ├── burger.png ├── pizza.png └── drink.png
---

## How to Run
1. Open the **project folder**.
2. Double-click `index.html` OR open it in a browser.
3. Click **food images** to add items to cart.
4. Total bill updates automatically.

---

## Adding New Menu Items
1. Place the **image** in the `assets/` folder.
2. Add a new `<div class="item">` block in `index.html`:

```html
<div class="item">
  <img src="assets/IMAGE_NAME.png" onclick="addItem('ITEM_NAME',PRICE)">
  <p>ITEM_NAME - ₹PRICE</p>
  <button onclick="addItem('ITEM_NAME',PRICE)">Add</button>
</div>
