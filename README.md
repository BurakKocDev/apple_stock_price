English Report

Apple Stock Price Analysis and Prediction Using LSTM Model
1. Introduction
This project involves analyzing Apple's historical stock data and predicting its future closing price using an LSTM (Long Short-Term Memory) model. Various techniques such as moving averages, daily returns, and stock volume analysis were used to explore the stock data, followed by using a deep learning model (LSTM) to predict future prices.

2. Data Overview
The dataset used includes Apple's stock data, specifically focusing on adjusted closing prices (Adj Close), volumes, and daily returns. The data spans a significant period, allowing for an in-depth analysis and effective modeling for future predictions.

3. Data Preprocessing
Date Conversion: The Date column was converted to datetime format for better handling and set as the index.
Handling Missing Values: The dataset was analyzed for missing values, and appropriate cleaning steps were applied if necessary.
Feature Selection: The adjusted closing price was the main focus for modeling, but additional features like volume and moving averages were also calculated for exploratory analysis.
4. Exploratory Data Analysis
Closing Price Plot: The historical closing price of AAPL was visualized, showing price trends over time.
Volume Plot: The volume of Apple stock traded over time was plotted, helping in understanding the buying and selling pressure during different market periods.
Moving Averages: Moving averages for 10, 20, and 50 days were calculated and plotted alongside the adjusted closing price to smooth out short-term fluctuations and identify trends.
Daily Returns: The daily percentage return of Apple's stock was calculated to analyze the stock's volatility.
Daily Return Histogram: A histogram of daily returns was plotted to observe the distribution, helping to understand the stock's risk and return profile.
5. Building the LSTM Model
Data Splitting: The dataset was split into 95% for training and 5% for testing.
Scaling: MinMaxScaler was used to normalize the closing price data between 0 and 1.
LSTM Architecture:
Two LSTM layers with 128 and 64 units, respectively, were used. Dense layers followed to output the prediction.
The model was compiled with adam optimizer and mean_squared_error loss function.
6. Model Training and Evaluation
Training: The model was trained on the prepared dataset with 60-time steps (past 60 days of data) for prediction.
Testing: The model predicted the closing prices for the test data, and the predictions were compared against actual values.
RMSE: Root Mean Squared Error (RMSE) was calculated as 2.29, showing the model's performance in predicting the stock price.
7. Results
Plotting Predictions vs Actual Prices: A graph was created comparing the model's predicted prices with the actual closing prices for the test set. The model captures the trends reasonably well but can be further improved with hyperparameter tuning or more epochs.
Validation and Predictions: The predicted prices were visualized, showing a good fit with the actual prices, demonstrating the effectiveness of the LSTM model.
8. Conclusion
The LSTM model successfully predicted Apple's stock price with reasonable accuracy. The model can be improved further by tweaking the architecture, adjusting parameters, and incorporating additional data features. Moving averages and daily returns provide insight into the stock's behavior, while the LSTM model serves as a robust tool for future price prediction.









Türkçe Rapor
Apple Hisse Senedi Fiyatı Analizi ve LSTM Modeli ile Tahmin
1. Giriş
Bu proje, Apple'ın geçmiş hisse senedi verilerini analiz etmek ve gelecekteki kapanış fiyatını LSTM (Uzun Kısa Süreli Bellek) modeli ile tahmin etmeyi amaçlamaktadır. Hisse senedi verilerini keşfetmek için hareketli ortalamalar, günlük getiriler ve işlem hacmi analiz edilmiş, ardından derin öğrenme modeli (LSTM) kullanılarak gelecekteki fiyat tahminleri yapılmıştır.

2. Veri Genel Bakışı
Kullanılan veri seti, Apple'ın hisse senedi verilerini içerir ve özellikle Adj Close (ayarlanmış kapanış fiyatları), işlem hacimleri ve günlük getiriler üzerinde yoğunlaşılmıştır. Veri seti, geniş bir dönemi kapsayarak derinlemesine analiz ve gelecekteki tahminler için etkili bir modellemeye olanak tanımıştır.

3. Veri Ön İşleme
Tarih Dönüşümü: Date sütunu, işlenebilirliği artırmak amacıyla datetime formatına dönüştürülmüş ve indeks olarak ayarlanmıştır.
Eksik Verilerin İşlenmesi: Veri seti eksik değerler açısından analiz edilerek gerekirse uygun temizlik adımları uygulanmıştır.
Özellik Seçimi: Modelleme için esas olarak ayarlanmış kapanış fiyatları kullanılmış, ancak işlem hacmi ve hareketli ortalamalar gibi ek özellikler de keşif amaçlı hesaplanmıştır.
4. Keşifsel Veri Analizi
Kapanış Fiyatı Grafiği: Apple hisse senedinin tarihsel kapanış fiyatları görselleştirilmiş ve fiyat eğilimleri incelenmiştir.
İşlem Hacmi Grafiği: Apple hisse senedinin işlem hacmi zamanla çizilmiş ve farklı piyasa dönemlerinde alım satım baskıları anlaşılmıştır.
Hareketli Ortalamalar: 10, 20 ve 50 günlük hareketli ortalamalar hesaplanarak, kısa vadeli dalgalanmaları yumuşatmak ve eğilimleri belirlemek için kullanılmıştır.
Günlük Getiriler: Apple'ın hisse senedinin günlük yüzdelik getirileri hesaplanarak volatilite analiz edilmiştir.
Günlük Getiriler Histogramı: Günlük getirilerin dağılımını anlamak için histogram oluşturulmuştur.
5. LSTM Modeli Oluşturma
Veri Bölünmesi: Veri seti %95 eğitim ve %5 test olacak şekilde bölünmüştür.
Ölçeklendirme: Kapanış fiyatları MinMaxScaler ile 0 ve 1 arasında normalize edilmiştir.
LSTM Mimarisi:
İki LSTM katmanı (128 ve 64 birimli) kullanılmış, ardından tahmin sonucunu veren yoğun katmanlar eklenmiştir.
Model adam optimizasyon algoritması ve mean_squared_error kayıp fonksiyonu ile derlenmiştir.
6. Model Eğitimi ve Değerlendirmesi
Eğitim: Model, geçmiş 60 günün verilerini kullanarak tahmin yapmak için eğitilmiştir.
Test: Model, test verisi için kapanış fiyatlarını tahmin etmiş ve bu tahminler gerçek değerlerle karşılaştırılmıştır.
RMSE: Hata ölçütü olarak Kök Ortalama Kare Hata (RMSE) 2.29 olarak hesaplanmış ve modelin performansı değerlendirilmiştir.
7. Sonuçlar
Tahminler ve Gerçek Fiyatlar Grafiği: Modelin tahmin ettiği fiyatlar ile gerçek kapanış fiyatları karşılaştırılarak grafiği çizilmiştir. Model genel eğilimleri yakalamayı başarmış, ancak hiperparametre ayarlamaları ile daha da geliştirilebilir.
Doğrulama ve Tahminler: Tahmin edilen fiyatlar görselleştirilmiş ve gerçek fiyatlarla uyum gösterdiği gözlemlenmiştir.
8. Sonuç
LSTM modeli, Apple hisse senedi fiyatlarını makul bir doğrulukla tahmin etmeyi başarmıştır. Modelin mimarisi ve parametreleri üzerinde yapılan ayarlamalarla daha iyi sonuçlar elde edilebilir. Hareketli ortalamalar ve günlük getiriler hisse senedi davranışına dair önemli içgörüler sunarken, LSTM modeli gelecekteki fiyat tahminleri için güçlü bir araç olarak kullanılmıştır.
