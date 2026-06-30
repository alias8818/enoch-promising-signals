# Reusable Operator Doctrine: Updated Rules Transfer Across Task Families

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `reusable-operator-doctrine-updated-rules-transfer-across-task-families-e42606c3aa6e`
Run ID: `reusable-operator-doctrine-updated-rules-transfer-across-task-families-e42606c3aa6e-20260611T131141855479+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfc61bad5e15

## What looked useful

Across 10 seeds and 2,400 related target tasks, related transfer reduced mean expected rank from 1734.845 to 702.109 and improved 83.7% of tasks on average. Mismatched transfer worsened mean rank by 945.109, and transfer to an unrelated family worsened mean rank by 1247.871, showing transfer is structure-specific rather than universal.

## Boundaries and scale limits

Synthetic task families only; no real agent traces, no execution-based program synthesis, no long programs, no natural-language tasks, no model training, and no production tool-use validation.

## Claim scope

In a synthetic DSL search benchmark with 18 operators and length-2/3 programs, smoothed operator priors updated on an arithmetic-list source family reduced expected search rank on a related numeric-aggregate target family versus a uniform prior, while mismatched or unrelated transfer hurt search.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism for related families but does not validate the broader real-world task-family transfer claim.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded direct benchmark using execution-based program synthesis or real tool-use traces with frozen source-family doctrine updates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Execution-Based Operator Doctrine Transfer on Real Program-Synthesis Families
- Success threshold: Related-family transfer must reduce median candidate evaluations by at least 25% versus uniform and improve at least 65% of held-out target tasks, while mismatched/unrelated transfer must not show comparable gains.
- Stop condition: Stop if related-family transfer fails to beat uniform by 10% median candidate evaluations in two independently seeded task-family pairs or if mismatched transfer performs similarly to related transfer.

## Evidence references

- Artifact root: `<local-path>/projects/reusable-operator-doctrine-updated-rules-transfer-across-task-families-e42606c3aa6e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
