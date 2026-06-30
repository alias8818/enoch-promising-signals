# Real-Corpus False Accept and False Reject Test for Tiered Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-false-accept-and-false-reject-test-for-tiered-6d1bf1278b`
Run ID: `real-corpus-false-accept-and-false-reject-test-for-tiered-6d1bf1278b-20260612T061403981974+0000`

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

- Parent run decision: Falsifiable Evidence Ledger with Tiered Validation: enoch://control-plane/projects/falsifiable-evidence-ledger-with-tiered-validation-421bc729f683/runs/falsifiable-evidence-ledger-with-tiered-validation-421bc729f683-20260612T052130669313+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/998410ae075f

## What looked useful

Main run: flat false accept rate 100% and tiered false accept rate 0.5% on 400 false claims; both false reject rates 0% on 400 true claims. Across five seeds and 4,000 total claims, mean tiered false accept rate was 0.8% versus flat 100%, with 0% false rejects for both policies.

## Boundaries and scale limits

Test used 1,164 usable AG News training rows per run, 400 true/false pairs in the main run, and five 400-pair confirmation seeds. It did not test natural LLM-generated claims, paraphrases, human-labeled entailment, multi-hop evidence, or larger heterogeneous corpora.

## Claim scope

On AG News real-corpus exact-span claims with controlled salient-token corruptions, a tiered ledger requiring exact quote evidence except for a strict weak-evidence backoff reduced false accepts from a flat lexical ledger without increasing false rejects.

## Why it stopped

Tier 1 direct test met the predefined false accept/false reject threshold, but the evidence remains controlled and lexical, so it is a useful mechanism signal rather than paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up on a human-labeled claim/evidence or LLM-generated hallucination corpus with semantic entailment scoring and an entity/number consistency ablation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-Labeled Semantic False Accept Test for Tiered Evidence Ledgers
- Success threshold: At least 30% relative false accept reduction versus flat semantic retrieval, no more than 10 percentage point false reject increase, and the effect persists across at least two claim sources or seeds.
- Stop condition: Stop if tiered false accept reduction is below 10%, false reject increase exceeds 10 percentage points, or gains disappear when entity/number consistency controls are added.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-false-accept-and-false-reject-test-for-tiered-6d1bf1278b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
