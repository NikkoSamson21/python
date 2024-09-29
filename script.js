const productsUrl = 'https://fakestoreapi.com/products';
const cartsUrl = 'https://fakestoreapi.com/carts';
let cartId = null;
let cart = { products: [] };

function fetchAllProducts() {
    fetch(productsUrl)
        .then(response => response.json())
        .then(data => {
            displayProducts(data);
        })
        .catch(error => console.error('Error fetching products:', error));
}

function displayProducts(products) {
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';

    products.forEach(product => {
        const productItem = document.createElement('div');
        productItem.className = 'product-item';
        productItem.innerHTML = `
            <img src="${product.image}" alt="${product.title}">
            <h3>${product.title}</h3>
            <p>${product.price} USD</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(productItem);
    });
}

function createCart() {
    fetch(cartsUrl, {
        method: 'POST',
        body: JSON.stringify({
            userId: 1,
            date: new Date().toISOString(),
            products: cart.products
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        cartId = data.id;
        console.log('Cart created:', data);
    })
    .catch(error => console.error('Error creating cart:', error));
}

function addToCart(productId) {
    const existingProduct = cart.products.find(item => item.productId === productId);
    if (existingProduct) {
        existingProduct.quantity += 1;
    } else {
        cart.products.push({ productId, quantity: 1 });
    }
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    cartItems.innerHTML = '';
    let total = 0;

    Promise.all(cart.products.map(item => 
        fetch(`${productsUrl}/${item.productId}`)
            .then(response => response.json())
            .then(product => {
                total += product.price * item.quantity;
                const cartItem = document.createElement('div');
                cartItem.className = 'cart-item';
                cartItem.innerHTML = `
                    <span>${product.title} (x${item.quantity})</span>
                    <span>${(product.price * item.quantity).toFixed(2)} USD</span>
                `;
                cartItems.appendChild(cartItem);
            })
    )).then(() => {
        cartTotal.innerHTML = `Total: ${total.toFixed(2)} USD`;

        if (cartId) {
            updateCartApi();
        } else {
            createCart();
        }
    });
}

function updateCartApi() {
    fetch(`${cartsUrl}/${cartId}`, {
        method: 'PUT',
        body: JSON.stringify({
            userId: 1,
            date: new Date().toISOString(),
            products: cart.products
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Cart updated:', data);
    })
    .catch(error => console.error('Error updating cart:', error));
}

function deleteCart() {
    if (cartId) {
        fetch(`${cartsUrl}/${cartId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            console.log('Cart deleted:', data);
            cart = { products: [] };
            cartId = null;
            updateCart();
        })
        .catch(error => console.error('Error deleting cart:', error));
    } else {
        alert('No cart to delete!');
    }
}

function checkout() {
    if (cart.products.length === 0) {
        alert('Your cart is empty!');
        return;
    }

    alert('Thank you for your purchase!');
    deleteCart();
}

document.getElementById('checkout-button').addEventListener('click', checkout);
document.getElementById('delete-cart-button').addEventListener('click', deleteCart);

fetchAllProducts();
