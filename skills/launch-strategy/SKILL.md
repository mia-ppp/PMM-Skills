---
name: launch-strategy
description: "When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user mentions 'launch,' 'Product Hunt,' 'feature release,' 'announcement,' 'go-to-market,' 'beta launch,' 'early access,' 'waitlist,' 'product update,' 'how do I launch this,' 'launch checklist,' 'GTM plan,' or 'we're about to ship.' Also use for launch post-mortems, such as 'our launch flopped,' 'launch didn't work,' or 'what went wrong with our launch.' Use this whenever someone is preparing to release something publicly. For ongoing marketing after launch, see marketing-ideas."
metadata:
  version: 1.2.0
---

# Launch Strategy

You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capture attention, and convert interest into users.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

**Load the shared references:** read `../_shared/evidence-gaps.md` and `../_shared/segment-selection.md` (relative to this skill's folder). Label every claim, segment, and number Sourced, Assumed, or Gap. Never drop a segment or opportunity because it lacks proof.

**Never stop for missing facts.** Proceed with a stated assumption, and record it in the "Inputs and assumptions" note that opens the plan.

---

## Choose the Launch Audience

A launch plan starts with who it is for. Do this before picking channels.

**For any launch that enters a new segment, a new product, or a GTM plan:** follow sections 1 to 5 of `../_shared/segment-selection.md`. This applies at every tier, even a minor feature, if it targets a segment you do not serve today.
1. List every plausible segment, including ones with zero published proof.
2. Size the full addressable market across every segment before choosing. Reconcile any headline loss or market figure with it, and name every exclusion and its reason.
3. Score each on pain intensity, reach or revenue, and proof strength, as separate columns.
4. Pick a lead segment and say why in 2 to 3 sentences.
5. Write the sequencing line for the segments that follow, with a trigger for each. Then size the year-one wedge as a share of the full market.

**For a launch only to segments you already serve:** name the customer segments that get the announcement, with labels. Skip scoring and sizing.

A segment with published stats and logos is easier to launch into. That makes it a candidate for lead, not the whole plan.

## Set Launch KPIs

- **Give the lead segment launch KPIs.** Examples: signups, activation, pipeline, or revenue from that segment.
- **Give each sequenced segment the KPI that measures its trigger.** When the trigger fires, that segment's launch starts.
- **Tag every KPI with the segment it tracks.** A KPI with no segment shows up as a mismatch in the consistency check.

---

## Core Philosophy

The best companies don't just launch once: they launch again and again. Every new feature, improvement, and update is an opportunity to capture attention and engage your audience.

A strong launch isn't about a single moment. It's about:
- Getting your product into users' hands early
- Learning from real feedback
- Making a splash at every stage
- Building momentum that compounds over time

---

## The ORB Framework

Structure your launch marketing across three channel types. Everything should ultimately lead back to owned channels.

### Owned Channels
You own the channel (though not the audience). Direct access without algorithms or platform rules.

**Examples:**
- Email list
- Blog
- Podcast
- Branded community (Slack, Discord)
- Website/product

**Why they matter:**
- Get more effective over time
- No algorithm changes or pay-to-play
- Direct relationship with audience
- Compound value from content

**Start with 1-2 based on audience:**
- Industry lacks quality content → Start a blog
- People want direct updates → Focus on email
- Engagement matters → Build a community

**Example - Superhuman:**
Built demand through an invite-only waitlist and one-on-one onboarding sessions. Every new user got a 30-minute live demo. This created exclusivity, FOMO, and word-of-mouth, all through owned relationships. Years later, their original onboarding materials still drive engagement.

### Rented Channels
Platforms that provide visibility but you don't control. Algorithms shift, rules change, pay-to-play increases.

**Examples:**
- Social media (Twitter/X, LinkedIn, Instagram)
- App stores and marketplaces
- YouTube
- Reddit

**How to use correctly:**
- Pick 1-2 platforms where your audience is active
- Use them to drive traffic to owned channels
- Don't rely on them as your only strategy

**Example - Notion:**
Hacked virality through Twitter, YouTube, and Reddit where productivity enthusiasts were active. Encouraged community to share templates and workflows. But they funneled all visibility into owned assets: every viral post led to signups, then targeted email onboarding.

**Platform-specific tactics:**
- Twitter/X: Threads that spark conversation → link to newsletter
- LinkedIn: High-value posts → lead to gated content or email signup
- Marketplaces (Shopify, Slack): Optimize listing → drive to site for more

Rented channels give speed, not stability. Capture momentum by bringing users into your owned ecosystem.

### Borrowed Channels
Tap into someone else's audience to shortcut the hardest part: getting noticed.

**Examples:**
- Guest content (blog posts, podcast interviews, newsletter features)
- Collaborations (webinars, co-marketing, social takeovers)
- Speaking engagements (conferences, panels, virtual summits)
- Influencer partnerships

**Be proactive, not passive:**
1. List industry leaders your audience follows
2. Pitch win-win collaborations
3. Use tools like SparkToro or Listen Notes to find audience overlap
4. Set up affiliate/referral incentives (for channel partner launches, use [Introw](../../tools/integrations/introw.md) to manage deal registration and commissions)

**Example - TRMNL:**
Sent a free e-ink display to YouTuber Snazzy Labs, not a paid sponsorship, just hoping he'd like it. He created an in-depth review that racked up 500K+ views and drove $500K+ in sales. They also set up an affiliate program for ongoing promotion.

Borrowed channels give instant credibility, but only work if you convert borrowed attention into owned relationships.

---

## Five-Phase Launch Approach

Launching isn't a one-day event. It's a phased process that builds momentum.

### Phase 1: Internal Launch
Gather initial feedback and iron out major issues before going public.

**Actions:**
- Recruit early users one-on-one to test for free
- Collect feedback on usability gaps and missing features
- Ensure prototype is functional enough to demo (doesn't need to be production-ready)

**Goal:** Validate core functionality with friendly users.

### Phase 2: Alpha Launch
Put the product in front of external users in a controlled way.

**Actions:**
- Create landing page with early access signup form
- Announce the product exists
- Invite users individually to start testing
- MVP should be working in production (even if still evolving)

**Goal:** First external validation and initial waitlist building.

### Phase 3: Beta Launch
Scale up early access while generating external buzz.

**Actions:**
- Work through early access list (some free, some paid)
- Start marketing with teasers about problems you solve
- Recruit friends, investors, and influencers to test and share

**Consider adding:**
- Coming soon landing page or waitlist
- "Beta" sticker in dashboard navigation
- Email invites to early access list
- Early access toggle in settings for experimental features

**Goal:** Build buzz and refine product with broader feedback.

### Phase 4: Early Access Launch
Shift from small-scale testing to controlled expansion.

**Actions:**
- Leak product details: screenshots, feature GIFs, demos
- Gather quantitative usage data and qualitative feedback
- Run user research with engaged users (incentivize with credits)
- Optionally run product/market fit survey to refine messaging

**Expansion options:**
- Option A: Throttle invites in batches (5-10% at a time)
- Option B: Invite all users at once under "early access" framing

**Goal:** Validate at scale and prepare for full launch.

### Phase 5: Full Launch
Open the floodgates.

**Actions:**
- Open self-serve signups
- Start charging (if not already)
- Announce general availability across all channels

**Launch touchpoints:**
- Customer emails
- In-app popups and product tours
- Website banner linking to launch assets
- "New" sticker in dashboard navigation
- Blog post announcement
- Social posts across platforms
- Product Hunt, BetaList, Hacker News, etc.

**Goal:** Maximum visibility and conversion to paying users.

---

## Product Hunt Launch Strategy

Product Hunt can be powerful for reaching early adopters, but it's not magic: it requires preparation.

### Pros
- Exposure to tech-savvy early adopter audience
- Credibility bump (especially if Product of the Day)
- Potential PR coverage and backlinks

### Cons
- Very competitive to rank well
- Short-lived traffic spikes
- Requires significant pre-launch planning

### How to Launch Successfully

**Before launch day:**
1. Build relationships with influential supporters, content hubs, and communities
2. Optimize your listing: compelling tagline, polished visuals, short demo video
3. Study successful launches to identify what worked
4. Engage in relevant communities: provide value before pitching
5. Prepare your team for all-day engagement

**On launch day:**
1. Treat it as an all-day event
2. Respond to every comment in real-time
3. Answer questions and spark discussions
4. Encourage your existing audience to engage
5. Direct traffic back to your site to capture signups

**After launch day:**
1. Follow up with everyone who engaged
2. Convert Product Hunt traffic into owned relationships (email signups)
3. Continue momentum with post-launch content

### Case Studies

**SavvyCal** (Scheduling tool):
- Optimized landing page and onboarding before launch
- Built relationships with productivity/SaaS influencers in advance
- Responded to every comment on launch day
- Result: #2 Product of the Month

**Reform** (Form builder):
- Studied successful launches and applied insights
- Crafted clear tagline, polished visuals, demo video
- Engaged in communities before launch (provided value first)
- Treated launch as all-day engagement event
- Directed traffic to capture signups
- Result: #1 Product of the Day

---

## Post-Launch Product Marketing

Your launch isn't over when the announcement goes live. Now comes adoption and retention work.

### Immediate Post-Launch Actions

**Educate new users:**
Set up automated onboarding email sequence introducing key features and use cases.

**Reinforce the launch:**
Include announcement in your weekly/biweekly/monthly roundup email to catch people who missed it.

**Differentiate against competitors:**
Publish comparison pages highlighting why you're the obvious choice.

**Update web pages:**
Add dedicated sections about the new feature/product across your site.

**Offer hands-on preview:**
Create no-code interactive demo (using tools like Navattic) so visitors can explore before signing up.

### Keep Momentum Going
It's easier to build on existing momentum than start from scratch. Every touchpoint reinforces the launch.

---

## Ongoing Launch Strategy

Don't rely on a single launch event. Regular updates and feature rollouts sustain engagement.

### How to Prioritize What to Announce

Use this matrix to decide how much marketing each update deserves:

**Major updates** (new features, product overhauls):
- Full campaign across multiple channels
- Blog post, email campaign, in-app messages, social media
- Maximize exposure

**Medium updates** (new integrations, UI enhancements):
- Targeted announcement
- Email to relevant segments, in-app banner
- Don't need full fanfare

**Minor updates** (bug fixes, small tweaks):
- Changelog and release notes
- Signal that product is improving
- Don't dominate marketing

### Announcement Tactics

**Space out releases:**
Instead of shipping everything at once, stagger announcements to maintain momentum.

**Reuse high-performing tactics:**
If a previous announcement resonated, apply those insights to future updates.

**Keep engaging:**
Continue using email, social, and in-app messaging to highlight improvements.

**Signal active development:**
Even small changelog updates remind customers your product is evolving. This builds retention and word-of-mouth: customers feel confident you'll be around.

---

## Launch Checklist

### Pre-Launch
- [ ] Landing page with clear value proposition
- [ ] Email capture / waitlist signup
- [ ] Early access list built
- [ ] Owned channels established (email, blog, community)
- [ ] Rented channel presence (social profiles optimized)
- [ ] Borrowed channel opportunities identified (podcasts, influencers)
- [ ] Product Hunt listing prepared (if using)
- [ ] Launch assets created (screenshots, demo video, GIFs)
- [ ] Onboarding flow ready
- [ ] Analytics/tracking in place

### Launch Day
- [ ] Announcement email to list
- [ ] Blog post published
- [ ] Social posts scheduled and posted
- [ ] Product Hunt listing live (if using)
- [ ] In-app announcement for existing users
- [ ] Website banner/notification active
- [ ] Team ready to engage and respond
- [ ] Monitor for issues and feedback

### Post-Launch
- [ ] Onboarding email sequence active
- [ ] Follow-up with engaged prospects
- [ ] Roundup email includes announcement
- [ ] Comparison pages published
- [ ] Interactive demo created
- [ ] Gather and act on feedback
- [ ] Plan next launch moment

---

## Task-Specific Questions

1. What are you launching? (New product, major feature, minor update)
2. What's your current audience size and engagement?
3. What owned channels do you have? (Email list size, blog traffic, community)
4. What's your timeline for launch?
5. Have you launched before? What worked/didn't work?
6. Are you considering Product Hunt? What's your preparation status?
7. Who has the problem this solves, beyond the customers you already have proof for?

---

## Output Format

For any launch that enters a new segment, a new product, or a GTM plan, use this structure:

```
## Inputs and assumptions
[Files and sources used, facts that were missing, and what was assumed in their place, each labeled. See ../_shared/evidence-gaps.md]

## Market sizing
[Headline figure reconciled to the full addressable market, every segment sized or labeled "Gap: not sized", counts shown as a share of their anchor, revenue per account built from a formula, exclusions with reasons]

## Lead segment and sequence
[Scoring table, lead segment with 2 to 3 sentences of reasoning, sequencing lines, year-one wedge as a share of the full market]

## Positioning and copy
[Statement from positioning-strategy, or a provisional one labeled Assumed. If the plan includes copy: hero line, subhead, and each segment's first line]

## Launch plan
[Phases, ORB channels, and launch-day plan for the lead segment]

## KPIs
| KPI | Segment | Target | Label |

## Consistency check
[Tables from section 6 of ../_shared/segment-selection.md]

## Evidence gaps (top five)
[Ranked by impact on the main number or lead claim, with why each matters]

## Appendix: Remaining evidence gaps
[Every other Assumed and Gap item, in ranked order]
```

If the plan includes launch copy with open Gaps, label it "Draft, not publish-ready" at the top. Give every hero or headline that depends on a Gap a provable fallback line.

The plan is internal, so "Inputs and assumptions" opens it. When the skill delivers customer-facing copy on its own, such as a launch email or announcement post, put the note after the copy as a separate note. Never put it inside the copy.

## Final Review

Run these checks before delivering, and fix what they find. Only the consistency check tables go in the plan. Do not add a pass or fail report.

1. **Consistency check.** Run section 6 of `../_shared/segment-selection.md`. The segments in the sizing, positioning, Phase 2 plan, KPIs, and copy must match. Fix mismatches such as "scale to all customers" in the strategy while every KPI tracks one segment. Also fix segment-specific words, such as "free credits," in a hero meant for several segments.
2. **Figure trace.** Run section 7 of `../_shared/segment-selection.md`. Remove or relabel any figure that is not Sourced, derived from labeled inputs, or Assumed with a stated basis.
3. **No silent exclusions.** Every segment from the list appears in the lead, the sequence, or the parked list with a reason.
4. **Labels and gaps.** Every claim, score, and size is labeled. The plan opens with "Inputs and assumptions" and ends with the ranked Evidence gaps lists.

---

## Output Rules

- No em dashes in output.

## Related Skills

- **marketing-ideas**: For additional launch tactics (#22 Product Hunt, #23 Early Access Referrals)
- **email-sequence**: For launch and onboarding email sequences
- **page-cro**: For optimizing launch landing pages
- **marketing-psychology**: For psychology behind waitlists and exclusivity
- **programmatic-seo**: For comparison pages mentioned in post-launch
- **sales-enablement**: For launch sales collateral and enablement materials
- **positioning-strategy**: For setting or pressure-testing positioning before a launch
- **messaging-framework**: For launch messaging, hero lines, capabilities, and proof
- **buyer-personas**: For profiling the lead segment and its buying committee in depth
