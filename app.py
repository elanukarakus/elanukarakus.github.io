from flask import Flask, render_template, request, flash, Markup
import numpy as np 
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


wapp = Flask(__name__)
wapp.secret_key = "teknofest_turizm_5147_9622"

@wapp.route("/st")
def index():
	flash("")
	return render_template("index.html")

@wapp.route("/nd", methods=['POST', 'GET'])
def kesfet():
	flash("")
	filtre = request.args.get('filtre_input', False)
	yer = request.args.get("yer_input", False)
	df2 = pd.read_csv("C:\\Users\\elanu\\Desktop\\ms\\dataset.csv", sep=";") 
	df2.head()
	df2.shape
	df2.info()
	df2.head()
	df2.shape
	df2.columns
	df2[filtre].head(10)
	tfidf = TfidfVectorizer(stop_words='english')
	df2[filtre] = df2[filtre].fillna('')
	tfidf_matrix = tfidf.fit_transform(df2[filtre])
	tfidf_matrix.shape
	cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
	indices = pd.Series(df2.index, index=df2['yer']).drop_duplicates()
	def tavsiye_ver(title, cosine_sim=cosine_sim):
		idx = indices[title]
		sim_scores = list(enumerate(cosine_sim[idx]))
		sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
		sim_scores = sim_scores[1:6]
		movie_indices = [i[0] for i in sim_scores]
		return df2['yer'].iloc[movie_indices]
	oneri = tavsiye_ver(yer)
	onerim = oneri.tolist()
	y1 = onerim[0]
	y2 = onerim[1]
	y3 = onerim[2]
	y4 = onerim[3]
	y5 = onerim[4]
	yer1= "http://127.0.0.1:5000/" + y1
	yer1 = yer1.strip()
	yer2= "http://127.0.0.1:5000/" + y2
	yer2 = yer2.strip()
	yer3= "http://127.0.0.1:5000/" + y3
	yer3 = yer3.strip()
	yer4= "http://127.0.0.1:5000/" + y4
	yer4 = yer4.strip()
	yer5= "http://127.0.0.1:5000/" + y5
	yer5 = yer5.strip()
	y11 = '<a href='+yer1+'>' + y1 +'</a>'
	y22 = '<a href='+yer2+'>' + y2 +'</a>'
	y33 = '<a href='+yer3+'>' + y3 +'</a>'
	y44 = '<a href='+yer4+'>' + y4 +'</a>'
	y55 = '<a href='+yer5+'>' + y5 +'</a>'

	e= "1." + y11 + "," + "  2." + y22 + "," + "  3." + y33 + "," +"  4." + y44 + "," + "  5." + y55 +"."

	flash(e)	
	return render_template("index.html")




@wapp.route("/th", methods=['POST', "GET"])
def foto():
	flash("")	
	fotokarar = request.form.get("hangi_foto", False)
	if fotokarar == None:
		flash("Lütfen, doldurun.")
	elif fotokarar == "Fotoğraf 1":
		flash("1.Abant Gölü, 2.Boraboy Gölü, 3.Güzeldere Şelalesi Tabiat Parkı, 4.Ayıkayası Tabiat Parkı, 5.Ulugöl Tabiat Parkı, 6.Perşembe Yaylası")
	elif fotokarar == "Fotoğraf 2":
		flash("1.Kıbledağ Camii, 2.Nasrullah Camii, 3.Hz. Pir Şeyh Saban-ı Veli Külliyesi, 4.Sümele Manastırı, 5. 2.Bayezid Camiisi, 6.Kastamonu Müzesi")
	elif fotokarar == "Fotoğraf 3":
		flash("1.Güzeldere Şelalesi Tabiat Parkı, 2.Aktaş Şelalesi, 3.Ayıkayası Tabiat Parkı, 4.Samandere Şelalesi Tabiat Anıtı, 5.Karagöl Tabiat Parkı, 6.Aydınpınar Şelalesi")
	elif fotokarar == "Fotoğraf 4":
		flash("1.Sinop Arkeoloji Müzesi, 2.Kulakkaya Yaylası, 3.Ereğli Müzesi, 4.Bartın Kent Müzesi, 5.Kasım Sipahioğlu Konağı, 6.Karabük Tarihi Demirciler Çarşısı")
	elif fotokarar == "Fotoğraf 5":
		flash("1.İnkum Plajı, 2.Filyos Plajı, 3.İnceburun Feneri, 4. Ulukaya Kanyonu ve Şelalesi, 5.Mavi Göl, 6.Yenice Ormanı ")
	elif fotokarar == "Fotoğraf 6":
		flash("1.Çorum Müzesi, 2.Tokat Müzesi, 3.Baksı Müzesi, 4.Sinop Arkeoloji Müzesi, 5.Amasya Arkeoloji Müzesi, 6.Bandırma Vapuru Müzesi")
	return render_template("index4.html")

@wapp.route("/if", methods=["POST", "GET"])
def hakk():
	return render_template("index5.html")

@wapp.route("/ile", methods=["POST", "GET"])
def ilet():
	return render_template("index3.html")

@wapp.route("/pl", methods=["POST", "GET"])
def planla():
	brow = request.form.get("brow", False)
	print(brow)
	flash(brow)
	return render_template("index2.html", visibility="hidden")

@wapp.route("/mencuna", methods=["POST", "GET"])
def goooooo():
	return render_template("mencuna.html")