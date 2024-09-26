from flask import Flask, render_template, jsonify, request
import stripe

app = Flask(__name__)

# Настройки Stripe
stripe.api_key = 'sk_test_51Q2bUMIKvKOwbcDFPqzma6KaZMgkEu3bdZDxs8hP132u4vdgkb0eowNbN7OkFArilOlS3JobMiTP6hidgTKxNdxP00FkwkaJ7d'  # Замени на свой секретный ключ из панели Stripe

@app.route('/')
def index():
    return render_template('index.html')

# Эндпоинт для создания платежа
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        # Создаем сессию Stripe для оплаты
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Dish Buddy',
                    },
                    'unit_amount': 1999,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:5000/success',
            cancel_url='http://localhost:5000/cancel',
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

# Успешная страница
@app.route('/success')
def success():
    return "Оплата прошла успешно!"

# Страница отмены
@app.route('/cancel')
def cancel():
    return "Оплата была отменена."

if __name__ == '__main__':
    app.run(debug=True)
