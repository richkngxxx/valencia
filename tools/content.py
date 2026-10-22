# Source content for lessons.js.
# Lesson: (title, words, phrases)
# word:   (valencià, español[, nota[, alternativas aceptadas]])
# phrase: (valencià, español[, nota])
# IDs are positional (a1-1-1 ...). Append new lessons at the END of a unit so saved progress stays valid.
C = {}
C["A1"] = ("Principiante", [
 ("Saludos", "#58cc02", [
  ("Hola y adiós", [("hola","hola"),("bon dia","buenos días","Saludo de la mañana."),("bona vesprada","buenas tardes"),("bona nit","buenas noches"),("adéu","adiós"),("fins demà","hasta mañana"),("fins després","hasta luego"),("fins prompte","hasta pronto"),("com estàs?","¿cómo estás?"),("molt bé","muy bien")],
   [("Bon dia, com estàs?","Buenos días, ¿cómo estás?"),("Molt bé, gràcies","Muy bien, gracias"),("Adéu, fins demà","Adiós, hasta mañana"),("Bona nit, fins prompte","Buenas noches, hasta pronto")]),
  ("Presentarse", [("com et dius?","¿cómo te llamas?"),("em dic","me llamo","Em dic Anna = Me llamo Anna."),("encantat","encantado"),("encantada","encantada"),("molt de gust","mucho gusto"),("d'on eres?","¿de dónde eres?"),("soc de","soy de"),("i tu?","¿y tú?"),("on vius?","¿dónde vives?"),("visc a","vivo en","Con ciudades: visc a València.")],
   [("Em dic Marta, molt de gust","Me llamo Marta, mucho gusto"),("Soc de València, i tu?","Soy de Valencia, ¿y tú?"),("Encantada, em dic Laura","Encantada, me llamo Laura"),("Visc a Alacant","Vivo en Alicante")]),
  ("Cortesía", [("gràcies","gracias"),("moltes gràcies","muchas gracias"),("de res","de nada"),("per favor","por favor"),("perdó","perdón"),("disculpa","disculpa"),("no passa res","no pasa nada"),("sí","sí"),("no","no"),("d'acord","de acuerdo")],
   [("Un café, per favor","Un café, por favor"),("Moltes gràcies! De res","¡Muchas gracias! De nada"),("Perdó, no parle valencià","Perdón, no hablo valenciano"),("D'acord, no passa res","De acuerdo, no pasa nada")]),
  ("¿Qué tal?", [("què tal?","¿qué tal?"),("estic bé","estoy bien"),("estic cansat","estoy cansado","Femenino: cansada."),("estic content","estoy contento","Femenino: contenta."),("malament","mal"),("regular","regular"),("una mica","un poco"),("i vosté?","¿y usted?"),("tranquil","tranquilo")],
   [("Què tal? Estic molt bé","¿Qué tal? Estoy muy bien"),("Estic una mica cansada","Estoy un poco cansada"),("I vosté, com està?","Y usted, ¿cómo está?"),("Hui estic molt content","Hoy estoy muy contento","«Hui» = hoy.")]),
 ]),
 ("Números", "#1cb0f6", [
  ("Del 0 al 5", [("zero","cero"),("u","uno","«Un» delante de nombre: un café."),("una","una"),("dos","dos (masculino)"),("dues","dos (femenino)","Dues germanes = dos hermanas."),("tres","tres"),("quatre","cuatro"),("cinc","cinco")],
   [("Tinc quatre gats","Tengo cuatro gatos"),("Tinc dues germanes","Tengo dos hermanas"),("Vull dos cafés","Quiero dos cafés"),("Dos i tres són cinc","Dos y tres son cinco")]),
  ("Del 6 al 10", [("sis","seis"),("set","siete"),("huit","ocho","Forma valenciana (también «vuit»).",["vuit"]),("nou","nueve"),("deu","diez"),("quants?","¿cuántos?"),("número","número"),("telèfon","teléfono")],
   [("Són les huit","Son las ocho"),("Set i tres són deu","Siete y tres son diez"),("Tinc nou anys","Tengo nueve años"),("El meu número de telèfon","Mi número de teléfono")]),
  ("Del 11 al 20", [("onze","once"),("dotze","doce"),("tretze","trece"),("catorze","catorce"),("quinze","quince"),("setze","dieciséis"),("dèsset","diecisiete","También «disset».",["disset"]),("díhuit","dieciocho","También «divuit».",["divuit"]),("dènou","diecinueve","También «dinou».",["dinou"]),("vint","veinte")],
   [("Tinc vint anys","Tengo veinte años"),("Hi ha quinze alumnes","Hay quince alumnos"),("La classe és a les onze","La clase es a las once"),("Tinc dotze euros","Tengo doce euros")]),
  ("Decenas", [("vint-i-u","veintiuno"),("trenta","treinta"),("quaranta","cuarenta"),("cinquanta","cincuenta"),("seixanta","sesenta"),("setanta","setenta"),("huitanta","ochenta","También «vuitanta».",["vuitanta"]),("noranta","noventa"),("cent","cien")],
   [("La meua iaia té huitanta anys","Mi abuela tiene ochenta años"),("Costa cinquanta euros","Cuesta cincuenta euros"),("Tinc trenta-dos anys","Tengo treinta y dos años"),("Cent per cent","Cien por cien")]),
 ]),
 ("Familia", "#ce82ff", [
  ("Padres y hermanos", [("mare","madre"),("pare","padre"),("pares","padres"),("germà","hermano"),("germana","hermana"),("germans","hermanos"),("família","familia"),("la meua","mi (femenino)","Valenciano: meua, teua, seua."),("el meu","mi (masculino)")],
   [("Esta és la meua mare","Esta es mi madre"),("El meu pare es diu Vicent","Mi padre se llama Vicent"),("Tinc dos germans","Tengo dos hermanos"),("La meua família és gran","Mi familia es grande")]),
  ("Abuelos e hijos", [("iaio","abuelo"),("iaia","abuela"),("iaios","abuelos"),("fill","hijo"),("filla","hija"),("fills","hijos"),("nét","nieto"),("néta","nieta")],
   [("El meu fill es diu Pau","Mi hijo se llama Pau"),("Els meus iaios viuen al poble","Mis abuelos viven en el pueblo"),("Tinc una filla i un fill","Tengo una hija y un hijo"),("La iaia té tres néts","La abuela tiene tres nietos")]),
  ("Más familia", [("oncle","tío"),("tia","tía"),("cosí","primo"),("cosina","prima"),("nebot","sobrino"),("neboda","sobrina"),("xiquet","niño"),("xiqueta","niña")],
   [("La meua tia viu a Castelló","Mi tía vive en Castellón"),("El xiquet té cinc anys","El niño tiene cinco años"),("Tinc tres cosins","Tengo tres primos"),("La meua neboda és molt simpàtica","Mi sobrina es muy simpática")]),
  ("Describir personas", [("alt","alto"),("baix","bajo"),("jove","joven"),("major","mayor"),("simpàtic","simpático"),("guapo","guapo","También «bonic» / «formós»."),("ros","rubio","Femenino: rossa."),("moré","moreno","Femenino: morena (DNV: moré).")],
   [("El meu germà és molt alt","Mi hermano es muy alto"),("La meua mare és jove","Mi madre es joven"),("La meua cosina és rossa","Mi prima es rubia"),("És un xiquet molt simpàtic","Es un niño muy simpático")]),
 ]),
 ("Comida", "#ff9600", [
  ("Básicos", [("pa","pan"),("aigua","agua"),("llet","leche"),("formatge","queso"),("ou","huevo"),("fruita","fruta"),("poma","manzana"),("taronja","naranja"),("carn","carne"),("peix","pescado")],
   [("Vull pa i formatge","Quiero pan y queso"),("M'agrada la taronja","Me gusta la naranja"),("No menge carn","No como carne"),("Un got d'aigua, per favor","Un vaso de agua, por favor")]),
  ("En la cocina", [("creïlla","patata","Forma valenciana más habitual."),("tomaca","tomate"),("ceba","cebolla"),("arròs","arroz"),("all","ajo"),("oli","aceite"),("sal","sal"),("pebre","pimienta"),("verdura","verdura")],
   [("M'agrada l'arròs","Me gusta el arroz"),("Necessite oli i sal","Necesito aceite y sal"),("Una truita de creïlla","Una tortilla de patata"),("No m'agrada la ceba","No me gusta la cebolla")]),
  ("Las comidas", [("esmorzar","desayunar"),("dinar","comer al mediodía"),("berenar","merendar"),("sopar","cenar"),("tinc fam","tengo hambre"),("tinc set","tengo sed"),("cuinar","cocinar"),("el menjar","la comida"),("bo","bueno (rico)","Femenino: bona.")],
   [("Hui sopem a casa","Hoy cenamos en casa"),("Tinc fam, anem a dinar","Tengo hambre, vamos a comer"),("Esmorze a les set","Desayuno a las siete"),("Este menjar està molt bo","Esta comida está muy buena")]),
  ("En el bar", [("cambrer","camarero"),("el compte","la cuenta"),("cervesa","cerveza"),("café amb llet","café con leche"),("entrepà","bocadillo"),("tallat","cortado"),("quant és?","¿cuánto es?"),("per a mi","para mí")],
   [("Un café amb llet, per favor","Un café con leche, por favor"),("Per a mi, un entrepà de formatge","Para mí, un bocadillo de queso"),("El compte, per favor","La cuenta, por favor"),("Quant és tot?","¿Cuánto es todo?")]),
 ]),
])
C["A2"] = ("Elemental", [
 ("Días y horas", "#58cc02", [
  ("Los días", [("dilluns","lunes"),("dimarts","martes"),("dimecres","miércoles"),("dijous","jueves"),("divendres","viernes"),("dissabte","sábado"),("diumenge","domingo"),("setmana","semana"),("dia","día"),("cap de setmana","fin de semana")],
   [("Dilluns treballe","El lunes trabajo","1.ª persona en -e: treballe."),("El cap de setmana descanse","El fin de semana descanso"),("Dissabte anem a la platja","El sábado vamos a la playa"),("Quin dia és hui?","¿Qué día es hoy?")]),
  ("¿Cuándo?", [("hui","hoy"),("demà","mañana (día siguiente)"),("ahir","ayer"),("ara","ahora"),("després","después"),("abans","antes"),("prompte","pronto"),("tard","tarde (con retraso)"),("matí","mañana (parte del día)"),("vesprada","tarde (parte del día)")],
   [("Demà al matí treballe","Mañana por la mañana trabajo"),("Arribe tard","Llego tarde"),("Ara no puc","Ahora no puedo"),("Després de dinar","Después de comer")]),
  ("La hora", [("quina hora és?","¿qué hora es?"),("és la una","es la una"),("són les dues","son las dos"),("i quart","y cuarto"),("i mitja","y media"),("menys quart","menos cuarto"),("en punt","en punto"),("migdia","mediodía"),("mitjanit","medianoche")],
   [("Són les tres de la vesprada","Son las tres de la tarde"),("És la una en punt","Es la una en punto"),("Quedem a les set i mitja","Quedamos a las siete y media"),("Són les deu menys quart","Son las diez menos cuarto")]),
  ("Los meses", [("gener","enero"),("febrer","febrero"),("març","marzo"),("abril","abril"),("maig","mayo"),("juny","junio"),("juliol","julio"),("agost","agosto"),("setembre","septiembre"),("octubre","octubre"),("novembre","noviembre"),("desembre","diciembre")],
   [("El meu aniversari és al maig","Mi cumpleaños es en mayo"),("Les Falles són al març","Las Fallas son en marzo"),("A l'agost faig vacances","En agosto hago vacaciones"),("Gener és el primer mes","Enero es el primer mes")]),
  ("Estaciones y tiempo", [("primavera","primavera"),("estiu","verano"),("tardor","otoño"),("hivern","invierno"),("fa calor","hace calor"),("fa fred","hace frío"),("fa sol","hace sol"),("plou","llueve"),("núvol","nube")],
   [("A l'estiu fa molta calor","En verano hace mucho calor"),("Hui plou molt","Hoy llueve mucho"),("A l'hivern fa fred","En invierno hace frío"),("M'agrada la tardor","Me gusta el otoño")]),
 ]),
 ("Colores y ropa", "#1cb0f6", [
  ("Colores", [("roig","rojo","Femenino: roja."),("blau","azul"),("verd","verde"),("groc","amarillo","Femenino: groga."),("blanc","blanco"),("negre","negro"),("gris","gris"),("morat","morado"),("rosa","rosa"),("marró","marrón")],
   [("El cel és blau","El cielo es azul"),("Tinc un gat negre","Tengo un gato negro"),("La poma és roja","La manzana es roja"),("M'agrada el color verd","Me gusta el color verde")]),
  ("Ropa", [("camisa","camisa"),("pantalons","pantalones"),("sabates","zapatos"),("jaqueta","chaqueta"),("samarreta","camiseta"),("falda","falda"),("vestit","vestido"),("abric","abrigo"),("jersei","jersey"),("calcetins","calcetines")],
   [("Porte una camisa blanca","Llevo una camisa blanca","«Portar» = llevar puesto."),("Esta falda és molt bonica","Esta falda es muy bonita"),("Necessite unes sabates noves","Necesito unos zapatos nuevos"),("Fa fred, porta l'abric","Hace frío, lleva el abrigo")]),
  ("De compras", [("botiga","tienda"),("preu","precio"),("car","caro"),("barat","barato"),("talla","talla"),("comprar","comprar"),("diners","dinero"),("targeta","tarjeta"),("en efectiu","en efectivo")],
   [("Quant costa esta jaqueta?","¿Cuánto cuesta esta chaqueta?"),("És molt car","Es muy caro"),("Puc pagar amb targeta?","¿Puedo pagar con tarjeta?"),("Busque una talla més gran","Busco una talla más grande")]),
 ]),
 ("La casa", "#ce82ff", [
  ("Habitaciones", [("casa","casa"),("cuina","cocina"),("dormitori","dormitorio"),("bany","baño"),("menjador","comedor"),("saló","salón"),("terrassa","terraza"),("jardí","jardín"),("escala","escalera"),("habitació","habitación")],
   [("La cuina és xicoteta","La cocina es pequeña","«Xicotet» = pequeño."),("La casa té tres dormitoris","La casa tiene tres dormitorios"),("El bany és a dalt","El baño está arriba"),("Sopem a la terrassa","Cenamos en la terraza")]),
  ("Muebles", [("taula","mesa"),("cadira","silla"),("finestra","ventana"),("porta","puerta"),("llit","cama (mueble)"),("sofà","sofá"),("armari","armario"),("làmpada","lámpara"),("nevera","nevera"),("rentadora","lavadora")],
   [("Obri la finestra, per favor","Abre la ventana, por favor"),("Tanca la porta","Cierra la puerta"),("El gat dorm al sofà","El gato duerme en el sofá"),("La llet és a la nevera","La leche está en la nevera")]),
  ("Dónde vivo", [("visc","vivo"),("pis","piso"),("carrer","calle"),("poble","pueblo"),("ciutat","ciudad"),("barri","barrio"),("veí","vecino","Femenino: veïna."),("prop","cerca"),("lluny","lejos"),("plaça","plaza")],
   [("Visc en un poble xicotet","Vivo en un pueblo pequeño"),("El meu pis és a prop de la plaça","Mi piso está cerca de la plaza"),("La meua veïna és molt amable","Mi vecina es muy amable"),("Visc lluny del centre","Vivo lejos del centro")]),
  ("Tareas de casa", [("netejar","limpiar"),("escurar","fregar los platos"),("agranar","barrer"),("granera","escoba"),("rentar","lavar"),("planxar","planchar"),("fer el llit","hacer la cama"),("tirar el fem","sacar la basura"),("ordenar","ordenar")],
   [("Jo escure i tu agranes","Yo friego y tú barres"),("Has de fer el llit","Tienes que hacer la cama"),("Dissabte netegem la casa","El sábado limpiamos la casa"),("Qui tira el fem?","¿Quién saca la basura?")]),
 ]),
 ("Verbos y preguntas", "#ff9600", [
  ("Presente I", [("parle","hablo"),("menge","como"),("bec","bebo"),("escric","escribo"),("llig","leo"),("treballe","trabajo"),("estudie","estudio"),("dorm","duermo")],
   [("Parle valencià i castellà","Hablo valenciano y castellano"),("Llig un llibre","Leo un libro"),("Treballe en una oficina","Trabajo en una oficina"),("Dorm huit hores","Duermo ocho horas")]),
  ("Presente II", [("vaig","voy"),("isc","salgo","Del verbo «eixir»."),("faig","hago"),("puc","puedo"),("vull","quiero"),("sé","sé"),("vinc","vengo"),("conec","conozco"),("dic","digo")],
   [("Isc de casa a les huit","Salgo de casa a las ocho"),("No sé on és","No sé dónde está"),("Vinc de la platja","Vengo de la playa"),("Vull aprendre valencià","Quiero aprender valenciano")]),
  ("Preguntas", [("què","qué"),("qui","quién"),("on","dónde"),("quan","cuándo"),("per què","por qué"),("com","cómo"),("quant","cuánto"),("quants","cuántos"),("quin","cuál / qué (+ nombre)"),("quina","cuál / qué (femenino)")],
   [("On és l'estació?","¿Dónde está la estación?","Para situar se usa «ser»: on és…?"),("Quant costa?","¿Cuánto cuesta?"),("Per què no véns?","¿Por qué no vienes?"),("Qui és eixe home?","¿Quién es ese hombre?")]),
  ("Conjugar «parlar»", [("jo","yo"),("tu","tú"),("ell","él"),("ella","ella"),("nosaltres","nosotros"),("vosaltres","vosotros"),("ells","ellos"),("parles","hablas"),("parla","habla"),("parlem","hablamos"),("parleu","habláis"),("parlen","hablan")],
   [("Nosaltres parlem valencià","Nosotros hablamos valenciano"),("Ella parla anglés","Ella habla inglés"),("Vosaltres parleu molt","Vosotros habláis mucho"),("Tu parles molt bé","Tú hablas muy bien")]),
 ]),
])
C["B1"] = ("Intermedio", [
 ("Pasado perifrástico", "#58cc02", [
  ("Vaig anar", [("vaig anar","fui","Pasado: «anar» conjugado + infinitivo."),("vas anar","fuiste"),("va anar","fue"),("vam anar","fuimos"),("vau anar","fuisteis"),("van anar","fueron")],
   [("Ahir vaig anar al mercat","Ayer fui al mercado"),("Vam anar a la platja dissabte","Fuimos a la playa el sábado"),("On vas anar ahir?","¿Adónde fuiste ayer?")]),
  ("Otros verbos", [("vaig menjar","comí"),("vaig vore","vi","«Vore» y «veure» son normativos.",["vaig veure"]),("vaig parlar","hablé"),("vaig dormir","dormí"),("vaig fer","hice"),("vaig tindre","tuve","También «vaig tenir».",["vaig tenir"]),("vaig poder","pude"),("vaig dir","dije")],
   [("Vam sopar a les deu","Cenamos a las diez"),("Vaig fer els deures","Hice los deberes"),("No vaig poder vindre","No pude venir"),("Vaig vore una pel·lícula","Vi una película")]),
  ("Marcadores de pasado", [("la setmana passada","la semana pasada"),("l'any passat","el año pasado"),("fa dos dies","hace dos días"),("anit","anoche"),("abans-d'ahir","anteayer"),("el mes passat","el mes pasado"),("una vegada","una vez")],
   [("Anit vaig dormir molt poc","Anoche dormí muy poco"),("L'any passat vam viatjar a Roma","El año pasado viajamos a Roma"),("Fa molt de temps que no et veig","Hace mucho tiempo que no te veo")]),
 ]),
 ("Futuro y condicional", "#1cb0f6", [
  ("Futuro", [("parlaré","hablaré"),("aniré","iré"),("faré","haré"),("eixiré","saldré"),("tindré","tendré"),("vindré","vendré"),("podré","podré"),("serà","será")],
   [("Demà aniré a la platja","Mañana iré a la playa"),("L'any que ve parlaré millor","El año que viene hablaré mejor"),("Vindré a les sis","Vendré a las seis")]),
  ("Condicional", [("voldria","querría"),("podria","podría"),("m'agradaria","me gustaría"),("hauries de","deberías"),("seria","sería"),("aniria","iría"),("faria","haría")],
   [("M'agradaria viatjar a Itàlia","Me gustaría viajar a Italia"),("Podries ajudar-me?","¿Podrías ayudarme?"),("Hauries de descansar","Deberías descansar")]),
  ("Planes", [("l'estiu que ve","el verano que viene"),("pròxim","próximo"),("potser","quizás"),("segurament","seguramente"),("tinc pensat","tengo pensado"),("algun dia","algún día"),("projecte","proyecto")],
   [("Si plou, em quedaré a casa","Si llueve, me quedaré en casa"),("Potser vindré demà","Quizás vendré mañana"),("Tinc pensat estudiar a l'estranger","Tengo pensado estudiar en el extranjero")]),
 ]),
 ("Opiniones y conectores", "#ce82ff", [
  ("Opinar", [("crec que","creo que"),("pense que","pienso que"),("estic d'acord","estoy de acuerdo"),("no estic d'acord","no estoy de acuerdo"),("al meu parer","en mi opinión"),("tens raó","tienes razón"),("em sembla que","me parece que")],
   [("Crec que tens raó","Creo que tienes razón"),("Em sembla que és massa car","Me parece que es demasiado caro"),("No estic d'acord amb tu","No estoy de acuerdo contigo")]),
  ("Conectores", [("però","pero"),("perquè","porque"),("així que","así que"),("a més","además"),("també","también"),("tampoc","tampoco"),("o","o")],
   [("No vaig eixir perquè plovia","No salí porque llovía"),("A mi tampoc m'agrada","A mí tampoco me gusta"),("Estava cansat, així que vaig dormir","Estaba cansado, así que dormí")]),
  ("Adverbios de tiempo", [("encara","todavía"),("ja","ya"),("mai","nunca"),("sempre","siempre"),("sovint","a menudo"),("de vegades","a veces"),("només","solo")],
   [("Encara no he dinat","Todavía no he comido"),("Mai no he estat a Londres","Nunca he estado en Londres"),("De vegades vaig a peu","A veces voy a pie")]),
 ]),
 ("Viajes", "#ff9600", [
  ("Transporte", [("bitllet","billete"),("estació","estación"),("tren","tren"),("aeroport","aeropuerto"),("autobús","autobús"),("andana","andén"),("eixida","salida"),("arribada","llegada"),("retard","retraso")],
   [("Un bitllet per a València, per favor","Un billete para Valencia, por favor"),("El tren porta retard","El tren lleva retraso"),("On és l'eixida?","¿Dónde está la salida?")]),
  ("Alojamiento", [("habitació doble","habitación doble"),("maleta","maleta"),("reserva","reserva"),("clau","llave"),("recepció","recepción"),("passaport","pasaporte"),("inclòs","incluido")],
   [("He reservat una habitació doble","He reservado una habitación doble"),("L'esmorzar està inclòs?","¿El desayuno está incluido?"),("He perdut la clau","He perdido la llave")]),
  ("Direcciones", [("a la dreta","a la derecha"),("a l'esquerra","a la izquierda"),("tot recte","todo recto"),("a prop","cerca"),("lluny","lejos"),("cantó","esquina"),("semàfor","semáforo"),("gira","gira")],
   [("L'hotel és a prop de la platja","El hotel está cerca de la playa"),("Gira a la dreta al semàfor","Gira a la derecha en el semáforo"),("És lluny d'ací?","¿Está lejos de aquí?")]),
 ]),
])
C["B2"] = ("Intermedio alto", [
 ("Trabajo", "#58cc02", [
  ("En la empresa", [("feina","trabajo (empleo)"),("empresa","empresa"),("cap","jefe"),("sou","sueldo"),("treballador","trabajador"),("oficina","oficina"),("company de treball","compañero de trabajo")],
   [("Busque feina de mestre","Busco trabajo de maestro"),("La meua empresa té cent treballadors","Mi empresa tiene cien trabajadores"),("El meu cap és molt exigent","Mi jefe es muy exigente")]),
  ("Organización", [("reunió","reunión"),("horari","horario"),("contracte","contrato"),("entrevista","entrevista"),("vacances","vacaciones"),("torn","turno"),("jornada","jornada")],
   [("Tinc una entrevista de treball dijous","Tengo una entrevista de trabajo el jueves"),("Tinc jornada completa","Tengo jornada completa"),("La reunió ha durat dues hores","La reunión ha durado dos horas")]),
  ("Buscar empleo", [("currículum","currículum"),("experiència","experiencia"),("aprofitar","aprovechar"),("sol·licitud","solicitud","Ela geminada: l·l."),("formació","formación"),("atur","paro"),("contractar","contratar")],
   [("Envie el currículum per correu","Envío el currículum por correo"),("Estic a l'atur des de març","Estoy en paro desde marzo"),("Volen contractar gent amb experiència","Quieren contratar gente con experiencia")]),
 ]),
 ("Salud", "#1cb0f6", [
  ("En el médico", [("metge","médico"),("malalt","enfermo"),("febre","fiebre"),("mal de cap","dolor de cabeza"),("panxa","barriga"),("gola","garganta"),("esquena","espalda"),("infermera","enfermera")],
   [("Em fa mal la panxa","Me duele la barriga"),("Tinc mal de gola","Me duele la garganta"),("M'ha pujat la febre","Me ha subido la fiebre")]),
  ("En la farmacia", [("farmàcia","farmacia"),("recepta","receta"),("pastilla","pastilla"),("tos","tos"),("xarop","jarabe"),("ferida","herida"),("urgències","urgencias"),("cita","cita")],
   [("Prenga una pastilla cada huit hores","Tome una pastilla cada ocho horas"),("Vull demanar cita amb el metge","Quiero pedir cita con el médico"),("Hem anat a urgències","Hemos ido a urgencias")]),
  ("Hábitos", [("descansar","descansar"),("fer exercici","hacer ejercicio"),("tinc son","tengo sueño"),("dieta","dieta"),("estrés","estrés"),("sa","sano"),("caminar","caminar")],
   [("Has de descansar més","Tienes que descansar más"),("Camine una hora cada dia","Camino una hora cada día"),("Menjar sa és important","Comer sano es importante")]),
 ]),
 ("Pronombres débiles I", "#ce82ff", [
  ("Complemento directo", [("el veig","lo veo"),("la veig","la veo"),("els compre","los compro"),("les compre","las compro"),("l'he vist","lo he visto"),("no la conec","no la conozco")],
   [("El llibre? Ja el tinc","¿El libro? Ya lo tengo"),("La pel·lícula? L'he vista dues vegades","¿La película? La he visto dos veces","Con «la», el participio concuerda: vista."),("Les claus? No les trobe","¿Las llaves? No las encuentro")]),
  ("Complemento indirecto", [("li dic","le digo"),("els escric","les escribo"),("li ho done","se lo doy"),("m'ho dius","me lo dices"),("et telefone","te llamo (por teléfono)"),("ens ajuden","nos ayudan")],
   [("Li ho done demà","Se lo doy mañana"),("Et telefone esta nit","Te llamo esta noche"),("Els escric un correu","Les escribo un correo")]),
  ("En e hi", [("en vull dos","quiero dos (de eso)","«En» sustituye a un nombre ya mencionado."),("hi vaig","voy (allí)","«Hi» = a ese lugar."),("n'hi ha","hay (de eso)"),("no en queda","no queda (de eso)"),("hi visc","vivo allí"),("en parle","hablo de ello")],
   [("Pa? No en queda","¿Pan? No queda"),("La platja? Hi vaig cada estiu","¿La playa? Voy cada verano"),("Hi ha molta gent","Hay mucha gente")]),
 ]),
 ("Conectores avanzados", "#ff9600", [
  ("Contraste", [("tanmateix","sin embargo"),("per tant","por lo tanto"),("mentre","mientras"),("malgrat","a pesar de"),("encara que","aunque"),("ja que","ya que")],
   [("Malgrat la pluja, vam eixir","A pesar de la lluvia, salimos"),("Ja que estàs ací, ajuda'm","Ya que estás aquí, ayúdame"),("Mentre cuine, escolte la ràdio","Mientras cocino, escucho la radio")]),
  ("Precisar", [("sinó","sino"),("és a dir","es decir"),("en canvi","en cambio"),("de fet","de hecho"),("per exemple","por ejemplo"),("sobretot","sobre todo")],
   [("No és roig sinó taronja","No es rojo sino naranja"),("M'agrada la fruita, sobretot la taronja","Me gusta la fruta, sobre todo la naranja"),("Ell és alt; en canvi, el seu germà és baix","Él es alto; en cambio, su hermano es bajo")]),
  ("Organizar un texto", [("d'una banda","por un lado"),("d'altra banda","por otro lado"),("en resum","en resumen"),("finalment","finalmente"),("en primer lloc","en primer lugar"),("a continuació","a continuación"),("per acabar","para terminar")],
   [("En resum, la proposta és bona","En resumen, la propuesta es buena"),("En primer lloc, vull donar-vos les gràcies","En primer lugar, quiero daros las gracias"),("Per acabar, una pregunta","Para terminar, una pregunta")]),
 ]),
])
C["C1"] = ("Avanzado", [
 ("Frases hechas", "#58cc02", [
  ("Expresiones I", [("fer-se el desentés","hacerse el sueco","Coloquial también «fer-se el longui»."),("ploure a bots i barrals","llover a cántaros"),("anar de bòlit","ir muy liado"),("parlar pels colzes","hablar por los codos"),("estar fet pols","estar hecho polvo"),("no tindre pèls a la llengua","no tener pelos en la lengua")],
   [("Esta setmana vaig de bòlit","Esta semana voy muy liado"),("Ma mare no té pèls a la llengua","Mi madre no tiene pelos en la lengua"),("Plou a bots i barrals","Llueve a cántaros")]),
  ("Expresiones II", [("fer campana","hacer novillos"),("costar un ull de la cara","costar un ojo de la cara"),("tindre la mosca darrere l'orella","tener la mosca detrás de la oreja"),("estar com una cabra","estar como una cabra"),("tirar la casa per la finestra","tirar la casa por la ventana")],
   [("Este cotxe costa un ull de la cara","Este coche cuesta un ojo de la cara"),("Per Falles tiren la casa per la finestra","En Fallas tiran la casa por la ventana"),("Està com una cabra","Está como una cabra")]),
  ("Refranes", [("qui matina fa farina","a quien madruga Dios le ayuda"),("qui no plora no mama","quien no llora no mama"),("a poc a poc s'arriba lluny","poco a poco se llega lejos"),("de mica en mica s'omple la pica","poco a poco se llena el saco"),("més val pardal en mà que cent volant","más vale pájaro en mano que ciento volando"),("refrany","refrán")],
   [("A poc a poc s'arriba lluny","Poco a poco se llega lejos"),("De mica en mica s'omple la pica","Poco a poco se llena el saco"),("Qui matina fa farina","A quien madruga Dios le ayuda")]),
 ]),
 ("Subjuntivo", "#1cb0f6", [
  ("Presente de subjuntivo", [("vull que vingues","quiero que vengas"),("que siga","que sea"),("és possible que ploga","es posible que llueva"),("espere que","espero que"),("potser vinga","quizás venga")],
   [("Espere que tingues un bon dia","Espero que tengas un buen día"),("Vull que m'ho expliques","Quiero que me lo expliques"),("És possible que demà ploga","Es posible que mañana llueva")]),
  ("Imperfecto de subjuntivo", [("si tinguera","si tuviera","En valenciano es habitual -ra (tinguera); «tingués» también es normativo."),("si poguera","si pudiera"),("si fóra","si fuera"),("com si","como si"),("si haguera sabut","si hubiera sabido")],
   [("Si tinguera temps, llegiria més","Si tuviera tiempo, leería más"),("Parla com si ho sabera tot","Habla como si lo supiera todo"),("Si fóra ric, viatjaria","Si fuera rico, viajaría")]),
  ("Indicativo o subjuntivo", [("crec que ve","creo que viene"),("no crec que vinga","no creo que venga"),("quan arribes","cuando llegues"),("encara que ploga","aunque llueva"),("és veritat que","es verdad que")],
   [("Avisa'm quan arribes","Avísame cuando llegues"),("No crec que vinga hui","No creo que venga hoy"),("Encara que ploga, eixirem","Aunque llueva, saldremos")]),
 ]),
 ("Registro formal y AVL", "#ce82ff", [
  ("Cartas formales", [("vosté","usted"),("benvolgut senyor","estimado señor"),("benvolguda senyora","estimada señora"),("atentament","atentamente"),("sol·licite","solicito"),("salutacions cordials","saludos cordiales")],
   [("Li agrairia una resposta","Le agradecería una respuesta"),("Li escric per a sol·licitar informació","Le escribo para solicitar información"),("Quede a la seua disposició","Quedo a su disposición")]),
  ("Formas valencianas I", [("xicotet","pequeño","Junto a «petit», ambas normativas."),("eixir","salir","Junto a «sortir»."),("espill","espejo","Junto a «mirall»."),("hui","hoy","Forma valenciana de «avui»."),("este","este","Junto a «aquest»."),("eixe","ese","Junto a «aqueix»; «eixe» es el habitual.")],
   [("Eixim a les huit","Salimos a las ocho"),("Este xiquet és molt xicotet","Este niño es muy pequeño"),("Eixe espill és nou","Ese espejo es nuevo")]),
  ("Formas valencianas II", [("servici","servicio","La AVL admite «servici» y «servei»."),("la meua","la mía / mi","Valenciano: meua, teua, seua."),("vore","ver","«Vore» y «veure» son normativos.",["veure"]),("estudie","estudio (yo)","1.ª persona del presente en -e."),("tindre","tener","También «tenir».",["tenir"]),("vindre","venir","También «venir».",["venir"])],
   [("Hui estudie a la biblioteca","Hoy estudio en la biblioteca"),("Has de vindre demà","Tienes que venir mañana"),("Vull vore la teua casa","Quiero ver tu casa")]),
 ]),
 ("Cultura valenciana", "#ff9600", [
  ("Las Fallas", [("falla","falla (monumento)"),("mascletà","mascletà (traca de mediodía)"),("cremà","cremà (quema final)"),("ninot","ninot (figura)"),("plantà","plantà (montaje de la falla)"),("ofrena","ofrenda"),("casal","casal (sede de la falla)")],
   [("La cremà és la nit del dènou de març","La cremà es la noche del diecinueve de marzo"),("L'ofrena és a la plaça de la Mare de Déu","La ofrenda es en la plaza de la Virgen"),("La mascletà comença a les dues","La mascletà empieza a las dos")]),
  ("Tradiciones", [("horta","huerta"),("orxata","horchata"),("xufa","chufa"),("Tribunal de les Aigües","Tribunal de las Aguas"),("all i pebre","all i pebre (guiso de anguila)"),("fartons","fartons (bollos para la horchata)"),("Albufera","Albufera")],
   [("L'orxata es fa amb xufa","La horchata se hace con chufa"),("L'all i pebre es fa amb anguila","El all i pebre se hace con anguila"),("El Tribunal de les Aigües es reuneix els dijous","El Tribunal de las Aguas se reúne los jueves")]),
  ("Literatura I", [("Ausiàs March","poeta valenciano del siglo XV"),("Tirant lo Blanc","novela caballeresca de Joanot Martorell"),("Vicent Andrés Estellés","poeta valenciano del siglo XX"),("Joan Fuster","ensayista de Sueca"),("Teodor Llorente","poeta de la Renaixença valenciana")],
   [("Tirant lo Blanc és una novel·la de cavalleries","Tirant lo Blanc es una novela de caballerías"),("Ausiàs March va escriure poesia amorosa","Ausiàs March escribió poesía amorosa"),("Joan Fuster va nàixer a Sueca","Joan Fuster nació en Sueca")]),
 ]),
])
C["C2"] = ("Maestría", [
 ("Falsos amigos", "#58cc02", [
  ("Cuerpo y casa", [("cama","pierna","¡Ojo! No es «cama»."),("llit","cama (mueble)"),("constipat","resfriado","No significa «estreñido»."),("tasca","tarea","No es un bar."),("acostar","acercar","«Acostar-se» = acercarse."),("embolicar","envolver")],
   [("M'he trencat la cama","Me he roto la pierna"),("Acosta't, que no et sent","Acércate, que no te oigo"),("Embolica el regal","Envuelve el regalo")]),
  ("Verbos traicioneros", [("escurar","fregar los platos"),("fregar","frotar"),("llevar","quitar","En valenciano «llevar» = quitar."),("portar","llevar / traer")],
   [("Lleva't la jaqueta","Quítate la chaqueta"),("Escura els plats, per favor","Friega los platos, por favor"),("Porta'm un got d'aigua","Tráeme un vaso de agua")]),
  ("Cuantificadores", [("prou","bastante / suficiente"),("massa","demasiado"),("gens","nada (de)","En frases negativas: no tinc gens de…"),("res","nada"),("gaire","mucho (en negativas)"),("cap","ningún / ninguna")],
   [("No tinc gens de son","No tengo nada de sueño"),("No en queda gaire","No queda mucho"),("Ja n'hi ha prou!","¡Ya basta!")]),
 ]),
 ("Pronombres débiles avanzados", "#1cb0f6", [
  ("Combinaciones", [("te'l done","te lo doy"),("me la deixes?","¿me la dejas?"),("li'n done dos","le doy dos (de ellos)"),("l'hi porte","se lo llevo (a él/ella)"),("els ho explique","se lo explico (a ellos)")],
   [("Te'l porte demà","Te lo traigo mañana"),("Me la deixes un moment?","¿Me la dejas un momento?"),("Els ho explicaré demà","Se lo explicaré mañana")]),
  ("Imperativo", [("dona-li-ho","dáselo"),("digues-m'ho","dímelo"),("fes-ho","hazlo"),("anem-nos-en","vámonos"),("dona-me'n","dame (de eso)")],
   [("Digues-m'ho clar","Dímelo claro"),("Fes-ho ara mateix","Hazlo ahora mismo"),("Anem-nos-en, que és tard","Vámonos, que es tarde")]),
  ("En e hi avanzados", [("me'n recorde","me acuerdo (de eso)"),("ens n'anem","nos vamos"),("no hi pense","no pienso en ello"),("hi ha","hay"),("se n'ha anat","se ha ido")],
   [("Ja me'n recorde","Ya me acuerdo"),("Se n'ha anat sense dir res","Se ha ido sin decir nada"),("Hi ha massa gent","Hay demasiada gente")]),
 ]),
 ("Matices y registro", "#ce82ff", [
  ("Subjuntivo avanzado", [("per molt que","por mucho que"),("sense que","sin que"),("abans que","antes de que"),("tant si plou com si no","llueva o no"),("fins que","hasta que")],
   [("Per molt que ho intente, no ho entenc","Por mucho que lo intento, no lo entiendo"),("Ho repetiré fins que ho aprengues","Lo repetiré hasta que lo aprendas"),("Ix sense que ningú et veja","Sal sin que nadie te vea")]),
  ("Registro culto", [("àdhuc","incluso"),("llevat de","excepto"),("així mateix","asimismo"),("tot i que","aunque"),("nogensmenys","no obstante")],
   [("Tots hi eren, llevat de Joan","Estaban todos, excepto Juan"),("Àdhuc els xiquets ho saben","Incluso los niños lo saben"),("Tot i que plovia, vam eixir","Aunque llovía, salimos")]),
  ("Administración", [("instància","instancia"),("expedient","expediente"),("termini","plazo"),("tràmit","trámite"),("registre","registro"),("al·legació","alegación")],
   [("El termini acaba el divendres","El plazo acaba el viernes"),("Cal presentar la instància al registre","Hay que presentar la instancia en el registro"),("Han resolt l'expedient","Han resuelto el expediente")]),
 ]),
 ("Cultura avanzada", "#ff9600", [
  ("Refranes II", [("qui té boca s'equivoca","quien tiene boca se equivoca"),("no digues blat fins que no estiga al sac","no vendas la piel del oso antes de cazarlo"),("fer-ne un gra massa","pasarse de la raya"),("a cada porc li arriba el seu sant Martí","a cada cerdo le llega su San Martín"),("cadascú","cada uno")],
   [("Qui té boca s'equivoca","Quien tiene boca se equivoca"),("No digues blat fins que no estiga al sac","No vendas la piel del oso antes de cazarlo"),("A cada porc li arriba el seu sant Martí","A cada cerdo le llega su San Martín")]),
  ("Literatura II", [("Isabel de Villena","abadesa y autora de «Vita Christi»"),("Enric Valor","autor de rondalles valencianas"),("rondalla","cuento popular"),("Segle d'Or","Siglo de Oro valenciano (s. XV)"),("Joan Roís de Corella","prosista valenciano del siglo XV")],
   [("Enric Valor va recollir rondalles","Enric Valor recopiló cuentos populares"),("Isabel de Villena va escriure Vita Christi","Isabel de Villena escribió Vita Christi"),("El Segle d'Or valencià és el segle XV","El Siglo de Oro valenciano es el siglo XV")]),
  ("La lengua", [("Acadèmia Valenciana de la Llengua","institución normativa del valenciano"),("Normes de Castelló","normas ortográficas de 1932"),("llengua","lengua"),("normatiu","normativo"),("Estatut d'Autonomia","Estatuto de Autonomía")],
   [("Les Normes de Castelló són de 1932","Las Normas de Castelló son de 1932"),("L'AVL va ser creada l'any 1998","La AVL fue creada en 1998"),("La llengua és patrimoni de tots","La lengua es patrimonio de todos")]),
 ]),
])

# ---------------------------------------------------------------------------
# v18: units aligned with the official A1–A2 path (Ajuntament de Finestrat course used only as a
# topic/sequence reference; all text below is original). New units carry a 4th element = stable slug:
# their lesson ids are "<level>-<slug>-<n>", so the positional ids of the existing units never change.
# Insert them anywhere; old units keep their positional numbering (counted over old units only).
NEW = {
 "lletres": ("Letras y sonidos", "#ff4b4b", [
  ("El alfabeto I", [("a","la letra a"),("be","la letra b","También «be alta»."),("ce","la letra c"),("de","la letra d"),("e","la letra e"),("efe","la letra f"),("ge","la letra g"),("hac","la letra h","La h no suena: hola, home."),("i","la letra i"),("jota","la letra j")],
   [("A de arròs","A de arroz"),("Com s'escriu?","¿Cómo se escribe?"),("S'escriu amb hac","Se escribe con hache"),("Pots lletrejar-ho?","¿Puedes deletrearlo?","«Lletrejar» = deletrear.")]),
  ("El alfabeto II", [("ca","la letra k"),("ele","la letra l"),("eme","la letra m"),("ene","la letra n"),("pe","la letra p"),("cu","la letra q"),("erre","la letra r"),("esse","la letra s"),("te","la letra t"),("ve","la letra v","También «ve baixa»."),("ics","la letra x"),("zeta","la letra z")],
   [("S'escriu amb ve","Se escribe con uve"),("Erre, a, ics","Erre, a, equis"),("El meu nom s'escriu amb zeta","Mi nombre se escribe con zeta"),("Ics de xocolate","Equis de chocolate")]),
  ("Deletrear", [("lletrejar","deletrear"),("lletra","letra"),("majúscula","mayúscula"),("minúscula","minúscula"),("ela geminada","ele geminada (l·l)","Se escribe con punto volado: col·legi."),("ce trencada","ce con cedilla (ç)","Como en «plaça»."),("apòstrof","apóstrofo","Como en «l'home»."),("guionet","guion"),("dièresi","diéresis (ï, ü)","Como en «veïna».")],
   [("Amb majúscula, per favor","Con mayúscula, por favor"),("Plaça porta ce trencada","Plaza lleva ce con cedilla"),("Col·legi porta ela geminada","Colegio lleva ele geminada"),("Pots repetir la lletra?","¿Puedes repetir la letra?")]),
  ("Los acentos", [("accent","acento"),("accent obert","acento abierto (à, è, ò)","Vocal abierta: cafè no; café sí, porque la e es cerrada."),("accent tancat","acento cerrado (é, í, ó, ú)"),("vocal","vocal"),("síl·laba","sílaba"),("aguda","aguda"),("també","también","Aguda acabada en vocal: lleva acento."),("cançó","canción","Aguda acabada en -on: lleva acento."),("però","pero"),("més","más","Acento diacrítico: «més» (más) / «mes» (mes).")],
   [("Café porta accent tancat","Café lleva acento cerrado"),("Això porta accent obert","Esto lleva acento abierto"),("Soc no porta accent","Soc no lleva acento","Desde 2018 la AVL escribe «soc» sin acento."),("Vull més pa","Quiero más pan")]),
 ]),
 "dades": ("Datos personales", "#00cd9c", [
  ("Edad y dirección", [("quants anys tens?","¿cuántos años tienes?"),("tinc trenta anys","tengo treinta años"),("adreça","dirección"),("número","número"),("pis","piso (planta)"),("porta","puerta"),("codi postal","código postal"),("correu electrònic","correo electrónico"),("data de naixement","fecha de nacimiento"),("nàixer","nacer","Forma valenciana (DNV: nàixer/néixer).",["néixer"])],
   [("Quina és la teua adreça?","¿Cuál es tu dirección?"),("Visc al carrer Major, número cinc","Vivo en la calle Mayor, número cinco"),("Vaig nàixer al maig","Nací en mayo"),("Em dones el teu correu electrònic?","¿Me das tu correo electrónico?")]),
  ("Países y nacionalidades", [("Espanya","España"),("França","Francia"),("Anglaterra","Inglaterra"),("Alemanya","Alemania"),("Itàlia","Italia"),("espanyol","español","Femenino: espanyola."),("francés","francés","Femenino: francesa. DNV: francés (también francès).",["francès"]),("anglés","inglés","Femenino: anglesa.",["anglès"]),("alemany","alemán","Femenino: alemanya."),("italià","italiano","Femenino: italiana.")],
   [("Soc francesa, de París","Soy francesa, de París"),("Ell és alemany","Él es alemán"),("Parle anglés i espanyol","Hablo inglés y español"),("La meua parella és italiana","Mi pareja es italiana")]),
  ("Estado civil", [("parella","pareja"),("casat","casado","Femenino: casada."),("solter","soltero","Femenino: soltera."),("divorciat","divorciado","Femenino: divorciada."),("nóvio","novio","Femenino: nóvia."),("marit","marido"),("dona","mujer / esposa"),("amic","amigo","Femenino: amiga."),("company","compañero","Femenino: companya.")],
   [("Estic casada i tinc dos fills","Estoy casada y tengo dos hijos"),("Ell és solter","Él es soltero"),("Visc amb la meua parella","Vivo con mi pareja"),("És un amic de la feina","Es un amigo del trabajo","DNV: «faena» (forma principal) o «feina».")]),
 ]),
 "gram1": ("Gramática básica", "#2b70c9", [
  ("Artículos y apóstrofo", [("el","el"),("la","la"),("els","los"),("les","las"),("l'home","el hombre","Delante de vocal o h: l'."),("l'amiga","la amiga","«La» también se apostrofa: l'amiga."),("la illa","la isla","No se apostrofa «la» ante i/u átonas: la illa, la universitat."),("la universitat","la universidad"),("un","un"),("unes","unas")],
   [("L'home i la dona","El hombre y la mujer"),("L'amiga de la meua germana","La amiga de mi hermana"),("La illa és xicoteta","La isla es pequeña"),("Els xiquets i les xiquetes","Los niños y las niñas")]),
  ("Contracciones", [("al","al (a + el)"),("als","a los (a + els)"),("del","del (de + el)"),("dels","de los (de + els)"),("pel","por el (per + el)"),("pels","por los (per + els)"),("a la","a la (no se contrae)"),("de l'","de la / del (ante vocal)","Ante vocal no hay contracción: de l'home.")],
   [("Vaig al mercat","Voy al mercado"),("Venim del poble","Venimos del pueblo"),("Passegem pel parc","Paseamos por el parque"),("La casa de l'iaio","La casa del abuelo")]),
  ("Posesivos", [("el teu","tu (masculino)"),("la teua","tu (femenino)"),("el seu","su (masculino)"),("la seua","su (femenino)"),("el nostre","nuestro"),("la nostra","nuestra"),("el vostre","vuestro"),("els meus","mis (masculino)"),("les meues","mis (femenino)")],
   [("La teua casa és molt gran","Tu casa es muy grande"),("El nostre pare treballa a València","Nuestro padre trabaja en Valencia"),("Les meues amigues viuen ací","Mis amigas viven aquí"),("És el vostre cotxe?","¿Es vuestro coche?")]),
  ("Femenino y plural", [("xic","chico","Femenino: xica."),("xica","chica"),("gat","gato"),("gata","gata"),("llibre","libro"),("llibres","libros"),("cases","casas","-a → -es: casa, cases."),("peixos","peces","Tras -s, -x, -ç: -os."),("nou","nuevo","Femenino: nova."),("nova","nueva")],
   [("Dos llibres nous","Dos libros nuevos"),("Tres cases noves","Tres casas nuevas"),("La xica és nova","La chica es nueva"),("Tinc dues gates","Tengo dos gatas")]),
  ("Concordancia", [("blanca","blanca"),("blancs","blancos"),("blanques","blancas","-ca → -ques."),("alta","alta"),("alts","altos"),("altes","altas"),("bonic","bonito","Femenino: bonica."),("bonics","bonitos"),("bonica","bonita"),("boniques","bonitas")],
   [("Una casa blanca","Una casa blanca"),("Unes sabates blanques","Unos zapatos blancos"),("Els meus germans són alts","Mis hermanos son altos"),("Les flors són boniques","Las flores son bonitas")]),
 ]),
 "mercat": ("Mercado y horno", "#ff9600", [
  ("En el mercado", [("mercat","mercado"),("parada","puesto (del mercado)"),("quilo","kilo"),("mig quilo","medio kilo"),("dotzena","docena"),("paquet","paquete"),("pot","bote / tarro"),("bossa","bolsa"),("botella","botella"),("res més?","¿algo más?")],
   [("Un quilo de tomaques, per favor","Un kilo de tomates, por favor"),("Mig quilo de cireres","Medio kilo de cerezas"),("Una dotzena d'ous","Una docena de huevos"),("Res més, gràcies","Nada más, gracias")]),
  ("Carne y pescado", [("carnisseria","carnicería"),("peixateria","pescadería"),("pollastre","pollo"),("porc","cerdo"),("vedella","ternera"),("corder","cordero"),("sardina","sardina"),("lluç","merluza"),("gamba","gamba"),("calamar","calamar")],
   [("Vull un pollastre sencer","Quiero un pollo entero"),("Mig quilo de lluç","Medio kilo de merluza"),("No menge porc","No como cerdo"),("Les sardines són fresques?","¿Las sardinas son frescas?")]),
  ("En el horno", [("forn","horno / panadería","En Valencia la panadería es «el forn»."),("barra de pa","barra de pan"),("pa integral","pan integral"),("coca","coca (masa horneada)"),("pastís","pastel / tarta"),("magdalena","magdalena"),("galeta","galleta"),("ensaïmada","ensaimada"),("pastisseria","pastelería"),("dolç","dulce","Femenino: dolça.")],
   [("Una barra de pa, per favor","Una barra de pan, por favor"),("Vaig al forn","Voy al horno"),("M'agraden les coses dolces","Me gustan las cosas dulces"),("Un pastís de xocolate","Un pastel de chocolate")]),
 ]),
 "aficions": ("Aficiones y deportes", "#ce82ff", [
  ("Me gusta", [("afició","afición"),("m'encanta","me encanta"),("no m'agrada gens","no me gusta nada"),("llegir","leer"),("cantar","cantar"),("ballar","bailar"),("pintar","pintar"),("música","música"),("pel·lícula","película"),("temps lliure","tiempo libre")],
   [("M'encanta llegir","Me encanta leer"),("No m'agrada gens ballar","No me gusta nada bailar"),("En el temps lliure pinte","En el tiempo libre pinto"),("Quina és la teua afició?","¿Cuál es tu afición?")]),
  ("Deportes", [("esport","deporte"),("futbol","fútbol"),("bàsquet","baloncesto"),("tenis","tenis"),("nadar","nadar"),("córrer","correr"),("piscina","piscina"),("equip","equipo"),("partit","partido"),("guanyar","ganar")],
   [("Faig esport cada dia","Hago deporte cada día"),("Vaig a nadar a la piscina","Voy a nadar a la piscina"),("El meu equip ha guanyat","Mi equipo ha ganado"),("Diumenge hi ha partit de futbol","El domingo hay partido de fútbol")]),
  ("Con qué frecuencia", [("sempre","siempre"),("sovint","a menudo"),("de vegades","a veces"),("mai","nunca"),("cada setmana","cada semana"),("una vegada","una vez"),("dues vegades","dos veces"),("pilota","pelota"),("bicicleta","bicicleta"),("caminar","caminar")],
   [("Sempre camine pel matí","Siempre camino por la mañana"),("De vegades jugue a tenis","A veces juego al tenis"),("Mai faig esport","Nunca hago deporte"),("Vaig en bicicleta dues vegades per setmana","Voy en bicicleta dos veces por semana")]),
 ]),
 "receptes": ("Recetas e instrucciones", "#ff4b4b", [
  ("Imperativo en la cocina", [("talla","corta (tú)","Imperativo de «tallar»."),("pela","pela"),("posa","pon"),("afig","añade","Imperativo de «afegir»."),("remena","remueve"),("bull","hierve","Imperativo de «bullir»."),("fregix","fríe","Imperativo de «fregir»."),("tasta","prueba"),("servix","sirve","Imperativo de «servir»."),("no cremes","no quemes","Imperativo negativo: no + subjuntivo.")],
   [("Pela les creïlles","Pela las patatas"),("Afig un poc de sal","Añade un poco de sal"),("Talla la ceba ben fina","Corta la cebolla bien fina"),("No cremes l'arròs","No quemes el arroz")]),
  ("Una receta", [("recepta","receta"),("ingredient","ingrediente"),("cassola","cazuela"),("olla","olla"),("paella","paella (sartén / plato)"),("cullera","cuchara"),("ganivet","cuchillo"),("minut","minuto"),("primer","primero"),("després","después")],
   [("Primer, escalfa l'oli","Primero, calienta el aceite"),("Després, posa la verdura","Después, pon la verdura"),("Deixa-ho deu minuts","Déjalo diez minutos"),("Servix-ho calent","Sírvelo caliente")]),
  ("Haver de", [("he de","tengo que"),("has de","tienes que"),("ha de","tiene que"),("hem de","tenemos que"),("heu de","tenéis que"),("han de","tienen que"),("s'ha de","hay que (se debe)"),("cal","hace falta / hay que"),("no cal","no hace falta")],
   [("He de comprar pa","Tengo que comprar pan"),("Hem de netejar la cuina","Tenemos que limpiar la cocina"),("S'ha de bullir vint minuts","Hay que hervirlo veinte minutos"),("No cal afegir sal","No hace falta añadir sal")]),
 ]),
 "perfet": ("¿Qué ha pasado?", "#58cc02", [
  ("El participio", [("parlat","hablado"),("menjat","comido"),("begut","bebido"),("fet","hecho"),("vist","visto"),("dit","dicho"),("escrit","escrito"),("llegit","leído"),("obert","abierto"),("estat","estado")],
   [("He parlat amb ma mare","He hablado con mi madre"),("Has vist la pel·lícula?","¿Has visto la película?"),("Ja hem menjat","Ya hemos comido"),("Qui ha obert la finestra?","¿Quién ha abierto la ventana?")]),
  ("He menjat", [("he","he"),("has","has"),("ha","ha"),("hem","hemos"),("heu","habéis"),("han","han"),("he fet","he hecho"),("has dormit","has dormido"),("hem arribat","hemos llegado"),("han eixit","han salido")],
   [("Hui he fet moltes coses","Hoy he hecho muchas cosas"),("Has dormit bé?","¿Has dormido bien?"),("Hem arribat tard","Hemos llegado tarde"),("Els xiquets han eixit al pati","Los niños han salido al patio")]),
  ("Hoy o ayer", [("este matí","esta mañana"),("esta setmana","esta semana"),("ja","ya"),("encara no","todavía no"),("alguna vegada","alguna vez"),("mai","nunca"),("ahir vaig menjar","ayer comí","Tiempo terminado → vaig + infinitivo."),("hui he menjat","hoy he comido","Tiempo no terminado (hui, este matí) → he + participio."),("què ha passat?","¿qué ha pasado?")],
   [("Este matí he esmorzat a casa","Esta mañana he desayunado en casa"),("Ahir vaig sopar amb amics","Ayer cené con amigos"),("Encara no he acabat","Todavía no he terminado"),("Has estat alguna vegada a Alacant?","¿Has estado alguna vez en Alicante?")]),
 ]),
 "mitjans": ("Noticias y medios", "#1cb0f6", [
  ("Los medios", [("diari","periódico"),("notícia","noticia"),("ràdio","radio"),("televisió","televisión"),("periodista","periodista"),("titular","titular"),("revista","revista"),("xarxes socials","redes sociales"),("informatiu","informativo"),("entrevista","entrevista")],
   [("Llig el diari cada matí","Leo el periódico cada mañana"),("Has vist la notícia?","¿Has visto la noticia?"),("Escolte la ràdio al cotxe","Escucho la radio en el coche"),("Ho he llegit a les xarxes socials","Lo he leído en las redes sociales")]),
  ("Sucesos", [("accident","accidente"),("incendi","incendio"),("trànsit","tráfico"),("policia","policía"),("ferit","herido","Femenino: ferida."),("tempesta","tormenta"),("carretera","carretera"),("segons","según"),("ha passat","ha pasado"),("ahir a la nit","anoche")],
   [("Hi ha hagut un accident a la carretera","Ha habido un accidente en la carretera"),("Segons la ràdio, hi ha molt de trànsit","Según la radio, hay mucho tráfico"),("No hi ha ferits","No hay heridos"),("La tempesta ha tallat la carretera","La tormenta ha cortado la carretera")]),
  ("Opinar sobre noticias", [("crec que","creo que"),("estic d'acord","estoy de acuerdo"),("no estic d'acord","no estoy de acuerdo"),("tens raó","tienes razón"),("és veritat","es verdad"),("és mentida","es mentira"),("potser","quizás"),("segur","seguro"),("per a mi","para mí")],
   [("Crec que és mentida","Creo que es mentira"),("Tens raó, és veritat","Tienes razón, es verdad"),("No estic d'acord amb el titular","No estoy de acuerdo con el titular"),("Potser té raó","Quizás tiene razón")]),
 ]),
 "eines": ("Herramientas y aparatos", "#ff9600", [
  ("Herramientas", [("eina","herramienta"),("martell","martillo"),("tornavís","destornillador"),("tisores","tijeras"),("clau","clavo / llave"),("cargol","tornillo / caracol"),("cinta","cinta"),("caixa d'eines","caja de herramientas"),("penjar","colgar"),("arreglar","arreglar")],
   [("Em deixes el martell?","¿Me dejas el martillo?"),("Necessite un tornavís per a arreglar-ho","Necesito un destornillador para arreglarlo"),("Les tisores són al calaix","Las tijeras están en el cajón"),("Per a què servix això?","¿Para qué sirve esto?","«Servir» → servix.")]),
  ("Aparatos de casa", [("aparell","aparato"),("microones","microondas"),("rentaplats","lavavajillas"),("assecador","secador"),("planxa","plancha"),("endoll","enchufe"),("carregador","cargador"),("encendre","encender"),("apagar","apagar"),("funcionar","funcionar")],
   [("El microones no funciona","El microondas no funciona"),("Apaga la planxa, per favor","Apaga la plancha, por favor"),("On és el carregador del mòbil?","¿Dónde está el cargador del móvil?"),("Encén el rentaplats","Enciende el lavavajillas")]),
 ]),
 "cotxe": ("Coches y reclamaciones", "#ce82ff", [
  ("El coche y la bici", [("cotxe","coche"),("roda","rueda"),("volant","volante"),("fre","freno"),("gasolina","gasolina"),("conduir","conducir"),("aparcar","aparcar"),("carnet de conduir","carné de conducir"),("taller","taller"),("avaria","avería")],
   [("El cotxe té una avaria","El coche tiene una avería"),("No sé on aparcar","No sé dónde aparcar"),("He portat el cotxe al taller","He llevado el coche al taller"),("La bicicleta no té fre","La bicicleta no tiene freno")]),
  ("Hacer una reclamación", [("reclamació","reclamación"),("queixa","queja"),("full de reclamacions","hoja de reclamaciones"),("factura","factura"),("tiquet","tique"),("garantia","garantía"),("canviar","cambiar"),("tornar els diners","devolver el dinero"),("trencat","roto","Femenino: trencada."),("responsable","responsable")],
   [("Vull fer una reclamació","Quiero hacer una reclamación"),("Este aparell està trencat","Este aparato está roto"),("Encara té garantia","Todavía tiene garantía"),("Em poden tornar els diners?","¿Me pueden devolver el dinero?")]),
 ]),
 "medi": ("Medio ambiente", "#58cc02", [
  ("Reciclar", [("medi ambient","medio ambiente"),("reciclar","reciclar"),("contenidor","contenedor"),("vidre","vidrio"),("paper","papel"),("plàstic","plástico"),("envàs","envase","Plural: envasos."),("residus","residuos"),("reutilitzar","reutilizar"),("reduir","reducir")],
   [("El vidre va al contenidor verd","El vidrio va al contenedor verde"),("Hem de reciclar més","Tenemos que reciclar más"),("Reutilitze les bosses","Reutilizo las bolsas"),("Cal reduir el plàstic","Hay que reducir el plástico")]),
  ("Cuidar el planeta", [("contaminació","contaminación"),("energia","energía"),("estalviar","ahorrar"),("aigua","agua"),("llum","luz"),("arbre","árbol"),("natura","naturaleza"),("transport públic","transporte público"),("calor","calor"),("canvi climàtic","cambio climático")],
   [("Estalvia aigua i llum","Ahorra agua y luz"),("Vaig a la feina en transport públic","Voy al trabajo en transporte público","DNV: «faena» o «feina»."),("La contaminació és un problema","La contaminación es un problema"),("Si plantem arbres, hi haurà menys calor","Si plantamos árboles, habrá menos calor")]),
 ]),
}
# placement: (level, insert before the existing unit with this title or None = append at end of level)
PLACE = [("A1","lletres","Números"),("A1","dades","Números"),("A1","gram1","Comida"),("A1","mercat",None),("A1","aficions",None),
         ("A2","receptes","Verbos y preguntas"),("A2","perfet",None),("A2","mitjans",None),("A2","eines",None),("A2","cotxe",None),("A2","medi",None)]
for lv, slug, before in PLACE:
    units = C[lv][1]; u = NEW[slug] + (slug,)
    if before is None: units.append(u)
    else: units.insert([x[0] for x in units].index(before), u)
