from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CustomUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError

class MainView(View):
    def get(self, request):
        login_forms = LoginForm()
        custom_user_form = CustomUserForm()
        return render(request, template_name='main/home.html', context={'reg_form': custom_user_form, 'login_form': login_forms})

    def post(self, request):
        if request.POST.get('submit') == 'signup':
            custom_user_form = CustomUserForm(request.POST)

            if custom_user_form.is_valid():
                custom_user_form.save()

                messages.success(request, 'Registration success')
                return render(request, template_name='main/home.html')
            
            error = '\n'.join([msg[0] for msg in tuple(custom_user_form.errors.values())])
            messages.warning(request, error)
            custom_user_form = CustomUserForm()
            return render(request, template_name='main/home.html', context={'reg_form': custom_user_form})


class HomeView(LoginRequiredMixin, View):
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

class AboutView(LoginRequiredMixin, View): 
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

    def post(self, request):
        subject = f"Message from {request.user.first_name} {request.user.last_name}"
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")

        try:
            send_mail(subject, message, email)
            messages.success(request, 'Message has been send successfully!')
        except BadHeaderError as e:
            messages.warning(request, f"Message can't be send because {e}")

        return redirect('about_view')

class NewsView(LoginRequiredMixin, View):
    pictures = {1:'images/logo1.png', 2:'images/logo2.png', 3:'images/logo3.png', 4:'images/logo4.png', 5:'images/logo5.png'}
    data = [
        {"image":"images/news1.jpg", 
        'descriprion':"The world's biggest memory-chip and smartphone maker forecast operating profit of $11bn (£8bn) for the three months to the end of June. It said strong demand for memory chips had offset weaker sales of devices due to the shortage of components. A year ago, in the first few months of the pandemic, Samsung saw sales of products such as phones and TVs slump.",
        'header': 'Tech giant Samsung Electronics has said it expects its quarterly profit to rise by 53%, amid a global chip shortage.'}, 
        
        {"image":"images/news2.jpg", 
        'descriprion': "Incredibly powerful graphics card with TITAN-class performance At the heart of Ampere - the second generation NVIDIA RTX architecture - with double the performance of ray tracing and artificial intelligence technologies thanks to improved cores for ray tracing (RT), tensor cores and new streaming multiprocessors. The graphics card also features the G6X's impressive 24GB video memory designed to deliver an exceptional level of gaming.",
        'header': "GEFORCE RTX 3090."}, 
        
        {"image":"images/news3.jpg", 
        'descriprion':"Windows has always existed to be a stage for the world’s innovation. It’s been the backbone of global businesses and where scrappy startups became household names. The web was born and grew up on Windows. It’s the place where many of us wrote our first email, played our first PC game and wrote our first line of code. Windows is the place people go to create, to connect, to learn and to achieve – a platform over a billion people today rely on. ",
        'header': "Introducing Windows 11."},
       
       {"image":"images/news4.jpg", 
        'descriprion':"Intel has finally announced its new Intel Core processors of the 11th generation (Rocket Lake-S series). The architecture was updated for the first time in 5 years. The ancient Skylake was replaced by the modern Cypress Cove. The Rocket Lake-S family currently consists of almost two dozen models. The TDP level is from 35 to 125 watts. Cores — 6 or 8, the frequency of operation-up to 5.3 GHz. The new chips are compatible with both 500-series and 400-series motherboards.",
        'header': "Intel Core processors of the 11th generation (Rocket Lake-S)are presented."}
        ]
    def get(self, request):
        return render(request, template_name="main/news.html", context={"pictures":self.pictures, "data":self.data})

class ServicesView(LoginRequiredMixin, View):
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
