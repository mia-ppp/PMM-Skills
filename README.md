# PMM Skills for AI Agents

Product marketing skills for AI agents, built around a positioning-first workflow and measured against a no-skill baseline.

**Original work in this repo:**

- **[positioning-strategy](skills/positioning-strategy/)**: finds the wedge, fills a positioning canvas, and states the trade-offs it is making.
- **[messaging-framework](skills/messaging-framework/)**: turns a position into an umbrella message, pillars, and messaging by persona.
- **[buyer-personas](skills/buyer-personas/)**: segments before it profiles, maps the buying committee, and labels every attribute as evidence or hypothesis.
- **[Eval harness](evals/)**: checks that each request reaches the right skill, scores every skill against a no-skill baseline on four rubric dimensions (grounded, decisive, usable, sharp), and measures how often the judge agrees with hand grades.

**Measured results ([RESULTS.md](evals/RESULTS.md)):** in the latest run, positioning-strategy (+0.90) and messaging-framework (+0.88) show the largest lift over baseline on a 0 to 2 scale, and the router picks the right skill for 94.6% of 222 test prompts. These are early results from small samples.

The rest of the collection carries that foundation into launches, sales collateral, competitive pages, and copy, plus the growth work a lean marketing team handles: conversion optimization, SEO, paid ads, email, analytics, and retention. 43 skills in total. Works with Claude Code, Cursor, Windsurf, and any agent that supports the Agent Skills spec.

---

## How Skills Work Together

Skills reference each other and build on shared context. The `product-marketing-context` skill is the foundation. Every other skill checks it first to understand your product, audience, and positioning before doing anything. The Positioning & Messaging skills decide what to say, and the rest of the skills express it.

```
                    ┌──────────────────────────────────────┐
                    │      product-marketing-context       │
                    │    (read by all other skills first)  │
                    └──────────────────┬───────────────────┘
                                       │
                    ┌──────────────────┴───────────────────┐
                    │       Positioning & Messaging        │
                    ├──────────────────────────────────────┤
                    │  positioning-strategy                │
                    │  messaging-framework                 │
                    │  buyer-personas                      │
                    └──────────────────┬───────────────────┘
                                       │
  ┌──────────────┬──────────────┬──────┴───────┬──────────────┬──────────────┬──────────────┐
  ▼              ▼              ▼              ▼              ▼              ▼              ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌──────────┐ ┌─────────────┐ ┌───────────┐
│  SEO &   │ │   CRO    │ │Content & │ │  Paid &    │ │ Growth & │ │  Sales &    │ │ Strategy  │
│ Content  │ │          │ │   Copy   │ │Measurement │ │Retention │ │    GTM      │ │           │
├──────────┤ ├──────────┤ ├──────────┤ ├────────────┤ ├──────────┤ ├─────────────┤ ├───────────┤
│seo-audit │ │page-cro  │ │copywritng│ │paid-ads    │ │referral  │ │revops       │ │mktg-ideas │
│ai-seo    │ │signup-cro│ │copy-edit │ │ad-creative │ │free-tool │ │sales-enable │ │mktg-psych │
│site-arch │ │onboard   │ │cold-email│ │ab-test     │ │churn-    │ │launch       │ │customer-  │
│programm  │ │form-cro  │ │email-seq │ │analytics   │ │ prevent  │ │pricing      │ │ research  │
│schema    │ │popup-cro │ │social    │ │            │ │community │ │comp-alts    │ │           │
│content   │ │paywall   │ │video     │ │            │ │lead-magnt│ │comp-profile │ │           │
│aso-audit │ │          │ │image     │ │            │ │          │ │directory    │ │           │
└──────────┘ └──────────┘ └──────────┘ └────────────┘ └──────────┘ └─────────────┘ └───────────┘
```

Skills cross-reference each other:
- `positioning-strategy` → `messaging-framework` → `copywriting`, `sales-enablement`
- `buyer-personas` ↔ `customer-research` ↔ `positioning-strategy`
- `copywriting` ↔ `page-cro` ↔ `ab-test-setup`
- `revops` ↔ `sales-enablement` ↔ `cold-email`
- `seo-audit` ↔ `schema-markup` ↔ `ai-seo`
- `customer-research` → `copywriting`, `page-cro`, `competitor-alternatives`

See each skill's Related Skills section for the full dependency map.

---

## Available Skills

| Skill | Description |
|---|---|
| `ab-test-setup` | Plan, design, or implement A/B tests and growth experimentation programs. Covers hypothesis frameworks, sample size, statistical significance, ICE scoring, and experiment velocity. |
| `ad-creative` | Generate, iterate, and scale ad creative: headlines, descriptions, primary text, and full ad sets across formats. |
| `ai-seo` | Optimize content for AI search engines, get cited by LLMs, and appear in AI-generated answers. |
| `analytics-tracking` | Set up, improve, or audit analytics tracking and measurement. |
| `aso-audit` | Audit or optimize an App Store or Google Play listing. |
| `buyer-personas` | Create, research, validate, or refresh buyer personas, ICP profiles, and buying committee maps. |
| `churn-prevention` | Reduce churn, build cancellation flows, set up save offers, recover failed payments, and improve retention. |
| `cold-email` | Write B2B cold emails and follow-up sequences that get replies. |
| `community-marketing` | Build and leverage online communities to drive product growth and brand loyalty. |
| `competitor-alternatives` | Create competitor comparison or alternative pages for SEO and sales enablement. |
| `competitor-profiling` | Research, profile, and analyze competitors from their URLs. |
| `content-strategy` | Plan a content strategy, decide what content to create, and map out topics by funnel stage. |
| `copy-editing` | Edit, review, or improve existing marketing copy, or refresh outdated content. |
| `copywriting` | Write, rewrite, or improve marketing copy for any page: homepage, landing pages, product pages, and more. |
| `customer-research` | Conduct, analyze, and synthesize customer research. |
| `directory-submissions` | Submit a product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks and distribution. |
| `email-sequence` | Create or optimize email sequences, drip campaigns, automated flows, and lifecycle emails. |
| `form-cro` | Optimize any lead capture or contact form that is not a signup flow. |
| `free-tool-strategy` | Plan, evaluate, or build a free tool for lead generation or SEO value. |
| `image` | Create, generate, edit, or optimize images for marketing: blog heroes, social graphics, product visuals. |
| `launch-strategy` | Plan a product launch, feature announcement, or release strategy. |
| `lead-magnets` | Create, plan, or optimize a lead magnet for email capture or lead generation. |
| `marketing-ideas` | Generate marketing ideas, inspiration, and strategies for SaaS or software products. |
| `marketing-psychology` | Apply psychological principles, mental models, and behavioral science to marketing. |
| `messaging-framework` | Build or fix a messaging framework: umbrella message, pillars, proof, persona messaging, and boilerplate. |
| `onboarding-cro` | Optimize post-signup onboarding, user activation, first-run experience, and time-to-value. |
| `page-cro` | Optimize any marketing page for conversions: homepage, landing pages, product pages. |
| `paid-ads` | Plan and optimize paid advertising campaigns on Google, Meta, LinkedIn, and other platforms. |
| `paywall-upgrade-cro` | Create or optimize in-app paywalls, upgrade screens, upsell modals, and feature gates. |
| `popup-cro` | Create or optimize popups, modals, overlays, slide-ins, and banners for conversion. |
| `positioning-strategy` | Create, rework, or pressure-test product positioning, differentiation, and market category. |
| `pricing-strategy` | Make pricing decisions, structure packaging, and improve monetization strategy. |
| `product-marketing-context` | Create or update the product marketing context document that all other skills read first. |
| `programmatic-seo` | Create SEO-driven pages at scale using templates and data. |
| `referral-program` | Create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. |
| `revops` | Manage revenue operations, lead lifecycle, and marketing-to-sales handoff processes. |
| `sales-enablement` | Create sales collateral, pitch decks, one-pagers, objection handling docs, and demo scripts. |
| `schema-markup` | Add, fix, or optimize schema markup and structured data on a site. |
| `seo-audit` | Audit, review, or diagnose SEO issues on a site. |
| `signup-flow-cro` | Optimize signup, registration, account creation, or trial activation flows. |
| `site-architecture` | Plan, map, or restructure a website's page hierarchy, navigation, URL structure, or internal linking. |
| `social-content` | Create, schedule, or optimize social media content for LinkedIn, Twitter/X, Instagram, and other platforms. |
| `video` | Create, generate, or produce video content using AI tools or programmatic frameworks. |

---

## Installation

### Option 1: Clone and Copy

```bash
git clone https://github.com/mia-ppp/PMM-Skills.git
mkdir -p .agents/skills
cp -r PMM-Skills/skills/* .agents/skills/
```

### Option 2: Download a Single Folder

Use [DownGit](https://downgit.github.io): paste the GitHub folder URL and download as a ZIP.

### Option 3: Git Submodule

Add as a submodule for easy updates:

```bash
git submodule add https://github.com/mia-ppp/PMM-Skills.git .agents/PMM-Skills
```

Then reference skills from `.agents/PMM-Skills/skills/`.

### Option 4: Fork and Customize

1. Fork this repository
2. Customize skills for your specific needs
3. Clone your fork into your projects

---

## Folder Structure

```
skills/
├── product-marketing-context/
│   └── SKILL.md
├── copywriting/
│   └── SKILL.md
├── page-cro/
│   └── SKILL.md
└── [all other skills]/
    └── SKILL.md
```

Keep all skill folders at the same level. Each skill references others by relative path, so the flat structure is required.

---

## Usage

Once installed, ask your agent to help with marketing tasks:

```
"Help me position our product against Asana and Monday"
→ Uses positioning-strategy skill

"Build a messaging framework for our launch"
→ Uses messaging-framework skill

"Help me optimize this landing page for conversions"
→ Uses page-cro skill

"Write homepage copy for my SaaS"
→ Uses copywriting skill

"Set up GA4 tracking for signups"
→ Uses analytics-tracking skill

"Create a 5-email welcome sequence"
→ Uses email-sequence skill
```

You can also invoke skills directly:

```
/positioning-strategy
/page-cro
/email-sequence
/seo-audit
```

---

## Skill Categories

### Positioning & Messaging
- `positioning-strategy`: Positioning, differentiation, and market category
- `messaging-framework`: Messaging pillars, proof, and boilerplate
- `buyer-personas`: Personas, ICP, and buying committees
- `product-marketing-context`: Shared product, audience, and positioning context

### Conversion Optimization
- `page-cro`: Any marketing page
- `signup-flow-cro`: Registration flows
- `onboarding-cro`: Post-signup activation
- `form-cro`: Lead capture forms
- `popup-cro`: Modals and overlays
- `paywall-upgrade-cro`: In-app upgrade moments

### Content & Copy
- `copywriting`: Marketing page copy
- `copy-editing`: Edit and polish existing copy
- `cold-email`: B2B cold outreach emails and sequences
- `email-sequence`: Automated email flows
- `social-content`: Social media content
- `image`: AI image generation, design tools, and optimization

### SEO & Discovery
- `seo-audit`: Technical and on-page SEO
- `ai-seo`: AI search optimization
- `programmatic-seo`: Scaled page generation
- `site-architecture`: Page hierarchy, navigation, URL structure
- `competitor-alternatives`: Comparison and alternative pages
- `schema-markup`: Structured data

### Paid & Distribution
- `paid-ads`: Google, Meta, LinkedIn ad campaigns
- `ad-creative`: Bulk ad creative generation and iteration
- `social-content`: Social media scheduling and strategy

### Measurement & Testing
- `analytics-tracking`: Event tracking setup
- `ab-test-setup`: Experiment design

### Retention
- `churn-prevention`: Cancel flows, save offers, dunning, payment recovery

### Growth Engineering
- `free-tool-strategy`: Marketing tools and calculators
- `referral-program`: Referral and affiliate programs

### Strategy & Monetization
- `marketing-ideas`: SaaS marketing ideas
- `marketing-psychology`: Mental models and psychology
- `launch-strategy`: Product launches and announcements
- `pricing-strategy`: Pricing, packaging, and monetization

### Sales & RevOps
- `revops`: Lead lifecycle, scoring, routing, pipeline management
- `sales-enablement`: Sales decks, one-pagers, objection docs, demo scripts

---

## Contributing

Found a way to improve a skill or have a new one to add? PRs and issues welcome.

See CONTRIBUTING.md for guidelines on adding or improving skills.

---

## License

MIT. Free to use, modify, and share, as long as you keep the copyright notice. See [LICENSE](LICENSE).
