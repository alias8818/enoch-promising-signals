# Real-export ledger mutation replay for semantic notary fingerprints

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-export-ledger-mutation-replay-for-semantic-notary-fin-e414683962`
Run ID: `real-export-ledger-mutation-replay-for-semantic-notary-fin-e414683962-20260522T022446317338+0000`

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

- Parent run decision: Semantic Ledger Notary: enoch://control-plane/projects/semantic-ledger-notary-6ed8c4237097/runs/semantic-ledger-notary-6ed8c4237097-20260521T223326136473+0000
- Parent run decision: Held-out realistic ledger mutation benchmark for semantic notary fingerprints: enoch://control-plane/projects/held-out-realistic-ledger-mutation-benchmark-for-semantic-66ffaff727/runs/held-out-realistic-ledger-mutation-benchmark-for-semantic-66ffaff727-20260522T003742717609+0000

## What looked useful

Semantic fingerprints achieved 0.000 benign false positive rate and 1.000 malicious detection rate over 1,800 benign and 1,800 malicious fixed-seed replay trials. Raw SHA-256 had 1.000 benign false positive rate; final-balance audit detected only 0.667 of semantic mutations.

## Boundaries and scale limits

Only public example exports from BittyTax and Beancount were tested. The run did not include private production bank/exchange exports, repeated exports from the same live system, independent parser implementations, or domain-expert adversarial mutations.

## Claim scope

On three public ledger/export examples totaling 1,267 parsed events, a canonical semantic-event fingerprint was stable under generated harmless export drift and detected generated amount, account/asset-swap, and semantic metadata mutations across fixed seeds.

## Why it stopped

Tier-2 local evidence supports the mechanism but is not broad or independent enough for publication-grade claims.

## Recommended next action

Stop this run as no-paper useful signal; deepen only by adding independent real-export adapters and repeated-export drift from at least three additional systems.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-adapter real-export semantic notary replay
- Success threshold: Across at least six total export datasets, semantic fingerprint benign false positive rate <= 1%, malicious detection rate >= 98%, and at least a 20 percentage point detection advantage over final-balance audit on balance-preserving or metadata-only attacks.
- Stop condition: Stop negative if any added real-export family has benign false positive rate above 5% after documented canonicalization fixes, or malicious detection below 95% for non-noop semantic mutations.

## Evidence references

- Artifact root: `<local-path>/projects/real-export-ledger-mutation-replay-for-semantic-notary-fin-e414683962`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
