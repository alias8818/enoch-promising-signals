# CPU spec decoding via n-gram suffix draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-spec-decoding-via-n-gram-suffix-draft-1022c30bf1d9`
Run ID: `cpu-spec-decoding-via-n-gram-suffix-draft-1022c30bf1d9-20260629T065252173265+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d7b7caee9d55

## What looked useful

Suffix-only n-grams achieved 0.877 market accuracy versus 0.302 shuffled control and 0.438 fine-grained suffix-power accuracy versus 0.088 shuffled control, showing real suffix signal but insufficient accuracy for paper-grade full spec decoding.

## Boundaries and scale limits

Small hand-curated dataset; no vendor-scraped corpus; no release-time or family-held-out split; no exact clocks/cache/TDP targets; CPU-only local run completed in about 76 seconds.

## Claim scope

On a 73-item hand-curated CPU SKU table, suffix character n-grams recover some naming-convention attributes, especially market class, above majority and shuffled-label controls; they do not establish robust full CPU spec decoding.

## Why it stopped

Bounded local evidence supports suffix-taxonomy signal but not publication-grade CPU spec decoding; this is a small direct mechanism test, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a scraped vendor-attributed CPU database and family/time-held-out validation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Vendor-scraped CPU SKU suffix decoding with family-held-out validation
- Success threshold: On held-out families or later release generations, suffix n-grams must exceed shuffled controls by at least 0.30 absolute accuracy for suffix-coded fields and demonstrate calibrated abstention; exact numeric spec decoding must either exceed a rule baseline or be reported as unsupported.
- Stop condition: Stop if suffix-only features fall within 0.10 absolute accuracy of shuffled controls on held-out data, or if exact numeric spec targets remain below a simple vendor-rule baseline after adding full-token features.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-spec-decoding-via-n-gram-suffix-draft-1022c30bf1d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
