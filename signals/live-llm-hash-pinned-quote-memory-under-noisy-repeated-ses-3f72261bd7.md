# Live-LLM hash-pinned quote memory under noisy repeated sessions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-llm-hash-pinned-quote-memory-under-noisy-repeated-ses-3f72261bd7`
Run ID: `live-llm-hash-pinned-quote-memory-under-noisy-repeated-ses-3f72261bd7-20260621T124832195241+0000`

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

- Parent run decision: Anchored Long-Context: Hash-Pinned Quote Memory: enoch://control-plane/projects/anchored-long-context-hash-pinned-quote-memory-c2e888158f43/runs/anchored-long-context-hash-pinned-quote-memory-c2e888158f43-20260621T114604638743+0000
- Parent run decision: LLM-in-the-loop hash-pinned quote memory under noisy repeated sessions: enoch://control-plane/projects/llm-in-the-loop-hash-pinned-quote-memory-under-noisy-repea-e31d208eb1/runs/llm-in-the-loop-hash-pinned-quote-memory-under-noisy-repea-e31d208eb1-20260621T120752308955+0000

## What looked useful

Across 20 seeds, 48 tasks, 8 sessions, and noise levels 0/2/5/9, hash-pinned quote memory achieved 1.000 joint exact quote plus hash success and 0.000 false quote rate. Transcript search and flat retrieval had 0.000 joint success because they did not cite the target hash, and the unverified-pin ablation dropped to 0.301 joint success under noisy pins.

## Boundaries and scale limits

No live LLM was called; tasks were synthetic; retrieval baselines were simple lexical/frequency controls; no embedding retrieval, trained memory module, prompt robustness, latency, cost, or multi-model behavior was tested.

## Claim scope

In a deterministic seeded repeated-session simulator, retrieving exact quotes by verified target SHA-256 hash preserved quote bytes and hash citations under noisy same-topic paraphrases better than transcript search, flat retrieval, no memory, and an unverified-pin ablation.

## Why it stopped

Useful simulator mechanism evidence was produced, but the controller's live-LLM paper threshold is not satisfied by deterministic synthetic retrieval.

## Recommended next action

Run a bounded live-LLM follow-up using the same replay generator and scoring contract with transcript-only, flat memory, unverified pin, and hash-pinned memory conditions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-LLM quote-memory replay with target-hash scoring
- Success threshold: On at least 20 seeds and 48 tasks, hash-pinned memory reaches at least 0.90 joint exact quote plus hash success, improves by at least 0.30 over the best ordinary baseline, and keeps false quote rate at or below 0.05.
- Stop condition: Stop if hash-pinned memory fails to beat the best ordinary baseline by 0.10 joint success on the first 10 seeds, or if live model access is unavailable after verifying local/API configuration.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-hash-pinned-quote-memory-under-noisy-repeated-ses-3f72261bd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
