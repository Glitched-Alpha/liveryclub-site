from .common import livery

BODY = f'''
        <h2 id="check">How to check when your tax and MOT are due</h2>
        <p>Both dates are on DVLA's free <a href="https://vehicleenquiry.service.gov.uk/" rel="noopener">vehicle enquiry service</a>. Enter the registration and it shows whether the car is taxed, when the tax runs out, and the MOT expiry date. You don't need the V5C or to be the owner.</p>
        <p>You can also find the MOT expiry on your last MOT certificate or in the car's <a href="/guides/check-mot-history/">MOT history</a>, and the tax date on the V11 reminder DVLA sends before it's due.</p>
{livery("Never look them up again", [
    "Add your car to Livery by its number plate and your MOT and tax dates fill in automatically, with countdowns on your garage and a reminder 30 days, 7 days and 1 day before each one, by email and in the app.",
    "Add your insurance, breakdown cover, warranty and service dates too, and everything that's due sits in one place.",
])}

        <h2 id="mot">The MOT: when it's due and the rules</h2>
        <ul>
          <li><strong>First MOT:</strong> most cars need their first MOT by the third anniversary of first registration. Some vehicles, such as taxis and ambulances, need one from their first birthday. Cars in Northern Ireland follow different rules.</li>
          <li><strong>After that:</strong> every year, by the expiry date on the last certificate.</li>
          <li><strong>Getting it done early:</strong> you can have an MOT up to a month, minus a day, before it runs out and keep the same renewal date. If your MOT expires on 15 May, the earliest you can test and keep the date is 16 April. Test any earlier and your next MOT is due a year, minus a day, from the pass.</li>
          <li><strong>Driving without one:</strong> you can be fined up to £1,000. The only exceptions are driving to a pre-booked MOT, or to a garage for repairs needed to pass.</li>
          <li><strong>It affects your tax too:</strong> you can't renew your vehicle tax while the MOT has expired.</li>
        </ul>
        <div class="callout">
          <p><strong>Book early, test in the window.</strong> Book your MOT a few weeks before the window opens. Testing early in the window leaves time to fix a fail without the car going a day without a valid MOT.</p>
        </div>

        <h2 id="tax">Vehicle tax: when it's due and how to pay</h2>
        <p>Vehicle tax (officially Vehicle Excise Duty, still often called road tax) has to be paid for every car kept or used on a public road, unless it's declared off the road with a SORN. There's no paper tax disc any more: DVLA and the police check it against the registration.</p>
        <ul>
          <li><strong>Renewing:</strong> do it online at <a href="https://www.gov.uk/vehicle-tax" rel="noopener">GOV.UK</a> using the reference number on your V11 reminder or your V5C logbook. You need a valid MOT and insurance first.</li>
          <li><strong>Paying monthly:</strong> you can pay by Direct Debit every month, every 6 months or once a year. Monthly and 6-monthly payments cost 5% more than paying for the year in one go.</li>
          <li><strong>Buying a car:</strong> tax doesn't transfer to a new owner. Tax the car before you drive it home, using the reference number on the green new keeper slip from the V5C.</li>
          <li><strong>Selling a car:</strong> tell DVLA and any remaining full months of tax are refunded automatically, and a Direct Debit is cancelled.</li>
          <li><strong>Off the road:</strong> if you're keeping a car on private land and not using it, make a SORN instead of taxing it. A SORN car can't be kept or driven on a public road, except to a pre-booked MOT.</li>
        </ul>

        <h2 id="rates">How much is car tax? (rates from 1 April 2026)</h2>
        <p>What you pay depends mainly on when the car was first registered.</p>
        <h3>Cars first registered on or after 1 April 2017</h3>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Type</th><th>12 months (single payment)</th></tr></thead>
            <tbody>
              <tr><td>Standard rate</td><td>£200 a year, for petrol, diesel, hybrid and, since April 2025, electric cars</td></tr>
              <tr><td>Expensive car supplement</td><td>An extra £440 a year, for years 2 to 6, if the car's list price was over £40,000 (over £50,000 for zero-emission cars registered from 1 April 2025)</td></tr>
              <tr><td>First year</td><td>Set by the car's CO₂ emissions and usually included in the on-the-road price of a new car. Zero-emission cars pay £10.</td></tr>
            </tbody>
          </table>
        </div>
        <p>The supplement is based on the list price when new, including options, not what you paid. It applies for five years from the car's second tax payment, so buying a used car doesn't avoid it.</p>
        <h3>Cars first registered from 1 March 2001 to 31 March 2017</h3>
        <p>Tax is set by the car's CO₂ emissions, in bands from A to M. From 1 April 2026, band A and B cars pay £20 a year, a band D car £170, band G £275, band K £445 and the highest band, M, £790. Your car's band is on DVLA's vehicle enquiry service.</p>
        <h3>Cars first registered before 1 March 2001</h3>
        <p>Tax is based on engine size, with one rate for engines up to 1,549cc and a higher one above. Cars made or first registered 40 or more years ago can usually be taxed in the historic vehicle class, which is free, though you still need to tax them.</p>
        <p>The full tables are on <a href="https://www.gov.uk/vehicle-tax-rate-tables" rel="noopener">GOV.UK</a>.</p>

        <h2 id="miss">What happens if you miss them</h2>
        <div class="table-wrap">
          <table>
            <thead><tr><th>If you…</th><th>What can happen</th></tr></thead>
            <tbody>
              <tr><td>Drive without a valid MOT</td><td>A fine of up to £1,000. Your insurance may also be affected if you need to claim.</td></tr>
              <tr><td>Keep an untaxed car</td><td>An automatic £80 penalty from DVLA, reduced to £40 if paid within 33 days. If it goes to court, a fine of up to £1,000 or five times the tax owed, whichever is more.</td></tr>
              <tr><td>Use an untaxed car on the road</td><td>The car can be clamped or impounded, with a £100 release fee within 24 hours, £200 if it's taken to a pound, plus £21 for each day it's stored.</td></tr>
            </tbody>
          </table>
        </div>
        <p>DVLA checks its records automatically and the police check tax by number plate, so an expired date is noticed even if you're never stopped.</p>

        <h2 id="other">The other dates worth tracking</h2>
        <ul>
          <li><strong>Insurance renewal:</strong> shopping around a few weeks before renewal is usually cheaper than renewing automatically.</li>
          <li><strong>Servicing:</strong> usually every 12 months or a set mileage, whichever comes first. Our <a href="/guides/car-service-history/">service history guide</a> explains why it matters.</li>
          <li><strong>Breakdown cover and warranty:</strong> both easy to forget until you need them.</li>
          <li><strong>Driving licence photocard:</strong> needs renewing every 10 years.</li>
        </ul>
{livery("Every date, one garage", [
    "Livery shows every key date for every car you own on one screen, with a countdown and a reminder before each one. With Livery Plus you can share a car with family, so everyone who drives it sees the same dates.",
])}
'''

FAQ = [
    ("How do I check when my car tax and MOT are due?",
     "Enter your registration on DVLA's free vehicle enquiry service. It shows the tax status and expiry and the MOT expiry date. Livery fills both in automatically from your number plate and reminds you before each one."),
    ("How early can I get an MOT?",
     "Up to a month, minus a day, before the current one runs out, and you keep the same renewal date. For example, if it expires on 15 May, the earliest you can test is 16 April."),
    ("Can I tax my car without an MOT?",
     "No. You need a valid MOT, and insurance, before you can renew your vehicle tax."),
    ("Is it cheaper to pay car tax monthly or yearly?",
     "Yearly. Paying monthly or every 6 months by Direct Debit costs 5% more than paying for 12 months in one go."),
    ("Do electric cars pay road tax?",
     "Yes, since 1 April 2025. A new zero-emission car pays £10 in its first year, then the standard rate, which is £200 a year from 1 April 2026. Electric cars with a list price over £50,000 (if registered from 1 April 2025) also pay the expensive car supplement for years 2 to 6."),
    ("What's the fine for no MOT?",
     "Up to £1,000. You can only drive a car without a valid MOT to a pre-booked test or to a garage for repairs needed to pass."),
]

GUIDE = {
    "slug": "car-tax-and-mot-due-dates",
    "crumb": "Car tax and MOT dates",
    "topic": "Running a car",
    "title": "When is my car tax and MOT due? How to check and renew | Livery",
    "h1": "When is my car tax and MOT due? How to check, renew and never miss either",
    "desc": "How to check your car tax and MOT dates, how early you can MOT, car tax rates from April 2026, paying monthly, and the fines if you miss them.",
    "card": "How to check both dates, how early you can MOT, car tax rates from April 2026, paying monthly, and what happens if you miss them.",
    "lede": "Your MOT and car tax run on different dates, and DVLA's reminder is easy to lose in the post. Here's how to check both, the rules for each, what car tax costs in 2026, and how to make sure you never miss them.",
    "published": "2026-11-09",
    "updated": "2026-11-09",
    "body": BODY,
    "faq": FAQ,
    "related": ["check-mot-history", "car-service-history", "ulez-clean-air-zone-check"],
    "cta": {
        "title": "Never miss an MOT or tax date.",
        "text": "Add your number plate to Livery and your MOT and tax dates are set up automatically, with a reminder 30 days, 7 days and 1 day before each. Free for up to two cars.",
        "button": "Set up my reminders",
        "href": "https://app.liveryclub.com/auth?mode=signup",
    },
    "sources": [
        ("GOV.UK, MOT test rules", "https://www.gov.uk/getting-an-mot/mot-test-rules"),
        ("DVLA, Rates of vehicle tax from 1 April 2026 (V149)", "https://assets.publishing.service.gov.uk/media/69a83810dcb774b435560510/v149-rates-of-vehicle-tax-for-cars-motorcycles-light-goods-vehicles-and-private-light-goods-vehicles-april-2026.pdf"),
        ("GOV.UK, Vehicle tax Direct Debit payments", "https://www.gov.uk/vehicle-tax-direct-debit"),
        ("GOV.UK, DVLA enforcement of vehicle tax, registration and insurance offences", "https://www.gov.uk/government/publications/vehicle-enforcement-policy/dvla-enforcement-of-vehicle-tax-registration-and-insurance-offences"),
    ],
}
