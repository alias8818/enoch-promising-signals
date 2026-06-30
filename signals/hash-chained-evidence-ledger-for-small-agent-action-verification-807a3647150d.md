# Hash-Chained Evidence Ledger for Small Agent Action Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hash-chained-evidence-ledger-for-small-agent-action-verification-807a3647150d`
Run ID: `hash-chained-evidence-ledger-for-small-agent-action-verification-807a3647150d-20260520T123721896821+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b11c7497bb69

## What looked useful

Across 200 trials per tamper mode, plain parseable JSON logs detected 0% of synthetic attacks, while hash-chain verification against a trusted head and HMAC receipt verification detected 100%. The negative control showed that if the HMAC receipt key is compromised, a full rewrite plus forged receipt is accepted. The 100k-entry benchmark appended about 271k entries/sec and verified about 348k entries/sec with 212 MB max RSS.

## Boundaries and scale limits

Tested only deterministic synthetic traces, 100k-entry CPU runs, one-process append/verify, and a controller-held HMAC receipt model. It did not test real agent framework integration, concurrent writers, crash recovery, external transparency-log anchoring, hardware-backed key custody, or agents that omit or falsify events before commit.

## Claim scope

Synthetic local evidence shows that a SHA-256 hash-chained action ledger with an independently retained head or HMAC receipt detects post-hoc edits, deletion, adjacent reordering, truncation, and full rewrites of small agent action traces at low CPU overhead.

## Why it stopped

Closed as no-paper useful signal: the mechanism works in a synthetic local test but is not novel enough or externally validated enough for a paper, and its trust boundary limitation is material.

## Recommended next action

Run one bounded real-agent integration follow-up that intercepts actual tool calls below the agent layer, keeps the receipt key outside the agent process, and compares the ledger against framework-native traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real agent tool-call ledger with separated receipt authority
- Success threshold: At least 99% agreement with framework-native observed tool calls, 100% detection of tested post-hoc tamper attacks under separated-key assumptions, and under 5% median runtime overhead.
- Stop condition: Stop if protocol-level interception misses more than 1% of tool calls, if separated key custody cannot be enforced locally, or if median overhead exceeds 5% on the 100-task benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-for-small-agent-action-verification-807a3647150d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
