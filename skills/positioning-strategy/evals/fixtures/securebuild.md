# SecureBuild research packet: product capability regression

Synthetic B2B developer-security case. No real customers or quotes.

SRC-S1 Verified product scope for this fixture: SecureBuild scans container images and blocks promotion when a policy fails. Its signed exception record binds vulnerability, image digest, approver, expiry and deployment policy; the same record follows the digest across supported CI systems.
SRC-S2 Fixture study: in a five-team controlled pilot, all five reproduced the signed approval history across two CI systems. No measured breach, time-saved or revenue result exists.
SRC-S3 Buyer evidence supplied: platform engineers use spreadsheets and ticket links to carry security exceptions between CI systems. Security leaders care about accountable exception expiry; application teams prioritize release continuity. Budget typically sits with security, but authority must be confirmed per account.
SRC-S4 Alternatives: MegaSec has broader scanners and richer threat research, but requires a separate governance deployment and team; TinyScan is simpler but lacks cross-CI signed exception continuity. Internal scripts are cheap to retain but have incomplete expiry handling. These facts apply only to this fixture.
SRC-S5 Scope: accepted exploratory customer scope is multi-CI software companies with production container delivery and a recurring exception-governance problem. Positioning remains provisional pending paid conversion evidence and implementation-support cost. No existing customer relationship advantage is supplied.
