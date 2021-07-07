from django.db import models

# tema1 = [{
#         'header': 'We are a Creative Digital Agency & Marketing Experts',
#         'description': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In rhoncus turpis nisl, vitae dictum mi semper convallis. Ut sapien leo, varius ac dapibus a, cursus quis ante.",
#         'description2': "Nunc sodales lobortis arcu, sit amet venenatis erat placerat a. Donec lacinia magna nulla, cursus impediet augue egestas id. Suspendisse dolor lectus, pellentesque quis tincidunt ac, dictum id neque.",
#         'button': "Learn More"
#     }]

#     tema2 = [{
#         'header': 'Explore The Services We Offer For You',
#         'description': "Nunc sodales lobortis arcu, sit amet venenatis erat placerat a. Donec lacinia magna nulla, cursus\n impediet augue egestas id. Suspendisse dolor lectus, pellentesque quis tincidunt ac, dictum id neque.",
#         'button': 'All Services'
#     }]

#     avatar1 = [{
#         'image_logo': 'images/web-design.png',
#         'header': 'Web Design',
#         'description': "Web design encompasses many different skills and disciplines in the production and maintenance of websites."
#     },
#     {   'image_logo': 'images/marketing.png',
#         'header': 'Marketing',
#         'description': "Marketing refers to activities a company undertakes to promote the buying or selling of a product, service, or good."
#     }]
#     avatar2 = [{   'image_logo': 'images/seo.png',
#         'header': 'SEO',
#         'description': "Search Engine Optimization is the process of improving the quality and quantity of website traffic to a website or a web page from search engines."
#     },
#     {   'image_logo': 'images/graphics-design.png',
#         'header': 'Graphics Design',
#         'description': "Graphic design is the profession and academic discipline whose activity consists in projecting visual communications intended to transmit specific messages to social groups, with specific objectives."
#     }]

class HomeViewSubjects1(models.Model):
    header = models.CharField(max_length=100)
    description = models.TextField()
    description2 = models.TextField()
    button = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.header

class HomeViewSubjects2(models.Model):
    header = models.CharField(max_length=100)
    description = models.TextField()
    button = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.header

class HomeViewSubjects3(models.Model):
    image_logo = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.header

class HomeViewSubjects4(models.Model):
    image_logo = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.header

    # about_start = [{
    #     'number': 125,
    #     'header': 'Active Projects'
    # },
    # {   'number': 200,
    #     'header': 'Business Growth'
    # },
    # {   'number': 530,
    #     'header': 'Completed Projects'
    # },
    # {   'number': 941,
    #     'header': 'Happy Clients'
    # }]
    # worker = [{
    #     'first_name': 'Lisa',
    #     'last_name': 'Gally',
    #     'duty': 'Project Manager',
    #     'description': '“ Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat ”',
    #     'avatar': 'images/customer1.jpg'
    # },
    # {   'first_name': 'Missy',
    #     'last_name': 'Limana',
    #     'duty': 'Microsoft Office Word',
    #     'description': "“ With over 6 years of English teaching experience in the U.S. and abroad, from elementary to university level, I'm here for your proofreading needs! ”",
    #     'avatar': 'images/customer2.jpg'
    # },
    # {   'first_name': 'Aana',
    #     'last_name': 'Brown',
    #     'duty': 'Linux Admin Specialist',
    #     'description': '“ A skilled Linux System Administrator with over 7years of experience in web hosting Industry. Experience of managing hundreds of hosting servers and over two thousand virtual servers operating on CentOS, Debian, Virtuozzo, OpenVZ and Xen platforms, running cPanel, Plesk and other control panels. ”',
    #     'avatar': 'images/customer3.jpg'
    # },
    # {   'first_name': 'Mikle',
    #     'last_name': 'Tyson',
    #     'duty': 'Design',
    #     'description': "“ Hi, my name is Mikhail. I have been doing 3D modeling for 3D printing for more than 3 years. In addition to 3D modeling, I can perform 3d interior design. I have a bachelor's degree in construction.  ”",
    #     'avatar': 'images/customer4.webp'
    # },
    # {   'first_name': 'Nilson',
    #     'last_name': 'Kim',
    #     'duty': 'Engineering CAD',
    #     'description': "“ I had a lot of experience in Cad 3D projects in inventor or solidworks, today I freelance work with 3D projects modeling with animation, if I want to know more about my work, I'm going to make my! ”",
    #     'avatar': 'images/customer5.jpeg'
    # },
    # {   'first_name': 'Elis',
    #     'last_name': 'Tyberg',
    #     'duty': 'IT System Engineer',
    #     'description': "“ I pledge to deliver professional, clear to understand, no-fuss-around results to niche customers. Time if precious, let's talk business!”",
    #     'avatar': 'images/customer6.jpeg'
    # }]
    # more = [{
    #     'image': 'images/quality-results.png',
    #     'header': 'Quality Results',
    #     'description': "Response Quality uses machine learning to scan your survey results and flag poor-quality responses. For example, if a survey-taker fills a comment box with gibberish, or answers option A on every question, we’ll flag the responses so you can focus on high-quality survey data. A survey needs to be in English, and have more than 50 responses in order to see Response Quality results. Survey responses collected before March 2nd, 2020 can’t be reviewed for quality."
    # },
    # {   'image': 'images/analytics.png',
    #     'header': 'Analytics',
    #     'description': 'Take action with deeper insights to improve your customer experience. See how customers from your ads engage with your site, from ad click to conversion and beyond, and discover your most valuable customers. Re-engage audiences with better, more personalized ads.'
    # },
    # {   'image': 'images/affordable-pricing.png',
    #     'header': 'Affordable Pricing',
    #     'description': "The best method is to introduce more attractive alternatives that work at the right time, in the right place and at an affordable price."
    # },
    # {   'image': 'images/easy-to-use.png',
    #     'header': 'Easy To Use',
    #     'description': "AbobaCompany offers really easy-to-use free backlink checking software solutions."
    # },
    # {   'image': 'images/free-support.png',
    #     'header': 'Free Support',
    #     'description': "Free Support and Installation on your server!"
    # },
    # {   'image': 'images/effectively-increase.png',
    #     'header': 'Effectively Increase',
    #     'description': "This will help create more jobs, reduce unemployment of urban and effectively increase working time."
    # }]
    # advert_logo = [{
    #     'logo': 'images/logo1.png'
    # },
    # {   'logo': 'images/logo2.png'
    # },
    # {   'logo': 'images/logo3.png'
    # },
    # {   'logo': 'images/logo4.png'
    # },
    # {   'logo': 'images/logo5.png'
    # },
    # {   'logo': 'images/logo6.png'
    # }]

class AboutViewSubjects1(models.Model):
    number = models.CharField(max_length=100)
    header = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.header

class AboutViewSubjects2(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    duty = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class AboutViewSubjects3(models.Model):
    image = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.header

class AboutViewSubjects4(models.Model):
    logo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.logo


    # text = 'What our customers say about us.'
    # pictures = {logo:'images/logo1.png', logo:'images/logo2.png', logo:'images/logo3.png', logo:'images/logo4.png', logo:'images/logo5.png'}
    # data = [
    #     {"image":"images/news1.jpg", 
        # 'descriprion':"The world's biggest memory-chip and smartphone maker forecast operating profit of $11bn (£8bn) for the three months to the end of June. It said strong demand for memory chips had offset weaker sales of devices due to the shortage of components. A year ago, in the first few months of the pandemic, Samsung saw sales of products such as phones and TVs slump.",
        # 'header': 'Tech giant Samsung Electronics has said it expects its quarterly profit to rise by 53% amid a global chip shortage.'}, 
    
    #     {"image":"images/news2.jpg", 
        # 'descriprion': "The latest incarnation of the iconic Gaming series from MSI is still the same combination of high speed, efficient cooling and impeccable aesthetics, which has long been loved by enthusiastic gamers. This video card will allow you to run the latest games while remaining cold and quiet – exactly the way you want.",
        # 'header': "GeForce RTX 3090 Gaming X Trio."}, 
    
    #     {"image":"images/news3.jpg", 
        # 'descriprion':"Windows has always existed to be a stage for the world’s innovation. It’s been the backbone of global businesses and where scrappy startups became household names. The web was born and grew up on Windows. It’s the place where many of us wrote our first email, played our first PC game and wrote our first line of code. Windows is the place people go to create, to connect, to learn and to achieve – a platform over a billion people today rely on. ",
        # 'header': "Introducing Windows 11."}б
    
    #    {"image":"images/news4.jpg", 
        # 'descriprion':"Intel has finally announced its new Intel Core processors of the 11th generation (Rocket Lake-S series). The architecture was updated for the first time in 5 years. The ancient Skylake was replaced by the modern Cypress Cove. The Rocket Lake-S family currently consists of almost two dozen models. The TDP level is from 35 to 125 watts. Cores — 6 or 8, the frequency of operation-up to 5.3 GHz. The new chips are compatible with both 500-series and 400-series motherboards.",
        # 'header': "Intel Core processors of the 11th generation (Rocket Lake-S)are presented."}
    
    #     ]

class NewsViewSubjects1(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.text

class NewsViewSubjects2(models.Model):
    logo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.logo

class NewsViewSubjects3(models.Model):
    image = models.CharField(max_length=100)
    header = models.CharField(max_length=200)
    descriprion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.header

