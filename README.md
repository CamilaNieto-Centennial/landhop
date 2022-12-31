# LANDHOP
#### Project made for CS50W - Final Project
#### Video Demo:  <a href="">Youtube Video</a>
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
    <li>Go to the folder where you cloned the repository. Copy the path of it, and open your terminal. There you need to type <strong><code>cd YOUR_PATH</code></strong></li>
    <li>Now, install a virtual environment by typing <strong><code>pip install virtualenv</code></strong></li>
    <li>Go to <code>env/Scripts</code> folder. By doing: <strong><code>cd env/Scripts</code></strong> </li>
    <li>Type <strong><code>activate</code></strong>. If this went successfully you should see an <code>(env)</code> message at the beginning of the path.</li>
    <li>Install Django. Type <strong><code>pip install django</code></strong></li>
    <li>Check Django was installed. Type <strong><code>django-admin --version</code></strong></li>
    <li>Type <strong><code>python manage.py runserver</code></strong></li>
    <li>Copy the URL given, and paste it into your browser.</li>
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
</ul>
