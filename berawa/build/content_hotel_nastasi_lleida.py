# Contenido de la demo Hotel Nastasi (Lleida) (es/en/fr/de). Hechos de hotelnastasi.com leidos el 02/11/2026 (ver berawa/sources.json). Tono sobrio: las suites tematicas se describen sin sus nombres; sin precios, sin valoraciones; nada sobre mascotas (la web se contradice).
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Habitaciones estándar','Junior suites y suites temáticas'],'en':['Standard rooms','Junior suites and themed suites'],'fr':['Chambres standard','Junior suites et suites thématiques'],'de':['Standardzimmer','Junior-Suiten und Themensuiten']}
RD={
'es':['Doble con dos camas, triple, cuádruple interior y habitación con cama matrimonial: opciones para viajar en pareja, con amigos o en familia.','Cada suite tiene su propia ambientación. Son solo para adultos y se reservan exclusivamente por teléfono, en el 973 249 222.'],
'en':['Double with two beds, triple, interior quadruple and a room with a double bed: options for couples, friends or families.','Each suite has its own setting. They are adults only and are booked exclusively by phone, on 973 249 222.'],
'fr':['Double à deux lits, triple, quadruple intérieure et chambre avec lit double : des options pour voyager en couple, entre amis ou en famille.','Chaque suite a sa propre ambiance. Elles sont réservées aux adultes et se réservent exclusivement par téléphone, au 973 249 222.'],
'de':['Doppelzimmer mit zwei Betten, Dreibettzimmer, innenliegendes Vierbettzimmer und Zimmer mit Doppelbett: für Paare, Freunde oder Familien.','Jede Suite hat ihr eigenes Ambiente. Sie sind nur für Erwachsene und werden ausschließlich telefonisch gebucht, unter 973 249 222.']}
ART={
'hero':('columns',7311,['#141418','#b8956a','#e9d6b4','#5a4a3c','#3a3029','#1f1a17']),
'intro':('arches',7312,['#f3efe9','#faf7f2','#8c6d4f','#5e4836','#2e241c']),
'r1':('columns',7321,['#efe9e1','#c9a77e','#8c6d4f','#5e4836','#2e241c']),
'r2':('arches',7322,['#141418','#c2a074','#ecdcbf','#6a5646','#4a3d33','#26201c']),
'g1':('waves',7331,['#141418','#b8956a','#e9d6b4','#5a4a3c','#3a3029','#1f1a17']),
'g2':('hills',7332,['#ece6dc','#efe2cc','#c9a77e','#9c8b70','#6f6450','#4a4337']),
'g3':('arches',7333,['#f0ebe4','#f9f6f0','#9a7a58','#62503e','#2e241c']),
'g4':('skyline',7334,['#141418','#c2a074','#ecdcbf','#6a5646','#4a3d33','#26201c'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Nastasi · Hotel & Spa en Lleida',see_rooms='Ver las habitaciones',hero_k='Lleida · Av. Alcalde Rovira Roure, 214',hero_t='Una estancia cuidada, con spa y piscina',hero_s='Habitaciones, suites temáticas solo para adultos y estudios para largas estancias.',
 intro_t='Hotel & Spa en Lleida',intro_p1='Hotel Nastasi combina habitaciones estándar, junior suites y suites temáticas solo para adultos con spa, piscina y gimnasio.',
 intro_p2='Para estancias largas, el Living Resort ofrece estudios con cocina y apartamentos de un dormitorio con servicios de hotel.',
 stats=['Recepción 24 h','Spa y piscina','Parking vigilado gratuito','Desayuno buffet'],nav_rooms='Habitaciones',rooms_t='Habitaciones y suites',rooms_s='Habitaciones estándar para todos los viajeros y suites con ambientación propia, solo para adultos.',
 svcs=['Spa y piscina','Zona fitness','Desayuno buffet','Parking vigilado gratuito','Sala de eventos','Estudios para largas estancias'],
 loc_p='Avenida Alcalde Rovira Roure, 214 · 25198 Lleida. Recepción: 973 24 92 22. Check-in desde las 16.30 h; check-out hasta las 12.00 h.',
 chips=['¿Qué habitaciones tenéis?','¿Hay spa?','¿Hay parking?','¿Cómo reservo?']),
'en':dict(title='Hotel Nastasi · Hotel & Spa in Lleida',see_rooms='See the rooms',hero_k='Lleida · Av. Alcalde Rovira Roure, 214',hero_t='A carefully kept stay, with spa and pool',hero_s='Rooms, adults-only themed suites and studios for long stays.',
 intro_t='Hotel & Spa in Lleida',intro_p1='Hotel Nastasi combines standard rooms, junior suites and adults-only themed suites with a spa, pool and gym.',
 intro_p2='For long stays, the Living Resort offers studios with kitchen and one-bedroom apartments with hotel services.',
 stats=['24-hour reception','Spa and pool','Free supervised parking','Buffet breakfast'],nav_rooms='Rooms',rooms_t='Rooms and suites',rooms_s='Standard rooms for every traveller and suites with their own setting, adults only.',
 svcs=['Spa and pool','Fitness area','Buffet breakfast','Free supervised parking','Events room','Studios for long stays'],
 loc_p='Avenida Alcalde Rovira Roure, 214 · 25198 Lleida. Reception: 973 24 92 22. Check-in from 16.30; check-out until 12.00.',
 chips=['Which rooms do you have?','Is there a spa?','Is there parking?','How do I book?']),
'fr':dict(title='Hôtel Nastasi · Hôtel & Spa à Lleida',see_rooms='Voir les chambres',hero_k='Lleida · Av. Alcalde Rovira Roure, 214',hero_t='Un séjour soigné, avec spa et piscine',hero_s='Chambres, suites thématiques réservées aux adultes et studios pour longs séjours.',
 intro_t='Hôtel & Spa à Lleida',intro_p1='L’Hôtel Nastasi réunit chambres standard, junior suites et suites thématiques réservées aux adultes, avec spa, piscine et salle de sport.',
 intro_p2='Pour les longs séjours, le Living Resort propose des studios avec cuisine et des appartements d’une chambre avec services hôteliers.',
 stats=['Réception 24 h/24','Spa et piscine','Parking surveillé gratuit','Petit-déjeuner buffet'],nav_rooms='Chambres',rooms_t='Chambres et suites',rooms_s='Des chambres standard pour tous les voyageurs et des suites à l’ambiance propre, réservées aux adultes.',
 svcs=['Spa et piscine','Espace fitness','Petit-déjeuner buffet','Parking surveillé gratuit','Salle d’événements','Studios pour longs séjours'],
 loc_p='Avenida Alcalde Rovira Roure, 214 · 25198 Lleida. Réception : 973 24 92 22. Arrivée à partir de 16.30 h ; départ jusqu’à 12.00 h.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un spa ?','Y a-t-il un parking ?','Comment réserver ?']),
'de':dict(title='Hotel Nastasi · Hotel & Spa in Lleida',see_rooms='Zimmer ansehen',hero_k='Lleida · Av. Alcalde Rovira Roure, 214',hero_t='Ein gepflegter Aufenthalt, mit Spa und Pool',hero_s='Zimmer, Themensuiten nur für Erwachsene und Studios für längere Aufenthalte.',
 intro_t='Hotel & Spa in Lleida',intro_p1='Das Hotel Nastasi verbindet Standardzimmer, Junior-Suiten und Themensuiten nur für Erwachsene mit Spa, Pool und Fitnessraum.',
 intro_p2='Für längere Aufenthalte bietet das Living Resort Studios mit Küche und Apartments mit einem Schlafzimmer und Hotelservice.',
 stats=['Rezeption rund um die Uhr','Spa und Pool','Kostenloser bewachter Parkplatz','Frühstücksbuffet'],nav_rooms='Zimmer',rooms_t='Zimmer und Suiten',rooms_s='Standardzimmer für alle Reisenden und Suiten mit eigenem Ambiente, nur für Erwachsene.',
 svcs=['Spa und Pool','Fitnessbereich','Frühstücksbuffet','Kostenloser bewachter Parkplatz','Veranstaltungsraum','Studios für längere Aufenthalte'],
 loc_p='Avenida Alcalde Rovira Roure, 214 · 25198 Lleida. Rezeption: 973 24 92 22. Check-in ab 16.30 Uhr; Check-out bis 12.00 Uhr.',
 chips=['Welche Zimmer gibt es?','Gibt es ein Spa?','Gibt es Parkplätze?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
BOOK=dict(mode='mail',email='reservas@hotelnastasi.com')
D=dict(name='Hotel Nastasi',ac='#1c1b22',ac2='#8c6d4f',ac2_a11y='#6a5240',book=BOOK,around=[],foot=FOOT,
 address='Avenida Alcalde Rovira Roure, 214 · 25198 Lleida',phones=['+34 973 24 92 22'],emails=['reservas@hotelnastasi.com','hotelnastasi@hotelnastasi.com'],maps='Hotel Nastasi, Avenida Alcalde Rovira Roure 214, 25198 Lleida',t=T)
META=dict(repo='demo-hotel-nastasi-lleida',name='Hotel Nastasi',legal_name='Titular con CIF B25745936 (aviso legal de su web)',registry_ids=['B25745936'],
 url='https://www.hotelnastasi.com/',domain='hotelnastasi.com',municipality='Lleida',province='Lleida',sector='hotel y spa con habitaciones, suites tematicas solo para adultos y estudios de larga estancia en Lleida',
 read_at='2026-11-02T06:43:00+01:00',created_at='2026-11-02T06:42:00+01:00',built_at='2026-11-02T07:05:00+01:00',audit_date='2026-11-02T06:42:00+01:00',
 rating=dict(value=4.1,coincide=['web'],date='2026-10-29',url='https://www.google.com/maps/place/Nastasi+Hotel+%26+Spa+%7C+Lleida/@41.63071,0.59598,17z'),
 book=dict(mode='mail',url='mailto:reservas@hotelnastasi.com',note='sin motor de reservas propio verificable: su web dice «Reservas exclusivas llamando al +34 973 249 222». Los botones Reservar abren un correo a reservas@hotelnastasi.com (correo de su pagina de contacto) y el telefono real 973 24 92 22 va en tel:. Decision de Juan 30/10/2026.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Tenéis suites?','K02'),('¿Hay spa?','K03'),('¿Hay gimnasio?','K04'),('¿Hay parking?','K05'),('¿Hay desayuno?','K06'),('¿A qué hora es el check-in?','K07'),('¿Dónde está el hotel?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Tenéis estudios para larga estancia?','K10'),('¿Hay recepción 24 horas?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis campo de golf?',None)],
'en':[('Which rooms do you have?','K01'),('Do you have suites?','K02'),('Is there a spa?','K03'),('Is there a gym?','K04'),('Is there parking?','K05'),('Is there breakfast?','K06'),('What time is check-in?','K07'),('Where is the hotel?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('Do you have studios for long stays?','K10'),('Is reception open 24 hours?','K11'),('How much is a night?',None),('Do you have a golf course?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Avez-vous des suites ?','K02'),('Y a-t-il un spa ?','K03'),('Y a-t-il une salle de sport ?','K04'),('Y a-t-il un parking ?','K05'),('Y a-t-il un petit-déjeuner ?','K06'),('À quelle heure est l’arrivée ?','K07'),('Où se trouve l’hôtel ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Avez-vous des studios pour longs séjours ?','K10'),('La réception est-elle ouverte 24 h/24 ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous un terrain de golf ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Haben Sie Suiten?','K02'),('Gibt es ein Spa?','K03'),('Gibt es einen Fitnessraum?','K04'),('Gibt es Parkplätze?','K05'),('Gibt es Frühstück?','K06'),('Ab wann ist der Check-in?','K07'),('Wo liegt das Hotel?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Haben Sie Studios für längere Aufenthalte?','K10'),('Ist die Rezeption rund um die Uhr besetzt?','K11'),('Was kostet eine Nacht?',None),('Haben Sie einen Golfplatz?',None)]}
