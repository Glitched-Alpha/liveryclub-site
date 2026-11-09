from .common import livery

BODY = f'''
        <h2 id="how">How to check it</h2>
        <div class="steps-pair">
          <div class="step-card">
            <h3>Quick one-off check</h3>
            <p>Go to <a href="https://www.gov.uk/check-mot-history" rel="noopener">Check the MOT history of a vehicle</a> on GOV.UK and enter the registration. It's free, and you don't need to own the car.</p>
          </div>
          <div class="step-card step-card-livery">
            <h3>Keep it with everything else</h3>
            <p>In Livery, add your car by its plate and its MOT history sits alongside your MOT and tax reminders, service records and receipts, so you never have to look it up again.</p>
            <a class="btn btn-primary" href="https://app.liveryclub.com/auth?mode=signup">Create my free garage</a>
          </div>
        </div>
        <p>For cars in England, Scotland and Wales you'll see results back to 2005. In Northern Ireland, results go back to 2017. To download the actual certificates or see which garage did each test (England, Scotland and Wales only), you'll also need the 11-digit reference number from the V5C logbook.</p>

        <h2 id="results">What the results mean</h2>
        <p>Since May 2018, problems found at an MOT are sorted into categories:</p>
        <dl class="defects">
          <div class="defect defect-dangerous"><dt>Dangerous</dt><dd>An immediate risk to road safety or a serious environmental issue. It's a fail, and the car shouldn't be driven until it's fixed.</dd></div>
          <div class="defect defect-major"><dt>Major</dt><dd>Could affect safety, other road users or the environment. It's a fail, and it needs repairing straight away.</dd></div>
          <div class="defect defect-minor"><dt>Minor</dt><dd>Little or no effect on safety. The car passes, but get it repaired as soon as you can.</dd></div>
          <div class="defect defect-advisory"><dt>Advisory</dt><dd>Something that could get worse. The car passes, but keep an eye on it.</dd></div>
        </dl>
        <p>Advisories are where most people get caught out. A tyre "close to the legal limit" or brake pads "wearing thin" this year is often next year's fail.</p>

        <h2 id="buying">What to look for when buying a used car</h2>
        <ul>
          <li><strong>Mileage that goes backwards, or jumps oddly.</strong> Each test records the mileage, so a drop between tests is a big warning sign. Our guide to <a href="/guides/spot-clocked-car-mileage/">spotting a clocked car</a> goes into detail.</li>
          <li><strong>The same advisory year after year.</strong> Repeated "corrosion" or "oil leak" notes suggest a problem that's never been fixed.</li>
          <li><strong>Gaps.</strong> A missing year can mean the car was off the road, or driven without an MOT. Ask the seller why.</li>
          <li><strong>Lots of fails on the same item.</strong> Suspension or brake parts failing again and again can point to a bigger issue.</li>
        </ul>
        <p>The MOT history is one part of checking a car you're thinking of buying. Our <a href="/guides/used-car-checks-before-buying/">used car checklist</a> covers the rest, from the V5C to outstanding finance.</p>

        <h2 id="record">Keep your own record</h2>
        <p>The MOT history only covers the test itself. It won't show the services, repairs and receipts in between, and those are what prove a car has been looked after. Our guide to <a href="/guides/car-service-history/">car service history</a> explains what to keep.</p>
{livery("How Livery helps", [
    "Livery keeps your car's MOT history next to everything else: your MOT and tax dates with a reminder 30 days, 7 days and 1 day before they're due, and every service, repair and receipt in one history file.",
    "With Livery Plus, the MOT advisory tracker turns the advisories from your latest test into a list you can tick off as you fix them, and flags any that have come up on more than one MOT.",
])}
'''

GUIDE = {
    "slug": "check-mot-history",
    "crumb": "Check MOT history",
    "topic": "MOT",
    "title": "How to check MOT history and what advisories mean | Livery",
    "h1": "How to check your car's MOT history, and what it's actually telling you",
    "desc": "Check any car's MOT history free in under a minute. What dangerous, major, minor and advisory items mean, and what to look for before you buy.",
    "card": "Find any car's MOT history for free, what dangerous, major, minor and advisory items mean, and what to look for before you buy.",
    "lede": "Your car's MOT history is one of the most useful free records there is. It shows every test the car has had, what it failed on, what the tester flagged and the mileage each time. Here's how to find it and how to read it.",
    "published": "2026-11-04",
    "updated": "2026-11-09",
    "body": BODY,
    "faq": [],
    "related": ["used-car-checks-before-buying", "spot-clocked-car-mileage", "car-tax-and-mot-due-dates"],
    "sources": [
        ("GOV.UK, Check the MOT history of a vehicle", "https://www.gov.uk/check-mot-history"),
        ("GOV.UK, MOT changes from May 2018", "https://www.gov.uk/government/publications/mot-changes-from-may-2018-guidance-for-mot-testers/overview-of-mot-changes-from-may-2018"),
    ],
}
