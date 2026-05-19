# Medium real-trace confirmation for evidence-ledger auditing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-real-trace-confirmation-for-evidence-ledger-auditin-3817c20ac4`
Run ID: `medium-real-trace-confirmation-for-evidence-ledger-auditin-3817c20ac4-20260518T132605510006+0000`

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

- Internal Enoch project: Medium real-trace confirmation for evidence-ledger auditing: internal_generated:medium-real-trace-confirmation-for-evidence-ledger-auditin-3817c20ac4

## What looked useful

Anchors are the key mechanism: the unanchored hash-chain ablation missed all truncation and recompute-suffix trials, while the anchored chain detected all trials and provided exact event localization for ordinary tampering. File digest detected tampering but provided no event localization; batch manifests localized only to 128-event batches.

## Boundaries and scale limits

Validation used 6,000 real trace events total and deterministic local attacks in a research harness. It did not test long production audit ledgers, trusted timestamp services, key custody, concurrent writers, anchor compromise, replay across services, or recovery workflows.

## Claim scope

On three public LogHub 2,000-event real log traces with fixed-seed tamper injections, an externally anchored canonical hash-chain evidence ledger detected 100% of tested tampering and exactly localized 100% of ordinary modify/delete/insert/reorder/truncate attacks, outperforming file-digest and batch-manifest baselines on exact localization. Under recompute-suffix tampering, anchors preserved detection but localized only to the next anchor boundary.

## Why it stopped

Tier 2 evidence supports the scoped mechanism but remains no-paper evidence because the traces are short public samples and production deployment properties were not directly tested.

## Recommended next action

Run a bounded deepen follow-up on longer real traces with streaming append verification, anchor cadence sweeps, and adversarial recompute/truncate attacks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer streaming real-trace anchor-cadence validation for evidence-ledger auditing
- Success threshold: Anchored chain detects 100% of tamper trials, exact-localizes at least 99% of ordinary attacks, bounds recompute-capable localization to the configured anchor interval, and sustains at least 50k events/s streaming append throughput with less than 4x raw storage overhead in the research representation.
- Stop condition: Stop as negative if anchored detection falls below 99.9%, ordinary exact localization falls below 99%, recompute-capable localization exceeds the anchor interval, or streaming overhead becomes impractical relative to batch manifests.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-trace-confirmation-for-evidence-ledger-auditin-3817c20ac4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
