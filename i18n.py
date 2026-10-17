"""UI translations: English, Persian (fa), Turkish (tr), Arabic (ar)."""
LANGS = {"en": "English", "fa": "فارسی", "tr": "Türkçe", "ar": "العربية"}
AI_LANG = {"en": "English", "fa": "Persian (Farsi)", "tr": "Turkish", "ar": "Arabic"}
RTL = {"fa", "ar"}


def _t(en, fa, tr, ar):
    return {"en": en, "fa": fa, "tr": tr, "ar": ar}


TEXT = {
    "title": _t("🎓 Scholarship Agent", "🎓 ایجنت بورسیه تحصیلی", "🎓 Burs Ajanı", "🎓 وكيل المنح الدراسية"),
    "settings": _t("⚙️ Settings", "⚙️ تنظیمات", "⚙️ Ayarlar", "⚙️ الإعدادات"),
    "api_key": _t("Gemini API key", "کلید API جمینای", "Gemini API anahtarı", "مفتاح Gemini API"),
    "api_key_help": _t(
        "**How to get a Gemini API key**\n\n"
        "1. Go to [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys)\n"
        "2. Sign in with your Google account (@gmail.com). If you don't have one, you will be asked to create one.\n"
        "3. Click **Create API key**.\n"
        "4. In the window that opens, enter a name for your key and click **Create key**.\n"
        "5. After it is created, click the name shown under the **Key** column, copy your API key "
        "and paste it into this box.",
        "**مراحل دریافت کلید API**\n\n"
        "1. به آدرس [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys) مراجعه کنید.\n"
        "2. با اکانت ایمیل خود (@gmail.com) وارد شوید؛ اگر اکانت ندارید، از شما خواسته می‌شود یک اکانت بسازید.\n"
        "3. روی گزینه «ایجاد کلید API» یا **Create API key** کلیک کنید.\n"
        "4. در پنجره باز شده یک نام برای کلید خود وارد کنید و روی **Create key** بزنید.\n"
        "5. بعد از ایجاد، روی نامی که زیر بخش **Key** نوشته شده کلیک کنید، کلید API خود را کپی کنید "
        "و در همین کادر وارد کنید.",
        "**Gemini API anahtarı nasıl alınır**\n\n"
        "1. [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys) adresine gidin.\n"
        "2. Google hesabınızla (@gmail.com) giriş yapın. Hesabınız yoksa bir hesap oluşturmanız istenir.\n"
        "3. **API anahtarı oluştur** (**Create API key**) seçeneğine tıklayın.\n"
        "4. Açılan pencerede anahtarınız için bir ad girin ve **Create key**'e tıklayın.\n"
        "5. Oluşturulduktan sonra **Key** bölümünün altında yazan ada tıklayın, API anahtarınızı kopyalayın "
        "ve bu kutuya yapıştırın.",
        "**كيفية الحصول على مفتاح Gemini API**\n\n"
        "1. افتح الرابط [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys)\n"
        "2. سجّل الدخول بحساب Google الخاص بك (@gmail.com). إذا لم يكن لديك حساب فسيُطلب منك إنشاء حساب.\n"
        "3. انقر على **إنشاء مفتاح API** (**Create API key**).\n"
        "4. في النافذة التي تظهر، أدخل اسمًا لمفتاحك ثم انقر على **Create key**.\n"
        "5. بعد الإنشاء، انقر على الاسم المكتوب تحت عمود **Key**، وانسخ مفتاح API والصقه في هذا المربع."),
    "nationality": _t("Your nationality", "ملیت شما", "Uyruğunuz", "جنسيتك"),
    "nat_any": _t("Any (open to all)", "همه (باز برای همه)", "Herhangi biri (herkese açık)", "أي جنسية (مفتوح للجميع)"),
    "nat_other": _t("Other…", "سایر…", "Diğer…", "أخرى…"),
    "nat_type": _t("Type your nationality", "ملیت خود را بنویسید", "Uyruğunuzu yazın", "اكتب جنسيتك"),
    "model": _t("Gemini model", "مدل جمینای", "Gemini modeli", "نموذج Gemini"),
    "fallback": _t("Fallback if overloaded: {m}", "مدل جایگزین در صورت شلوغی: {m}",
                   "Aşırı yüklenirse yedek model: {m}", "النموذج البديل عند الضغط: {m}"),
    "clear": _t("🗑️ Clear saved results", "🗑️ پاک کردن نتایج ذخیره‌شده", "🗑️ Kayıtlı sonuçları temizle", "🗑️ مسح النتائج المحفوظة"),
    "sec1": _t("1) Collect scholarships", "۱) جمع‌آوری بورسیه‌ها", "1) Bursları topla", "1) جمع المنح"),
    "tab_import": _t("📚 Import from websites (fast, 100+)", "📚 دریافت از وب‌سایت‌ها (سریع، بیش از ۱۰۰ مورد)",
                     "📚 Web sitelerinden içe aktar (hızlı, 100+)", "📚 الاستيراد من المواقع (سريع، 100+)"),
    "tab_ai": _t("🤖 AI web search (Gemini)", "🤖 جستجوی هوشمند وب (جمینای)",
                 "🤖 Yapay zekâ web araması (Gemini)", "🤖 بحث ذكي على الويب (Gemini)"),
    "import_caption": _t("Reads the listing pages of scholarship websites directly. No API key needed.",
                         "صفحات لیست وب‌سایت‌های بورسیه را مستقیم می‌خواند. نیازی به API key نیست.",
                         "Burs sitelerinin liste sayfalarını doğrudan okur. API anahtarı gerekmez.",
                         "يقرأ صفحات القوائم في مواقع المنح مباشرة. لا يحتاج إلى مفتاح API."),
    "sources": _t("Websites", "وب‌سایت‌ها", "Web siteleri", "المواقع"),
    "pages": _t("Max pages per website (~10-20 scholarships per page)",
                "حداکثر تعداد صفحه برای هر وب‌سایت (هر صفحه حدود ۱۰ تا ۲۰ بورسیه)",
                "Web sitesi başına en fazla sayfa (sayfa başına ~10-20 burs)",
                "الحد الأقصى للصفحات لكل موقع (~10-20 منحة لكل صفحة)"),
    "custom_url": _t("Custom URL (optional): a category page of a site with the same layout",
                     "آدرس دلخواه (اختیاری): صفحه دسته‌بندی یک سایت با ساختار مشابه",
                     "Özel URL (isteğe bağlı): aynı düzene sahip bir sitenin kategori sayfası",
                     "رابط مخصص (اختياري): صفحة تصنيف لموقع بنفس البنية"),
    "import_btn": _t("📥 Import", "📥 دریافت", "📥 İçe aktar", "📥 استيراد"),
    "no_site": _t("Select at least one website.", "حداقل یک وب‌سایت انتخاب کنید.",
                  "En az bir web sitesi seçin.", "اختر موقعًا واحدًا على الأقل."),
    "importing": _t("Reading websites…", "در حال خواندن وب‌سایت‌ها…", "Web siteleri okunuyor…", "جارٍ قراءة المواقع…"),
    "page_progress": _t("{site}: page {p}/{t} — {n} so far", "{site}: صفحه {p}/{t} — تا اینجا {n} مورد",
                        "{site}: sayfa {p}/{t} — şu ana kadar {n}", "{site}: الصفحة {p}/{t} — {n} حتى الآن"),
    "site_failed": _t("⚠️ {site} failed: {e}", "⚠️ {site} ناموفق بود: {e}", "⚠️ {site} başarısız: {e}", "⚠️ فشل {site}: {e}"),
    "imported": _t("Imported {n} scholarships", "{n} بورسیه دریافت شد", "{n} burs içe aktarıldı", "تم استيراد {n} منحة"),
    "ai_caption": _t("Leave **Destination countries** empty to search ALL countries (one search pass per world region).",
                     "فیلد **کشورهای مقصد** را خالی بگذارید تا در همه کشورها جستجو شود (برای هر منطقه جهان یک مرحله جستجو).",
                     "**Hedef ülkeler** boşsa TÜM ülkelerde aranır (her dünya bölgesi için bir arama turu).",
                     "اترك **الدول المستهدفة** فارغًا للبحث في جميع الدول (جولة بحث لكل منطقة في العالم)."),
    "level": _t("Education level", "مقطع تحصیلی", "Eğitim düzeyi", "المستوى الدراسي"),
    "countries": _t("Destination countries (comma separated, empty = all)",
                    "کشورهای مقصد (با کاما جدا کنید، خالی = همه)",
                    "Hedef ülkeler (virgülle ayırın, boş = hepsi)", "الدول المستهدفة (مفصولة بفاصلة، فارغ = الكل)"),
    "field": _t("Field of study (empty = any)", "رشته تحصیلی (خالی = هر رشته)", "Alan (boş = herhangi)", "التخصص (فارغ = أي تخصص)"),
    "funding": _t("Funding", "نوع تأمین مالی", "Finansman", "التمويل"),
    "deep": _t("Deep search (more passes = more results, slower)", "جستجوی عمیق (مراحل بیشتر = نتایج بیشتر، کندتر)",
               "Derin arama (daha fazla tur = daha çok sonuç, daha yavaş)", "بحث عميق (جولات أكثر = نتائج أكثر، أبطأ)"),
    "find_btn": _t("🔎 Find scholarships with AI", "🔎 جستجوی بورسیه با هوش مصنوعی",
                   "🔎 Yapay zekâ ile burs ara", "🔎 ابحث عن المنح بالذكاء الاصطناعي"),
    "enter_key": _t("Enter your Gemini API key in the sidebar.", "کلید API جمینای را در نوار کناری وارد کنید.",
                    "Kenar çubuğuna Gemini API anahtarınızı girin.", "أدخل مفتاح Gemini API في الشريط الجانبي."),
    "searching": _t("Searching the web with Gemini…", "در حال جستجوی وب با جمینای…",
                    "Gemini ile web'de aranıyor…", "جارٍ البحث على الويب عبر Gemini…"),
    "found_saved": _t("{n} scholarships found and saved", "{n} بورسیه پیدا و ذخیره شد",
                      "{n} burs bulundu ve kaydedildi", "تم العثور على {n} منحة وحفظها"),
    "search_failed": _t("Search failed", "جستجو ناموفق بود", "Arama başarısız", "فشل البحث"),
    "error": _t("Error: {e}", "خطا: {e}", "Hata: {e}", "خطأ: {e}"),
    "sec2": _t("2) Browse & filter saved results", "۲) مرور و فیلتر نتایج ذخیره‌شده",
               "2) Kayıtlı sonuçlara göz at ve filtrele", "2) تصفح النتائج المحفوظة وتصفيتها"),
    "nothing": _t("Nothing saved yet. Import or search first.", "هنوز چیزی ذخیره نشده. ابتدا دریافت یا جستجو کنید.",
                  "Henüz kayıt yok. Önce içe aktarın veya arama yapın.", "لا يوجد شيء محفوظ بعد. استورد أو ابحث أولاً."),
    "f_level": _t("Level", "مقطع", "Düzey", "المستوى"),
    "f_country": _t("Country", "کشور", "Ülke", "الدولة"),
    "f_funding": _t("Funding", "تأمین مالی", "Finansman", "التمويل"),
    "f_keyword": _t("Field / keyword", "رشته / کلیدواژه", "Alan / anahtar kelime", "التخصص / كلمة مفتاحية"),
    "hide_expired": _t("Hide expired", "پنهان کردن منقضی‌شده‌ها", "Süresi dolanları gizle", "إخفاء المنتهية"),
    "only_nat": _t("Only eligible for: {nat} (unknown rules are kept)",
                   "فقط واجد شرایط برای: {nat} (موارد نامشخص نگه داشته می‌شوند)",
                   "Yalnızca uygun olanlar: {nat} (belirsiz kurallar korunur)",
                   "المؤهلة فقط لـ: {nat} (يتم الاحتفاظ بالقواعد غير المعروفة)"),
    "results_count": _t("**{n}** results (of {total} saved)", "**{n}** نتیجه (از {total} مورد ذخیره‌شده)",
                        "**{n}** sonuç (kayıtlı {total} içinden)", "**{n}** نتيجة (من أصل {total} محفوظة)"),
    "enrich_exp": _t("✨ {n} shown results lack funding / nationality info — enrich with AI",
                     "✨ {n} نتیجه نمایش‌داده‌شده اطلاعات تأمین مالی / ملیت ندارند — تکمیل با هوش مصنوعی",
                     "✨ Gösterilen {n} sonuçta finansman / uyruk bilgisi yok — yapay zekâ ile tamamla",
                     "✨ {n} نتيجة معروضة تفتقر لمعلومات التمويل / الجنسية — أكملها بالذكاء الاصطناعي"),
    "enrich_howmany": _t("How many to enrich now", "چند مورد الان تکمیل شود", "Şimdi kaç tanesi tamamlansın", "كم عنصرًا يتم إكماله الآن"),
    "enrich_btn": _t("Read their pages with Gemini", "خواندن صفحه‌هایشان با جمینای",
                     "Sayfalarını Gemini ile oku", "قراءة صفحاتها بواسطة Gemini"),
    "enrich_status": _t("Reading scholarship pages…", "در حال خواندن صفحه‌های بورسیه…",
                        "Burs sayfaları okunuyor…", "جارٍ قراءة صفحات المنح…"),
    "enriched": _t("Enriched {n} scholarships", "{n} بورسیه تکمیل شد", "{n} burs tamamlandı", "تم إكمال {n} منحة"),
    "failed": _t("Failed", "ناموفق", "Başarısız", "فشل"),
    "official": _t("Official page", "صفحه رسمی", "Resmî sayfa", "الصفحة الرسمية"),
    "university": _t("University", "دانشگاه", "Üniversite", "الجامعة"),
    "fields": _t("Fields", "رشته‌ها", "Alanlar", "التخصصات"),
    "amount": _t("Amount", "مبلغ", "Tutar", "المبلغ"),
    "deadline": _t("Deadline", "مهلت", "Son tarih", "الموعد النهائي"),
    "eligible": _t("Eligible", "واجدین شرایط", "Uygun olanlar", "المؤهلون"),
    "language": _t("Language", "زبان", "Dil", "اللغة"),
    "source": _t("Source", "منبع", "Kaynak", "المصدر"),
    "unknown": _t("unknown", "نامشخص", "bilinmiyor", "غير معروف"),
    "export": _t("⬇️ Export CSV", "⬇️ خروجی CSV", "⬇️ CSV olarak indir", "⬇️ تصدير CSV"),
    "verify": _t("⚠️ Always verify deadlines and eligibility on the official page.",
                 "⚠️ مهلت‌ها و شرایط را همیشه در صفحه رسمی بررسی کنید.",
                 "⚠️ Son tarihleri ve uygunluk koşullarını her zaman resmî sayfada doğrulayın.",
                 "⚠️ تحقق دائمًا من المواعيد والشروط في الصفحة الرسمية."),
    "footer_website": _t("Website", "وب‌سایت", "Web sitesi", "الموقع"),
    "footer_support": _t("Support", "پشتیبانی", "Destek", "الدعم"),
    "app_name": _t("Dara Scholarship Agent", "ایجنت بورسیه تحصیلی دارا", "Dara Burs Ajanı", "وكيل دارا للمنح الدراسية"),
    "site_blocked": _t(
        "🚫 {site}: the website refused automated access (HTTP {code}) — skipped. "
        "Try the AI search tab or open the site manually.",
        "🚫 {site}: وب‌سایت دسترسی خودکار را رد کرد (HTTP {code}) — رد شد. "
        "از تب جستجوی هوشمند استفاده کنید یا سایت را دستی باز کنید.",
        "🚫 {site}: web sitesi otomatik erişimi reddetti (HTTP {code}) — atlandı. "
        "Yapay zekâ arama sekmesini deneyin veya siteyi elle açın.",
        "🚫 {site}: رفض الموقع الوصول الآلي (HTTP {code}) — تم تخطيه. "
        "جرّب تبويب البحث الذكي أو افتح الموقع يدويًا."),
    'nav_search': _t('Search scholarships', 'جستجوی بورسیه', 'Burs ara', 'البحث عن منح'),
    'nav_saved': _t('Saved results', 'نتایج ذخیره\u200cشده', 'Kayıtlı sonuçlar', 'النتائج المحفوظة'),
    'tagline': _t('Find global scholarship opportunities with the power of AI', 'فرصت\u200cهای بورسیه جهانی را با قدرت هوش مصنوعی پیدا کنید', 'Yapay zekânın gücüyle küresel burs fırsatlarını bulun', 'اكتشف فرص المنح الدراسية العالمية بقوة الذكاء الاصطناعي'),
    'hero_a': _t('Dara ', 'ایجنت ', 'Dara ', 'وكيل دارا '),
    'hero_accent': _t('Scholarship', 'بورسیه تحصیلی', 'Burs', 'للمنح'),
    'hero_b': _t(' Agent', ' دارا', ' Ajanı', ' الدراسية'),
    'feat1_t': _t('Discover', 'کشف', 'Keşfet', 'اكتشف'),
    'feat1_d': _t('Scholarships worldwide', 'بورسیه\u200cهای سراسر جهان', 'Dünya çapında burslar', 'منح من حول العالم'),
    'feat2_t': _t('AI-Powered', 'مبتنی بر هوش مصنوعی', 'Yapay zekâ destekli', 'مدعوم بالذكاء الاصطناعي'),
    'feat2_d': _t('Smart search & matching', 'جستجو و تطبیق هوشمند', 'Akıllı arama ve eşleştirme', 'بحث ومطابقة ذكية'),
    'feat3_t': _t('Filter easily', 'فیلتر آسان', 'Kolay filtre', 'تصفية سهلة'),
    'feat3_d': _t('Find what fits you', 'آنچه به شما می\u200cخورد را پیدا کنید', 'Size uyanı bulun', 'اعثر على ما يناسبك'),
    'feat4_t': _t('Study anywhere', 'تحصیل در هر کجا', 'Her yerde oku', 'ادرس في أي مكان'),
    'feat4_d': _t('Turn your dreams into reality', 'رویاهایتان را به واقعیت تبدیل کنید', 'Hayallerinizi gerçeğe dönüştürün', 'حوّل أحلامك إلى حقيقة'),
    'stat_sch': _t('Scholarships', 'بورسیه', 'Burs', 'منحة'),
    'stat_cnt': _t('Countries', 'کشور', 'Ülke', 'دولة'),
    'stat_lvl': _t('Levels', 'مقطع', 'Düzey', 'مستوى'),
    'quote_a': _t('Education has no borders.', 'آموزش مرز نمی\u200cشناسد.', 'Eğitimin sınırı yoktur.', 'التعليم بلا حدود.'),
    'quote_b': _t('A brighter future is within your reach.', 'آینده\u200cای روشن\u200cتر در دسترس شماست.', 'Daha parlak bir gelecek ulaşabileceğiniz yerde.', 'مستقبل أكثر إشراقًا في متناول يدك.'),
    'load_more': _t('Show more', 'نمایش بیشتر', 'Daha fazla göster', 'عرض المزيد'),
    'no_results': _t('No scholarships match these filters.', 'بورسیه\u200cای با این فیلترها پیدا نشد.', 'Bu filtrelerle eşleşen burs yok.', 'لا توجد منح مطابقة لهذه المرشحات.'),
    'chip_Full': _t('Full funding', 'تأمین مالی کامل', 'Tam burs', 'تمويل كامل'),
    'chip_Partial': _t('Partial funding', 'تأمین مالی بخشی', 'Kısmi burs', 'تمويل جزئي'),
    'chip_Tuition only': _t('Tuition only', 'فقط شهریه', 'Yalnızca harç', 'الرسوم الدراسية فقط'),
    'chip_Unknown': _t('Funding: unknown', 'تأمین مالی: نامشخص', 'Finansman: bilinmiyor', 'التمويل: غير معروف'),
    'get_key': _t('Get a free API key ↗', 'دریافت کلید API رایگان ↗', 'Ücretsiz API anahtarı al ↗', 'احصل على مفتاح API مجاني ↗'),
    'key_remember': _t('Remember the key on this computer', 'ذخیره کلید روی این کامپیوتر', 'Anahtarı bu bilgisayarda hatırla', 'تذكّر المفتاح على هذا الكمبيوتر'),
    'key_saved': _t('API key saved to .env on this computer', 'کلید API در فایل .env همین کامپیوتر ذخیره شد', 'API anahtarı bu bilgisayardaki .env dosyasına kaydedildi', 'تم حفظ مفتاح API في ملف .env على هذا الكمبيوتر'),
    'key_forget': _t('Forget saved key', 'حذف کلید ذخیره\u200cشده', 'Kayıtlı anahtarı unut', 'حذف المفتاح المحفوظ'),
    'key_session_only': _t('Server mode: the key is kept only for this browser session and is never written to disk.', 'حالت سرور: کلید فقط برای همین نشست مرورگر نگه داشته می\u200cشود و روی دیسک ذخیره نمی\u200cشود.', 'Sunucu modu: anahtar yalnızca bu tarayıcı oturumu için tutulur ve diske yazılmaz.', 'وضع الخادم: يُحفظ المفتاح لهذه الجلسة فقط ولا يُكتب على القرص.'),
    'save_stats': _t('{n} processed: {added} new, {updated} updated, {same} already up to date', '{n} مورد بررسی شد: {added} جدید، {updated} به\u200cروزرسانی\u200cشده، {same} بدون تغییر', '{n} işlendi: {added} yeni, {updated} güncellendi, {same} zaten güncel', 'تمت معالجة {n}: {added} جديدة، {updated} محدّثة، {same} دون تغيير'),
    'badge_new': _t('NEW', 'جدید', 'YENİ', 'جديد'),
    # level / funding labels
    "lvl_Bachelor": _t("Bachelor", "لیسانس", "Lisans", "البكالوريوس"),
    "lvl_Master": _t("Master", "ارشد", "Yüksek lisans", "الماجستير"),
    "lvl_PhD": _t("PhD", "دکتری", "Doktora", "الدكتوراه"),
    "lvl_Postdoc": _t("Postdoc", "پسادکتری", "Doktora sonrası", "ما بعد الدكتوراه"),
    "lvl_Other": _t("Other", "سایر", "Diğer", "أخرى"),
    "fund_Any": _t("Any", "هر کدام", "Herhangi", "أي"),
    "fund_Full": _t("Full", "کامل", "Tam", "كامل"),
    "fund_Partial": _t("Partial", "بخشی", "Kısmi", "جزئي"),
    "fund_Tuition only": _t("Tuition only", "فقط شهریه", "Yalnızca harç", "الرسوم الدراسية فقط"),
    "fund_Unknown": _t("Unknown", "نامشخص", "Bilinmiyor", "غير معروف"),
}


def tr(lang, key, **kw):
    s = TEXT[key].get(lang) or TEXT[key]["en"]
    return s.format(**kw) if kw else s


def label(lang, prefix, value):
    key = f"{prefix}_{value}"
    return tr(lang, key) if key in TEXT else value
