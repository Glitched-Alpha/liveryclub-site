from .common import livery

BODY = f'''
        <h2 id="what">What a service history is</h2>
        <p>A service history is the record of every service a car has had: when, at what mileage, who did it and what they did. Traditionally that was a stamped service book in the glovebox. Many manufacturers now keep it digitally instead, and a dealer can print it out for you.</p>
        <p>Around it sits everything else that shows how a car's been looked after: repair invoices, receipts for tyres and brakes, old MOT certificates, recall and warranty work, and records of any big jobs such as a cambelt change.</p>

        <h2 id="types">What "full", "partial" and "main dealer" mean</h2>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Term in the advert</th><th>What it should mean</th></tr></thead>
            <tbody>
              <tr><td>Full main dealer service history (FMDSH)</td><td>Every scheduled service done by a franchised dealer for that make, on time.</td></tr>
              <tr><td>Full service history (FSH)</td><td>Every scheduled service done on time, by a dealer or an independent garage.</td></tr>
              <tr><td>Partial service history</td><td>Some services are missing, or were done late.</td></tr>
              <tr><td>No service history</td><td>No records at all. Price the car accordingly and budget for a full service straight away.</td></tr>
            </tbody>
          </table>
        </div>
        <p>"Full" only means something if you check it. Count the services against the car's age and mileage: a five-year-old car serviced every year should have five. Make sure the mileages on each service go up and line up with the <a href="/guides/check-mot-history/">MOT history</a>, and that the garages named are real.</p>

        <h2 id="why">Why it matters</h2>
        <ul>
          <li><strong>It keeps the car healthy.</strong> Fresh oil, filters and fluids are cheap. Engines, turbos and gearboxes that have gone without them aren't.</li>
          <li><strong>It protects your warranty.</strong> A manufacturer can refuse a warranty claim if the car hasn't been serviced to schedule with the right parts and fluids.</li>
          <li><strong>It's worth money when you sell.</strong> Buyers pay more for a car with a complete, believable history, and it sells faster. A car with gaps often has to be priced lower.</li>
          <li><strong>It proves the mileage.</strong> A trail of dated readings is one of the best defences against <a href="/guides/spot-clocked-car-mileage/">clocking</a>, for you as a buyer and as a seller.</li>
          <li><strong>It shows when big jobs are due.</strong> Things like cambelts, brake fluid and coolant are replaced every few years, not every service. The history tells you whether they've been done.</li>
        </ul>

        <h2 id="independent">Main dealer or independent garage?</h2>
        <p>You don't have to use a main dealer to keep your manufacturer warranty. Under competition rules the UK kept after Brexit (often called "block exemption"), a carmaker can't void your warranty just because an independent garage did the service. What matters is that:</p>
        <ul class="checklist">
          <li>the car is serviced on time, at or before the intervals in the handbook;</li>
          <li>the garage uses parts of matching quality and the right specification of oil and fluids;</li>
          <li>you keep proof: a stamp or digital record, plus an itemised invoice showing what was done, down to the oil grade.</li>
        </ul>
        <p>Extended warranties sold by dealers and warranty companies are different. They're contracts with their own terms, and some do require servicing at particular garages, so read yours. Recall and warranty repairs still need to be done by a franchised dealer.</p>

        <h2 id="how-often">How often should a car be serviced?</h2>
        <p>Your handbook or the manufacturer's website gives the exact schedule. Most cars fall into one of two patterns:</p>
        <ul>
          <li><strong>Fixed:</strong> every 12 months or a set mileage, often around 10,000 to 12,000 miles, whichever comes first.</li>
          <li><strong>Variable or "long-life":</strong> the car works out when it needs a service from how it's driven, sometimes up to two years or around 20,000 miles. Short trips and town driving bring it forward.</li>
        </ul>
        <p>Garages usually offer an <strong>interim</strong> service (oil and filter plus checks, often every 6 months or 6,000 miles for high-mileage drivers) and a <strong>full</strong> service (more filters and a longer list of checks, usually yearly). Following the manufacturer's own schedule is what counts for the warranty.</p>
        <div class="callout">
          <p><strong>An MOT is not a service.</strong> The MOT checks the car meets minimum safety and emissions standards on the day. It doesn't change the oil or replace anything. Plenty of people combine the two for convenience, which is fine, but one doesn't replace the other.</p>
        </div>

        <h2 id="keep">What to keep</h2>
        <ul class="checklist">
          <li>Every service record, with the date, mileage and garage</li>
          <li>Itemised invoices for services and repairs</li>
          <li>Receipts for tyres, brakes, batteries and parts you've fitted yourself</li>
          <li>Proof of cambelt, clutch and gearbox work and any other major job</li>
          <li>Recall and warranty work from the dealer</li>
          <li>MOT certificates and advisory notes</li>
          <li>Records of modifications, and who fitted them</li>
          <li>The V5C, the handbook, and all the keys</li>
        </ul>
        <p>Paper fades, gets lost and is easy to leave in the car you've just sold. A photo of each receipt, kept with the date and mileage, is far easier to hold on to.</p>
{livery("Your car's history, kept for you", [
    "Livery gives every car a history file: log each service, repair, MOT and mod with the date, mileage, cost and garage, and attach the invoice or receipt. Livery Plus can read a receipt photo and fill the details in for you.",
    "Tell Livery how often the car should be serviced, by months and miles, and it works out when the next one is due and reminds you. Your MOT history and mileage sit alongside, so the whole story of the car is in one place when you come to sell.",
])}

        <h2 id="buying">Checking a service history when you're buying</h2>
        <ul>
          <li><strong>Ask to see it before you travel</strong>, or at least ask what it includes.</li>
          <li><strong>Call the garages</strong> named in the book. Most will confirm whether they did the work.</li>
          <li><strong>Ask a dealer for the digital record</strong> if the car's manufacturer keeps one.</li>
          <li><strong>Match the mileages</strong> against the MOT history. Services should fall between MOTs at mileages that make sense.</li>
          <li><strong>Look for the big jobs.</strong> If the cambelt is due or overdue and there's no proof it's been done, budget for it or negotiate.</li>
        </ul>
        <p>Our <a href="/guides/used-car-checks-before-buying/">used car checklist</a> covers the rest of what to check.</p>

        <h2 id="missing">If your car's history has gaps</h2>
        <p>Start from now. Book a full service, ask the garage to note it's the first under your ownership, and keep everything from then on. If you know who serviced the car before, ask them for copies of their records. A clear history from today is still worth a lot more than none.</p>
'''

FAQ = [
    ("Does servicing at an independent garage void my warranty?",
     "No, not for a manufacturer's warranty, as long as the car is serviced on time with parts and fluids of the right specification, and you keep the records and itemised invoices. Extended warranties can have their own terms, so check yours."),
    ("What is a full service history?",
     "Every service the manufacturer recommends, done on time, with a record of each one. A full main dealer service history means they were all done by a franchised dealer for that make."),
    ("Does service history affect a car's value?",
     "Yes. A complete, believable history usually helps a car sell faster and for more, while gaps or no history at all usually mean a lower price."),
    ("Is an MOT the same as a service?",
     "No. An MOT checks the car meets minimum safety and emissions standards on the day. A service replaces oil, filters and fluids and checks the car over to keep it running well."),
    ("How do I find my car's service history?",
     "Check the service book and paperwork that came with the car. If the manufacturer keeps a digital record, a franchised dealer can print it. Garages that serviced the car can also give you copies of their records."),
]

GUIDE = {
    "slug": "car-service-history",
    "crumb": "Service history",
    "topic": "Looking after your car",
    "title": "Car service history: why it matters and how to keep one | Livery",
    "h1": "Car service history: what it is, why it matters and how to keep one",
    "desc": "What full and partial service history mean, whether an independent garage affects your warranty, how often to service, and what records to keep.",
    "card": "Full vs partial history, dealer vs independent garage and your warranty, how often to service, and what records to keep.",
    "lede": "A complete service history keeps a car healthy, protects its warranty and adds to its value when you sell. Here's what counts, what doesn't, and how to keep one without a glovebox full of paper.",
    "published": "2026-11-09",
    "updated": "2026-11-09",
    "body": BODY,
    "faq": FAQ,
    "related": ["car-tax-and-mot-due-dates", "check-mot-history", "spot-clocked-car-mileage"],
    "cta": {
        "title": "Start your car's history file today.",
        "text": "Add your car to Livery and log every service, repair and receipt in one place, with a reminder when the next service is due. Free for up to two cars.",
        "button": "Create my free garage",
        "href": "https://app.liveryclub.com/auth?mode=signup",
    },
    "sources": [
        ("RAC, New car warranty: do I have to get my car serviced at the dealership?", "https://www.rac.co.uk/drive/advice/buying-and-selling-guides/new-car-warranty-do-i-have-to-get-my-car-serviced-at-the-dealership/"),
        ("GOV.UK, Getting an MOT", "https://www.gov.uk/getting-an-mot/mot-test-rules"),
    ],
}
