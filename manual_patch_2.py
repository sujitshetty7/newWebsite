import re

with open('index_backup.html', 'r', encoding='utf-8') as f:
    text = f.read()

# SAFE METADATA
text = re.sub(r'<title>.*?</title>', '<title>SUJIT SHETTY | Real Estate Expert &amp; Advertising Expert</title>', text)
text = re.sub(r'<meta name="description" content="[^"]+">', '<meta name="description" content="Sujit Shetty is a real estate expert, sole selling specialist and advertising expert helping businesses, developers and property owners generate visibility, leads and sales.">', text)
text = re.sub(r'<meta property="og:title" content="[^"]+">', '<meta property="og:title" content="SUJIT SHETTY | Real Estate Expert & Advertising Expert">', text)
text = re.sub(r'<meta property="og:description" content="[^"]+">', '<meta property="og:description" content="Sujit Shetty is a real estate expert, sole selling specialist and advertising expert helping businesses, developers and property owners generate visibility, leads and sales.">', text)

# BRAND REPLACEMENTS - global text node safe replacements
text = text.replace('GymPropel', 'Sujit Shetty')
text = text.replace('Vincent Yu', 'Sujit Shetty')
text = text.replace('Vincent, the founder', 'Sujit Shetty')
text = text.replace('Vincent', 'Sujit Shetty')
text = text.replace('gympropel.com', 'sujitshetty.in')

# HERO
text = text.replace('Gym marketing agency', 'Trusted Property Advisor &amp; Marketer')

# We must use EXACT regex for the hero__title spans
hero_title_new = '<h1 class="hero__title">Your Trusted Guide to Real Estate in Shahapur – Sujit Shetty</h1>'
text = re.sub(r'<h1 class="hero__title"[^>]*>.*?</h1>', hero_title_new, text, flags=re.DOTALL)
hero_lead_new = '<p class="hero__lead">Helping you buy, sell, and market residential homes, NA plots, and investment properties across Shahapur and Thane. Simple guidance, honest advice, and proven results.</p>'
text = re.sub(r'<p class="hero__lead".*?</p>', hero_lead_new, text, flags=re.DOTALL)

# Nav structure
text = text.replace('Property marketing agency', 'Real Estate × Sales × Marketing')
text = re.sub(r'Claim free intro', 'Get Free Consultation', text, flags=re.IGNORECASE)
text = re.sub(r'data-text="Claim free intro"', 'data-text="Get Free Consultation"', text, flags=re.IGNORECASE)
text = re.sub(r'data-text="See the results"', 'data-text="Get Free Consultation"', text, flags=re.IGNORECASE)
text = re.sub(r'See the results', 'Get Free Consultation', text, flags=re.IGNORECASE)
text = re.sub(r'Book a call', 'Contact Me', text, flags=re.IGNORECASE)
text = re.sub(r'data-text="Book a call"', 'data-text="Contact Me"', text, flags=re.IGNORECASE)

# Nav Links specific targeting (keeping classes)
nav_block = '''<ul class="nav__list">
<li class="nav__item"><a class="nav__link" href="/">Real Estate</a></li>
<li class="nav__item"><a class="nav__link" href="/">Sole Selling</a></li>
<li class="nav__item"><a class="nav__link" href="/">Advertising</a></li>
<li class="nav__item"><a class="nav__link" href="/">Personal Branding</a></li>
<li class="nav__item"><a class="nav__link" href="/">About</a></li>
<li class="nav__item"><a class="nav__link" href="/">Insights</a></li>
</ul>'''
text = re.sub(r'<ul class="nav__list">.*?</ul>', nav_block, text, flags=re.DOTALL)

menu_block = '''<ul class="menu__list">
<li class="menu__item"><a class="menu__link" href="/">Real Estate</a></li>
<li class="menu__item"><a class="menu__link" href="/">Sole Selling</a></li>
<li class="menu__item"><a class="menu__link" href="/">Advertising</a></li>
<li class="menu__item"><a class="menu__link" href="/">Personal Branding</a></li>
<li class="menu__item"><a class="menu__link" href="/">About</a></li>
<li class="menu__item"><a class="menu__link" href="/">Insights</a></li>
</ul>'''
text = re.sub(r'<ul class="menu__list">.*?</ul>', menu_block, text, flags=re.DOTALL)


# Hero Badges
text = text.replace('Real gyms, real owners.', 'Real Estate Expert')
text = text.replace('29M+ in total revenue.', 'Sole Selling Agency')
text = text.replace('116+ active gyms.', 'Advertising Expert')
text = text.replace('5.0 out of 5 stars.', '8+ Years Experience')

# Floating items in hero removal
text = re.sub(r'<div class="hero__floating.*?</div>\s*</div>\s*</div>', '', text, flags=re.DOTALL)
text = text.replace('First month free.', '8+ YEARS OF EXPERIENCE · SHAHAPUR & NEARBY REGIONS')

# Proof
text = re.sub(r'<h2 class="proof__title".*?</h2>', '<h2 class="proof__title">TRUSTED BY REAL ESTATE BUSINESSES.</h2>', text, flags=re.DOTALL)
text = re.sub(r'<p class="proof__lead".*?</p>', '<p class="proof__lead">From project launches to lead generation, sales and closures — I work across the complete real estate sales ecosystem.</p>', text, flags=re.DOTALL)
text = text.replace('<span class="stat-num">116</span>', '<span class="stat-num">08+</span>')
text = text.replace('<span class="stat-desc">Active Gyms</span>', '<span class="stat-desc">Years Experience</span>')
text = text.replace('<span class="stat-num">29M</span>', '<span class="stat-num">Shahapur</span>')
text = text.replace('<span class="stat-desc">Total Revenue</span>', '<span class="stat-desc">Core Market</span>')
text = text.replace('<span class="stat-num">300K</span>', '<span class="stat-num">360°</span>')
text = text.replace('<span class="stat-desc">Leads Generated</span>', '<span class="stat-desc">Sales & Marketing</span>')
text = text.replace('<span class="stat-num">500</span>', '<span class="stat-num">End-to-End</span>')
text = text.replace('<span class="stat-desc">Campaigns Built</span>', '<span class="stat-desc">Project Support</span>')

logos_block = '''<ul class="trusted-by__list" style="display:flex;flex-wrap:wrap;justify-content:center;gap:2rem;">
<li style="font-size:1.2rem;font-weight:bold;opacity:0.7">Real Estate Developers</li>
<li style="font-size:1.2rem;font-weight:bold;opacity:0.7">Property Owners</li>
<li style="font-size:1.2rem;font-weight:bold;opacity:0.7">Builders</li>
<li style="font-size:1.2rem;font-weight:bold;opacity:0.7">Brokers</li>
<li style="font-size:1.2rem;font-weight:bold;opacity:0.7">Investors</li>
<li style="font-size:1.2rem;font-weight:bold;opacity:0.7">Local Businesses</li>
</ul>'''
text = re.sub(r'<ul class="trusted-by__list".*?</ul>', logos_block, text, flags=re.DOTALL)

# Process Section -> CMP (You build it, I help sell it)
text = text.replace('<span class="process__title">They bill upfront.<br>\nWe show up.</span>', '<span class="process__title">YOU BUILD IT. I HELP SELL IT.<br>WITHOUT BUILDING A HUGE IN-HOUSE TEAM.</span>')
text = text.replace('Most gym marketing agencies bill upfront and disappear. We take a different approach. We are your partner. Meaning we are right alongside you in the trenches of running a gym and only charge for results.', 'Marketing is only useful when it moves people closer to a sale. I combine branding, advertising, lead generation, calling, property showcases, sales coordination and closing support into one execution system.')
text = text.replace('<span class="eyebrow" data-i="03">business model</span>', '<span class="eyebrow" data-i="03">business model</span>')

# Modify the process cards exactly without breaking ul classes
text = text.replace('<h3 class="process-p__title">No contracts.</h3>', '<h3 class="process-p__title">BRANDING</h3>')
text = text.replace('<p class="process-p__desc">We don\'t lock you in. You stay because it works, not because you have to.</p>', '<p class="process-p__desc">Position your project so people remember it.</p>')

text = text.replace('<h3 class="process-p__title">No setup fees.</h3>', '<h3 class="process-p__title">ADVERTISING</h3>')
text = text.replace('<p class="process-p__desc">We cover the cost of building your ads, landing pages, and automated follow-up.</p>', '<p class="process-p__desc">Put your property in front of the right audience.</p>')

text = text.replace('<h3 class="process-p__title">No ad spend.</h3>', '<h3 class="process-p__title">LEAD GENERATION</h3>')
text = text.replace('<p class="process-p__desc">We cover the ad spend for your first 30 days. No catch. No hidden fees.</p>', '<p class="process-p__desc">Turn attention into qualified enquiries.</p>')

text = text.replace('<h3 class="process-p__title">No brainer.</h3>', '<h3 class="process-p__title">SALES</h3>')
text = text.replace('<p class="process-p__desc">If we don\'t make you money, we part as friends. Zero risk on your end.</p>', '<p class="process-p__desc">Follow up, showcase and move prospects toward booking.</p>')

# Add a 5th card to process
process_card_5 = '''<li class="process-p">
<div class="process-p__no mono" aria-hidden="true" data-nosnippet="">05</div>
<div class="process-p__main">
<h3 class="process-p__title">CLOSURES</h3>
<p class="process-p__desc">Stay involved until the transaction moves forward.</p>
</div>
</li>'''
# Append to end of process__list
text = re.sub(r'(<ul class="process__list"[^>]*>.*?</li\s*>)\s*(</ul>)', lambda m: m.group(1) + process_card_5 + m.group(2), text, flags=re.DOTALL)

# FN (Funnel)
text = text.replace('<span class="fn__title">From scroll to <em class="serif">signed.</em></span>', '<span class="fn__title">FROM SEARCH TO SITE VISIT.<br>TO <em class="serif">SIGNED.</em></span>')
text = text.replace('Watch a stranger in a feed become a member on the floor. Everything is tracked, measured and optimised for revenue, not just clicks.', 'A property buyer doesn\'t wake up ready to book. They search. They compare. They enquire. They visit. They negotiate. Then they decide. My job is to build and manage that journey.')
text = text.replace('01 — DISCOVER', '01 — DISCOVER')
text = text.replace('Instagram, Facebook, Google', 'Google · Instagram · Facebook · Ads')
text = text.replace('02 — ENGAGE', '02 — ENQUIRE')
text = text.replace('Ads that stop the scroll', 'WhatsApp · Calls · Lead Forms')
text = text.replace('03 — CAPTURE', '03 — QUALIFY')
text = text.replace('Lead gen forms & landing pages', 'Budget · Requirement · Location · Timeline')
text = text.replace('04 — NURTURE', '04 — VISIT')
text = text.replace('Automated follow-up text & email', 'Property Showcase · Site Visit · Follow-up')
text = text.replace('05 — BOOK', '05 — NEGOTIATE')
text = text.replace('Online calendar scheduling', 'Pricing · Documentation · Loan Coordination')
text = text.replace('06 — SHOW', '06 — CLOSE')
text = text.replace('In-person intro & close', 'Booking · Registration · Handover')


# NUM (Numbers)
text = text.replace('<span class="num__title">Numbers with <em class="serif">names.</em></span>', '<span class="num__title">NUMBERS WITH <em class="serif">PURPOSE.</em></span>')
text = text.replace('Real gym owners, on camera, talking about the real impact Sujit Shetty has made on their business and their life.', 'Real estate isn\'t about collecting leads. It\'s about moving the right leads forward.')
text = text.replace('<span class="num-p__no">88</span>', '<span class="num-p__no">08+</span>')
text = text.replace('"Sujit Shetty helped us add 88 members in 3 months."', '"Years in the Industry"')
text = text.replace('<span class="num-p__no">2x</span>', '<span class="num-p__no">360°</span>')
text = text.replace('"We doubled our revenue in 6 months."', '"Marketing + Sales Approach"')
text = text.replace('<span class="num-p__no">$22k</span>', '<span class="num-p__no">1</span>')
text = text.replace('"We had a $22k month, our best ever."', '"Point of Contact"')
text = text.replace('<span class="num-p__no">220</span>', '<span class="num-p__no">Shahapur</span>')
text = text.replace('"We grew from 140 to 220 members."', '"Primary Market"')
text = text.replace('<span class="num-p__no">30%</span>', '<span class="num-p__no">End-to-End</span>')
text = text.replace('"Our close rate jumped 30%."', '"Project Execution"')
text = text.replace('<span class="num-p__no">#1</span>', '<span class="num-p__no">₹</span>')
text = text.replace('"We are the #1 gym in our city now."', '"Revenue-Focused Strategy"')


# SVC (Services)
text = text.replace('<span class="svc__title">What we <em class="serif">run.</em></span>', '<span class="svc__title">WHAT I <em class="serif">DO.</em></span>')
text = re.sub(r'<p class="svc__intro"><strong>Six services.*?</p>', '<p class="svc__intro">One real estate project can require ten different people. Marketing. Advertising. Calling. Sales. Site visits. Negotiation. Loans. Registration. Recovery. Handover. I connect the pieces.</p>', text, flags=re.DOTALL)

text = text.replace('<h3 class="svc-p__title">Facebook ads</h3>', '<h3 class="svc-p__title">REAL ESTATE</h3>')
text = text.replace('<p class="svc-p__desc">Hyper-local campaigns targeting your ideal demographic within a 5-10 mile radius of your gym.</p>', '<p class="svc-p__desc">Property sales, market knowledge and buyer acquisition across Shahapur and nearby regions.</p>')

text = text.replace('<h3 class="svc-p__title">Instagram ads</h3>', '<h3 class="svc-p__title">SOLE SELLING</h3>')
text = text.replace('<p class="svc-p__desc">Visual-first creative that showcases your facility, community and workouts.</p>', '<p class="svc-p__desc">End-to-end sales and marketing execution for developers and projects.</p>')

text = text.replace('<h3 class="svc-p__title">Google ads</h3>', '<h3 class="svc-p__title">BRANDING</h3>')
text = text.replace('<p class="svc-p__desc">Capture high-intent search traffic for keywords like "gyms near me" or "crossfit [city]".</p>', '<p class="svc-p__desc">Positioning, creative direction and communication that makes projects stand out.</p>')

text = text.replace('<h3 class="svc-p__title">Lead follow-up</h3>', '<h3 class="svc-p__title">ADVERTISING</h3>')
text = text.replace('<p class="svc-p__desc">Automated SMS, email and voicemail sequences that trigger within 5 minutes of a new lead.</p>', '<p class="svc-p__desc">Meta, Google and digital campaigns built around measurable enquiries.</p>')

text = text.replace('<h3 class="svc-p__title">Websites</h3>', '<h3 class="svc-p__title">SALES</h3>')
text = text.replace('<p class="svc-p__desc">Conversion-optimised landing pages that turn ad clicks into booked intro classes.</p>', '<p class="svc-p__desc">Lead calling, qualification, site visits, follow-ups and closure support.</p>')

text = text.replace('<h3 class="svc-p__title">Automation</h3>', '<h3 class="svc-p__title">PROJECT MARKETING</h3>')
text = text.replace('<p class="svc-p__desc">Zapier integrations that sync leads across your CRM, email platform and billing software.</p>', '<p class="svc-p__desc">Launch strategy, campaign planning, property showcases and sales infrastructure.</p>')

# Add the two additional services cleanly
extra_svc_lis = r'''<li class="svc-p">
<div aria-hidden="true" class="svc-p__top" data-nosnippet=""><span class="svc-p__no mono">07</span><span class="svc-p__live mono"><i class="svc-pulse"></i>Live</span></div>
<h3 class="svc-p__title">CLIENT MANAGEMENT</h3>
<p class="svc-p__desc">Communication between buyers, developers, sales teams and other stakeholders.</p>
</li>
<li class="svc-p">
<div aria-hidden="true" class="svc-p__top" data-nosnippet=""><span class="svc-p__no mono">08</span><span class="svc-p__live mono"><i class="svc-pulse"></i>Live</span></div>
<h3 class="svc-p__title">AFTER-SALES</h3>
<p class="svc-p__desc">Documentation, loan coordination, registration, recovery and handover support.</p>
</li>
'''
text = re.sub(r'(<ul class="svc-grid" role="list">.*?)(</ul>)', lambda m: m.group(1) + extra_svc_lis + m.group(2), text, flags=re.DOTALL)


# OFFER (Clarity)
text = text.replace('<span class="offer__title">Month one is <em class="serif">on us.</em></span>', '<span class="offer__title">YOUR FIRST MOVE STARTS WITH <em class="serif">CLARITY.</em></span>')
text = text.replace('Your first 30 days of gym marketing are free. No catch. No setup fee. We cover the cost of the ads, the software and the work. If you don\'t make money, we part as friends.', 'Before spending more on advertising, understand what\'s actually stopping your project from selling.')

text = text.replace('Account audit & strategy', 'Project Positioning')
text = text.replace('Ad creation & launch', 'Market Analysis')
text = text.replace('Automated follow-up setup', 'Pricing & Offer')
text = text.replace('Landing page build', 'Advertising Strategy')
text = text.replace('Weekly reporting', 'Lead Generation')
text = text.replace('Monthly strategy call', 'Sales Process')
text = text.replace('Cancel anytime', 'Conversion')


# MARKET MAP
text = text.replace('<span class="map__title">Your market. <em class="serif">Locked.</em></span>', '<span class="map__title">YOUR MARKET. <em class="serif">MY TERRITORY.</em></span>')
text = text.replace('One gym per market. Once we partner with you, we won\'t work with another gym within a 5-mile radius. Your leads are yours, and your market is locked.', 'Shahapur is not just a location on a map. It\'s a market with its own buyers, price points, developers, micro-markets and buying behaviour. My primary focus is Shahapur and nearby regions.')
# Clean out the visual pins to avoid random text
text = re.sub(r'<div class="map-p".*?</div>', '', text, flags=re.DOTALL)

map_labels = ["Shahapur", "Vasind", "Asangaon", "Atgaon", "Khardi", "Kasara", "Nearby Growth Corridors"]
map_divs = re.findall(r'<div class="map-l__name">.*?</div>', text)
for i, div in enumerate(map_divs):
    if i < len(map_labels):
        text = text.replace(div, f'<div class="map-l__name">{map_labels[i]}</div>')

# FOUNDER (Chat)
text = text.replace('<span class="duel__title">You talk to the <em class="serif">founder.</em></span>', '<span class="duel__title">YOU TALK TO THE PERSON <em class="serif">DOING THE WORK.</em></span>')
text = text.replace('No account manager, no ticket queue, no waiting 48 hours for a reply. When you have a question about your ads, you message Sujit Shetty directly, and he answers in minutes.', 'No endless meetings. No passing the project through five departments. Talk directly with Sujit about your property, marketing, sales or personal brand.')
text = text.replace('Why did my leads drop this week?', 'We need more enquiries.')
text = text.replace('Thanks for reaching out! A support ticket has been created.<span class="msg__meta" data-v="Ticket #4821 · Expected reply: 48h"></span>', 'Let\'s first find out why the current enquiries aren\'t converting.')
text = text.replace('Your account assistant will follow up.', 'Our project isn\'t getting enough visibility.')
text = text.replace('Any update?', 'Let\'s fix the positioning before increasing the ad spend.')
text = text.replace('On it. I\'m looking at your numbers now.', 'I want my name to show up on Google.')
text = text.replace('Found it. Let\'s talk tomorrow at 9?', 'Let\'s build the personal brand and search presence around it.')
text = text.replace('Perfect. See you then.', 'Exactly.')
text = text.replace('One gets a ticket. One gets <em class="serif">Sujit Shetty.</em>', '')
# Ensure the "waiting for an agent" and "Call booked" stuff is scrubbed
text = re.sub(r'<li class="chat__wait".*?</li>', '', text, flags=re.DOTALL)
text = re.sub(r'<li class="chat__booked".*?</li>', '', text, flags=re.DOTALL)


# BLOG -> Personal Branding
text = text.replace('<span class="eyebrow" data-i="09">latest insights</span>', '<span class="eyebrow" data-i="09">personal branding</span>')
text = text.replace('<span class="blog__title">The Sujit Shetty <em class="serif">playbook.</em></span>', '<span class="blog__title">YOUR COMPANY HAS A WEBSITE. DOES YOUR <em class="serif">NAME</em> HAVE ONE?</span>')
text = text.replace('Strategies, tactics and lessons from growing 116+ gyms and managing $29M+ in revenue.', 'Build a professional personal brand around your name — with a website, content, SEO and digital presence designed to make you more discoverable.')
text = text.replace('How to price your memberships for maximum retention', 'PERSONAL WEBSITE')
text = text.replace('The 3-step framework for closing 80% of your intro classes', 'GOOGLE VISIBILITY')
text = text.replace('Why your Facebook ads stopped working (and how to fix them)', 'CONTENT')
text = text.replace('The exact automated follow-up sequence that generated 300k leads', 'LINKEDIN')
text = text.replace('How to run a profitable 6-week challenge without discounts', 'SEO')
text = text.replace('The ultimate guide to local SEO for gym owners', 'PERSONAL BRAND')

# Replace the descriptions using direct matches
desc_replacements = [
    ("A professional digital home built around you.", 1),
    ("Build your presence across search.", 1),
    ("Turn your experience into authority.", 1),
    ("Position yourself where business happens.", 1),
    ("Build long-term organic visibility.", 1),
    ("Become more than the company you represent.", 1)
]

for desc, count in desc_replacements:
    text = re.sub(r'<p class="blog-p__desc">.*?</p>', f'<p class="blog-p__desc">{desc}</p>', text, count=1, flags=re.DOTALL)


# BOOK
text = text.replace('<span class="book__title">Straight to<br>\nthe <em class="serif">point.</em></span>', '<span class="book__title">STRAIGHT TO<br>\nTHE <em class="serif">POINT.</em></span>')
text = text.replace('<p class="book__intro">Your next project starts here.</p>', '<p class="book__intro">YOUR NEXT PROJECT STARTS HERE.<br>I DON\'T SELL MARKETING. I SOLVE BUSINESS PROBLEMS.</p>')


# FOOTER
text = text.replace('<h2 class="footer__title">Grow your gym.<br>\nProtect your peace.</h2>', '<h2 class="footer__title">BUILD YOUR PRESENCE.<br>\nBUILD YOUR SALES.</h2>')
text = text.replace('<p class="footer__desc">Sujit Shetty is a marketing agency exclusively for gym owners. We run ads, follow up with leads, and guarantee new members.</p>', '<p class="footer__desc">Sujit Shetty is a real estate expert, sole selling specialist and advertising expert with 8+ years of experience, focused on Shahapur and nearby regions.</p>')

footer_nav_1 = '''<ul class="footer__nav" role="list">
<li><a href="/">About</a></li>
<li><a href="/">Real Estate</a></li>
<li><a href="/">Sole Selling</a></li>
<li><a href="/">Advertising</a></li>
<li><a href="/">Personal Branding</a></li>
<li><a href="/">Insights</a></li>
<li><a href="/">Portfolio</a></li>
<li><a href="/">Contact</a></li>
</ul>'''
text = re.sub(r'<ul class="footer__nav" role="list">.*?</ul>', footer_nav_1, text, count=1, flags=re.DOTALL)

footer_nav_2 = '''<ul class="footer__nav" role="list">
<li><a href="/">Real Estate Sales</a></li>
<li><a href="/">Sole Selling Agency</a></li>
<li><a href="/">Project Marketing</a></li>
<li><a href="/">Digital Advertising</a></li>
<li><a href="/">Website Development</a></li>
<li><a href="/">Personal Branding</a></li>
<li><a href="/">SEO</a></li>
</ul>'''
text = re.sub(r'<ul class="footer__nav" role="list">.*?</ul>', footer_nav_2, text, count=1, flags=re.DOTALL)

text = text.replace('© 2024 Sujit Shetty. All rights reserved.', '© 2026 Sujit Shetty. All rights reserved.')

# NULLIFY GYM LOGOS AND AVATARS
text = re.sub(r'src="[^"]*gympropel-logo[^"]*"', 'src=""', text)
text = re.sub(r'src="[^"]*vincent-[^"]*"', 'src=""', text)
text = re.sub(r'src="[^"]*yourgym\.com[^"]*"', 'src=""', text)
text = re.sub(r'src="[^"]*crossfit[^"]*"', 'src=""', text)
text = re.sub(r'src="[^"]*hiit[^"]*"', 'src=""', text)
text = re.sub(r'src="[^"]*muv[^"]*"', 'src=""', text)


# SCRUB REMAINING STRAGGLERS VERY CAREFULLY
text = re.sub(r'>([^<]*)(?i)gym([^<]*)<', r'>\1property\2<', text)
text = re.sub(r'>([^<]*)(?i)gyms([^<]*)<', r'>\1properties\2<', text)
text = re.sub(r'>([^<]*)(?i)crossfit([^<]*)<', r'>\1real estate\2<', text)
text = re.sub(r'>([^<]*)(?i)hiit([^<]*)<', r'>\1sales\2<', text)
text = re.sub(r'>([^<]*)(?i)members?([^<]*)<', r'>\1buyers\2<', text)
text = re.sub(r'>([^<]*)(?i)group classes([^<]*)<', r'>\1site visits\2<', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
