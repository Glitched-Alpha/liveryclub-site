from .common import livery, SIGNUP_CHECK

BODY = f'''
        <h2 id="categories">The four categories at a glance</h2>
        <p>When an insurer decides a damaged car isn't worth repairing, it's "written off" and given a category under the motor insurance industry's salvage code of practice. The category tells everyone who buys it afterwards how bad the damage was.</p>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Category</th><th>What it means</th><th>Back on the road?</th></tr></thead>
            <tbody>
              <tr><td>Category A – Scrap only</td><td>So badly damaged it must be crushed, whole. No parts can be reused.</td><td>Never</td></tr>
              <tr><td>Category B – Break for parts</td><td>The body shell must be crushed, but some parts can be taken off and sold.</td><td>Never</td></tr>
              <tr><td>Category S – Structural damage</td><td>The structural frame or chassis was damaged, for example a bent chassis leg or crumpled crash structure. It can be professionally repaired.</td><td>Yes, once repaired</td></tr>
              <tr><td>Category N – Non-structural damage</td><td>No structural damage, but the insurer chose not to repair it. That can be cosmetic, electrical or safety-related, such as airbags or brakes.</td><td>Yes, once repaired</td></tr>
            </tbody>
          </table>
        </div>
        <div class="callout callout-warn">
          <p><strong>If a Cat A or Cat B car is for sale as a road car, walk away.</strong> These cars should never be driven again, and DVLA won't re-register them. A car being sold whole with one of these markers may have a cloned identity.</p>
        </div>

        <h2 id="why">Why cars get written off, and why it isn't always serious</h2>
        <p>Insurers write off a car when repairing it doesn't make financial sense. That's partly about how bad the damage is and partly about money: the cost of repair compared with the car's value, plus the cost of a hire car while it's in the bodyshop and what the insurer gets back for selling the salvage.</p>
        <p>So an older car with modest damage can be written off simply because it isn't worth much, while a newer car with worse damage might be repaired. A Cat N car with a scuffed bumper and a dented door is a very different thing from a Cat S car that's been in a heavy front-end crash. The category is where your questions start, not where they end.</p>

        <h2 id="old">Cat C and Cat D: the old categories</h2>
        <p>Before October 2017, repairable write-offs were Category C and Category D. They were based on cost, not on what was damaged:</p>
        <ul>
          <li><strong>Cat C:</strong> repairable, but repairs would have cost more than the car was worth.</li>
          <li><strong>Cat D:</strong> repairable, and repairs would have cost less than the car was worth, but the insurer decided a payout made more sense.</li>
        </ul>
        <p>S and N replaced C and D for cars written off from 1 October 2017. They aren't a straight swap: an old Cat D car could have had structural damage, and an old Cat C car might not have. Cars written off before then keep their old category, so you'll still see C and D on older cars.</p>

        <h2 id="find-out">How to find out if a car has been written off</h2>
        <p>Write-offs are recorded on a national register that insurers share, and a full history check reads it. The V5C logbook may not tell you, and a free MOT or tax check won't.</p>
        <p>A dealer selling a written-off car must tell you, and can't hide known accident damage. A private seller doesn't have to volunteer it, but mustn't lie about it if you ask. So ask directly, in writing if you can, and check for yourself either way.</p>
{livery("See it in plain English", [
    "Livery's full history check names the category in full, shows the date of loss, where the car was damaged and which insurer recorded it, and explains what that category means for you. It also checks for theft, outstanding finance, scrapped and exported markers and plate changes in the same report.",
    "It's £5.99, £3.99 with Livery Plus, and yearly Plus includes 3 checks a year. The report stays saved in your account until you delete it.",
], "Check a car", SIGNUP_CHECK)}

        <h2 id="buy">Should you buy a Cat S or Cat N car?</h2>
        <p>GOV.UK's own advice is that there's nothing wrong with buying a written-off car that has been properly returned to good condition. Plenty of people do, and the lower price can be good value. The risk is in how well it was repaired, and that's what to check.</p>
        <h3>Questions to ask the seller</h3>
        <ul class="checklist">
          <li>What exactly was damaged, and how did it happen?</li>
          <li>Who repaired it? A specialist bodyshop working to the manufacturer's repair methods, or a home job?</li>
          <li>Can I see the invoices, the parts list and any photos of the damage and the repair?</li>
          <li>For Cat S: was the structural repair checked afterwards, for example with a wheel alignment and a jig or measurement report?</li>
          <li>For Cat N: if airbags went off, were they replaced with new ones, and have the airbag and seatbelt systems been checked?</li>
        </ul>
        <h3>Get it inspected</h3>
        <p>For a Cat S car especially, pay for an independent inspection from an engineer before you buy. They'll check the structure, the alignment, the welding and the panel fit, and often find faults the seller didn't know about. It costs far less than buying a badly repaired car.</p>
        <h3>Get an insurance quote first</h3>
        <p>Some insurers won't cover a previously written-off car, and others charge more or ask for an engineer's report. Get a real quote, telling the insurer the category, before you agree a price. You must disclose it: not mentioning a write-off can invalidate your cover.</p>

        <h2 id="value">What a write-off does to value</h2>
        <p>A Cat S or Cat N car is worth noticeably less than the same car with a clean history, and that gap doesn't go away. It's a good deal when you buy, but you'll get less when you sell, and you'll have to tell the next buyer too. Structural (Cat S) damage generally knocks more off than non-structural (Cat N). Price it against other write-offs, not against clean cars.</p>
{livery("Is the price right?", [
    "Livery Plus includes a valuation every month. On a history check it shows what the car is worth as a private sale and from a dealer, and how the seller's asking price compares, so you can tell whether the discount for a write-off is a real one.",
])}

        <h2 id="own">If you already own one</h2>
        <p>Keep the repair invoices and inspection report with the car's history, because the next buyer will ask for them. Tell your insurer about the category at every renewal. If your own car is written off, your insurer handles the paperwork with DVLA when it takes the car, and you can sometimes buy a repairable (S or N) car back from the insurer and repair it yourself.</p>
'''

FAQ = [
    ("What does Cat N mean on a car?",
     "Category N means an insurer wrote the car off but it had no structural damage. The damage was to things like panels, lights, trim, electrics or airbags. It can be repaired and driven again, but it's usually worth less and some insurers charge more to cover it."),
    ("What does Cat S mean on a car?",
     "Category S means the car's structural frame or chassis was damaged and an insurer wrote it off, but it can be professionally repaired and driven again. It's worth getting an independent inspection before buying one."),
    ("Is it safe to buy a Cat S or Cat N car?",
     "It can be, if it was repaired properly. Ask for repair invoices and photos, get an independent inspection, especially for Cat S, and get an insurance quote before you buy."),
    ("Do I have to tell my insurer my car is Cat S or Cat N?",
     "Yes. You need to declare it when you take out or renew a policy. Not mentioning it can invalidate your insurance."),
    ("What replaced Cat C and Cat D?",
     "Categories S and N replaced C and D for cars written off from 1 October 2017. C and D were based on repair cost; S and N are based on whether the structure was damaged. Cars written off before then keep their old category."),
]

GUIDE = {
    "slug": "cat-s-cat-n-write-off-categories",
    "crumb": "Write-off categories",
    "topic": "Buying a car",
    "title": "Cat S and Cat N explained: car write-off categories | Livery",
    "h1": "Cat S and Cat N explained: what write-off categories mean when you're buying a car",
    "desc": "What Category A, B, S and N mean, how they replaced Cat C and D, how to find out if a car is a write-off, and how to buy a Cat S or Cat N car safely.",
    "card": "What Cat A, B, S and N mean, what happened to Cat C and D, how to find out if a car was written off, and how to buy one safely.",
    "lede": "A Cat S or Cat N car can be a bargain or a money pit. The category tells you what kind of damage the car had, but not how well it was put right. Here's what each category means and how to check the rest.",
    "published": "2026-11-09",
    "updated": "2026-11-09",
    "body": BODY,
    "faq": FAQ,
    "related": ["used-car-checks-before-buying", "spot-clocked-car-mileage", "car-service-history"],
    "cta": {
        "title": "Know before you buy.",
        "text": "Enter the plate in Livery for free MOT history and mileage, then run a full history check for write-offs, theft and outstanding finance, all explained in plain English.",
        "button": "Check a car",
        "href": SIGNUP_CHECK,
    },
    "sources": [
        ("ABI, Code of Practice for the categorisation of motor vehicle salvage (May 2025)", "https://www.abi.org.uk/globalassets/files/publications/public/motor/2019/codepracticecategorisationmotorisedvehiclesalvagemay2025.pdf"),
        ("GOV.UK, Buying repaired 'written off' vehicles", "https://www.gov.uk/government/publications/buying-repaired-written-off-vehicles-a-consumer-guide/buying-repaired-written-off-vehicles-a-consumer-guide"),
        ("The AA, Insurance write-off categories", "https://www.theaa.com/car-insurance/advice/damage-categories"),
    ],
}
