# KV-cache n-gram suffix speculation with zero extra VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-n-gram-suffix-speculation-with-zero-extra-vram-a50cc05a86ff`
Run ID: `kv-cache-n-gram-suffix-speculation-with-zero-extra-vram-a50cc05a86ff-20260620T125253569357+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/af51574fccbe

## What looked useful

Sliding KV-window suffix lookup matched all-context replay acceptance on all fixtures while using only current context tokens and lower CPU lookup time for the 128-token window; prompt-only lookup failed on the low-overlap question once useful repetition arose only in generated output.

## Boundaries and scale limits

Trace-level benchmark only; hand-written fixtures; distilgpt2 only; batch size 1; greedy decoding only; no production paged-KV verifier, scheduler, sampling, large model, public benchmark suite, or wall-clock serving latency comparison.

## Claim scope

On five fixed distilgpt2 greedy traces of 96 generated tokens each, a CPU-side n-gram suffix drafter restricted to tokens already in the active context/KV window produced accepted draft runs with zero extra GPU-resident suffix table and reduced target-pass count by 77.29% on average in replay.

## Why it stopped

Evidence is a bounded exact-greedy trace replay and pass-count proxy, not direct production serving validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the KV-window suffix drafter into a minimal real speculative verifier and measure wall-clock latency plus temporary KV allocation on a public repetitive/code workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real verifier latency test for KV-window suffix speculation
- Success threshold: At least 15% end-to-end decode latency reduction versus no speculation and at least 5% versus prompt-only lookup on the selected public workload, with identical greedy outputs and no persistent GPU-resident draft table.
- Stop condition: Stop if accepted draft tokens average below 1.5 per attempt or if verifier/lookup overhead makes latency no better than prompt-only lookup on the bounded workload.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-suffix-speculation-with-zero-extra-vram-a50cc05a86ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
