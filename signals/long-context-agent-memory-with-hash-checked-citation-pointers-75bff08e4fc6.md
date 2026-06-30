# Long-Context Agent Memory With Hash-Checked Citation Pointers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `long-context-agent-memory-with-hash-checked-citation-pointers-75bff08e4fc6`
Run ID: `long-context-agent-memory-with-hash-checked-citation-pointers-75bff08e4fc6-20260609T090602569956+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3ea99510e448

## What looked useful

Across 10,000 main trials, plain memory and no-hash pointers each had 0.500 overall undetected corruption rate in the mixed workload, while 128-bit hash-checked pointers had 0.000. Hash-length ablation showed 8-bit truncated hashes leaked 0.0018 undetected corruption, while 16, 32, 64, and 128 bits had zero observed misses in 20,000 trials each.

## Boundaries and scale limits

No real LLM, no learned retrieval, no natural long-context traces, no production document edits, and no adversarial prompt behavior were tested. Results are mechanism evidence only, not publication-grade validation.

## Claim scope

In a deterministic synthetic fact-memory benchmark, source-span citation pointers with 128-bit SHA-256 checks convert source drift and coordinated memory/source corruption into abstentions and eliminate undetected corrupted answers under the tested corruption modes.

## Why it stopped

Closed as no-paper useful signal: the synthetic mechanism is supported, but direct LLM/agent evidence is required before a paper-positive claim.

## Recommended next action

Run a bounded real-agent benchmark where an LLM creates and uses memories over multi-step long-context tasks, comparing plain summaries, no-hash citation pointers, and 128-bit hash-checked citation pointers under source mutation and adversarial distractors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Validation of Hash-Checked Citation Memory
- Success threshold: Hash-checked pointers reduce undetected corrupted-memory use by at least 80% versus both baselines while preserving at least 90% of clean-condition task success.
- Stop condition: Stop if hash-checked pointers fail to reduce undetected corruption by at least 50% in a smoke set of 100 real-agent memory-use episodes or if abstention reduces clean task success below 75%.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-agent-memory-with-hash-checked-citation-pointers-75bff08e4fc6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
