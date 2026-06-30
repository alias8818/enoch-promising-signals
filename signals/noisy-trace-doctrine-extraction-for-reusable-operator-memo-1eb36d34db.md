# Noisy Trace Doctrine Extraction for Reusable Operator Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `noisy-trace-doctrine-extraction-for-reusable-operator-memo-1eb36d34db`
Run ID: `noisy-trace-doctrine-extraction-for-reusable-operator-memo-1eb36d34db-20260621T145645871649+0000`

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

- Parent run decision: Memory Doctrine: Do Stores Learn Reusable Operators?: enoch://control-plane/projects/memory-doctrine-do-stores-learn-reusable-operators-33800e434a53/runs/memory-doctrine-do-stores-learn-reusable-operators-33800e434a53-20260621T140942270171+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/55f35adcd078

## What looked useful

Layered doctrine memory reached precision 1.0000, recall 1.0000, F1 1.0000, exact-case accuracy 1.0000, and zero stale-rule hits. Transcript search had F1 0.7027 with 10 stale-rule hits. Flat retrieval had F1 0.9655 with 1 stale-rule hit, so the pre-set +0.20 F1-over-flat threshold was not met.

## Boundaries and scale limits

Eight synthetic cases with explicit doctrine IDs and supersession metadata; no natural operator logs, no LLM-generated memo scoring, and no large trace corpus.

## Claim scope

Small controlled synthetic replay tasks show that layered doctrine extraction can recover expected doctrine IDs and suppress stale rules better than raw transcript search, but it was only marginally better than a strong flat retrieval baseline.

## Why it stopped

Controlled small direct test produced useful mechanism evidence but failed the pre-set improvement threshold over flat retrieval, so this is no-paper evidence rather than publication readiness.

## Recommended next action

Run a frozen-threshold deepen test on a harder semi-natural corpus with independently annotated doctrine and generated memo scoring; do not write a paper from this synthetic Tier-1 signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder semi-natural doctrine-memory replay with generated memo scoring
- Success threshold: Layered doctrine memory F1 >= 0.85, stale-rule hits at least 50% lower than flat retrieval, and memo requirement F1 at least 0.15 above flat retrieval on the frozen corpus.
- Stop condition: Stop as negative if layered memory fails to beat flat retrieval by 0.15 F1 or if stale-rule reduction is below 50% on the frozen corpus.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-trace-doctrine-extraction-for-reusable-operator-memo-1eb36d34db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
