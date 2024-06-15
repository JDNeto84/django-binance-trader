# Django Binance Trader 📈

This Django web application connects to the Binance API using the Python Binance Connector library. Its main purpose is to provide an intuitive interface for viewing SPOT wallet balances and creating buy and sell orders for the BTC/USDT pair. 💰

The application leverages the HTMX library to dynamically update the webpage with the results of requests to the Binance API, without the need to reload the entire page. This results in a smoother and more responsive user experience. ✨

## Features 🚀

* **Balance View:** Displays real-time SPOT wallet balances, including the quantity of each cryptocurrency and its equivalent value in USDT.
* **Order Creation:** Allows for the creation of buy and sell orders for the BTC/USDT pair, specifying the order type (limit or market), quantity, and price.
* **Order History:** Displays the history of executed orders, including information about the order type, quantity, price, and status.

## Technologies Used 🛠️

* **Django:** Python web framework for rapid and scalable development of web applications.
* **Binance Connector:** Python library for interacting with the Binance API.
* **HTMX:** JavaScript library for updating parts of a webpage without reloading it entirely.
* **Bootstrap:** CSS framework for rapid and responsive development of web interfaces.

## Disclaimer ⚠️

This project is solely a demonstration of how to use the Binance API with Django and HTMX. It should not be used for real trading operations in the cryptocurrency market. This project is not affiliated with Binance in any way. Binance is not responsible for any loss or damage caused by the use of this project.

