# Marketing Skills for AI Agents

A collection of AI agent skills for marketing tasks. Built for technical marketers and founders who want AI coding agents to help with conversion optimization, copywriting, SEO, analytics, and growth engineering.

Works with Claude Code, Cursor, Windsurf, and any agent that supports the Agent Skills spec.

---

## How Skills Work Together

Skills reference each other and build on shared context. The `product-marketing-context` skill is the foundation — every other skill checks it first to understand your product, audience, and positioning before doing anything.

```
                    ┌──────────────────────────────────────┐
                    │      product-marketing-context       │
                    │    (read by all other skills first)  │
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
│aso-audit │ │          │ │image     │ │            │ │co-mktg   │ │directory    │ │           │
└──────────┘ └──────────┘ └──────────┘ └────────────┘ └──────────┘ └─────────────┘ └───────────┘
```

Skills cross-reference each other:
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
| `ad-creative` | Generate, iterate, and scale ad creative — headlines, descriptions, primary text, and full ad sets across formats. |
| `ai-seo` | Optimize content for AI search engines, get cited by LLMs, and appear in AI-generated answers. |
| `analytics-tracking` | Set up, improve, or audit analytics tracking and measurement. |
| `aso-audit` | Audit or optimize an App Store or Google Play listing. |
| `churn-prevention` | Reduce churn, build cancellation flows, set up save offers, recover failed payments, and improve retention. |
| `co-marketing` | Find co-marketing partners, plan joint campaigns, and brainstorm partnership opportunities. |
| `cold-email` | Write B2B cold emails and follow-up sequences that get replies. |
| `community-marketing` | Build and leverage online communities to drive product growth and brand loyalty. |
| `competitor-alternatives` | Create competitor comparison or alternative pages for SEO and sales enablement. |
| `competitor-profiling` | Research, profile, and analyze competitors from their URLs. |
| `content-strategy` | Plan a content strategy, decide what content to create, and map out topics by funnel stage. |
| `copy-editing` | Edit, review, or improve existing marketing copy, or refresh outdated content. |
| `copywriting` | Write, rewrite, or improve marketing copy for any page — homepage, landing pages, product pages, and more. |
| `customer-research` | Conduct, analyze, and synthesize customer research. |
| `directory-submissions` | Submit a product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks and distribution. |
| `email-sequence` | Create or optimize email sequences, drip campaigns, automated flows, and lifecycle emails. |
| `form-cro` | Optimize any lead capture or contact form that is not a signup flow. |
| `free-tool-strategy` | Plan, evaluate, or build a free tool for lead generation or SEO value. |
| `image` | Create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product visuals. |
| `launch-strategy` | Plan a product launch, feature announcement, or release strategy. |
| `lead-magnets` | Create, plan, or optimize a lead magnet for email capture or lead generation. |
| `marketing-ideas` | Generate marketing ideas, inspiration, and strategies for SaaS or software products. |
| `marketing-psychology` | Apply psychological principles, mental models, and behavioral science to marketing. |
| `onboarding-cro` | Optimize post-signup onboarding, user activation, first-run experience, and time-to-value. |
| `page-cro` | Optimize any marketing page for conversions — homepage, landing pages, product pages. |
| `paid-ads` | Plan and optimize paid advertising campaigns on Google, Meta, LinkedIn, and other platforms. |
| `paywall-upgrade-cro` | Create or optimize in-app paywalls, upgrade screens, upsell modals, and feature gates. |
| `popup-cro` | Create or optimize popups, modals, overlays, slide-ins, and banners for conversion. |
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
git clone https://github.com/[your-username]/[your-repo].git
cp -r marketingskills/skills/* .agents/skills/
```

### Option 2: Download a Single Folder

Use [DownGit](https://downgit.github.io) — paste the GitHub folder URL and download as a ZIP.

### Option 3: Git Submodule

Add as a submodule for easy updates:

```bash
git submodule add https://github.com/[your-username]/[your-repo].git .agents/marketingskills
```

Then reference skills from `.agents/marketingskills/skills/`.

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
/page-cro
/email-sequence
/seo-audit
```

---

## Skill Categories

### Conversion Optimization
- `page-cro` — Any marketing page
- `signup-flow-cro` — Registration flows
- `onboarding-cro` — Post-signup activation
- `form-cro` — Lead capture forms
- `popup-cro` — Modals and overlays
- `paywall-upgrade-cro` — In-app upgrade moments

### Content & Copy
- `copywriting` — Marketing page copy
- `copy-editing` — Edit and polish existing copy
- `cold-email` — B2B cold outreach emails and sequences
- `email-sequence` — Automated email flows
- `social-content` — Social media content
- `image` — AI image generation, design tools, and optimization

### SEO & Discovery
- `seo-audit` — Technical and on-page SEO
- `ai-seo` — AI search optimization
- `programmatic-seo` — Scaled page generation
- `site-architecture` — Page hierarchy, navigation, URL structure
- `competitor-alternatives` — Comparison and alternative pages
- `schema-markup` — Structured data

### Paid & Distribution
- `paid-ads` — Google, Meta, LinkedIn ad campaigns
- `ad-creative` — Bulk ad creative generation and iteration
- `social-content` — Social media scheduling and strategy

### Measurement & Testing
- `analytics-tracking` — Event tracking setup
- `ab-test-setup` — Experiment design

### Retention
- `churn-prevention` — Cancel flows, save offers, dunning, payment recovery

### Growth Engineering
- `co-marketing` — Partner identification and joint campaigns
- `free-tool-strategy` — Marketing tools and calculators
- `referral-program` — Referral and affiliate programs

### Strategy & Monetization
- `marketing-ideas` — SaaS marketing ideas
- `marketing-psychology` — Mental models and psychology
- `launch-strategy` — Product launches and announcements
- `pricing-strategy` — Pricing, packaging, and monetization

### Sales & RevOps
- `revops` — Lead lifecycle, scoring, routing, pipeline management
- `sales-enablement` — Sales decks, one-pagers, objection docs, demo scripts

---

## Contributing

Found a way to improve a skill or have a new one to add? PRs and issues welcome.

See CONTRIBUTING.md for guidelines on adding or improving skills.

---

## License

MIT — Use these however you want.
