from .common import livery, SIGNUP_CHECK

BODY = f'''
        <div class="callout">
          <p><strong>The short version.</strong> Before you hand over any money: check the MOT history and tax for free, run a full history check for theft, outstanding finance and write-offs, make sure the V5C logbook and the VIN on the car match each other and the seller, see the car where the seller lives, and pay by bank transfer once you're sure.</p>
        </div>

        <h2 id="before">Before you go and see it</h2>
        <p>Most problems can be spotted from your sofa. Ask the seller for the registration number before you travel. An honest seller will give it to you without fuss; one who won't is a reason to walk away.</p>
        <ol>
          <li><strong>Check the basics match.</strong> Use DVLA's free <a href="https://vehicleenquiry.service.gov.uk/" rel="noopener">vehicle enquiry service</a> to confirm the make, colour, engine size, year and tax status match the advert. A different colour or engine size can mean the plates belong to another car.</li>
          <li><strong>Read the MOT history.</strong> It's free on <a href="https://www.gov.uk/check-mot-history" rel="noopener">GOV.UK</a> and shows every test result, every advisory and the mileage at each test. Look for mileage that goes down, the same advisory year after year, and gaps. Our <a href="/guides/check-mot-history/">MOT history guide</a> explains how to read it.</li>
          <li><strong>Check for recalls.</strong> Enter the make, model and VIN on GOV.UK's <a href="https://www.gov.uk/check-vehicle-recall" rel="noopener">vehicle recall checker</a> to see if there's an outstanding safety recall. Recall work is free at a franchised dealer, but you want to know before you buy.</li>
          <li><strong>Run a full history check.</strong> The free checks can't tell you if the car is stolen, has finance owing or was written off by an insurer. Only a paid history check covers those, and they're the three things that cost buyers the most.</li>
          <li><strong>Work out what it's worth.</strong> Compare the asking price with similar cars of the same age and mileage, or a valuation. A price far below the rest is usually below for a reason.</li>
        </ol>
{livery("Check it in Livery before you travel", [
    "Open <strong>Buying a car?</strong> in Livery and enter the plate. The car's details, tax, MOT status, full MOT history and mileage readings come up free, with a warning if the mileage has ever gone backwards.",
    "The full history check then looks for police stolen records, outstanding finance, insurance write-offs, scrapped or exported markers, plate and keeper changes and V5C dates, and explains each result in plain English. It's £5.99, £3.99 with Livery Plus, and yearly Plus includes 3 checks a year. Your report stays saved in your account.",
], "Check a car", SIGNUP_CHECK)}

        <h2 id="history-check">What a full history check covers, and why it matters</h2>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Check</th><th>Why it matters</th></tr></thead>
            <tbody>
              <tr><td>Stolen</td><td>If the car is recorded as stolen, the police can take it back and you lose what you paid. Never buy it.</td></tr>
              <tr><td>Outstanding finance</td><td>On hire purchase or PCP, the finance company owns the car until it's paid off. The law gives some protection to private buyers who didn't know, but proving that is stressful and dealers don't get it. Ask the seller to settle the finance first and get written confirmation from the lender.</td></tr>
              <tr><td>Insurance write-off</td><td>A Cat S or Cat N car can be fine to buy if it was repaired properly, but it's worth less and some insurers won't cover it. Cat A and B cars should never be back on the road. See our <a href="/guides/cat-s-cat-n-write-off-categories/">write-off categories guide</a>.</td></tr>
              <tr><td>Scrapped or exported</td><td>A car recorded as scrapped or exported shouldn't be for sale here under that plate. It can be a sign the car's identity has been copied.</td></tr>
              <tr><td>Plate and keeper changes</td><td>Private plates are common, but several recent changes, or a car that's changed hands many times, are worth asking about.</td></tr>
              <tr><td>V5C issue dates</td><td>The seller's logbook should match the latest one issued. An older logbook may have been replaced, lost or stolen.</td></tr>
            </tbody>
          </table>
        </div>

        <h2 id="viewing">At the viewing</h2>
        <p>See the car in daylight, when it's dry, at the address on the V5C. A seller who wants to meet in a car park or service station, or brings the car to you, makes it hard to check who they are.</p>
        <h3>The paperwork</h3>
        <ul class="checklist">
          <li><strong>The V5C (logbook) is genuine.</strong> Hold it up to the light and look for the "DVL" watermark. GOV.UK warns that logbooks with serial numbers from <strong>BG8229501 to BG9999030</strong> or <strong>BI2305501 to BI2800000</strong> may be stolen. If it's one of those, leave, and call the police when it's safe.</li>
          <li><strong>The name and address match the seller.</strong> You should be at that address. If the seller isn't the registered keeper, ask why.</li>
          <li><strong>The VIN matches.</strong> Find the 17-character vehicle identification number on the car, usually at the bottom of the windscreen and on a door pillar, and check it against the V5C and your history report. Check the engine number too if you can.</li>
          <li><strong>The service history adds up.</strong> Stamps or digital records, invoices and MOT certificates should tell the same story as the MOT mileage. Our <a href="/guides/car-service-history/">service history guide</a> explains what a good one looks like.</li>
          <li><strong>All the keys are there.</strong> Replacement keys can cost hundreds of pounds, and a missing key is worth asking about.</li>
        </ul>
        <h3>The car itself</h3>
        <ul class="checklist">
          <li><strong>Bodywork:</strong> uneven panel gaps, paint that doesn't quite match, overspray on rubber seals or bolts that have been turned can all point to accident repairs.</li>
          <li><strong>Tyres:</strong> legal tread is at least 1.6mm across the central three-quarters. Uneven wear on the inside or outside edge can mean alignment or suspension problems.</li>
          <li><strong>Under the bonnet:</strong> look at the oil level and colour, coolant level and any leaks. Ask for the engine to be cold when you arrive, as some problems only show on a cold start.</li>
          <li><strong>Inside:</strong> check every warning light comes on with the ignition and then goes out. Try the air conditioning, windows, central locking and infotainment.</li>
          <li><strong>Wear that matches the mileage:</strong> a shiny steering wheel, worn pedal rubbers or a sagging driver's seat on a "low mileage" car don't add up. Our <a href="/guides/spot-clocked-car-mileage/">clocking guide</a> covers this in detail.</li>
        </ul>
        <h3>The test drive</h3>
        <p>Make sure you're insured to drive it first. Drive for at least 20 minutes on different roads, including a faster road if you can. Listen for knocks over bumps, check the car pulls up straight under braking, the clutch bites at a sensible height, gear changes are smooth and the steering doesn't pull to one side.</p>

        <h2 id="paying">Paying, and what to get</h2>
        <ul>
          <li><strong>Pay by bank transfer</strong>, once you're happy, and never before you've seen the car and the logbook. Paying a deposit for a car you haven't seen is how most online car scams work.</li>
          <li><strong>Get a written receipt</strong> with both names and addresses, the date, the price, the registration, the VIN and the mileage.</li>
          <li><strong>Take the green "new keeper" slip</strong> (section 6 of the V5C). The seller tells DVLA about the sale, and you'll get a new logbook in your name.</li>
          <li><strong>Tax it before you drive it.</strong> Vehicle tax doesn't transfer to a new owner, so you need to tax the car yourself, using the reference number on the new keeper slip. Our <a href="/guides/car-tax-and-mot-due-dates/">tax and MOT guide</a> explains how.</li>
          <li><strong>Insure it before you drive it</strong>, even just to get it home.</li>
        </ul>

        <h2 id="rights">Your rights: dealer or private seller</h2>
        <div class="table-wrap">
          <table>
            <thead><tr><th></th><th>From a dealer</th><th>From a private seller</th></tr></thead>
            <tbody>
              <tr><td>Must be as described</td><td>Yes</td><td>Yes</td></tr>
              <tr><td>Satisfactory quality and fit for purpose</td><td>Yes, under the Consumer Rights Act 2015</td><td>No, unless the seller said so</td></tr>
              <tr><td>Refund if faulty</td><td>Full refund if you reject it within 30 days</td><td>No automatic right</td></tr>
              <tr><td>Faults in the first 6 months</td><td>Assumed to have been there when you bought it, unless the dealer proves otherwise</td><td>Not applicable</td></tr>
              <tr><td>Must own the car</td><td>Yes</td><td>Yes</td></tr>
            </tbody>
          </table>
        </div>
        <p>A dealer can't avoid these rights by writing "sold as seen" or by hiding known accident damage. Buying privately is often cheaper, but you're relying almost entirely on your own checks, which is why the history check and inspection matter more.</p>

        <h2 id="after">Once it's yours</h2>
        <p>The first week is the time to set the car up properly: put the MOT, tax and insurance renewal dates somewhere you won't miss them, file the receipt, the service history and the history check report together, and book a service if the history has gaps or you're not sure when it was last done.</p>
{livery("Bought it? It moves straight into your garage", [
    "In Livery, tap <strong>Bought it? Add to my garage</strong> on your history check and the car joins your garage with the report attached. Its MOT, tax and insurance dates are set up with reminders, and its service history file starts from day one.",
    "If you're unsure about the price, Livery Plus includes a valuation every month, showing private sale, dealer, part exchange and trade prices, and how the asking price compares.",
])}
'''

FAQ = [
    ("What checks should I do before buying a used car?",
     "Check the MOT history, tax and recall status for free on GOV.UK, run a full history check for theft, outstanding finance and insurance write-offs, check the V5C logbook is genuine and matches the seller and the car's VIN, inspect and test drive the car, and only pay by bank transfer once you're satisfied."),
    ("Is a free car check enough?",
     "Free checks show the car's details, tax, MOT history and recalls. They can't tell you if the car is stolen, has outstanding finance or was written off by an insurer. Only a paid history check covers those."),
    ("What happens if I buy a car with outstanding finance?",
     "The finance company owns the car until the agreement is paid off. The law gives some protection to private buyers who bought in good faith without knowing, but it can be difficult and stressful to rely on. Check for finance before you buy, and if there is some, get the seller to settle it and get written confirmation from the lender."),
    ("Does car tax transfer when you buy a car?",
     "No. Since October 2014 vehicle tax doesn't pass to the new keeper. You need to tax the car before you drive it, using the reference number on the green new keeper slip from the V5C."),
    ("Can I return a used car bought from a private seller?",
     "Usually not. A private seller must describe the car accurately and must own it, but you don't get the Consumer Rights Act protections you'd have from a dealer, such as the 30-day right to reject a faulty car."),
]

GUIDE = {
    "slug": "used-car-checks-before-buying",
    "crumb": "Used car checks",
    "topic": "Buying a car",
    "title": "Used car checks before you buy: the complete UK checklist | Livery",
    "h1": "How to check a used car before you buy: the complete UK checklist",
    "desc": "Every check before buying a used car in the UK: free MOT and tax checks, stolen, finance and write-off checks, the V5C, VIN, test drive and your rights.",
    "card": "The free checks, the paid history check, the V5C and VIN, the test drive, paying safely, and your rights from a dealer or a private seller.",
    "lede": "Buying a used car is one of the biggest purchases most of us make, and almost every expensive mistake can be avoided with checks that take an evening. Here's every check worth doing, in the order to do them.",
    "published": "2026-11-09",
    "updated": "2026-11-09",
    "body": BODY,
    "faq": FAQ,
    "related": ["cat-s-cat-n-write-off-categories", "spot-clocked-car-mileage", "check-mot-history"],
    "cta": {
        "title": "Check it before you buy it.",
        "text": "Enter the plate in Livery for the car's details, MOT history and mileage free, then run a full history check for theft, finance and write-offs. Your report is saved to your account.",
        "button": "Check a car",
        "href": SIGNUP_CHECK,
    },
    "sources": [
        ("GOV.UK, Check a used vehicle you're buying", "https://www.gov.uk/checks-when-buying-a-used-car"),
        ("GOV.UK, Buying repaired 'written off' vehicles", "https://www.gov.uk/government/publications/buying-repaired-written-off-vehicles-a-consumer-guide/buying-repaired-written-off-vehicles-a-consumer-guide"),
        ("GOV.UK, Check if a vehicle has been recalled", "https://www.gov.uk/check-vehicle-recall"),
        ("Pembrokeshire County Council Trading Standards, Used motor vehicles: your rights", "https://www.pembrokeshire.gov.uk/consumer-advice-information/used-motor-vehicles-your-rights"),
    ],
}
