class God():
    def __init__(self, name, gender, description) -> None:
        self.name = name
        self.gender = gender
        self.description = description

    def __str__(self) -> str:
        return f"god/godess name:\n{self.name}\ngod/goddess description:\n{self.description}"


# list of viking gods (19)
thor = God("Thor", "M",
           ".. zvaný též Donor / Donar, je bohem hromu, blesku, války, plodnosti země, deště, počasí a je také ochráncem prostých lidí a rolníků. Přebývá v paláci Bilskirni. Po obloze jezdí ve voze taženém dvěma kozly Tanngjóstem a Tanngrisnem. Jeho ženou je Sif. Jeho děti jsou synové Modi a Magni  a dcera Trůd. K jeho symbolům patří kladivo Mjolni (lomozník), opasek síly, rukavice a kozel. Jeho dnem je čtvrtek (Thursday, Torsdag) a nápojem pivo.")
tyr = God("Tyr", "M",
          ".. zvaný také Tý / Ziu, je bůh války, zákonného shromáždění – Thingu, práva, přísahy a daného slova. Je také bohem válečníků a promyšleného / taktického boje. Svou pravou ruku obětoval, aby dodržel slib bohů daný vlku Fenrimu. Jeho jménem vysloveným dvakrát se před bitvou chrání válečníci. Pro štěstí a úspěch v boji také bojovníci ryli jeho runu na čepele kopí a oštěpů. Jeho zvířetem je divoký tur a býk. Jeho dnem je úterý (Tuesday, Tisdag).")
odin = God("Odin", "M",
           ".. bůh větru, bouře, války, běsnícího houfu, magie, léčitelství, vědění, moudrosti, úskoku, šalby, klamu, šamanismu a mrtvých (patří mu polovina padlých válečníků). V touze po vyšším vědění své pravé oko vyměnil za doušek ze studnice moudrosti. Jeho domovem je síň padlých Valhalla a patří mu jedna polovina padlých válečníků (ta druhý patří Freye). Bojovníci vyznávající nejdivočejší způsoby Odina se nazývají berserkové - bojovali beze zbroje, často jen ve vlčích kožešinách a propadali bojové zuřivosti a šílenství. Odin shlíží na svět lidí ze svého trůnu Hlidskjálfu z věže Valaskjálf, přičemž mu u nohou sedí dva vlci Geri a Freki (žravý a chtivý). Jezdí na osminohém koni Sleipnirovi. Ku pomoci má dva krkavce jménem Huginn a Muninn (myšlenka a paměť), kteří mu nosí nové zprávy o všem, co se děje. Díky Odinovi mají lidé runy a runovou magii a nápoj básníků (skaldů) medovinu. Ve své divoké podobě vyráží s démony smrti na Divoký hon na okrajích lesů a jen málokdo má takové štěstí, aby z tohoto setkání vyvázl životem. Jeho ženou je Frigg. Jeho synové jsou Baldr, Tor, Váli, Ull, Vídar, Bragi, Hod a Hermod / Hermodur. K jeho symbolům patří prsten Draupni (kapka) a kopí / oštěp Gungni (houpající se). Jeho zvířetem je krkavec, vlk a válečný oř. Odin je také bohem viselců a obětovalo se mu oběšením. Jeho dnem je středa (Wednesday, Onsdag) a nápojem víno.")
frey = God("Frey", "M",
           ".. bůh deště, slunce, úrody, míru, plodnosti, vášně a mužné síly. Pro lásku ke Gerdě z rodů obrů se vzdá svého mocného meče. Je synem Njorda a Nerthus. Jezdí na zlatém kanci Gullinborstim (zlatoštětináč). Jeho symbolem je meč, kanec a loď Skídblani. Pokud bylo potřeba usmířit si Freye větší obětí, obětovalo se mu prolitou krví - podříznutím hrdla nebo stětím. Jeho dnem je pátek (Friday, Fredag) a nápojem medovina.")
loki = God("Loki", "M",
           ".. potměšilý a nevyzpytatelný bůh ohně, zemětřesení, sváru a lsti. Je pokrevně sbratřen s Odinem, kterému pomáhal při cestě za runami a moudrostí. Má na svědomí smrt Bílého Baldra. Někdy pomáhá bohům někdy obrům/jotunům. Při Ragnaroku se však přidá k obrům. Jeho ženou je Sigyn a jeho děti jsou synové Váli a Nárfi. K jeho nelidským potomkům patří dcera Hel, světový had Jormungand / Midgardsorm, vlk Fenri a kůň Sleipni.")
freya = God("Freya", "F",
            ".. zvaná též Freja, bohyně lásky, slasti, milování, plodnosti, čar a milostných kouzel a mrtvých (patří jí druhá polovina padlých válečníků). Když na svých cestách navštěvuje Midgard, jezdí ve svém voze taženém kočkami. Jejím mužem je Ód. Má dceru Hnoss. Jejím symbolem je kočka a náhrdelník Brísingam.")
njord = God("Njord", "M",
            ".. bůh moře a rybolovu, který je ochráncem mořeplavců. Jeho ženou je Skadi. Jeho děti jsou dvojčata Frey a Freya.")
baldr = God("Baldr", "M",
            ".. zvaný též Baldur, je 'bílý' bůh nevinnosti, čistoty, odpuštění, krásy a dobra. Přebývá ve svém paláci Breidablik. Při zábavě je zabit šípem z větvičky jmelí rukou bratra Hoda, díky lsti Lokiho. Jeho ženou je Nanna. Jeho syn je Forseti.")
frigg = God("Frigg", "F",
            ".. bohyně manželství, rodiny, přírody a mrtvých mužů, kteří přišli o život kvůli ženám. Jejím mužem je Odin.")
hel = God("Hel", "F",
          ".. půl černá půl bílá (a půl živá, půl mrtvá) vládkyně říše mrtvých Hel. Patří jí lidé, jenž zemřeli stářím či nemocí. Je dcerou Lokiho a Angrbody z rodu obrů.")
bragi = God("Bragi", "M",
            ".. bůh básníků, skaldů a řečníků, který neustále opěvuje a velebí svou krásnou ženu jménem Idunn.")
idunn = God("Idunn", "F",
            ".. bohyně mládí a zdraví. Hlídá posvátný sad a v něm rostoucí jablka mládí, jež jedí všichni bohové, aby si udrželi sílu a mládí. Díky těmto jablkům si bohové uchovávají nesmrtelnost a zdraví - na rozdíl od lidí, obrů, Álfů a trpaslíků.")
hodur = God("Hodur", "M",
            ".. zvaný též Hod, je slepý bůh a bojovník. Je vzýván pro zdar při nočních výpravách. Je zabit na příkaz Odina vlastním bratrem Válim, jako trest za zabití bratra Baldra.")
heimdall = God("Heimdall", "M",
               ".. zvaný též Ríg, je bůh strážce, který přebývá ve strážní věži Himinbjorg u duhového mostu Bifrost, kde vyhlíží nepřátele. Tento bůh vidí ve dne i v noci na sto honů, slyší růst trávu na zemi a vlnu na ovcích. Rozdělil společnost lidí na 3 stavy: 1. poddané a otroky, 2. svobodné lidi, 3. krále a panovníky. Je potomkem devíti matek, které jsou zároveň sestry. Jeho symbolem je troubící roh Gjallarhorn (zvučící roh). Zdůrazňuje nutnost aplikace trojitého principu pro svět (a společnost) lidí.")
ull = God("Ull", "M",
          ".. bůh zimy, lukostřelby, lovu a lyžování. Jeho ženou je Skadi z rodu obrů. ")
forseti = God("Forseti", "M",
              ".. bůh vládnoucí nad sudištěm, je soudcem sporů a hádek mezi bohy.")
aegir = God("Aegir", "M",
            ".. zvaný též Agi, je bůh (možná je i z rodu obrů) vládnoucí mořím a oceánům. Jeho ženou je Rán. Jeho dcery jsou vlny a vlnky. K jeho symbolů patří přilba a znamení Aegishjalmur (Helm of awe - Aegiho přilba hrůzy a děsu). Při bouři se mu obětovalo utopením - oběť byla rovnou (často svázána) vyhozena přes palubu.")
ran = God("Rán", "F",
          ".. bohyně (možná je i z rodu obrů) moře a utonulých, které chytá do své sítě.")
eostre = God("Eostre", "F",
             ".. zvaná též Eostra / Ostara je bohyně světla, jara, obnovy. Jejím časem je jarní rovnodennost = Ostara (Velikonoce).")

viking_gods = [thor, tyr, odin, frey, loki, freya, njord, baldr, frigg, hel, bragi, idunn, hodur, heimdall, ull,
               forseti, aegir, ran, eostre]

# list of celtic gods (16)
taranis = God("Taranis", "M",
              " .. bůh blesku, nebes, přímého fyzického boje, střetu, bitevní vřavy a válečníků a štěstí v boji. Jeho jméno dodnes přežívá v názvech taras, zatarasit, tarasnice a taranovat. Jeho symbolem je slunce, spirála a 'Taranisovo kolo' resp. loukoťové kolo, které vynalezli kelti. Obětovalo se mu upálením a jeho živlem je oheň.")
teutatis = God("Teutatis", "M",
               ".. též zvaný Toutatis, je kmenovým ochranným a pečujícím bohem a léčitelem, je moudrým vůdcem v časech války i míru, ochránce území a svého lidu. Je to bůh otec, ke kterému se lze obrátit pro radu a poučení. Obětovalo se mu utopením a jeho živlem je voda.")
esus = God("Esus", "M",
           ".. bůh řemesel, zručnosti, vynalézavosti, plodnosti a bohatství, ale je také bohem mrtvých, podsvětí a věštění. Jeho symbolem je kanec. Obětovalo se mu oběšením na strom a jeho živlem je vzduch. ")
epona = God("Epona", "F",
            ".. nazývaná také Velká klisna, je keltská bohyně koní a jezdectví. Je to silná bohyně hojnosti, prosperity, plodnosti a mateřství. Známá je také pod jménem Kotýs. Uznávali ji i Římané a známá byla v Galii. Jejím symbolem je klisna/kobyla na které jede po zemi - která je jejím živlem.")
cernunn = God("Cernunn", "M",
              ".. zvaný též Cernunnos, je prastarý bůh divokého lesa a zvířat, plodnosti, hojnosti a bohem zásvětí, života a smrti. Jeho symbolem je jelení paroží a ze zvířat jelen, had a vlk. Je také bohem magie a šamanismu.")
maponos = God("Maponos", "M",
              ".. zvaný též Velký syn, je keltský bůh síly, mládí, hudby a radosti. Jeho svátkem je Mabon (oslavy sklizně, úrody a hojnosti), jeho symbolem je harfa a jeho hudba radostně rozechvívá samotný vzduch - který je jeho živlem.")
eiocha = God("Eiocha", "F",
             ".. je klisna zrozená z mořské pěny prvotního moře. Matka lesního boha Cernunna, se kterým poté zplodili další bohy.")
lugh = God("Lugh", "M",
           ".. zvaný také Lámfada nebo-li „Dlouhá ruka“ a Samildánach „dovedný v mnoha řemeslech/uměních“, je bůh válečníků, boje a také magie a léčení a rolníků i řemeslníků. Lugh, zářící bůh slunce, je také ochráncem umění a bardů. Jeho symboly jsou zlaté kopí a vrhací prak a kůň Aenbarr, který jezdí po moři i po zemi. Jeho oslava připadá na letní Lughnasad.")
dagda = God("Dagda", "M",
            ".. zvaný také Eochaid ollathair nebo-li „Otec všech“ a Ruad rofhessa „Pán všeho vědění“ či „Pán čtyř živlů“, je bohem moudrosti, vzdělání a znalostí a také řemesel a hojnosti. Je ochránce druidů a bohem čarodějnictví a znovuzrození, života a smrti. Chrání bojovníky. Jeho symbolem je palice / kyj, který jedním koncem zabíjí, druhým život vrací a dokáže najednou zabít 9 mužů. Dalším symbolem je nevyčerpatelný kotel Undry, který dokáže přivést mrtvé k životu a dubová harfa Uaithne, která řídí střídání ročních období. V dutých kopcích má 4 paláce.")
oghma = God("Oghma", "M",
            ".. zvaný také Ogmios / Ogma, je bůh války a královské moci, bůh řečnického a básnického umění a zaklínadel a také průvodce do říše mrtvých. Provází jej zástup radostných lidí připoutaných tenkými řetízky ze zlata a jantaru. Řetízky vedou skrz jeho usmívající se ústa a jazyk  a jsou provlečeny ušima následovníků. Spojuje zdánlivé protiklady, když se jednou tváří usmívá a druhou mračí. Stvořil keltské stromové písmo ogham. Jeho symboly jsou kyj, luk a kouzelná harfa.")
morrigan = God("Morrigan", "F",
               ".. zvaná též Mórrígan, je protipól Brigit. Je bohyní osudu a války, vítězství a smrti. Dokáže měnit svoji podobu a proto se někdy nazývá 'Královna přízraků'. Je ženou boha Dagda a stejně tak jako on i ona v sobě zahrnuje tři aspekty - 'Tři  Morrígna' - Badb, Macha a Nemain. Badb Catha je bohyně v ptačí podobě vrány na válečných polí, Machu je hrdá bohyně vlády, panování, války a úrodné země, Nemain představuje bitevní vřavu a šílenství. Morrigan často přináší válečníkům jak slávu a odvahu, tak násilnou smrt a je spojována s bean-sidhe (banshee), což jsou víly smrti / ženy z dutých kopců.")
brigit = God("Brigit", "F",
             ".. zvaná též Birgid, irsky pak Cros Bríde, je dcera boha Dagda a je bohyní jara. Má také tři aspekty schopností, podobně jako její otec, a to léčení, básnictví a kovářství. Symbol Brigitina kříže se často zavěšoval nad okna a dveře, aby chránil domov a rodinu před neštěstím a nebezpečím. Kříž pomáhá také jako ochrana proti ohni a požáru. Její slavností je Imbolc (jarní rovnodennost).")
bel = God("Bél", "M",
          ".. zvaný též Belenus nebo Belenos, je sluneční bůh, který brázdí oblohu ve svém vozu taženém koňmi. Je bohem mládí, síly, plodnosti a očištění. Jeho symbolem je kůň a kolo. Jeho svátkem je Beltine - Valpružina noc, tzv. pálení čarodějnic či filipojakobská noc (v noci z 30. dubna na 1. květen) a je spojený s očistným ohněm. Dobytek se před vyhnáním na pastviny provází mezi dvěma ohni, aby se zbavil nemocí. Lidé prochází buď mezi ohni nebo přes tento oheň přeskakují, aby na sebe přivolali štěstí a udrželi (nebo vyléčili) plodnost. Staví se také májka coby spojení ženského (věnec) a mužského (vztyčený kůl) principu.")
danu = God("Danu", "F",
           ".. zvaná též Dana / Ana / Annan je bohyně - matka přírody. Zosobňuje přírodní principy: nový život - růst - zrání - smrt - regeneraci. Představuje cyklické pojetí života a času a také praktickou životní moudrost, která je předávána z pokolení na pokolení. Je prvotní bohyní Tuatha Dé Danann, což je pokolení bohů tzv. 'Danaů' z časů osidlování starého Irska. Je dávána také do spojení s řekou Dunajem (Danube).")
grannus = God("Grannus", "M",
              ".. bůh horkých minerálních pramenů a jejich léčebných účinků. V úcte jej chovali v Cáchách (Německo), které jsou dodnes proslulé svými lázněmi.")
sirona = God("Sirona", "F",
             "..  bohyně léčivých pramenů, jejichž účinek kombinuje s uzdravující silou slunce. Často byla oslavována společně s Grannusem. Mezi její symboly patří had a vejce.")

celtic_gods = [taranis, teutatis, esus, epona, cernunn, maponos, eiocha,
             lugh, dagda, oghma, morrigan, brigit, bel, danu, grannus, sirona]

# list of slavic gods (16)
rod = God("Rod", "M",
          ".. zvaný též Rid, Rožaj či Radaj je prabůh stvořitel, bůh zrodu, života a znovuzrození. Je vládcem stromu života a stvořitel našeho světa z moře chaosu. Představuje počátek i konec všeho. Rod dodnes přežívá ve slovech národ, rodina, porod či příroda. Jeho potomkem je Prove. Jeho symboly jsou vejce, dubová hůl, dubové žezlo a zlaté vejce. Jeho živlem je voda v podobě nekonečného praoceánu. Rodovým zvířetem je sokol. Je mu zasvěcena neděle. ")
lada = God("Lada", "F",
           ".. bohyně vody, lásky, milování a míru. Je královnou bohů. Je jí vlastní jemnost, nestálost, změna, porozumění i soulad, stejně jako posedlost, sex, náruživost a početí. Je ochránkyní rodiny a bohyní svateb. Jejím mužem je Svarog. Lada dodnes přežívá ve slovech jako ladný a soulad. Jejím symbolem je zlatý vůz tažený labutěmi a holuby, miska s jablkem a obilné klasy. Jejím živlem je proměnlivá voda. Jejím tancem je tanec svarga. Jejími stromy jsou lípa (jemnost) a bříza (obnova a regenerace). Je jí zasvěcena sobota (den svateb).")
triglav = God("Triglav", "M",
              ".. zvaný též Bělbog / Bělobog, představuje trojhlavé vtělení boha Roda (Svarog+Perun+Veles). Je pánem tří světů (svět v podobě dubu = nebe, země, podsvětí) a pánem tří živlů (vzduch, země, voda). Jeho číslem je proto číslo 3. Zosobňuje dobro, zákon, pořádek a sjednocení. Je bohem války a síly. Jeho symbolem je silný řetěz kolem krku či pasu. Triglavovým zvířetem je černý kůň. Je mu zasvěcena neděle.")
svarog = God("Svarog", "M",
             ".. zvaný též Svaroh, Svarod či Svaren, je nebeský kovář, stvořitel slunce a hvězdného nebe i kola souhvězdí zvěrokruhu. Dlí v ohni a jiskrách a je bohem řemesla a ochráncem manželství. Představuje sebevědomí, charizma a hrdost. Jeho ženou je Lada a jeho synové jsou Dažbog, Koliad, Simargl a Stribog. Jeho symbolem je kovářské kladivo a kleště, zářivá koruna a oko svargy. Jeho živlem je oheň a kov. Svarogovým zvířetem je zlatý kohout, který o svargu na vrcholu Svarogova paláce křeše jiskry, které pak jako oheň roznáší lidem do příbytků. Je mu zasvěceno úterý. ")
perun = God("Perun", "M",
            ".. zvaný též Perkun, Peraun či Perkunas, je vládce a ochránce země a strážce zlatého vejce. Je bohem bouře, deště, hromu a blesku. Je patronem vojáků, strážců a ochránců, stejně tak i zbraní a bojových umění. Obdarovává lidi životem a silou, dohlíží na dodržování zákonů. Je bohem přísahy, síly, odvahy a bojovnosti. Jeho číslem je číslo 7. Jeho ženou je Vesna. Jeho synové jsou Rugevit, Porenut a Porevit a jeho dcerou je Podaga. Jeho symbolem je hromová sekera, bleskový luk, hřmotný vůz tažený dvěma kozly, dubový háj a oheň z dubového dřeva. Jeho živly jsou oheň a vzduch. Perunovým zvířetem je kozel. Je mu zasvěcen čtvrtek.")
veles = God("Veles", "M",
            ".. zvaný též Vales, Volos či Velinas, je bůh úrody a dobytka, moudrosti a umění a také bohatství, vlastnictví a obchodu. Chrání před nebezpečím na cestách. Je bohem magie, věštění a podsvětí. Zjevuje se jako stařec / pastýř s holí nebo mladý válečník v kůži s rohy a s kopím. Jeho ženou je Mokoš, se kterou má syny Svatogora, Vodana, Polevika, Kurenta a Usuda a dceru Perplut. Jeho symbolem je pluh, který se dával při zimním slunovratu pod hodovní stůl, snop obilí (zvaný Velesova brada), studna a magický pramen. Velesovými zvířaty je medvěd a býk a jeho stromem je ořech. Je mu zasvěcena středa.")
mokos = God("Mokoš", "F",
            ".. zvaná též Pripeliga, Syria či matka země, je bohyně země, osudu, věštění, úrody a stád. Je svázána s podsvětím. Pomáhá těm, kdo se nevzdávají osudu navzdory. Hlídá dodržování zvyků a obřadů. Jejím mužem je Veles. Od Mokoš jsou odvozena slova jako mokřina a mokrý. Jejím symbolem je zlatá koruna s drahými kameny, vřeteno, koudel, roh / miska hojnosti, žito, len a konopí. Mokošiným zvířetem je kráva a jejím stromem je vrba. Je jí zasvěcen pátek.")
nij = God("Nij", "M",
          ".. temný bůh chaosu, neštěstí, nemoci, sváru, války a bezpráví. Je to ničitel zákonů, lhář a bůh iluze a klamu, který chrání lháře, zloděje a vrahy. To on přivolává neštěstí a porážky. Je bohem temná magie. Jeho živly jsou oheň a vzduch. Objevuje se v podobě černého létajícího hada / draka nebo černého bojovníka v černém plášti, který jede na černém trojhlavém vlkovi. Jeho symbolem je ohnivé kladivo a hadí rozeklaný jazyk. Nijovými zvířaty jsou černý had a netopýr a jeho bylinami durman a blín. Jsou mu zasvěceny tmavé noci.")
dazbog = God("Dažbog", "M",
             ".. zvaný též Svarožic či Radegast, je zářivý bojovník. Je bohem síly, odvahy, ohně a země - představuje slunce, dobro, světlo, teplo, bezpečí, dar, pomoc a je ochránce slovanského rodu. Zosobňuje čtyřhlavého boha (od dítěte ke starci). Dažbog je bojovník proti démonům a zlu. Jeho ženami byly Chors, Morana a nakonec Živa, se kterou má syny Jarila a Svantovíta. Jeho jméno znamená bůh, který dává či bůh - dárce. Jeho symboly jsou zlatý vůz a zlatá koruna, ohnivý meč a svarga (slunce). Jeho živly jsou oheň a země. Dažbogovým zvířetem je bílý kůň. O letním slunovratu (Vaján) se při jeho obřadech přeskakuje přes zapálený oheň. Je mu zasvěcena sobota.")
chors = God("Chors", "F",
            ".. zvaná též Zlatogorka, Chrs, Chers a Luna, je bohyně měsíce, kouzel, léčení, bylin, růstu a zánik všeho živého. Chors je vládkyně vlkodlaků a upírů, královna víl a rusalek. Je bohyní nočních démonů a zároveň bojovnice velké síly a odvahy. Jejím mužem byl Dažbog, se kterým má dceru Divu. Její symboly jsou Měsíc a stříbro - které jediné jí a jejím temným dětem dokáže ublížit. Jejími živly jsou voda a země. Chorsiným zvířetem je černá kočka. K její poctě se tančí kruhové tance zvané chorovody. ")
morana = God("Morana", "F",
             ".. zvaná též Morena, Mora a Marmuriena, je bohyně zimy, smrti, démonů, chorob, neštěstí a temných tajemství. Morana je temná / ledová královna, v jejíž jeskyni hoří každému smrtelníkovi lampa. Je pomocnice v boji s nepřítelem (toho očaruje a zničí). Jejím mužem byl Dažbog a potom Kaščej. Její sestra je Živa. Dodnes její jméno přežívá ve slovech můra a mor. Její symboly jsou bílé šaty s diamanty, diamantová koruna, černé vlasy, diamant, černé brnění, vybělená lebka, svíce a lampa. Její živly jsou vzduch a voda. Moraninými zvířaty jsou vrána a krkavec, jejím stromem smrk a rostlinou blín. S přívhodem jara se její slaměná figurína spaluje nebo hází do vody - tzv. vynášení Morany. Je jí zasvěcena sobota. ")
dij = God("Dij", "M",
          ".. pán tmy a noci a patron zlodějů a vrahů, které chrání a skrývá svým pláštěm. Jeho dcerou je Chors. Má podobu černého jezdce na černém koni s černým pláštěm a černou přilbou, v černém brnění a s černým mečem, který pohlcuje světlo. Dijovými zvířaty jsou černý kůň a netopýr a jeho stromem je tis - strom na pomezí království života a smrti. Jsou mu zasvěcena novoluní.")
ziva = God("Živa", "F",
           ".. zvaná též Živena, Siva, Dana či Ľeľa, je bohyně života, vitality, počátku světa, léta, plodnosti, životní síly, míru, usmíření, uzdravení, léčivé síly bylin, minerálů a vody, léčitelství. Její sestrou je Morana. Živa žehná nové rodině a je bohyní svateb. Zosobňuje obnovu a tvořivou sílu. U studánek býval její obrázek a hrnek pro žíznivé. Jejím mužem je Dažbog. Její symboly jsou zlatý vůz tažený holubicemi (letí-li vzduchem) nebo rybami (pluje-li pod vodou), duha, prameny (= živá voda), zlaté vlasy a zlaté šaty, zlatá korunka s drahokamy, zlaté šperky, duha a most přes vodní tok. Její živly jsou vzduch a voda. Živinými zvířaty jsou bílá holubice a zlaté ryby, její stromy jsou lípa a bříza. Je jí zasvěcena sobota.")
kascej = God("Kaščej", "M",
             ".. zvaný též Černobog, 'zemská kachna' nebo Černohlav, je původce a zastánce všeho zla a chaosu, vládne podzemnímu království Nav. Je pánem démonů, nemocí, hádek, zla, sporů a lží a je protivníkem bohů. Objevuje se s temnou tváří, v černé sutaně, s černým pláštěm, stříbřitou bradou a černou korunou s černými drahokamy. Jeho ženou je Morana, se kterou má syna Smrt a dceru Runu. Jeho symboly jsou temný palcát a černý meč, který pohlcuje světlo. Jeho živly jsou oheň, voda a vzduch. Černobogovým zvířaty jsou černý had, černá kachna a krkavec, jeho stromem je tis a náleží mu číslo 3. ")
stribog = God("Stribog", "M",
              ".. zvaný též Pohvizd, je pán větrů, vládce pustin, pohybu a rychlosti. Stribog je bůh vševědoucnosti, který pomáhá při hledání, je ochráncem poutníků, na cestách a výpravách a strážcem 4 světových stran. Jeho ženou je Větrnice a Pizmar, se kterou má dcery Vesnu a Jeseň. Objevuje se s ústy zkovanými k sobě, na koni bez sedla a bez postroje, v bílých šatech vyšitých stříbrem. Jeho symboly jsou vítr a číslo 4 (za 4 světové větry a 4 světové strany). Jeho živlem je vzduch. Stribogovým zvířetem je kůň a jeho rostlinou je sasanka. ")
simargl = God("Simargl", "M",
              ".. zvaný též Semargl, je dvojhlavý bůh ohně a domácího krbu, ochránce před mocnostmi temna. Představuje ohnivý očišťující vichr a božská dvojčata - blížence Sim (teplo a ochránce rostlin) + Rigl (světlo a ochránce dobytka). Simargl to je živý a svatý oheň a očistné vykuřování. Jeho synem je Kupalo a dcerou Magura. Jeho symboly jsou ohnivý kůň se zlatou hřívou a stříbrnou srstí, červené brnění, ohnivý meč / palice a plamen. Jeho živlem je oheň. Simarglovými zvířaty jsou pták ohnivák (fénix) a dvouhlavý orel. Jeho číslem je proto číslo 2. Je mu zasvěcena podzimní rovnodennost a uctívá se v tuto noc posvátným ohněm, který nesmí vyhasnout a u kterého se bdí přes noc - protože tuto jedinou noc v roce Simargl spí.")

slavic_gods = [rod, lada, triglav, svarog, perun, veles, mokos, nij, dazbog, chors,
               morana, dij, ziva, kascej, stribog, simargl]

error_god = God("neznámý bůh", "X", "nebyl stvořen - neznámý bůh")
# print(len(viking_gods), len(celtic_gods), len(slavic_gods))


