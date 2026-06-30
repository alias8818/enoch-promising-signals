# Jacobi Window Verification with CPU N-gram Seeding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `jacobi-window-verification-with-cpu-n-gram-seeding-e188f820c1a8`
Run ID: `jacobi-window-verification-with-cpu-n-gram-seeding-e188f820c1a8-20260604T124040993491+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4b3dd5e2c185

## What looked useful

CPU n-gram seeding produced exact accepted windows often enough to reduce verifier calls by up to 42.6% at window 16, but zero-accept windows remained high at 83.2%, so the mechanism is useful but not broadly validated.

## Boundaries and scale limits

Small hand-written prompt set, synthetic CPU seed corpus, greedy decoding only, verifier-call simulation rather than end-to-end serving latency, and no comparison against neural draft or retrieval draft baselines.

## Claim scope

In a bounded GPT-2 greedy-continuation simulator over 30 prompts and 1920 target tokens, CPU dynamic n-gram seeding reduced Jacobi-style verifier calls versus constant and random token seeds.

## Why it stopped

Mechanism supported locally, but evidence is simulator-scale and proxy-heavy rather than publication-grade direct serving evidence.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a held-out corpus benchmark and include end-to-end latency plus a neural or retrieval draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out corpus Jacobi n-gram seeding with latency accounting
- Success threshold: Mean end-to-end latency improves by at least 15% versus no-seed greedy verification and mean accepted tokens per verifier call is at least 1.5 with zero-accept rate below 70%.
- Stop condition: Stop if held-out zero-accept rate remains at or above 80% or CPU proposal overhead erases verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/jacobi-window-verification-with-cpu-n-gram-seeding-e188f820c1a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
