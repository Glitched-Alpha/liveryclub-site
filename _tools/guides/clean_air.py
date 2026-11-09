from .common import livery, SIGNUP_PLUS

BOX = livery("Livery checks it for you", [
    "With Livery Plus, every car in your garage gets a clean air zone check on its Overview: one verdict for London's ULEZ and the clean air and low emission zones that charge cars in England and Scotland, based on the car's fuel and Euro standard, with what each zone would cost if it doesn't comply.",
    'When you\'re <a href="/guides/used-car-checks-before-buying/">buying a car</a>, the history check shows its Euro status too, so you know before you buy whether it\'ll cost you to drive into town.',
], "See Livery Plus", SIGNUP_PLUS)

BODY = f'''
        <div class="callout">
          <p><strong>The quick answer.</strong> Every UK zone that affects private cars uses the same standard: <strong>Euro 4 for petrol</strong> (most petrol cars registered from 2006) and <strong>Euro 6 for diesel</strong> (most diesel cars registered from September 2015). Fully electric cars always meet it. If your car meets the standard, it's free to drive in London's ULEZ and every clean air zone in England and Scotland.</p>
        </div>

        <h2 id="check">How to check if your car is ULEZ compliant</h2>
        <ol>
          <li><strong>Use the official checkers.</strong> For London, enter your registration on <a href="https://tfl.gov.uk/modes/driving/check-your-vehicle/" rel="noopener">TfL's vehicle checker</a>. For England's clean air zones, use <a href="https://www.gov.uk/clean-air-zones" rel="noopener">GOV.UK's checker</a>, and for Scotland, the <a href="https://www.lowemissionzones.scot/vehicle-checker" rel="noopener">Low Emission Zones Scotland checker</a>.</li>
          <li><strong>Look at your V5C.</strong> Some logbooks show the car's Euro status. If yours doesn't, the date of first registration in section B is a good guide.</li>
          <li><strong>Don't go by age alone.</strong> The rules are based on the emissions standard the car was built to, not when it was registered. Some petrol cars from 2001 to 2005 meet Euro 4, and some diesels from before September 2015 meet Euro 6. If you're close to the line, ask the manufacturer for a certificate of conformity.</li>
        </ol>
{BOX}

        <h2 id="standards">The emissions standards</h2>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Fuel</th><th>Standard needed</th><th>Usually means</th></tr></thead>
            <tbody>
              <tr><td>Petrol (including petrol hybrids)</td><td>Euro 4 or newer</td><td>Registered from January 2006, and many from 2001</td></tr>
              <tr><td>Diesel (including diesel hybrids)</td><td>Euro 6 or newer</td><td>Registered from September 2015</td></tr>
              <tr><td>Fully electric</td><td>Always meets the standard</td><td>Any age</td></tr>
            </tbody>
          </table>
        </div>
        <p>The diesel standard is much tougher because older diesels produce far more nitrogen dioxide and particulates, which is what these zones are designed to cut.</p>

        <h2 id="london">London's ULEZ</h2>
        <ul>
          <li><strong>Where:</strong> all London boroughs and the City of London. The M25 itself isn't in the zone.</li>
          <li><strong>When:</strong> 24 hours a day, every day except Christmas Day. A charging day runs midnight to midnight, so a late-night trip that crosses midnight is two days.</li>
          <li><strong>Cost:</strong> £12.50 for each day you drive in the zone in a car that doesn't meet the standard.</li>
          <li><strong>If you don't pay:</strong> a £180 penalty charge, reduced to £90 if paid within 14 days, for each day.</li>
          <li><strong>Paying:</strong> through TfL's Pay to drive in London service, or set up Auto Pay so you're charged automatically. Check TfL for the latest deadlines.</li>
        </ul>
        <p>The ULEZ is separate from the Congestion Charge, which covers a smaller central London zone and applies to most cars regardless of emissions.</p>

        <h2 id="england">Clean air zones in England</h2>
        <p>Several English cities run clean air zones, but only two charge private cars. The others only charge buses, coaches, taxis, lorries and, in some cases, vans.</p>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Zone</th><th>Charges cars?</th><th>Daily charge for a car that doesn't meet the standard</th></tr></thead>
            <tbody>
              <tr><td>Birmingham</td><td>Yes</td><td>£8. Penalty £120, or £60 if paid within 14 days</td></tr>
              <tr><td>Bristol</td><td>Yes</td><td>£9</td></tr>
              <tr><td>Bath</td><td>No</td><td>Cars aren't charged</td></tr>
              <tr><td>Bradford</td><td>No</td><td>Cars aren't charged</td></tr>
              <tr><td>Portsmouth</td><td>No</td><td>Cars aren't charged</td></tr>
              <tr><td>Sheffield</td><td>No</td><td>Cars aren't charged</td></tr>
              <tr><td>Tyneside (Newcastle and Gateshead)</td><td>No</td><td>Cars aren't charged</td></tr>
            </tbody>
          </table>
        </div>
        <p>Oxford is different: its small city-centre Zero Emission Zone charges petrol and diesel cars, whatever their Euro standard. Check Oxfordshire County Council's website before driving in.</p>

        <h2 id="scotland">Low emission zones in Scotland</h2>
        <p>Scotland's zones work differently. You can't pay to drive in: a car that doesn't meet the standard simply isn't allowed, and driving in brings a penalty.</p>
        <ul>
          <li><strong>Where:</strong> the city centres of Glasgow (enforced since June 2023), Dundee (since 30 May 2024), Aberdeen and Edinburgh (both since 1 June 2024).</li>
          <li><strong>Penalty:</strong> £60, halved if paid within 14 days. Each further offence within 90 days doubles it, up to £480 for a car. It resets to £60 if you don't drive in again for 90 days.</li>
          <li><strong>Hours:</strong> 24 hours a day, every day.</li>
        </ul>

        <h2 id="exempt">Exemptions and discounts</h2>
        <ul>
          <li><strong>Historic vehicles:</strong> cars over 40 years old in the historic tax class are exempt from the London ULEZ, and from most other zones.</li>
          <li><strong>Disabled drivers:</strong> vehicles in the disabled tax class, and Blue Badge holders in some zones, can get exemptions or longer grace periods. Each zone sets its own rules.</li>
          <li><strong>Residents and workers:</strong> some English zones have offered temporary exemptions or support for local people. Check the council's own website.</li>
        </ul>

        <h2 id="buying">Thinking of buying a car?</h2>
        <p>If you live in or regularly drive into a zone, a car that doesn't meet the standard can cost thousands a year in daily charges, and it'll be harder to sell. Check the Euro status before you buy, not after. It's on the V5C, in a full history check, or in the official checkers above, and our <a href="/guides/used-car-checks-before-buying/">used car checklist</a> covers everything else to look at.</p>
'''

FAQ = [
    ("How do I know if my car is ULEZ compliant?",
     "Enter your registration on TfL's vehicle checker. As a rule, petrol cars need to meet Euro 4 (most registered from 2006) and diesel cars Euro 6 (most registered from September 2015). Fully electric cars always comply."),
    ("How much is the ULEZ charge?",
     "£12.50 a day for a car that doesn't meet the standard. If you don't pay, the penalty is £180, reduced to £90 if paid within 14 days."),
    ("Which clean air zones charge private cars?",
     "In England, Birmingham (£8 a day) and Bristol (£9 a day). Bath, Bradford, Portsmouth, Sheffield and Tyneside don't charge cars. Scotland's low emission zones in Glasgow, Edinburgh, Aberdeen and Dundee don't let non-compliant cars in at all, with penalties instead of a charge."),
    ("Is a 2005 petrol car ULEZ compliant?",
     "Possibly. Euro 4 became mandatory for new petrol cars from January 2006, but many cars from 2001 to 2005 already met it. Check the registration on TfL's checker, or ask the manufacturer for a certificate of conformity."),
    ("Do hybrid cars pay ULEZ?",
     "Hybrids are judged on their engine. A petrol hybrid needs to meet Euro 4 and a diesel hybrid Euro 6, which almost all hybrids do."),
]

GUIDE = {
    "slug": "ulez-clean-air-zone-check",
    "crumb": "ULEZ and clean air zones",
    "topic": "Running a car",
    "title": "Is my car ULEZ compliant? UK clean air zones explained | Livery",
    "h1": "Is my car ULEZ compliant? London's ULEZ and UK clean air zones explained",
    "desc": "How to check if your car is ULEZ compliant, the Euro 4 and Euro 6 standards, London ULEZ charges, which clean air zones charge cars, and Scotland's LEZs.",
    "card": "How to check your car, the Euro 4 and Euro 6 standards, London's ULEZ, which English zones charge cars, and how Scotland's zones differ.",
    "lede": "Whether your car is ULEZ compliant comes down to one question: which emissions standard it was built to. Here's how to check, which zones charge private cars, and what they cost.",
    "published": "2026-11-09",
    "updated": "2026-11-09",
    "body": BODY,
    "faq": FAQ,
    "related": ["used-car-checks-before-buying", "car-tax-and-mot-due-dates", "car-service-history"],
    "cta": {
        "title": "Know where your car can go.",
        "text": "Livery Plus checks every car in your garage against London's ULEZ and the UK zones that charge cars, and tells you what you'd pay. Livery is free for up to two cars.",
        "button": "Create my free garage",
        "href": "https://app.liveryclub.com/auth?mode=signup",
    },
    "sources": [
        ("TfL, ULEZ: where and when", "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone/ulez-where-and-when"),
        ("TfL, ULEZ standards for cars", "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone/cars"),
        ("TfL, Penalty charges for ULEZ", "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone/penalty-charges-for-ulez"),
        ("GOV.UK, Clean Air Zones", "https://www.gov.uk/guidance/driving-in-a-clean-air-zone"),
        ("Brum Breathes, Birmingham Clean Air Zone charges", "https://www.brumbreathes.co.uk/info/32/charges-operation/34/paying-drive-clean-air-zone"),
        ("Bristol City Council, Clean Air Zone charges", "https://www.bristol.gov.uk/residents/streets-travel/bristols-caz/charges-and-vehicle-checker"),
        ("Transport Scotland, Low Emission Zones introduced across Scotland", "https://www.transport.gov.scot/news/low-emission-zones-introduced-across-scotland/"),
    ],
}
