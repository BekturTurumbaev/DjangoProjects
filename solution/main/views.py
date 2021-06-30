from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    tema1 = [{
        'header': 'We are a Creative Digital Agency & Marketing Experts',
        'description': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In rhoncus turpis nisl, vitae dictum mi semper convallis. Ut sapien leo, varius ac dapibus a, cursus quis ante.",
        'description2': "Nunc sodales lobortis arcu, sit amet venenatis erat placerat a. Donec lacinia magna nulla, cursus impediet augue egestas id. Suspendisse dolor lectus, pellentesque quis tincidunt ac, dictum id neque.",
        'button': "Learn More"
    }]

    tema2 = [{
        'header': 'Explore The Services We Offer For You',
        'description': "Nunc sodales lobortis arcu, sit amet venenatis erat placerat a. Donec lacinia magna nulla, cursus\n impediet augue egestas id. Suspendisse dolor lectus, pellentesque quis tincidunt ac, dictum id neque.",
        'button': 'All Services'
    }]

    avatar1 = [{
        'image_logo': 'images/web-design.png',
        'header': 'Web Design',
        'description': "Web design encompasses many different skills and disciplines in the production and maintenance of websites."
    },
    {   'image_logo': 'images/marketing.png',
        'header': 'Marketing',
        'description': "Marketing refers to activities a company undertakes to promote the buying or selling of a product, service, or good."
    }]
    avatar2 = [{   'image_logo': 'images/seo.png',
        'header': 'SEO',
        'description': "Search Engine Optimization is the process of improving the quality and quantity of website traffic to a website or a web page from search engines."
    },
    {   'image_logo': 'images/graphics-design.png',
        'header': 'Graphics Design',
        'description': "Graphic design is the profession and academic discipline whose activity consists in projecting visual communications intended to transmit specific messages to social groups, with specific objectives."
    }]
    def get(self, request):
        return render(request, template_name="main/home.html", context={'avatars1': self.avatar1, 'avatars2': self.avatar2, 'temas': self.tema1,  'temas2': self.tema2})

class AboutView(View): 
    about_start = [{
        'number': 125,
        'header': 'Active Projects'
    },
    {   'number': 200,
        'header': 'Business Growth'
    },
    {   'number': 530,
        'header': 'Completed Projects'
    },
    {   'number': 941,
        'header': 'Happy Clients'
    }]
    worker = [{
        'first_name': 'Lisa',
        'last_name': 'Gally',
        'duty': 'Project Manager',
        'description': '“ Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat ”',
        'avatar': 'images/customer1.jpg'
    },
    {   'first_name': 'Missy',
        'last_name': 'Limana',
        'duty': 'Microsoft Office Word',
        'description': "“ With over 6 years of English teaching experience in the U.S. and abroad, from elementary to university level, I'm here for your proofreading needs! ”",
        'avatar': 'images/customer2.jpg'
    },
    {   'first_name': 'Aana',
        'last_name': 'Brown',
        'duty': 'Linux Admin Specialist',
        'description': '“ A skilled Linux System Administrator with over 7years of experience in web hosting Industry. Experience of managing hundreds of hosting servers and over two thousand virtual servers operating on CentOS, Debian, Virtuozzo, OpenVZ and Xen platforms, running cPanel, Plesk and other control panels. ”',
        'avatar': 'images/customer3.jpg'
    },
    {   'first_name': 'Mikle',
        'last_name': 'Tyson',
        'duty': 'Design',
        'description': "“ Hi, my name is Mikhail. I have been doing 3D modeling for 3D printing for more than 3 years. In addition to 3D modeling, I can perform 3d interior design. I have a bachelor's degree in construction.  ”",
        'avatar': 'images/customer4.webp'
    },
    {   'first_name': 'Nilson',
        'last_name': 'Kim',
        'duty': 'Engineering CAD',
        'description': "“ I had a lot of experience in Cad 3D projects in inventor or solidworks, today I freelance work with 3D projects modeling with animation, if I want to know more about my work, I'm going to make my! ”",
        'avatar': 'images/customer5.jpeg'
    },
    {   'first_name': 'Elis',
        'last_name': 'Tyberg',
        'duty': 'IT System Engineer',
        'description': "“ I pledge to deliver professional, clear to understand, no-fuss-around results to niche customers. Time if precious, let's talk business!”",
        'avatar': 'images/customer6.jpeg'
    }]
    more = [{
        'image': 'images/quality-results.png',
        'header': 'Quality Results',
        'description': "Response Quality uses machine learning to scan your survey results and flag poor-quality responses. For example, if a survey-taker fills a comment box with gibberish, or answers option A on every question, we’ll flag the responses so you can focus on high-quality survey data. A survey needs to be in English, and have more than 50 responses in order to see Response Quality results. Survey responses collected before March 2nd, 2020 can’t be reviewed for quality."
    },
    {   'image': 'images/analytics.png',
        'header': 'Analytics',
        'description': 'Take action with deeper insights to improve your customer experience. See how customers from your ads engage with your site, from ad click to conversion and beyond, and discover your most valuable customers. Re-engage audiences with better, more personalized ads.'
    },
    {   'image': 'images/affordable-pricing.png',
        'header': 'Affordable Pricing',
        'description': "The best method is to introduce more attractive alternatives that work at the right time, in the right place and at an affordable price."
    },
    {   'image': 'images/easy-to-use.png',
        'header': 'Easy To Use',
        'description': "AbobaCompany offers really easy-to-use free backlink checking software solutions."
    },
    {   'image': 'images/free-support.png',
        'header': 'Free Support',
        'description': "Free Support and Installation on your server!"
    },
    {   'image': 'images/effectively-increase.png',
        'header': 'Effectively Increase',
        'description': "This will help create more jobs, reduce unemployment of urban and effectively increase working time."
    }]
    advert_logo = [{
        'logo': 'images/logo1.png'
    },
    {   'logo': 'images/logo2.png'
    },
    {   'logo': 'images/logo3.png'
    },
    {   'logo': 'images/logo4.png'
    },
    {   'logo': 'images/logo5.png'
    },
    {   'logo': 'images/logo6.png'
    }]
    def get(self, request):
        return render(request, template_name="main/about.html", context={'data': self.about_start, 'workers': self.worker, 'mores': self.more, 'images': self.advert_logo})

class NewsView(View):
    pictures = {1:'images/logo1.png', 2:'images/logo2.png', 3:'images/logo3.png', 4:'images/logo4.png', 5:'images/logo5.png'}
    data = [
        {"image":"images/news1.jpg", 1:"Очки. Обыкновенные очки.", 2:"Эти очки состоавляют 2 очка: первое очко и второе очко. В линзах данных очков сы можем наблюдать, что этот \"программист\" использует Google Chrome. Земля ему пухом."}, 
        {"image":"images/news2.jpg", 1:"Finger. Just a regular finger.", 2:"Это палец. С помощью него можно stick finger в уникальную навигационную панель, расположенную прямо в воздухе. А ещё этот палец умеет светиться, как фонарик. Разве не круто?."}, 
        {"image":"images/news3.jpg", 1:"Компьютерный клуб...", 2:"Это компьютерный клуб 21-го века, где пацанчики могут рубиться в дотку, ксОчку, тунчики, в общем, стандартные игры гидроцефалов. Начинка компов: 2 гига, 2 ядра, игровая видеокарта и мониторы от Apple."}
        ]
    def get(self, request):
        return render(request, template_name="main/news.html", context={"pictures":self.pictures, "data":self.data})

class ServicesView(View):
    data_1 = [
        {"image":"images/web-design.png", "name":"Web Design", "text":"Our company will be happy to help you with the design of the site."}, 
        {"image":"images/marketing.png", "name":"Marketing", "text":"We also create excellent bright and memorable advertising."}
        ]
    data_2 = [
        {"image":"images/seo.png", "name":"SEO", "text":"SEO is a set of methods and measures that are designed to increase the visibility of a site in the eyes of search engines."}, 
        {"image":"images/graphics-design.png", "name":"Graphics Design", "text":"We create high quality and unique graphic designs."}
        ]
    def get(self, request):
        return render(request, template_name="main/services.html", context={"data_1":self.data_1, "data_2":self.data_2})