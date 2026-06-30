# Anchored Long-Context: Hash-Pinned Quote Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchored-long-context-hash-pinned-quote-memory-c2e888158f43`
Run ID: `anchored-long-context-hash-pinned-quote-memory-c2e888158f43-20260621T114604638743+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/55f35adcd078

## What looked useful

Across 1,200 synthetic tasks, hash_pinned_quote_memory achieved 1.000 exact quote accuracy, 1.000 provenance accuracy, and 0.000 tamper false accept rate. Transcript and flat retrieval baselines achieved about 0.28-0.30 exact/provenance accuracy and about 0.69-0.70 tamper false accept rate.

## Boundaries and scale limits

Evidence is limited to model-free synthetic replay tasks: 5 seeds, 240 tasks per seed, 420 transcript lines per task, 8 quote records per task, and 70% tamper injection. It does not validate LLM extraction, real long-context attention, real repeated-agent workflows, or production storage behavior.

## Claim scope

In a deterministic synthetic replay benchmark with generated quote records, near-duplicate distractors, and reused hash pins, recomputing quote digests before indexing by pin preserved exact quote text and provenance and rejected tampered spans.

## Why it stopped

The result is a bounded synthetic mechanism validation, not full long-context agent evidence or publication-grade validation.

## Recommended next action

Run a bounded LLM-in-the-loop follow-up where a small model extracts, stores, retrieves, and cites hash-pinned quotes across repeated noisy sessions; stop this run as no-paper useful synthetic evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop hash-pinned quote memory under noisy repeated sessions
- Success threshold: Hash-pinned memory improves exact quote and provenance accuracy by at least 20 absolute percentage points over the best baseline and keeps tamper false accept rate below 5% on at least 300 LLM-in-the-loop tasks.
- Stop condition: Stop as negative if hash-pinned memory does not beat the best baseline by 10 absolute percentage points or if miss rate rises above 20% because digest verification rejects too many usable memories.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-long-context-hash-pinned-quote-memory-c2e888158f43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
