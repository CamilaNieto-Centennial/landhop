# LANDHOP
#### Project made for CS50W - Final Project
#### Video Demo:  <a href="https://youtu.be/Rk1VNHPSfSs">Youtube Video</a>
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
    <li>Title Company. (2022). <em>Title Article.</em> <h>https://example.com/</h></li>
    <hr>
    <li>[<em>South America</em>] [Photograph]. (n.d.). Thoughtco. <h>https://www.thoughtco.com/thmb/S3YU2hCvC0z8lhnKFK8yYmUQ8H0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/christredeemer-10139156-567c92283df78ccc15684502.jpg</h></li>
    <li>[<em>Middle East</em>] [Photograph]. (n.d.). Youimg1. <h>https://youimg1.tripcdn.com/target/10051f000001gsq96340F.jpg?proc=source%2Ftrip</h></li>
    <li>[<em>Africa</em>] [Photograph]. (n.d.). Cloudfront. <h>https://d2kizjl6hyd5e4.cloudfront.net/2017/05/Safari-Travel-Insurance-e1513234836551.jpg</h></li>
    <li>[<em>Caribbean</em>] [Photograph]. (n.d.). Libertytravel. <h>https://www.libertytravel.com/sites/default/files/styles/full_size/public/Caribbean_hero.png?itok=bl54RuWL</h></li>
    <li>[<em>Oceania</em>] [Photograph]. (n.d.). Internationalinsurance. <h>https://www.internationalinsurance.com/wp-content/uploads/2015/01/sydney-opera-house-night.jpg</h></li>
    <li>[<em>Asia</em>] [Photograph]. (n.d.). Exoticca. <h>https://www.exoticca.com/us/blog/wp-content/uploads/2019/07/The-9-best-tips-to-travel-to-China-for-the-first-time.jpg</h></li>
    <li>[<em>North America</em>] [Photograph]. (n.d.). Agoda. <h>https://www.agoda.com/wp-content/uploads/2020/07/Statue-of-Liberty-things-to-do-in-new-york-USA.jpg</h></li>
    <li>[<em>Europe</em>] [Photograph]. (n.d.). Clairesfootsteps. <h>https://clairesfootsteps.com/wp-content/uploads/2018/06/shutterstock_556743958.jpg</h></li>
    <li>[<em>New York</em>] [Photograph]. (n.d.). Ngenespanol. <h>https://dam.ngenespanol.com/wp-content/uploads/2021/05/cuanto-cuesta-viajar-a-nueva-york.jpg </h></li>
    <li>[<em>London</em>] [Photograph]. (n.d.). Tripsavvy. <h>https://www.tripsavvy.com/thmb/jp1WOlSxGYDiW-rFSGEzNaq__pI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/London-big-Ben-58b5d2663df78cdcd8c69fd4.jpg</h></li>
    <li>[<em>Paris</em>] [Photograph]. (n.d.). Adsttc. <h>https://images.adsttc.com/media/images/5d44/14fa/284d/d1fd/3a00/003d/large_jpg/eiffel-tower-in-paris-151-medium.jpg?1564742900 </h></li>
    <li>[<em>Barcelona</em>] [Photograph]. (n.d.). Imgix. <h>https://lp-cms-production.imgix.net/2021-07/GettyRF_1137803766.jpg </h></li>
    <li>[<em>Tokyo</em>] [Photograph]. (n.d.). Hips. <h>https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-1058360160-1-1624796189.jpg</h></li>
    <li>[<em>Egypt</em>] [Photograph]. (n.d.). Fodors. <h>https://www.fodors.com/wp-content/uploads/2019/06/EgyptTours__HERO_CC_Giza_Pyramids_Desert_Camels.jpg</h></li>
    <li>[<em>Australia</em>] [Photograph]. (n.d.). Klook. <h>https://res.klook.com/image/upload/v1646641811/blog/hjsmdfvqyhd9egf9xoc1.jpg </h></li>
    <li>[<em>Statue of Liberty</em>] [Photograph]. (n.d.). CNN. <h>https://cdn.cnn.com/cnnnext/dam/assets/190503105157-statue-of-liberty-national-park-super-tease.jpg </h></li>
    <li>[<em>Eiffel Tower</em>] [Photograph]. (n.d.). Planetware. <h>https://www.planetware.com/photos-large/F/eiffel-tower.jpg</h></li>
    <li>[<em>Disneyland Paris</em>] [Photograph]. (n.d.). Aerotravels. <h>https://aerotravels.co.uk/blog/wp-content/uploads/2021/01/Disneyland-paris-travel-tips.jpg</h></li>
    <li>[<em>Louvre Museum</em>] [Photograph]. (n.d.). Tacdn. <h>https://media.tacdn.com/media/attractions-splice-spp-674x446/06/e4/a8/99.jpg</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
    <li>[<em></em>] [Photograph]. (n.d.). Thoughtco. <h>https://www</h></li>
</ul>
