# LANDHOP
#### Project made for CS50W - Final Project
#### Video Demo:  <a href="https://youtu.be/Rk1VNHPSfSs">Youtube Video</a>
#### <a href="https://landhop.up.railway.app/">Link of the Project</a>
<h3>Description:</h3>
<p>This project is a responsive webpage perfect for tourists and travelers. The goal of this project is to offer the user an opportunity to get an accurate tourist guide website by allowing people to rate sights and make comments about them. This website uses HTML, CSS, JavaScript, Bootstrap, Python (Django), and SQLite. Please keep in mind that this is not an official website that shows up as a real tourist guide webpage. I am just a developer who wants to showcase a cool website, taking inspiration from websites like "Lonely Planet", and "Get Your Guide".</p>
<p>The website has different features. To get to the home page, the user must log in or register. Once that is done, the user will be able to explore the full webpage by going through the Top cities or choosing a section. After choosing a city, the user can check the top sights for that city in particular. Once the sight is chosen, the user can read and/or make comments and rate that attraction.</p>
<h3>Distinctiveness and Complexity:</h3>
<p>Explanation of the files inside this repository:</p>
<ul>
    <li><strong>finalProject folder: </strong>It's where the main settings of the project live. It has all the configuration values that are necessary so the web application works. As well, the list of URLs are included in this folder</li>
    <li><strong>landhop folder: </strong> There, we can find many important files:
    <ul>
    <li>The <strong>static folder</strong> contains the styles, JavaScript files, and images of the web app.</li>
    <li>The <strong>templates folder</strong> has the HTML files necessary for the web application.</li>
    <li>The <strong><code>admin.py</code></strong> file makes possible the use of the Django Administration site by registering the name of the tables that we want to manage there.</li> 
    <li>In <strong><code>models.py</code></strong>, we can add/edit tables so, will be uploaded to the database. </li>
    <li>In <strong><code>urls.py</code></strong>, we can find the URLs that belongs to our landhop application.</li>
    <li>On <strong><code>views.py</code></strong> we can add logic to our website. For example, by retrieving certain data from our database, or by updating rows on our database.</li>
    </ul>
    </li>
    <li><strong><code>db.sqlite3</code>: </strong> It's the place where our database lives</li>
    <li><strong><code>manage.py</code>: </strong> Here we can interact with the Django project's settings</li>
    <li><strong><code>requirements.txt</code>: </strong> A list of the libraries, modules, and packages that are necessary for the project</li>
</ul>
<p>It's essential to clarify that this website is <strong>NOT</strong> an e-commerce site or a social media app. The reasons behind that are: </p>
<ul>
    <li>The landhop webpage is a tourist guide. A tourist guide does not sell any items. Instead, it's an informative site that's not for profit.</li>
    <li>Meeting new people is not the goal of this webpage. This website was created so users before traveling can get a better perspective about the place that they're planning to visit.</li>
</ul>
<h3>How to Run the website locally:</h3>
After you clone this repository, you must follow these steps:
<ul>
    <li>Go to the folder where you cloned the repository. Copy the path of it, and open your terminal. There you need to type <strong><code>cd YOUR_PATH</code></strong> . Now go inside of the <strong>landhop</strong> folder, by doing <strong><code>cd landhop</code></strong>. If you do <strong><code>ls</code></strong> you will be able to find the following files: <code>README.md  db.sqlite3  finalProject  landhop  manage.py  requirements.txt</code></li>
    <li>Now, install a virtual environment by typing <strong><code>pip install virtualenv</code></strong></li>
    <li>Type <strong><code>virtualenv env</code></strong></li>
    <li>Go to <code>env/Scripts</code> folder. By doing: <strong><code>cd env/Scripts</code></strong> </li>
    <li>Type <strong><code>activate</code></strong>. If this went successfully you should see an <code>(env)</code> message at the beginning of the path.</li>
    <li>Go back to our main folder by typing <strong><code>cd ../..</code></strong></li>
    <li>Install Django. Type <strong><code>pip install django</code></strong></li>
    <li>Check Django was installed. Type <strong><code>django-admin --version</code></strong></li>
    <li>Type <strong><code>python manage.py runserver</code></strong></li>
    <li>Copy the URL given on the terminal, and paste it into your browser.</li>
</ul>
<p></p>
<h3>Coming soon:</h3>
<ul>
    <li>Users can have the ability to add/edit top sights.</li>
    <li>Deploy the website totally.</li>
</ul>

<h3>References:</h3>
<p>The content inside the webpage was taken from inspiration from various sources. As well, the information and images were taken from:</p>
<ul>
    <li>Lonely Planet. (2022). <em>Discover story-worthy travel moments.</em> <h>https://www.lonelyplanet.com/</h></li>
    <li>GET YOUR GUIDE. (2022). <em>Discover unforgettable travel experiences.</em> <h>https://www.getyourguide.com/</h></li>
    <li>Imagine Dragons. [ImagineDragons]. (2022, June 24). <em>Imagine Dragons - Sharks (Official Music Video)</em> [Video]. YouTube. <h>https://www.youtube.com/watch?v=Te3_VlimRw0</h></li>
    <hr>
    <li>[<em>South America</em>] [Photograph]. (n.d.). Thoughtco. <h>https://www.thoughtco.com/thmb/S3YU2hCvC0z8lhnKFK8yYmUQ8H0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/christredeemer-10139156-567c92283df78ccc15684502.jpg</h></li>
    <li>[<em>Middle East</em>] [Photograph]. (n.d.). Youimg1. <h>https://youimg1.tripcdn.com/target/10051f000001gsq96340F.jpg?proc=source%2Ftrip</h></li>
    <li>[<em>Africa</em>] [Photograph]. (n.d.). Cloudfront. <h>https://d2kizjl6hyd5e4.cloudfront.net/2017/05/Safari-Travel-Insurance-e1513234836551.jpg</h></li>
    <li>[<em>Caribbean</em>] [Photograph]. (n.d.). Libertytravel. <h>https://www.libertytravel.com/sites/default/files/styles/full_size/public/Caribbean_hero.png?itok=bl54RuWL</h></li>
    <li>[<em>Oceania</em>] [Photograph]. (n.d.). Internationalinsurance. <h>https://www.internationalinsurance.com/wp-content/uploads/2015/01/sydney-opera-house-night.jpg</h></li>
    <li>[<em>Asia</em>] [Photograph]. (n.d.). Exoticca. <h>https://www.exoticca.com/us/blog/wp-content/uploads/2019/07/The-9-best-tips-to-travel-to-China-for-the-first-time.jpg</h></li>
    <li>[<em>North America</em>] [Photograph]. (n.d.). Agoda. <h>https://www.agoda.com/wp-content/uploads/2020/07/Statue-of-Liberty-things-to-do-in-new-york-USA.jpg</h></li>
    <li>[<em>Europe</em>] [Photograph]. (n.d.). Clairesfootsteps. <h>https://clairesfootsteps.com/wp-content/uploads/2018/06/shutterstock_556743958.jpg</h></li>
    <li>Civitalis. (2021). <em>New York.</em> <h>https://www.introducingnewyork.com/</h></li>
    <li>[<em>New York</em>] [Photograph]. (n.d.). Ngenespanol. <h>https://dam.ngenespanol.com/wp-content/uploads/2021/05/cuanto-cuesta-viajar-a-nueva-york.jpg </h></li>
    <li>Great Britain. (2022). <em>London.</em> <h>https://www.visitbritain.com/en/destinations/england/london</h></li>
    <li>[<em>London</em>] [Photograph]. (n.d.). Tripsavvy. <h>https://www.tripsavvy.com/thmb/jp1WOlSxGYDiW-rFSGEzNaq__pI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/London-big-Ben-58b5d2663df78cdcd8c69fd4.jpg</h></li>
    <li>Yatra. (2022). <em>A travel guide to paris.</em> <h>https://www.yatra.com/international-tourism/paris-travel-guide#:~:text=About%20paris,-Paris%20is%20not&text=Located%20by%20the%20River%20Seine,delicious%20food%20and%20exciting%20fashion.</h></li>
    <li>[<em>Paris</em>] [Photograph]. (n.d.). Adsttc. <h>https://images.adsttc.com/media/images/5d44/14fa/284d/d1fd/3a00/003d/large_jpg/eiffel-tower-in-paris-151-medium.jpg?1564742900 </h></li>
    <li>Barcelona.com. (2022). <em>Barcelona City guide.</em> <h>https://www.barcelona.com/barcelona_city_guide</h></li>
    <li>[<em>Barcelona</em>] [Photograph]. (n.d.). Imgix. <h>https://lp-cms-production.imgix.net/2021-07/GettyRF_1137803766.jpg </h></li>
    <li>NOMADIC MATT. (2022). <em>Tokyo Travel Guide.</em> <h>https://www.nomadicmatt.com/travel-guides/japan-travel-tips/tokyo/</h></li>
    <li>[<em>Tokyo</em>] [Photograph]. (n.d.). Hips. <h>https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-1058360160-1-1624796189.jpg</h></li>
    <li>Pin and travel. (2022). <em>Travel to the land of the Pharaohs and discover the best Egypt tourist attractions.</em> <h>https://www.barcelo.com/pinandtravel/en/egypt-tourist-attractions/</h></li>
    <li>[<em>Egypt</em>] [Photograph]. (n.d.). Fodors. <h>https://www.fodors.com/wp-content/uploads/2019/06/EgyptTours__HERO_CC_Giza_Pyramids_Desert_Camels.jpg</h></li>
    <li>US News. (2022). <em>Sydney Travel Guide.</em> <h>https://travel.usnews.com/Sydney_Australia/</h></li>
    <li>[<em>Australia</em>] [Photograph]. (n.d.). Klook. <h>https://res.klook.com/image/upload/v1646641811/blog/hjsmdfvqyhd9egf9xoc1.jpg </h></li>
    <li>
    <li>Statue of Liberty. (2022). <em>UNESCO.</em> <h>https://whc.unesco.org/en/list/307/</h></li>
    <li>[<em>Statue of Liberty</em>] [Photograph]. (n.d.). CNN. <h>https://cdn.cnn.com/cnnnext/dam/assets/190503105157-statue-of-liberty-national-park-super-tease.jpg</h></li>
    <li>Trip Savvy. (2022). <em>Central Park Visitors Guide.</em> <h>https://www.tripsavvy.com/central-park-visitors-guide-1612791</h></li>
    <li>[<em>Central Park</em>] [Photograph]. (n.d.). Travellemming. <h>https://travellemming.com/wp-content/uploads/Things-to-Do-in-Central-Park.jpg</h></li>
    <li>Independent Travel Cats. (2022). <em>Complete Guide to Visiting the Eiffel Tower in Paris.</em> <h>-	https://independenttravelcats.com/eiffel-tower-paris-france/</h></li>
    <li>[<em>Eiffel Tower</em>] [Photograph]. (n.d.). Planetware. <h>https://www.planetware.com/photos-large/F/eiffel-tower.jpg</h></li>
    <li>INSIGHT GUIDES. (2022). <em>France Travel Guide.</em> <h>https://www.insightguides.com/destinations/europe/france/disneyland-paris</h></li>
    <li>[<em>Disneyland Paris</em>] [Photograph]. (n.d.). Aerotravels. <h>https://aerotravels.co.uk/blog/wp-content/uploads/2021/01/Disneyland-paris-travel-tips.jpg</h></li>
    <li>Headout. (2022). <em>The Only Guide You Need To Explore The Best of Louvre Museum Paris.</em> <h>https://www.headout.com/blog/louvre-museum-paris/#:~:text=The%20Louvre%20Museum%20in%20Paris,art%20collection%20in%20the%20world.</h></li>
    <li>[<em>Louvre Museum</em>] [Photograph]. (n.d.). Tacdn. <h>https://media.tacdn.com/media/attractions-splice-spp-674x446/06/e4/a8/99.jpg</h></li>
    <li>Viator. (2022). <em>Harry Potter Tour of Warner Bros. Studio with Transport from London.</em> <h>https://www.viator.com/tours/London/Harry-Potter-Tour-of-Warner-Bros-Studio-in-London/d737-2452POTTER</h></li>
    <li>[<em>Warner Bros. Studio - The Making of Harry Potter</em>] [Photograph]. (n.d.). s28943. <h>https://s28943.pcdn.co/wp-content/uploads/2018/02/warner-bros-studio-tour-london-the-making-of-harry-potter-warner-bros-studio-tour-london-hogwarts-expressweb-8bda679e9fcb25322ddbae65bb6d49dc.jpg</h></li>
    <li>Britain Express. (2022). <em>London Eye.</em> <h>https://www.britainexpress.com/London/London-Eye.htm#:~:text=Visitors%20climb%20aboard%20glass%2Dencased,London%20in%20a%20unique%20way</h></li>
    <li>[<em>London Eye</em>] [Photograph]. (n.d.). Klook. <h>https://res.klook.com/image/upload/q_85/c_fill,w_750/v1644476606/blog/fy7chb94ivvyb3lhdtdj.jpg</h></li>
    <li>Japan Endless Discovery. (2022). <em>Tsukiji Outer Market.</em> <h>https://www.japan.travel/en/spot/1707/</h></li>
    <li>[<em>Tsukiji Outer Market</em>] [Photograph]. (n.d.). Nyt. <h>https://static01.nyt.com/images/2015/11/15/travel/15TOKYO1/15TOKYO1-superJumbo.jpg</h></li>
    <li>GO TOKYO. (2022). <em>Ueno travel guide - from Ameyoko to Ueno Park.</em> <h>https://www.gotokyo.org/en/destinations/northern-tokyo/ueno/index.html</h></li>
    <li>[<em>Ueno Park</em>] [Photograph]. (n.d.). Cdn. <h>https://cdn.cheapoguides.com/wp-content/uploads/sites/2/2019/03/ueno-park-cherry-blossoms_gdl-1024x600.jpg</h></li>
    <li>Sydney.com. (2022). <em>Taronga Zoo Sydney.</em> <h>https://int.sydney.com/destinations/sydney/sydney-north/mosman/attractions/taronga-zoo-sydney</h></li>
    <li>[<em>Taronga Zoo</em>] [Photograph]. (n.d.). Pinimg. <h>https://i.pinimg.com/originals/27/08/70/2708701f242501a46bb48ee1c768eee0.jpg</h></li>
    <li>Trip.com. (2022). <em>Sydney Opera House: A Detailed Guide.</em> <h>https://www.trip.com/blog/sydney-opera-house-detailed-guide/</h></li>
    <li>[<em>Sydney Opera House</em>] [Photograph]. (n.d.). Roadtripandtravel. <h>https://roadtripandtravel.com/wp-content/uploads/sydney-opera-house-night.jpg</h></li>
    <li>Egypt Time Travel. (2022). <em>A Journey to National Museum of Egyptian.</em> <h>https://egypttimetravel.com/national-museum-of-egyptian-civilization/</h></li>
    <li>[<em>National Museum of Egyptian Civilization</em>] [Photograph]. (n.d.). Egypttoursportal. <h>https://www.egypttoursportal.com/images/2021/04/The-National-Museum-of-Egyptian-Civilization-NMEC-Egypt-Tours-Portal.jpg</h></li>
    <li>AUDLEY. (2022). <em>Visit Dahshur, Egypt.</em> <h>https://www.audleytravel.com/egypt/places-to-go/dahshur</h></li>
    <li>[<em>Dahshur</em>] [Photograph]. (n.d.). Tripadvisor. <h>https://dynamic-media-cdn.tripadvisor.com/media/photo-o/05/63/a4/eb/dahshur.jpg?w=1200&h=-1&s=1</h></li>
    <li>Headout. (2022). <em>All You Need to Know About Park Guell in Barcelona.</em> <h>https://www.parkguell-tickets.com/park-guell-barcelona/</h></li>
    <li>[<em>Park Güell</em>] [Photograph]. (n.d.). Tacdn. <h>https://media.tacdn.com/media/attractions-splice-spp-674x446/0b/27/60/bb.jpg</h></li>
    <li>Headout. (2022). <em>Your Essential Guide to Visit Sagrada Familia in Barcelona | Timings, Location, Tips & More.</em> <h>https://sagradafamilia.barcelona-tickets.com/plan-your-visit-sagrada-familia/</h></li>
    <li>[<em>Sagrada Familia</em>] [Photograph]. (n.d.). Ricksteves. <h>https://blog.ricksteves.com/wp-content/uploads/2020/09/daily-dose-sagrada-IG.jpg</h></li>
    <li>US News. (2022). <em>Rio de Janeiro Travel Guide.</em> <h>https://travel.usnews.com/Rio_de_Janeiro_Brazil/</h></li>
    <li>[<em>Rio de Janeiro</em>] [Photograph]. (n.d.). Travelsafe. <h>https://cdn.travelsafe-abroad.com/wp-content/uploads/2482.jpg</h></li>
    <li>US News. (2022). <em>Buenos Aires Travel Guide.</em> <h>https://travel.usnews.com/Buenos_Aires_Argentina/</h></li>
    <li>[<em>Buenos Aires</em>] [Photograph]. (n.d.). Experiencechile. <h>https://www.experiencechile.org/wp-content/uploads/2018/10/ba1.jpg</h></li>
    <li>TRAVEL + LEISURE. (2022). <em>Dubai Travel Guide.</em> <h>https://www.travelandleisure.com/travel-guide/dubai</h></li>
    <li>[<em>Dubai</em>] [Photograph]. (n.d.). Forbestravelguide. <h>https://secure.s.forbestravelguide.com/img/destinations/Dubai-iStock-JandaliPhoto.jpg</h></li>
    <li>Trip.com. (2022). <em>Doha Travel Guide.</em> <h>https://www.trip.com/travel-guide/destination/doha-1733/</h></li>
    <li>[<em>Doha</em>] [Photograph]. (n.d.). Holidify. <h>https://www.holidify.com/images/bgImages/DOHA.jpg</h></li>
    <li>US News. (2022). <em>Havana, Cuba Travel Guide.</em> <h>https://travel.usnews.com/Havana_Cuba/</h></li>
    <li>[<em>Havana</em>] [Photograph]. (n.d.). R9cdn. <h>https://content.r9cdn.net/rimg/dimg/a3/1d/05f2b4a1-city-11020-1700c4dba73.jpg?crop=true&width=1020&height=498</h></li>
    <li>TRAVEL LEMMING. (2022). <em>San Juan, Puerto Rico.</em> <h>https://travellemming.com/san-juan-pr/</h></li>
    <li>[<em>San Juan</em>] [Photograph]. (n.d.). Thrillist. <h>https://assets3.thrillist.com/v1/image/2811871/1200x600/scale;</h></li>
    <li>MOWGLI ADVENTURES. (2022). <em>A practical guide to visiting Christ the Redeemer.</em> <h>https://mowgli-adventures.com/visiting-christ-the-redeemer-brazil/</h></li>
    <li>[<em>Christ the Redeemer</em>] [Photograph]. (n.d.). Fodors. <h>https://www.fodors.com/wp-content/uploads/2022/07/1-Avoiding-Crowds-shutterstock_1888737391.jpg</h></li>
    <li>FREE WALKS. (2022). <em>Caminito Buenos Aires.</em> <h>https://www.buenosairesfreewalks.com/batips/caminito-buenos-aires/</h></li>
    <li>[<em>Caminito Street</em>] [Photograph]. (n.d.). Tripadvisor. <h>https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/fe/95/b4/caminito-street-8.jpg?w=1200&h=-1&s=1</h></li>
    <li>Headout. (2022). <em>Your Ultimate Guide to Visiting the Burj Khalifa.</em> <h>https://www.headout.com/blog/burj-khalifa-dubai/</h></li>
    <li>[<em>Burj Khalifa</em>] [Photograph]. (n.d.). Makemytrip. <h>https://www.makemytrip.com/travel-guide/media/dg_image/dubai/Burj-Khalifa.jpg</h></li>
    <li>Lonely Planet. (2022). <em>Souq Waqif.</em> <h>https://www.lonelyplanet.com/qatar/doha/attractions/souq-waqif/a/poi-sig/451983/361125</h></li>
    <li>[<em>Souq Waqif</em>] [Photograph]. (n.d.). GetYourGuide. <h>https://cdn.getyourguide.com/img/location/59631c093b71d.jpeg/99.jpg</h></li>
    <li>Youth Hostel. (2022). <em>Havana.</em> <h>https://www.youth-hostel.si/en/page/everything-about-travel/cities-around-the-world/havana?linksubid=PPC-ANG_Travel&gclid=Cj0KCQiAtbqdBhDvARIsAGYnXBMi0cbIe_2g3h_l2sJwgtFCY2-s1cJTPFrdCtzHHWKipLHGmyJlYCMaAmGxEALw_wcB</h></li>
    <li>[<em>Old Havana</em>] [Photograph]. (n.d.). Istockphoto. <h>https://media.istockphoto.com/id/1327163693/photo/multicolored-vintage-taxi-cars-on-street-of-havana-against-historic-buildings.jpg?s=612x612&w=0&k=20&c=RGiKd-MWtJil7ZhW7liyiE0R7OKMXDoKzigdvRtOG0E=</h></li>
    <li>TRAVEL + LEISURE. (2022). <em>Las Vegas Travel Guide.</em> <h>https://www.travelandleisure.com/travel-guide/las-vegas-nevada</h></li>
    <li>[<em>Las Vegas</em>] [Photograph]. (n.d.). R9cdn. <h>https://content.r9cdn.net/rimg/dimg/60/fa/63274ccd-city-35107-16f0ffd226d.jpg?width=1750&height=1000&xhint=2074&yhint=1764&crop=true</h></li>
    <li>Tripadvisor. (2022). <em>The STRAT Hotel, Casino & SkyPod.</em> <h>https://www.tripadvisor.com/Hotel_Review-g45963-d114898-Reviews-The_STRAT_Hotel_Casino_SkyPod-Las_Vegas_Nevada.html</h></li>
    <li>[<em>The STRAT Hotel, Casino & SkyPod</em>] [Photograph]. (n.d.). Thestrat. <h>https://thestrat.com/userfiles/social/opengraph/121/Picture1.png</h></li>
</ul>
