# Hypothetical technical CRM task

Task scope: configuration and data hygiene only; no qualification, lead scoring,
audience messaging, stage semantics or routing decisions.
Sandbox records: R1 and R2 share normalized email user@example.test but have
external IDs EXT-1 and EXT-2. R3 has a different email. Email is not a unique key.
External ID is the documented unique key for this sandbox import. Missing IDs must
be quarantined. Existing row changes require a dry-run preview and operator approval.
Requested output: an idempotent import/matching plan and preview-only acceptance checks.
No live CRM access, writes or persona research is authorized. Actual connector capabilities
are unknown, so describe requirements rather than invent platform-specific settings.
