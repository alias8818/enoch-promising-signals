# Naturalistic Anchor-Indexed Memory Retrieval With Embedding and Lexical Controls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `naturalistic-anchor-indexed-memory-retrieval-with-embeddin-09cdf7bcfa`
Run ID: `naturalistic-anchor-indexed-memory-retrieval-with-embeddin-09cdf7bcfa-20260619T161832123268+0000`

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

- Parent run decision: Anchor-Indexed Memory vs Semantic Retrieval: enoch://control-plane/projects/anchor-indexed-memory-vs-semantic-retrieval-bbb9de080089/runs/anchor-indexed-memory-vs-semantic-retrieval-bbb9de080089-20260619T160322204749+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e23f283e0f4

## What looked useful

Anchor-indexed hybrid improved Top-1 from the best non-anchor control's 0.472 to 0.528 and improved Top-3/MRR, but failed the required 0.150 absolute Top-1 lift. Remaining errors were same-anchor wrong-field confusions, suggesting person/project anchors are too coarse without field or slot indexing.

## Boundaries and scale limits

Synthetic generated corpus only; no human-authored private transcripts, no production embedding model, no downstream agent answer-quality measurement, and no anchor-extraction noise study.

## Claim scope

Tier 1 generated naturalistic replay test with 42 memories and 36 queries comparing anchor-indexed hybrid retrieval against lexical, semantic embedding-style, and hybrid controls.

## Why it stopped

Controlled small direct test failed the predeclared success threshold; this is an early bounded falsification of the strong anchor-only retrieval claim, not a full validation.

## Recommended next action

Stop this follow-up as no-paper evidence; run a bounded deepen test of field/slot-aware anchor indexing against the same controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Field-Slot Anchor Indexing for Same-Anchor Memory Retrieval
- Success threshold: Mean field-slot anchor-indexed Top-1 across seeds exceeds the best non-anchor control by at least 0.15 absolute and cuts same-anchor wrong-field errors by at least 50%.
- Stop condition: Stop if the mean Top-1 lift is below 0.08 absolute or same-anchor wrong-field errors are not reduced by at least 25%, because field anchors would not be carrying enough mechanism signal.

## Evidence references

- Artifact root: `<local-path>/projects/naturalistic-anchor-indexed-memory-retrieval-with-embeddin-09cdf7bcfa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
