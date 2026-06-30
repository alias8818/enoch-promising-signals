# Independent real-export corpus semantic notary replay

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `independent-real-export-corpus-semantic-notary-replay-0314180bc8`
Run ID: `independent-real-export-corpus-semantic-notary-replay-0314180bc8-20260522T045832249327+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Multi-adapter real-export semantic notary replay: enoch://control-plane/projects/multi-adapter-real-export-semantic-notary-replay-469a7d17a2/runs/multi-adapter-real-export-semantic-notary-replay-469a7d17a2-20260522T035635112742+0000
- Parent run decision: Real-export ledger mutation replay for semantic notary fingerprints: enoch://control-plane/projects/real-export-ledger-mutation-replay-for-semantic-notary-fin-e414683962/runs/real-export-ledger-mutation-replay-for-semantic-notary-fin-e414683962-20260522T022446317338+0000

## What looked useful

Semantic canonicalization materially outperformed raw file hashes, raw record hashes, weak token signatures, and a semantic-normalization ablation for benign replay while retaining tamper detection in this bounded harness.

## Boundaries and scale limits

The corpus is small, limited to iCalendar/vCard fixtures, partly library test data, and uses synthetic benign replay transformations rather than independently regenerated exports from live applications. It does not validate arbitrary export formats, adversarial semantic edits, or a broad real user export corpus.

## Claim scope

On 63 public iCalendar/vCard export fixture files containing 81 records, a field-normalizing semantic record hash replayed benign export-style formatting and representation changes with 1.000 F1 across five fixed seeds and detected all single-field tamper edits in this harness.

## Why it stopped

The mechanism is supported locally, but the requested Tier 4 paper-readiness threshold requires broader independently regenerated real exports and adversarial robustness beyond this bounded corpus.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; do not chain another follow-up because the controller lineage is already at depth 4.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/independent-real-export-corpus-semantic-notary-replay-0314180bc8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
