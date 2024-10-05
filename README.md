### Web Scraping Project - E-Shop Data Extraction

**Aktualizováno 17.9.:**  
Věnujte prosím pozornost parametrům vytvářené datové sady níže (minimální počet produktů a jejich parametrů). Vytvořená datová sada bude následně využita v projektu 3 pro analýzu. Proto jsme počty mírně navýšili.

#### Cíle projektu:
- Vyzkoušet si využití webových stránek jako zdroje dat, konkrétně pro automatizované získávání:
  - Odkazů (seznamu URL) z dynamických webových stránek.
  - Konkrétních informací z většího množství webových stránek.

#### Pokyny k řešení:
1. **Výběr e-shopu**: 
   [OK] - Zvolte si vhodný e-shop nabízející libovolné produkty (ideálně zahraniční).
   [OK] - Produkty musí mít uvedeny doplňující parametry (např. u telefonů model procesoru, u kol hmotnost apod.), ideálně ve formě tabulky.
   [OK] - Vyhněte se nejběžnějším e-shopům (Alza.cz, Amazon.com apod.), abyste minimalizovali riziko, že si stejný e-shop zvolí jiný tým.
   [OK] - Nesdělujte volbu e-shopu mimo tým, předejdete tak komplikacím způsobeným přílišným zatížením serverů e-shopu provozem z FIT.

2. **Implementace skriptů**:
   [OK] - Skript 1: Získá automatizovaně seznam URL alespoň 150 srovnatelných produktů dostupných na e-shopu.
   [OK]  - Zpracujte stránky věnované konkrétní kategorii produktů s alespoň některými společnými parametry.
   [OK] - Skript 2: Pro každý produkt získá z URL název produktu, aktuální cenu a hodnoty minimálně pěti doplňujících parametrů.
   [OK]  - Parametry by měly být společné pro většinu produktů, ale mějte na paměti, že některé hodnoty nemusí být vždy dostupné.
   [OK]  - Je ideální, pokud alespoň jeden parametr bude číselný a jeden kategorický.

3. **Formát výstupu**:
   [OK] - Výstup bude ve formátu TSV:
   [OK]  - Každý řádek bude obsahovat: URL produktu, název produktu, aktuální cenu a hodnoty jednotlivých parametrů, tedy minimálně 8 sloupců.
   [OK]  - Nevypisujte názvy sloupců (záhlaví) – jejich význam zdokumentujte v README.
   [OK]  - Hodnoty ukládejte jako řetězce ve formátu uvedeném na stránkách (bez normalizace jednotek).

4. **Technické požadavky**:
   [CHECK] - Řešení musí být spustitelné na serveru merlin. Pokud je server příliš omezující, domluvte si individuální výjimku do 6.10.
   [OK] - Skripty budou vypisovat výsledky na standardní výstup (stdout). Uložení výsledků do souborů se provádí přesměrováním při spuštění z příkazové řádky.
   [OK] - Můžete využít libovolnou implementační platformu (Python, JavaScript, Java, bash apod.), ale program musí běžet lokálně a nesmí využívat online služby třetích stran.
   [OK] - Využití volně dostupných knihoven (puppeteer, BeautifulSoup apod.) je povoleno.
   [OK] - Je možné zpracovávat jak HTML kód stránek, tak i vložená strukturovaná data (např. JSON-LD, RDFa apod.).

5. **Opakovatelnost**:
   [OK] - Skripty musí umožnit opakované spuštění s výsledkem odpovídajícím zadání (seznam produktů a parametry), i když výsledky mohou být pokaždé jiné (jiné produkty, změněné ceny apod.).

#### Způsob odevzdání (požadované výstupy):
[WIP] - **Výsledné řešení** odevzdá pouze vedoucí týmu prostřednictvím IS VUT jako jeden ZIP archiv, který bude obsahovat:
[OK]  1. `urls.txt`: Ukázkový výstup obsahující seznam URL (minimálně 150 řádků).
[CHECK]  2. `data.tsv`: Ukázkový výstup s informacemi o produktech ve formátu TSV, s minimálně 150 řádky.
[CHECK]  3. `get.py` & `extract.py` Implementaci obou skriptů (pro získání URL a pro extrakci dat o produktech).
[CHECK]  4. `build.sh`: Skript, který zajistí případný překlad, instalaci závislostí nebo další kroky nutné ke spuštění programu. Pokud není speciální příprava nutná, bude tento skript prázdný.
[CHECK]  5. `run.sh`: Testovací skript, který spustí skript pro získání seznamu URL, uloží je do souboru `url_test.txt` a následně pro prvních 10 URL z tohoto seznamu spustí druhý skript, který získá informace o produktech a vypíše je na standardní výstup (stdout).
[WIP]  6. `README`: Dokumentace obsahující:
     - Název týmu a seznam řešitelů.
     - URL a název e-shopu, který jste zvolili.
     - Význam sloupců ve výstupu TSV.
     - Případné poznámky, pokud je třeba něco speciálně vysvětlit.
  
[CHECK] - **Neposílejte** knihovny třetích stran, přeložený kód, adresáře se závislostmi (`node_modules` apod.), ani další soubory, které je možné získat automaticky sestavením projektu.

#### Poznámky:
- Chovejte se ohleduplně k cizím serverům a nezatěžujte je velkým množstvím dotazů.
  - Vyvíjejte a testujte na malém množství stránek nebo lokálně uložených kopiích HTML dokumentů.
  - Finální datovou sadu (150 produktů) není nutné získat naráz. Můžete spuštění rozdělit a spouštět s časovým odstupem.
