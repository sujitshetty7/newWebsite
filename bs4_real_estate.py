from bs4 import BeautifulSoup
import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

def replace_text_in_tag(tag, old_text, new_text):
    for node in tag.find_all(text=re.compile(old_text, re.I)):
        node.replace_with(re.sub(re.compile(old_text, re.I), new_text, node))

# Metadata
if soup.title:
    soup.title.string = "SUJIT SHETTY | Real Estate Expert & Advertising Expert"

for meta in soup.find_all('meta'):
    name = meta.get('name', '')
    prop = meta.get('property', '')
    if name in ['description', 'twitter:description'] or prop in ['og:description']:
        meta['content'] = "Sujit Shetty is a real estate expert, sole selling specialist and advertising expert helping businesses, developers and property owners generate visibility, leads and sales."
    elif name in ['twitter:title'] or prop in ['og:title']:
        meta['content'] = "SUJIT SHETTY | Real Estate Expert & Advertising Expert"

# Clean any logos pointing to vincent or gympropel
for img in soup.find_all('img'):
    src = img.get('src', '')
    if 'vincent' in src or 'gympropel' in src:
        img['src'] = ''

# Global string replacements inside the text nodes safely
for text_node in soup.find_all(text=True):
    if text_node.parent.name in ['script', 'style']:
        continue
    # Replace explicit names
    s = str(text_node)
    s = s.replace('GymPropel', 'Sujit Shetty')
    s = s.replace('Vincent Yu', 'Sujit Shetty')
    s = s.replace('Vincent, the founder', 'Sujit Shetty')
    s = s.replace('Vincent', 'Sujit Shetty')
    
    # Generic button replacements
    s = re.sub(r'Claim free intro', 'Get Free Consultation', s, flags=re.IGNORECASE)
    s = re.sub(r'See the results', 'Get Free Consultation', s, flags=re.IGNORECASE)
    s = re.sub(r'Book a call', 'Contact Me', s, flags=re.IGNORECASE)
    
    # Hero text replacements specifically tailored to exact existing strings
    s = s.replace('Gym marketing agency', 'Trusted Property Advisor & Marketer')
    s = s.replace('Helping you buy, sell, and market residential homes, NA plots, and investment properties across Shahapur and Thane. Simple guidance, honest advice, and proven results.', 'Helping you buy, sell, and market residential homes, NA plots, and investment properties across Shahapur and Thane. Simple guidance, honest advice, and proven results.')
    
    s = s.replace('Real gyms, real owners.', 'Real Estate Expert')
    s = s.replace('29M+ in total revenue.', 'Sole Selling Agency')
    s = s.replace('116+ active gyms.', 'Advertising Expert')
    s = s.replace('5.0 out of 5 stars.', '8+ Years Experience')
    s = s.replace('First month free.', '8+ YEARS OF EXPERIENCE · SHAHAPUR & NEARBY REGIONS')

    # Proof
    s = s.replace('From project launches to lead generation, sales and closures — I work across the complete real estate sales ecosystem.', 'From project launches to lead generation, sales and closures — I work across the complete real estate sales ecosystem.')
    s = s.replace('Active Gyms', 'Years Experience')
    s = s.replace('Total Revenue', 'Core Market')
    s = s.replace('Leads Generated', 'Sales & Marketing')
    s = s.replace('Campaigns Built', 'Project Support')
    
    # Process
    s = s.replace('They bill upfront', 'YOU BUILD IT. I HELP SELL IT.')
    s = s.replace('We show up', 'WITHOUT BUILDING A HUGE IN-HOUSE TEAM.')
    s = s.replace('Most gym marketing agencies bill upfront and disappear. We take a different approach. We are your partner. Meaning we are right alongside you in the trenches of running a gym and only charge for results.', 'Marketing is only useful when it moves people closer to a sale. I combine branding, advertising, lead generation, calling, property showcases, sales coordination and closing support into one execution system.')
    
    # Funnel
    s = s.replace('Watch a stranger in a feed become a member on the floor. Everything is tracked, measured and optimised for revenue, not just clicks.', 'A property buyer doesn\'t wake up ready to book. They search. They compare. They enquire. They visit. They negotiate. Then they decide. My job is to build and manage that journey.')
    s = s.replace('Instagram, Facebook, Google', 'Google · Instagram · Facebook · Ads')
    s = s.replace('Ads that stop the scroll', 'WhatsApp · Calls · Lead Forms')
    s = s.replace('Lead gen forms & landing pages', 'Budget · Requirement · Location · Timeline')
    s = s.replace('Automated follow-up text & email', 'Property Showcase · Site Visit · Follow-up')
    s = s.replace('Online calendar scheduling', 'Pricing · Documentation · Loan Coordination')
    s = s.replace('In-person intro & close', 'Booking · Registration · Handover')

    # Numbers
    s = s.replace('Real gym owners, on camera, talking about the real impact Sujit Shetty has made on their business and their life.', 'Real estate isn\'t about collecting leads. It\'s about moving the right leads forward.')
    s = s.replace('"Sujit Shetty helped us add 88 members in 3 months."', '"Years in the Industry"')
    s = s.replace('"We doubled our revenue in 6 months."', '"Marketing + Sales Approach"')
    s = s.replace('"We had a $22k month, our best ever."', '"Point of Contact"')
    s = s.replace('"We grew from 140 to 220 members."', '"Primary Market"')
    s = s.replace('"Our close rate jumped 30%."', '"Project Execution"')
    s = s.replace('"We are the #1 gym in our city now."', '"Revenue-Focused Strategy"')

    # Offer
    s = s.replace('Your first 30 days of gym marketing are free. No catch. No setup fee. We cover the cost of the ads, the software and the work. If you don\'t make money, we part as friends.', 'Before spending more on advertising, understand what\'s actually stopping your project from selling.')
    s = s.replace('Account audit & strategy', 'Project Positioning')
    s = s.replace('Ad creation & launch', 'Market Analysis')
    s = s.replace('Automated follow-up setup', 'Pricing & Offer')
    s = s.replace('Landing page build', 'Advertising Strategy')
    s = s.replace('Weekly reporting', 'Lead Generation')
    s = s.replace('Monthly strategy call', 'Sales Process')
    s = s.replace('Cancel anytime', 'Conversion')
    
    # Map
    s = s.replace('One gym per market. Once we partner with you, we won\'t work with another gym within a 5-mile radius. Your leads are yours, and your market is locked.', 'Shahapur is not just a location on a map. It\'s a market with its own buyers, price points, developers, micro-markets and buying behaviour. My primary focus is Shahapur and nearby regions.')

    # Duel
    s = s.replace('No account manager, no ticket queue, no waiting 48 hours for a reply. When you have a question about your ads, you message Sujit Shetty directly, and he answers in minutes.', 'No endless meetings. No passing the project through five departments. Talk directly with Sujit about your property, marketing, sales or personal brand.')
    s = s.replace('Why did my leads drop this week?', 'We need more enquiries.')
    s = s.replace('Thanks for reaching out! A support ticket has been created.', 'Let\'s first find out why the current enquiries aren\'t converting.')
    s = s.replace('Your account assistant will follow up.', 'Our project isn\'t getting enough visibility.')
    s = s.replace('Any update?', 'Let\'s fix the positioning before increasing the ad spend.')
    s = s.replace('On it. I\'m looking at your numbers now.', 'I want my name to show up on Google.')
    s = s.replace('Found it. Let\'s talk tomorrow at 9?', 'Let\'s build the personal brand and search presence around it.')
    s = s.replace('Perfect. See you then.', 'Exactly.')
    
    # Footer
    s = s.replace('Sujit Shetty is a marketing agency exclusively for gym owners. We run ads, follow up with leads, and guarantee new members.', 'Sujit Shetty is a real estate expert, sole selling specialist and advertising expert with 8+ years of experience, focused on Shahapur and nearby regions.')
    
    # Generic fallback
    if re.search(r'\bgroup class(es)?\b', s, re.I): s = re.sub(r'\bgroup class(es)?\b', 'site visit', s, flags=re.I)
    if re.search(r'\bmembers?\b', s, re.I): s = re.sub(r'\bmembers?\b', 'buyers', s, flags=re.I)
    if re.search(r'\bHIIT\b', s, re.I): s = re.sub(r'\bHIIT\b', 'sales', s, flags=re.I)
    if re.search(r'\bcrossfit\b', s, re.I): s = re.sub(r'\bcrossfit\b', 'real estate', s, flags=re.I)
    
    if text_node.string != s:
        text_node.replace_with(s)

# Nav Links
for nav in soup.find_all('ul', class_='nav__list'):
    nav.clear()
    for text, link in [("Real Estate", "/"), ("Sole Selling", "/"), ("Advertising", "/"), ("Personal Branding", "/"), ("About", "/"), ("Insights", "/")]:
        li = soup.new_tag('li')
        li['class'] = 'nav__item'
        a = soup.new_tag('a', href=link)
        a['class'] = 'nav__link'
        a.string = text
        li.append(a)
        nav.append(li)

# Data text replacements
for tag in soup.find_all(attrs={"data-text": True}):
    if "Claim" in tag['data-text'] or "See the results" in tag['data-text']:
        tag['data-text'] = "Get Free Consultation"
    if "Book a call" in tag['data-text']:
        tag['data-text'] = "Contact Me"

# Remove hero funnels and chat waiting
for div in soup.find_all(class_=re.compile(r'hero__floating|chat__wait|chat__booked|map-p')):
    div.decompose()

# Titles needing exact structure replaced
hero_title = soup.find('h1', class_='hero__title')
if hero_title: hero_title.clear(); hero_title.string = "Your Trusted Guide to Real Estate in Shahapur – Sujit Shetty"
proof_title = soup.find('h2', class_='proof__title')
if proof_title: proof_title.clear(); proof_title.string = "TRUSTED BY REAL ESTATE BUSINESSES."
fn_title = soup.find('span', class_='fn__title')
if fn_title: fn_title.clear(); fn_title.string = "FROM SEARCH TO SITE VISIT. TO SIGNED."
num_title = soup.find('span', class_='num__title')
if num_title: num_title.clear(); num_title.string = "NUMBERS WITH PURPOSE."
book_title = soup.find('span', class_='book__title')
if book_title: book_title.clear(); book_title.string = "STRAIGHT TO THE POINT."
book_intro = soup.find('p', class_='book__intro')
if book_intro: book_intro.string = "YOUR NEXT PROJECT STARTS HERE. I DON'T SELL MARKETING. I SOLVE BUSINESS PROBLEMS."
footer_title = soup.find('h2', class_='footer__title')
if footer_title: footer_title.clear(); footer_title.string = "BUILD YOUR PRESENCE. BUILD YOUR SALES."

# Stat nums manual overwrite to fix exact
stats = soup.find_all('span', class_='stat-num')
if len(stats) >= 4:
    stats[0].string = "08+"
    stats[1].string = "Shahapur"
    stats[2].string = "360°"
    stats[3].string = "End-to-End"

# Logos
logo_ul = soup.find('ul', class_='trusted-by__list')
if logo_ul:
    logo_ul.clear()
    logo_ul['style'] = "display:flex;flex-wrap:wrap;justify-content:center;gap:2rem;"
    for t in ["Real Estate Developers", "Property Owners", "Builders", "Brokers", "Investors", "Local Businesses"]:
        li = soup.new_tag('li')
        li['style'] = "font-size:1.2rem;font-weight:bold;opacity:0.7"
        li.string = t
        logo_ul.append(li)

# Process List Overwrite (keeping classes)
process_ul = soup.find('ul', class_='process__list')
if process_ul:
    process_ul.clear()
    d = [("BRANDING", "Position your project so people remember it."), ("ADVERTISING", "Put your property in front of the right audience."), ("LEAD GENERATION", "Turn attention into qualified enquiries."), ("SALES", "Follow up, showcase and move prospects toward booking."), ("CLOSURES", "Stay involved until the transaction moves forward.")]
    for i, (t, p) in enumerate(d):
        li = soup.new_tag('li')
        li['class'] = 'process-p'
        div1 = soup.new_tag('div')
        div1['class'] = 'process-p__no mono'
        div1.string = f"0{i+1}"
        div2 = soup.new_tag('div')
        div2['class'] = 'process-p__main'
        h3 = soup.new_tag('h3')
        h3['class'] = 'process-p__title'
        h3.string = t
        pp = soup.new_tag('p')
        pp['class'] = 'process-p__desc'
        pp.string = p
        div2.append(h3)
        div2.append(pp)
        li.append(div1)
        li.append(div2)
        process_ul.append(li)

# Svc Grid
svc = soup.find('ul', class_='svc-grid')
if svc:
    svc.clear()
    sd = [("REAL ESTATE", "Property sales, market knowledge and buyer acquisition across Shahapur and nearby regions."), ("SOLE SELLING", "End-to-end sales and marketing execution for developers and projects."), ("BRANDING", "Positioning, creative direction and communication that makes projects stand out."), ("ADVERTISING", "Meta, Google and digital campaigns built around measurable enquiries."), ("SALES", "Lead calling, qualification, site visits, follow-ups and closure support."), ("PROJECT MARKETING", "Launch strategy, campaign planning, property showcases and sales infrastructure."), ("CLIENT MANAGEMENT", "Communication between buyers, developers, sales teams and other stakeholders."), ("AFTER-SALES", "Documentation, loan coordination, registration, recovery and handover support.")]
    for i, (t, p) in enumerate(sd):
        li = soup.new_tag('li')
        li['class'] = 'svc-p'
        div1 = soup.new_tag('div')
        div1['class'] = 'svc-p__top'
        sp1 = soup.new_tag('span')
        sp1['class'] = 'svc-p__no mono'
        sp1.string = f"0{i+1}"
        div1.append(sp1)
        h3 = soup.new_tag('h3')
        h3['class'] = 'svc-p__title'
        h3.string = t
        pp = soup.new_tag('p')
        pp['class'] = 'svc-p__desc'
        pp.string = p
        li.append(div1)
        li.append(h3)
        li.append(pp)
        svc.append(li)

# Blog -> PB
blog_h2 = soup.find('span', class_='blog__title')
if blog_h2: blog_h2.clear(); blog_h2.string = "YOUR COMPANY HAS A WEBSITE. DOES YOUR NAME HAVE ONE?"
blog_intro = soup.find('p', class_='blog__intro')
if blog_intro: blog_intro.string = "Build a professional personal brand around your name — with a website, content, SEO and digital presence designed to make you more discoverable."
blog_ul = soup.find('ul', class_='blog-grid')
if blog_ul:
    blog_ul.clear()
    bd = [("PERSONAL WEBSITE", "A professional digital home built around you."), ("GOOGLE VISIBILITY", "Build your presence across search."), ("CONTENT", "Turn your experience into authority."), ("LINKEDIN", "Position yourself where business happens."), ("SEO", "Build long-term organic visibility."), ("PERSONAL BRAND", "Become more than the company you represent.")]
    for t, p in bd:
        li = soup.new_tag('li')
        li['class'] = 'blog-p'
        h3 = soup.new_tag('h3')
        h3['class'] = 'blog-p__title'
        h3.string = t
        pp = soup.new_tag('p')
        pp['class'] = 'blog-p__desc'
        pp.string = p
        li.append(h3)
        li.append(pp)
        blog_ul.append(li)

# Footer nav
footer_navs = soup.find_all('ul', class_='footer__nav')
if len(footer_navs) >= 2:
    footer_navs[0].clear()
    for text, link in [("About", "/"), ("Real Estate", "/"), ("Sole Selling", "/"), ("Advertising", "/"), ("Personal Branding", "/"), ("Insights", "/"), ("Portfolio", "/"), ("Contact", "/")]:
        li = soup.new_tag('li')
        a = soup.new_tag('a', href=link)
        a.string = text
        li.append(a)
        footer_navs[0].append(li)
    footer_navs[1].clear()
    for text, link in [("Real Estate Sales", "/"), ("Sole Selling Agency", "/"), ("Project Marketing", "/"), ("Digital Advertising", "/"), ("Website Development", "/"), ("Personal Branding", "/"), ("SEO", "/")]:
        li = soup.new_tag('li')
        a = soup.new_tag('a', href=link)
        a.string = text
        li.append(a)
        footer_navs[1].append(li)

html = str(soup)
html = re.sub(r'(>)([^<]*?)(?i)\bgym\b([^<]*?)(<)', r'\1\2property\3\4', html)
html = re.sub(r'(>)([^<]*?)(?i)\bgyms\b([^<]*?)(<)', r'\1\2properties\3\4', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
