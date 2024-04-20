import random

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/random_fact">View a random fact!'

@app.route("/about")
def about():
    return """
    <html>
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>Tentang Kami</h1>
            <p>Ini adalah halaman tentang kami. Kami adalah tim yang fantastis!</p>
        </body>
    </html>
    """

facts_list = ["Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka.",
            "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
            "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan.", 
            "Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja.",
            "Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati.",
            "Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.",
            "Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita.",
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini."]

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p> <a href="/">Go back to home!</a>'

elements = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

@app.route("/kata_sandi")
def gen_pass():
    password = ""

    for i in range(random.randint(8,16)):
        password += random.choice(elements)

    return f'<p>{password}</p>'

app.run(debug=True)