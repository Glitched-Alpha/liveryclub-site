from .common import livery, SIGNUP_CHECK, SIGNUP

BODY = f'''
        <h2 id="what">What clocking is, and why it still happens</h2>
        <p>Clocking means winding back a car's odometer so it shows fewer miles than it has really done. A car that looks like it's done 40,000 miles instead of 90,000 sells for more, and the buyer pays for wear they can't see: an engine, gearbox, clutch and suspension that are much older than they seem.</p>
        <p>It's easy to assume digital dashboards put an end to it. They didn't. The equipment to change a digital reading is cheap and widely sold, often advertised as "mileage correction" or "dash repair", and it can take minutes.</p>

        <h2 id="law">Is it illegal?</h2>
        <p>Changing a car's odometer so it shows a false mileage, or selling a car you know has been clocked, can be a criminal offence under the Fraud Act 2006 and the Consumer Protection from Unfair Trading Regulations 2008. People have gone to prison for it.</p>
        <p>There are legitimate reasons to change a reading. If an instrument cluster fails and is replaced, the new one should be set to the car's real mileage, and the garage should give you paperwork saying what was done and what the reading was. That paperwork should stay with the car.</p>

        <h2 id="records">Check the records first</h2>
        <p>The most reliable evidence is mileage written down by someone else, on a date, over the years. Put every reading you can find in date order. The numbers should only ever go up, and by a believable amount each year.</p>
        <ol>
          <li><strong>The MOT history.</strong> Every MOT since 2005 records the mileage, and it's free to view on <a href="https://www.gov.uk/check-mot-history" rel="noopener">GOV.UK</a>. A drop between two tests is the single biggest warning sign. See our <a href="/guides/check-mot-history/">MOT history guide</a>.</li>
          <li><strong>Service records.</strong> Stamps, digital service records and invoices usually note the mileage.</li>
          <li><strong>Other mileage records.</strong> Mileage is also recorded at other points in a car's life, such as some services, sales and inspections. A full history check can bring these together.</li>
          <li><strong>Old MOT certificates and receipts</strong> for tyres, batteries and repairs.</li>
        </ol>
        <div class="callout">
          <p><strong>Not every drop is clocking.</strong> MOT testers occasionally type a reading wrong, and a car with a replaced instrument cluster can show an odd jump. One strange reading followed by sensible ones is usually a typing mistake. A car whose mileage stays low after a drop, or whose readings don't match the service history, is a different story.</p>
        </div>
{livery("Livery does this for you", [
    "Enter the plate in <strong>Buying a car?</strong> and Livery lays out the mileage from every MOT and warns you if it has ever gone backwards, free.",
    "The full history check adds other recorded mileage readings and gives you the last recorded mileage with where it came from, such as an MOT test or a service record. Add the seller's mileage and Livery tells you straight away if it's lower than the last record.",
], "Check a car's mileage", SIGNUP_CHECK)}

        <h2 id="annual">Is the mileage believable?</h2>
        <p>Most cars in the UK cover well under 10,000 miles a year, but there's a wide range: a retired driver might do 3,000, a sales rep 25,000. What matters is whether the story fits. A five-year-old car with 15,000 miles from a one-owner retired seller is plausible. The same mileage on an ex-fleet car with three keepers and heavy wear isn't.</p>
        <p>Watch for a car that did 15,000 miles a year for its first three years and then, according to the odometer, barely moved. Clockers often wind a car back to a low but plausible figure, which shows up as a sudden flattening in the readings.</p>

        <h2 id="car">Check the car itself</h2>
        <p>Wear doesn't lie as easily as numbers. Compare these with the mileage shown:</p>
        <ul class="checklist">
          <li><strong>Steering wheel:</strong> a shiny, smooth or worn rim, especially at ten and two, suggests high mileage.</li>
          <li><strong>Gear knob and handbrake:</strong> worn lettering, a shiny or cracked surface.</li>
          <li><strong>Pedals:</strong> worn-through rubbers, particularly the clutch and brake. Brand-new pedal rubbers on an older car can mean someone's hidden the wear.</li>
          <li><strong>Driver's seat:</strong> a flattened or torn side bolster from getting in and out.</li>
          <li><strong>Keys and buttons:</strong> worn key fob buttons, window switches and wiper stalks.</li>
          <li><strong>Stone chips:</strong> lots of chips on the bonnet and front bumper come from motorway miles.</li>
          <li><strong>Brake discs:</strong> a deep lip around the edge of the disc suggests a lot of use.</li>
        </ul>
        <h3>Ask a specialist</h3>
        <p>On many modern cars the mileage is stored in more than one control unit, not just the dashboard. A franchised dealer or a good independent garage with the right diagnostic equipment can often read those other readings, and a mismatch is strong evidence. It's worth paying for on an expensive car.</p>

        <h2 id="disclaimers">"Mileage not guaranteed"</h2>
        <p>Some adverts say "mileage not guaranteed" or "mileage unverified". A dealer can't use a disclaimer like that to sell a car they know or should know has been clocked, and should be able to tell you why the mileage can't be verified. Treat it as a reason to ask questions, not a reason to relax.</p>

        <h2 id="bought">If you think you've bought a clocked car</h2>
        <ul>
          <li><strong>Collect the evidence:</strong> the advert, your receipt, the MOT history and any service records showing the different readings.</li>
          <li><strong>From a dealer:</strong> a car that isn't as described gives you rights under the Consumer Rights Act 2015, including a full refund if you reject it within 30 days. Contact the dealer in writing.</li>
          <li><strong>From a private seller:</strong> they must describe the car accurately. If they told you a mileage they knew was false, you may be able to claim against them.</li>
          <li><strong>Get advice:</strong> <a href="https://www.citizensadvice.org.uk/consumer/" rel="noopener">Citizens Advice</a> can help and will pass reports to Trading Standards.</li>
        </ul>

        <h2 id="own">Protect your own car's mileage record</h2>
        <p>When you sell, a clear record of readings over the years makes your car easier to sell and harder to argue with. Note the mileage every time you service the car or have work done, and keep the receipts.</p>
{livery("Your mileage, recorded as you go", [
    "Livery records the mileage from every MOT and every service and repair you log, and draws it on a chart. When it's time to sell, the record is there to show a buyer, with the receipts to back it up.",
], "Create my free garage", SIGNUP)}
'''

FAQ = [
    ("How can I tell if a car has been clocked?",
     "Compare the mileage on the odometer with every recorded reading you can find: MOT history, service records and receipts. The numbers should only ever go up. Then check that wear on the steering wheel, pedals, gear knob and driver's seat matches the mileage shown."),
    ("Is clocking a car illegal in the UK?",
     "Altering an odometer to show a false mileage, or selling a car you know has been clocked, can be a criminal offence under the Fraud Act 2006 and the Consumer Protection from Unfair Trading Regulations 2008. Setting a replacement instrument cluster to the car's real mileage is legitimate and should come with paperwork."),
    ("Can you clock a car with a digital odometer?",
     "Yes. Digital readings can be changed with cheap equipment. On many modern cars the mileage is also stored in other control units, which a garage with diagnostic equipment can often read to spot a mismatch."),
    ("Where can I see a car's mileage history?",
     "The free GOV.UK MOT history shows the mileage at every MOT since 2005. A full history check can add other recorded readings. In Livery, the mileage from every MOT is shown free when you look up a plate."),
    ("Does a drop in MOT mileage always mean clocking?",
     "No. A tester may have typed the reading wrong, or the instrument cluster may have been replaced. A single odd reading followed by sensible ones is usually a mistake, but ask the seller to explain it and show paperwork."),
]

GUIDE = {
    "slug": "spot-clocked-car-mileage",
    "crumb": "Spot a clocked car",
    "topic": "Buying a car",
    "title": "How to spot a clocked car and check mileage history | Livery",
    "h1": "How to spot a clocked car: checking mileage before you buy",
    "desc": "How clocking works, whether it's illegal, how to check mileage history with MOT and service records, the signs of high mileage, and what to do next.",
    "card": "How clocking works on digital dashboards, how to check mileage history, the signs of wear that give it away, and what to do if you've bought one.",
    "lede": "Winding back the mileage still happens, digital dashboards included, and it can add thousands to a car's price. The good news is that a car's past leaves a trail. Here's how to follow it.",
    "published": "2026-11-09",
    "updated": "2026-11-09",
    "body": BODY,
    "faq": FAQ,
    "related": ["used-car-checks-before-buying", "check-mot-history", "car-service-history"],
    "cta": {
        "title": "Check the mileage before you pay.",
        "text": "Enter the plate in Livery for free MOT history and mileage readings, with a warning if they've ever gone backwards. The full history check adds the last recorded mileage and its source.",
        "button": "Check a car",
        "href": SIGNUP_CHECK,
    },
    "sources": [
        ("GOV.UK, Check the MOT history of a vehicle", "https://www.gov.uk/check-mot-history"),
        ("GOV.UK, Mileage correction businesses: compliance review", "https://www.gov.uk/cma-cases/mileage-correction-businesses-compliance-review"),
        ("Pembrokeshire County Council Trading Standards, Used motor vehicles: your rights", "https://www.pembrokeshire.gov.uk/consumer-advice-information/used-motor-vehicles-your-rights"),
    ],
}
