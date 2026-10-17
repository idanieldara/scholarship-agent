<div align="center">

<img src="assets/screenshots/banner.jpg" alt="Burs Ajanı: Google Gemini ile çalışan yapay zekâ burs bulucu, Python ve Streamlit ile geliştirildi" width="860">

<br />

# 🎓 Dara Burs Ajanı (Scholarship Agent)

**Ücretsiz ve açık kaynaklı yapay zekâ burs bulucu. Dünyadaki bursları eğitim düzeyine, hedef ülkeye, alana, finansman türüne ve kendi uyruğunuza göre arayın, filtreleyin ve karşılaştırın.**

**Google Gemini** ile güçlendirildi · **Python & Streamlit** ile geliştirildi · Arayüz: **English · فارسی · Türkçe · العربية**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-API-4285F4?logo=googlegemini&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

[Özellikler](#features) · [Hızlı başlangıç](#quick-start) · [Kullanım](#usage) · [Çevrimiçi yayın](#deploy) · [Sorun giderme](#troubleshooting) · [Değişiklik günlüğü](CHANGELOG.md)

🌐 [English](README.md) · [فارسی](README.fa.md) · **Türkçe**

</div>

---

<details open>
<summary><b>📑 İçindekiler</b></summary>

- [📖 Burs Ajanı nedir?](#what-is)
- [✨ Özellikler](#features)
- [🧠 Nasıl çalışır?](#how-it-works)
- [🚀 Hızlı başlangıç](#quick-start)
  - [📦 Yöntem 1: Doğrudan indirme (Git'siz)](#install-direct)
  - [🌿 Yöntem 2: Git ile](#install-git)
  - [🖱️ Tek tıkla başlatıcı: Run (Windows) / Run (Mac)](#launcher)
  - [🔑 Ücretsiz Gemini API anahtarı alma](#api-key)
  - [⚙️ Yapılandırma](#configuration)
- [🧭 Kullanım](#usage)
- [🌐 Desteklenen kaynaklar](#sources)
- [🗂️ Proje yapısı](#project-structure)
- [🖼️ Ülke görselleri](#country-images)
- [☁️ Çevrimiçi yayın](#deploy)
- [🛠️ Sorun giderme](#troubleshooting)
- [⚠️ Sorumlu kullanım ve uyarı](#responsible-use)
- [🗺️ Yol haritası](#roadmap)
- [📋 Değişiklik günlüğü](#changelog)
- [🤝 Katkıda bulunma](#contributing)
- [📄 Lisans](#license)
- [👤 Geliştirici ve destek](#author)

</details>

---

<a id="what-is"></a>

## 📖 Burs Ajanı nedir?

**Tam burslu** bir program bulmak, her biri farklı tasarıma, son tarihe ve koşula sahip onlarca siteyi açmak demektir.
**Burs Ajanı**, bu işi sizin yerinize yapan bir **burs arama motoru ve yapay zekâ ajanıdır**:

1. popüler burs sitelerinden **yüzlerce bursu saniyeler içinde içe aktarır** (yapay zekâ ve API anahtarı gerekmez),
2. bu sitelerde olmayan bursları **Gemini + Google Search** ile web'de arar,
3. her burs sayfasını **yapay zekâ ile okuyarak** finansman, uygun uyruklar, alanlar ve dil şartlarını doldurur,
4. ve her şeyi **eğitim düzeyi, ülke, alan, finansman, son tarih ve kendi uyruğunuza** göre anında filtreler. Veriler bilgisayarınızda yerel olarak saklanır.

Yurt dışında **Lisans, Yüksek lisans, Doktora ve Doktora sonrası** bursu arayan öğrenciler ve hızlı, tekrarlanabilir kısa listeler hazırlamak isteyen eğitim danışmanları için tasarlandı.

<a id="features"></a>

## ✨ Özellikler

- 🎨 **Modern panel arayüzü**: hero başlık, kenar çubuğu menüsü, canlı istatistikler, açılır burs kartları ve **her hedef ülke için bir simge yapı illüstrasyonu** (Fransa için Eyfel Kulesi, Birleşik Krallık için Big Ben, Almanya için Brandenburg Kapısı ve 35'ten fazlası).
- 🌍 **Eğitim düzeyine göre burslar**: Lisans, Yüksek lisans, Doktora, Doktora sonrası ve Diğer için ayrı sekmeler.
- 🔎 **Güçlü filtreler**: ülke, alan veya anahtar kelime, finansman türü (Tam / Kısmi / Yalnızca harç), süresi dolanları gizleme ve **uyruğa göre uygunluk** (istediğiniz ülkeyi veya "Herhangi biri"ni seçin).
- 📚 **Hızlı site içe aktarma (yapay zekâsız, anahtarsız)**: Scholars4Dev, ScholarshipTab, ScholarshipSet ile Almanya, Birleşik Krallık, Kanada, ABD ve Avustralya ülke siteleri. Uyumlu herhangi bir kategori URL'sini ekleyebilirsiniz.
- 🤖 **Yapay zekâ ile web araması**: Gemini + Google Search. *Hedef ülkeler* boşsa **tüm ülkelerde** aranır; derin arama modu her dünya bölgesi için bir tur çalıştırır.
- ✨ **Yapay zekâ ile zenginleştirme**: Gemini her burs sayfasını okur (URL context) ve finansman, tutar, uygun uyruklar, alanlar ve dil şartlarını doldurur.
- 🗣️ **Dört arayüz dili**: tam **RTL** desteği (Farsça ve Arapça) ve *IRANSansX* yazı tipi. Özetler seçtiğiniz dilde yazılır ve seçiminiz sayfa yenilenince korunur.
- 💾 **Yerel öncelikli**: sonuçlar yerel SQLite veritabanına kaydedilir. Filtreleme anlıktır ve API çağrısı gerektirmez.
- ⬇️ Excel ve Google Sheets için **CSV dışa aktarma**.
- 🛡️ **Güvenilir tasarım**: aşırı yüklenen modeller için otomatik yeniden deneme (503), kota hatalarında (429) hızlı geçiş ve yapılandırılabilir yedek model.
- 🔁 **Akıllı birleştirme**: birkaç sitede veya yapay zekâ aramasında bulunan aynı burs yalnızca bir kez görünür. Yeniden içe aktarmak yeni bursları ekler ve değişen son tarihleri günceller; yapay zekânın doldurduğu veriler silinmez. Yeni gelenler **YENİ** rozeti taşır.
- 🔐 **Gizli ve hatırlanan**: API anahtarınız yalnızca sizin bilgisayarınızda kalır. Kenar çubuğu onu yerel `.env` dosyanıza kaydeder (Git'e asla gönderilmez); böylece yenilemeden sonra yeniden yazmanız gerekmez. Dil, uyruk ve model de hatırlanır.

<a id="how-it-works"></a>

## 🧠 Nasıl çalışır?

```mermaid
flowchart LR
    A[Burs siteleri] -->|tarayıcı| D[(Yerel SQLite)]
    B[Gemini + Google Search] -->|Yapay zekâ web araması| D
    D -->|URL context| C[Yapay zekâ ile zenginleştirme]
    C --> D
    D --> E[Filtreler: düzey, ülke, alan, finansman, son tarih, uyruk]
    E --> F[Streamlit arayüzü: EN, FA, TR, AR + CSV]
```

<a id="quick-start"></a>

## 🚀 Hızlı başlangıç

**Gereksinimler:** Python 3.10 – 3.14 (3.12 veya 3.13 önerilir) ([python.org](https://www.python.org/downloads/); Windows'ta kurulumda **Add Python to PATH** seçeneğini işaretleyin) ve ücretsiz bir Gemini API anahtarı (yalnızca yapay zekâ özellikleri için). 3.15 gibi çok yeni sürümler henüz desteklenmiyor (bazı bağımlılıkların bu sürümler için hazır paketi yok). İki kurulum yönteminden birini seçin:

<a id="install-direct"></a>

### 📦 Yöntem 1: Doğrudan indirme (Git gerekmez)

1. GitHub'da depo sayfasını açın, yeşil **Code** düğmesine ve ardından **Download ZIP**'e tıklayın.
2. ZIP dosyasını istediğiniz yere çıkarın (örneğin `Belgeler/scholarship-agent`).
3. Uygulamayı başlatın:
   - **Windows:** **`Run (Windows).bat`** dosyasına çift tıklayın.
   - **macOS / Linux:** klasörde bir terminal açıp `bash "Run (Mac).sh"` komutunu çalıştırın.

   İlk çalıştırmada sanal ortam oluşturulur, bağımlılıklar yüklenir, `.env` dosyanız oluşturulur ve uygulama **http://localhost:8501** adresinde açılır. Sonraki açılışlar birkaç saniye sürer.
4. Gemini API anahtarınızı uygulamada (kenar çubuğundaki **Ayarlar**) veya `.env` dosyasında girin.

> Daha sonra güncellemek için yeni ZIP'i indirip dosyalarını eski klasörün üzerine kopyalayın. `.env` ve `scholarships.db` dosyalarınızı koruyun.

<a id="install-git"></a>

### 🌿 Yöntem 2: Git ile (güncellemeler ve katkıda bulunanlar için ideal)

```bash
git clone https://github.com/idanieldara/scholarship-agent.git
cd scholarship-agent
```

Ardından `Run (Windows).bat` (Windows) veya `bash "Run (Mac).sh"` (macOS / Linux) ile başlatın ya da elle çalıştırın:

```bash
python -m venv venv
venv\Scripts\activate            # Windows  |  macOS / Linux: source venv/bin/activate
pip install -r requirements.txt
copy .env.example .env           # Windows  |  macOS / Linux: cp .env.example .env
streamlit run app.py
```

İstediğiniz zaman `git pull` ile güncelleyin. Başlatma betikleri değişen bağımlılıkları otomatik yükler; elle başlatıyorsanız `pip install -r requirements.txt` komutunu tekrar çalıştırın.

> **Streamlit ilk çalıştırmada e-posta mı istiyor?** Sadece **Enter**'a basın. `Run (Windows).bat` ve `Run (Mac).sh` bu soruyu otomatik atlar. Uygulamayı her zaman proje klasöründen çalıştırın.

<a id="launcher"></a>

### 🖱️ Tek tıkla başlatıcıyı kullanma (`Run (Windows).bat` / `Run (Mac).sh`)

`Run (Windows).bat` (Windows) ve `Run (Mac).sh` (macOS / Linux), hiçbir komut yazmadan uygulamayı başlatır. Her açılışta şunları yapar:

1. `venv` sanal ortamı yoksa oluşturur (yalnızca ilk çalıştırmada),
2. tüm bağımlılıkların yüklü ve güncel olduğunu kontrol eder,
3. `.env` yoksa `.env.example` dosyasından oluşturur,
4. Streamlit'in ilk çalıştırmadaki e-posta sorusunu atlar,
5. `streamlit run app.py` komutunu çalıştırır ve uygulama **http://localhost:8501** adresinde açılır.

**Windows'ta**

1. Python 3.10 – 3.14 (3.12 veya 3.13 önerilir)nin kurulu olduğundan emin olun (kurulumda **Add Python to PATH** seçeneğini işaretleyin).
2. Proje klasörünü açın ve **`Run (Windows).bat` dosyasına çift tıklayın**.
3. Siyah bir Komut İstemi penceresi açılır. İlk açılış paketler yüklenirken birkaç dakika sürer; sonrakiler birkaç saniye.
4. Uygulama hazır olunca tarayıcınız açılır. Açılmazsa **http://localhost:8501** adresini kendiniz açın.

**macOS / Linux'ta:** proje klasöründe bir terminal açıp `bash "Run (Mac).sh"` komutunu çalıştırın.

> **Bilmekte fayda var**
> - Uygulamayı kullanırken siyah pencereyi açık tutun. Kapatmak (veya `Ctrl + C`) uygulamayı durdurur.
> - *No supported Python found* mesajını görürseniz Python 3.12 veya 3.13 kurup **Add Python to PATH** seçeneğini işaretleyin.
> - Gemini API anahtarınızı uygulamada (kenar çubuğundaki **Ayarlar**) veya `.env` dosyasında (`GEMINI_API_KEY=...`) girin.
> - Terminali mi tercih ediyorsunuz? Yöntem 2'deki elle komutlar aynı şekilde çalışır.

<a id="api-key"></a>

### 🔑 Ücretsiz Gemini API anahtarı alma

1. <https://aistudio.google.com/api-keys> adresine gidin.
2. Google hesabınızla (`@gmail.com`) giriş yapın. Hesabınız yoksa bir hesap oluşturmanız istenir.
3. **API anahtarı oluştur** (**Create API key**) seçeneğine tıklayın.
4. Anahtar için bir ad girin ve **Create key**'e tıklayın.
5. **Key** sütununun altındaki ada tıklayın, anahtarı kopyalayın ve `.env` dosyasına (`GEMINI_API_KEY=...`) veya uygulamanın kenar çubuğundaki alana yapıştırın.

> Site içe aktarma sekmesi **API anahtarı olmadan** çalışır.
>
> Uygulamada anahtar alanının altındaki **Ücretsiz API anahtarı al ↗** düğmesi yukarıdaki sayfayı açar. **Anahtarı bu bilgisayarda hatırla** işaretliyken (varsayılan) anahtar yerel `.env` dosyasına kaydedilir; yenileme veya yeniden başlatmadan sonra tekrar yazmanız gerekmez. Anahtar yalnızca uygulama `localhost` üzerinden açıldığında diske yazılır; sunucuda tarayıcı oturumunda kalır.

<a id="configuration"></a>

### ⚙️ Yapılandırma

| Değişken | Varsayılan | Açıklama |
|---|---|---|
| `GEMINI_API_KEY` | yok | Google AI Studio anahtarınız (veya kenar çubuğuna yazın). |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Ana model. Kenar çubuğundan da değiştirilebilir. |
| `GEMINI_FALLBACK_MODEL` | `gemini-2.5-flash-lite` | Ana model aşırı yüklenince veya kota dolunca otomatik kullanılır. |
| `DARA_SAVE_KEY` | otomatik | `1` kenar çubuğunun anahtarı her zaman `.env` dosyasına kaydetmesine izin verir, `0` asla vermez. Varsayılan olarak yalnızca uygulama `localhost` üzerinden açıldığında izin verilir (herkese açık sunucuda asla). |

<a id="usage"></a>

## 🧭 Kullanım

1. Kenar çubuğunda **Ayarlar**'ı açıp dilinizi, uyruğunuzu, Gemini modelinizi ve API anahtarınızı seçin (her şeyi görmek için *Herhangi biri* uyruğunu seçin). Kenar çubuğu menüsüyle **Burs ara** ve **Kayıtlı sonuçlar** arasında geçiş yapın. Anahtarınız, diliniz, uyruğunuz ve modeliniz oturumlar arasında hatırlanır.
2. **Bursları toplayın**
   - *Web sitelerinden içe aktar*: kaynakları seçin, en fazla sayfa sayısını belirleyin ve **İçe aktar**'a tıklayın. Dilediğiniz zaman yeniden çalıştırın: yeni burslar eklenir, değişen son tarihler güncellenir ve tekrarlar birleştirilir.
   - *Yapay zekâ web araması*: düzey, ülkeler (boş = hepsi), alan ve finansmanı seçip **Yapay zekâ ile burs ara**'ya tıklayın. Zaten kaydettiğiniz burslar atlanır, böylece yeni sonuçlar alırsınız; birkaç sitede bulunan burs tek kayıtta birleştirilir.
3. **Göz atın ve filtreleyin**: düzey sekmelerini ve filtreleri kullanın. Uygunluğu bilinmeyen kayıtlar, fırsat kaçırmamanız için tutulur.
4. **Yapay zekâ ile zenginleştirin** (isteğe bağlı): Gemini'nin finansman veya uyruk bilgisi eksik sonuçların sayfalarını okumasına izin verin.
5. **CSV olarak dışa aktarın** ve başvurmadan önce her son tarihi resmî sayfada doğrulayın.

<a id="sources"></a>

## 🌐 Desteklenen kaynaklar

| Kaynak | İçerik |
|---|---|
| Scholars4Dev | Uluslararası burslar (tüm düzeyler) |
| ScholarshipTab | Yüksek lisans, Doktora, MBA, Lisans, Lisansüstü, Fellowship, Tam burslu |
| ScholarshipSet (Afrika) | Yüksek lisans, Doktora, Lisans |
| GermanyScholarships · UKScholarships · ScholarshipCA · UScholarships · ScholarshipAU | Ülkeye özel burslar |
| Özel URL | Uyumlu düzene sahip herhangi bir kategori sayfası |
| Gemini + Google Search | Açık web'deki diğer her şey |

> Bazı siteler otomatik erişimi reddedebilir (HTTP 403). Uygulama bunları açık bir mesajla atlar; bunun yerine yapay zekâ arama sekmesini kullanın.

<a id="project-structure"></a>

## 🗂️ Proje yapısı

```text
scholarship-agent/
├── Run (Windows).bat / Run (Mac).sh    # tek tıkla başlatıcı (Windows / macOS-Linux)
├── app.py              # Streamlit arayüzü, filtreler, dil ve RTL yönetimi
├── agent.py            # Gemini ajanı: web araması, zenginleştirme, yeniden deneme ve yedek model
├── sources.py          # Site tarayıcıları (yapay zekâsız) ve tarih/düzey ayrıştırma
├── db.py               # Yerel SQLite depolama, tekrar birleştirme ve filtre yardımcıları
├── storage.py          # ayarları (settings.json) ve API anahtarını (.env) yerel olarak kaydeder
├── i18n.py             # EN / FA / TR / AR çevirileri
├── countries.py        # ülke adı -> simge yapı görseli (SVG veya kendi fotoğrafınız)
├── assets/countries/   # simge yapı illüstrasyonları (de.svg, fr.svg, ...) + isteğe bağlı fotoğraflar
├── tools/make_country_art.py  # SVG illüstrasyonlarını yeniden üretir
├── static/             # Farsça ve Arapça için IRANSansX yazı tipleri
├── docs/screenshots/   # README görselleri
├── requirements.txt
├── .env.example
├── CHANGELOG.md        # sürüm geçmişi
└── LICENSE
```

<a id="country-images"></a>

## 🖼️ Ülke görselleri

Her burs kartı, hedef ülkenin ünlü bir simge yapısının görselini gösterir (Eyfel Kulesi, Big Ben, Brandenburg Kapısı, Sidney Opera Binası, Fuji Dağı ve daha fazlası). Belirli bir ülkesi olmayan burslar dünya küresi alır.

Paketle gelen illüstrasyonlar yerine **kendi fotoğraflarınızı** kullanmak için iki harfli ülke koduyla adlandırılmış dosyayı `assets/countries/` klasörüne bırakın:

```text
assets/countries/de.jpg     # Almanya
assets/countries/gb.webp    # Birleşik Krallık
assets/countries/us.png     # ABD
```

Desteklenen biçimler: `.jpg`, `.png`, `.webp` (fotoğraf her zaman `.svg` dosyasına üstün gelir). Yalnızca size ait veya yeniden kullanım lisanslı görselleri kullanın. Değişikliği görmek için uygulamayı yeniden başlatın. Yeni bir ülke eklemek için adlarını `countries.py` içindeki `NAMES` sözlüğüne ekleyin ve aynı klasöre `<kod>.jpg` (veya `.svg`) koyun.

<a id="deploy"></a>

## ☁️ Çevrimiçi yayın

GitHub kodunuzu saklar; Streamlit uygulamalarını çalıştırmaz. Uygulamayı çevrimiçi sunmak için:

- **Streamlit Community Cloud (ücretsiz):** depoyu GitHub'a gönderin, <share.streamlit.io> adresini açın, **Create app**'e tıklayın, depoyu, `main` dalını ve `app.py` dosyasını seçip **Deploy** edin.
  Herkese açık bir uygulamada kendi API anahtarınızı *Secrets* içine **koymayın** (herkes kotanızı harcayabilir); boş bırakın ki her ziyaretçi kendi anahtarını kenar çubuğuna girsin. Uygulama yeniden başlayınca kayıtlı sonuçlar sıfırlanır. Sunucuda kenar çubuğu anahtarı asla diske yazmaz (bkz. `DARA_SAVE_KEY`).
- **Kendi sunucunuz (VPS):** `pip install -r requirements.txt`, ardından Nginx/Caddy arkasında HTTPS ile `streamlit run app.py --server.port 8501 --server.address 0.0.0.0` çalıştırın.

<a id="troubleshooting"></a>

## 🛠️ Sorun giderme

| Sorun | Anlamı ve çözüm |
|---|---|
| `429` / `RESOURCE_EXHAUSTED` | Kota veya hız sınırı doldu. Uygulama yedek modele geçer; turları azaltın (*Derin arama*'yı kapatın), bir dakika bekleyin veya faturalandırmayı etkinleştirin. |
| `503 UNAVAILABLE` | Model aşırı yüklü. Uygulama otomatik yeniden dener (3, 6, 12, 24 sn) ve ardından yedek modeli kullanır. |
| Bir site için `403 Forbidden` | O site otomatik erişimi engelliyor. Başka bir kaynak veya yapay zekâ arama sekmesini kullanın. |
| `ERROR: Could not open requirements file ... 'requirements.txt'` | Başlatıcı proje dosyalarının yanında değil (örneğin ZIP'in içinden çalıştırıldı veya klasörden çıkarıldı). ZIP'in **tamamını** çıkarın (sağ tık, *Tümünü ayıkla*) ve başlatıcıyı çıkarılan proje klasörünün içinden çalıştırın. Deponuzda `requirements.txt` dosyasının olduğunu da kontrol edin. Yeni başlatıcı bunu açık bir mesajla gösterir. |
| `Microsoft Visual C++ 14.0 or greater is required` / `Failed building wheel` (pyarrow, pyyaml) | Python sürümünüz çok yeni (örneğin 3.15) ve bazı paketlerin hazır sürümü yok. Python 3.12 veya 3.13 kurun, `venv` klasörünü silin ve `Run (Windows).bat` dosyasını yeniden çalıştırın; başlatıcı desteklenen bir Python'u otomatik seçer. |
| `'streamlit' is not recognized` | Bağımlılıklar yüklenemedi. Üstteki hatayı (yukarıdaki satırlara bakın) giderin, sonra başlatıcıyı yeniden çalıştırın. |
| API anahtarı hatırlanmıyor | Kaydetme yalnızca uygulama bu bilgisayarda (`localhost`) açıldığında ve *Anahtarı bu bilgisayarda hatırla* işaretliyken çalışır. Anahtarı kendiniz `.env` dosyasına yazabilir veya `DARA_SAVE_KEY=1` ayarlayabilirsiniz. |
| Aynı burs iki kez görünüyor | Tekrarlar her içe aktarmada, yapay zekâ aramasında ve uygulama açılışında otomatik birleştirilir. Hâlâ iki kayıt görünüyorsa başlıkları çok farklıdır ve farklı burslar sayılırlar. |
| Farsça yazı tipi uygulanmıyor | `static/Sans-Regular.woff2` ve `static/Sans-Bold.woff2` dosyalarını `app.py` ile aynı yerde tutun ve uygulamayı yeniden başlatın. |
| Yapay zekâ az sonuç veriyor | Gemini bir tarayıcı değildir. Hacim için site içe aktarmayı, keşif için yapay zekâ aramasını kullanın. |

<a id="responsible-use"></a>

## ⚠️ Sorumlu kullanım ve uyarı

- Burs bilgileri eksik veya güncel olmayabilir ve yapay zekâ hata yapabilir. **Son tarihleri, uygunluğu ve şartları her zaman resmî sayfada doğrulayın.**
- Tarayıcılar hafif ve kişisel kullanım içindir. Her sitenin kullanım koşullarına ve `robots.txt` dosyasına saygı gösterin, sayfa sınırlarını makul tutun.
- `static/` içindeki yazı tipi dosyaları *IRANSansX*'tir; bir fork'u yeniden dağıtmadan önce lisansını kontrol edin. Dosyalar yoksa uygulama Tahoma'ya döner.

<a id="roadmap"></a>

## 🗺️ Yol haritası

- [ ] Daha fazla burs kaynağı; DAAD, Chevening, Fulbright için resmî site bağlayıcıları
- [ ] E-posta / WhatsApp / Telegram ile son tarih hatırlatmaları
- [ ] Kayıtlı aramalar ve favoriler
- [ ] Docker imajı ve tek tıkla yayın

<a id="changelog"></a>

## 📋 Değişiklik günlüğü

Tüm önemli değişiklikler [CHANGELOG.md](CHANGELOG.md) dosyasında belgelenmiştir.
Son sürüm **v0.6.0**: API anahtarı ve ayarlar hatırlanıyor, tekrar eden burslar birleştiriliyor ve yeniden içe aktarma listeyi güncelliyor.

<a id="contributing"></a>

## 🤝 Katkıda bulunma

Issue ve pull request'ler memnuniyetle karşılanır. Büyük değişiklikler için önce bir issue açın, kodu düzenli tutun ve arayüzdeki yeni metinlerin çevirilerini `i18n.py` içinde dört dile de ekleyin.

<a id="license"></a>

## 📄 Lisans

[MIT Lisansı](LICENSE) ile yayımlanmıştır.

<a id="author"></a>

## 👤 Geliştirici ve destek

**Daniel Dara** tarafından geliştirildi; web geliştirici ve yapay zekâ otomasyonu üreticisi.

- 🌐 Web sitesi: [danieldara.com](https://danieldara.com)

Bu proje işinize yaradıysa GitHub'da bir ⭐ verin.
