# Opportunity discovery and use-case trace

Use this reference for broad market expansion, repositioning, new-category, or
product-opportunity questions. It is a reasoning contract, not a required set
of report sections. Keep the work lightweight when the user has already named a
narrow product, use case, or GTM motion.

## Classify the decision objects

Keep these concepts distinct. They may be linked, but one must not be silently
used as another:

| Object | Meaning | Example |
|---|---|---|
| Business use case | Business outcome or application the customer wants | Real-time fraud detection |
| AI workload | Technical processing that supports the use case | Stream transactions into an ML scoring system |
| Infrastructure requirement | Capability the workload requires | Fresh event data, low-latency access, reliable streaming |
| Customer problem | Failure, friction, cost, or limitation in the current workflow | Stale features make scoring unreliable |
| Buying trigger | Event that creates urgency to evaluate or buy | A production incident or new compliance rule |
| Product opportunity | Potential capability or solution | Managed streaming optimized for AI workloads |
| Beachhead | Initial segment plus use-case combination for GTM | Enterprise fraud teams with production streaming requirements |
| Positioning | Credible market position and differentiated value | Reliable operational data infrastructure for production AI |

Also distinguish solution categories such as AI-ready data, analytics, inference
infrastructure, and AI observability from the customer use cases they may serve.
When an item is ambiguous, explain the classification and carry the uncertainty.

## Broad-strategy sequence

For a broad decision, reason through the smallest useful version of this chain:

**Segments -> business use cases -> technical workloads -> infrastructure
requirements -> customer problems and buying triggers -> existing company
strengths -> product or packaging opportunities -> comparative selection ->
beachhead -> positioning.**

First generate a reasonable candidate set of business use cases. Do not call a
problem, trigger, feature, or infrastructure category a use case. For each
shortlisted use case, identify the workload and requirements, then test whether
the problem is material and whether the company has a credible advantage. A
missing link is a Gap; a plausible but unverified link is Assumed.

Before proposing a new product, compare at least one existing-product,
packaging, positioning, partner, or GTM route when it is credible. A conclusion
to improve or bundle existing capabilities is valid.

## Comparative opportunity choice

For broad work, compare credible alternatives before selecting a product
opportunity or beachhead. Use qualitative evidence when inputs do not justify
numbers. Consider urgency and frequency, realistically capturable opportunity,
company fit, customer access, differentiation, technical feasibility and
operating burden, monetization, implementation/support cost, time to value, and
evidence quality. Do not use arbitrary weighted scores.

State: opportunities considered; shortlist; selected option and why; credible
alternatives deprioritized and why; assumptions that could change the choice;
and the next evidence or validation experiment. Keep the customer beachhead
separate from the product hypothesis.

## Traceability and evidence boundary

For each meaningful recommendation, preserve this trace:

**Use case -> workload -> requirement -> problem -> company advantage -> product
opportunity -> beachhead -> positioning.**

Ownership follows the existing handoffs: `market-entry-brief` chooses or
sequences the candidate market segment, `go-to-market-strategy` proposes the
commercial beachhead by combining an accepted segment with a business use
case, and `positioning-strategy` consumes that proposal. `market-entry-
orchestration` coordinates accepted artifacts; it does not make the choice.

Support each link with observed customer evidence, verified market/product
research, an explicitly labeled assumption, or a proposed validation experiment.
Do not present an operational problem or buying trigger as a customer use case,
and do not present an unsupported solution hypothesis as an established finding.
The final deliverable can summarize the trace instead of reproducing a long
table when the intermediate artifact retains it.
